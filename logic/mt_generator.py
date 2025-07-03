import requests
import re
import random
import sys
import csv
import argparse

sys.path.append("/opt/2_github/python_sdk_test/http_req")
import action_req as req

sys.path.append("/opt/2_github/python_sdk_test/utils")
from config_io import read_ini_file

def check_result(test_cases, test_input):
    #print("test_cases", test_cases)
    #print("test_input", test_input)

    return True
    case_str = ''.join(re.findall(r"[A-Za-z_]+", test_cases))

    match case_str:
        case 'set_on_off_status':
            state_numbers = [ int(x) for x in test_input ]

            req.light_action_state(state_numbers[0])

            state = read_ini_file('power')
            if None == state:
                return False;

            state = state.strip()
            if 0 == state_numbers[0] and state == "Off":
                return True

            if 1 == state_numbers[0] and state == "On":
                return True

        case 'set_color':

            rgb_numbers = [ int(x) for x in test_input ]

            r = int(read_ini_file('r'))
            g = int(read_ini_file('g'))
            b = int(read_ini_file('b'))

            if None == r or None == g or None == b:
                return False

            if r == rgb_numbers[0] and g == rgb_numbers[1] and b == rgb_numbers[2]:
                return True

        case 'set_color_temperature':

            color_temperature_input_number = [ int(x) for x in test_input ]
            req.light_action_color_temperature(color_temperature_input_number[0])

            color_temperature = int(read_ini_file('color_temperature'))

            if None == color_temperature:
                return False

            if color_temperature_input_number[0] == color_temperature:
                return True

        case 'set_brightness':

            brightness_input_number = [ int(x) for x in test_input ]
            req.light_action_brightness(brightness_input_number[0])

            brightness = int(read_ini_file('brightness'))
            if None == brightness:
                return False

            if brightness_input_number[0] == brightness:
                return True

        case _:
            print("Matrh error")

    return False

def get_input_from_test_cases(case):
    input_numbers = re.findall(r'\d+\.\d+|\d+', case)
    #print(input_numbers)
    return input_numbers

def get_output_from_test_cases(case):
    output_numbers = re.findall(r'\d+\.\d+|\d+', case)
    #print(output_numbers)
    return output_numbers

def do_test_of_sequences(test_cases):
    for case in test_cases:
        test_input = get_input_from_test_cases(case)
        if False == check_result(case, test_input):
            return False

    return True;

def light_random_code_to_tests(num):
    match num:
        case 0:
            return "set_on_off_status-" + str(random.randint(0, 1))
        case 1:
            return "set_color-" + str(random.randint(0, 255)) + " " + str(random.randint(0, 255)) + " " + str(random.randint(0, 255))
        case 2:
            return "set_color_temperature-" + str(random.randint(1000, 7000))
        case 3:
            return "set_brightness-" + str(random.randint(0, 100))

        case _:
            return "error"

def tv_random_code_to_tests(num):
    match num:
        case 0:
            return "set_on_off_status_tv-" + str(random.randint(0, 1))
        case 1:
            return "set_channel-" + str(random.randint(1, 50))
        case 2:
            return "set_volume-" + str(random.randint(0, 100))

        case _:
            return "error"

def random_test_cases(dev_type='light'):
    if dev_type == 'light':
        rand = random.randint(0, 3)
        return light_random_code_to_tests(rand)
    if dev_type == 'tv':
        rand = random.randint(0, 2)
        return tv_random_code_to_tests(rand)

def generate_metamorphic_test_sequence(maxium_length = 10, dev_type='light'):
    test_cases = []
    test_sequences = []

    for i in range(maxium_length):
        new_test_case = random_test_cases(dev_type)
        test_cases.append(new_test_case)

        if False == do_test_of_sequences(test_cases):
            print("discard this sequences")
            break
        else:
            test_sequences = test_cases;

    return test_sequences

csv_file = "/tmp/test_sequences.csv"

def gemerate_metamorphic_testing_for_light(maxium_sequences_number = 10):

    with open(csv_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Index", "Seq"])

        for i in range(maxium_sequences_number):
            rand_sequence = random.randint(10, 15)
            test_sequence = generate_metamorphic_test_sequence(rand_sequence)
            print(test_sequence)
            writer.writerow([str(i), str(test_sequence)])

    return

def gemerate_metamorphic_testing_for_tv(maxium_sequences_number = 10):

    with open(csv_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Index", "Seq"])

        for i in range(maxium_sequences_number):
            rand_sequence = random.randint(5, 8)
            test_sequence = generate_metamorphic_test_sequence(rand_sequence, 'tv')
            print(test_sequence)
            writer.writerow([str(i), str(test_sequence)])

    return

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate test sequences")
    parser.add_argument("--device", type=str, default="light", help="Device type (e.g., light, tv)")
    #parser.add_argument("--input", type=str, help="Input CSV file")
    #parser.add_argument("--output", type=str, help="Output CSV file")
    #parser.add_argument("--function", type=str, help="Function to run")
    parser.add_argument("--number", type=int, help="number of sequences")

    args = parser.parse_args()

    print(args.device)
    if args.device == "tv":
        gemerate_metamorphic_testing_for_tv(args.number)
    elif args.device == "light":
        gemerate_metamorphic_testing_for_light(args.number)
    else:
        print("unknown device")



