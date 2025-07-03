import requests
import re
import random
import sys
import time

sys.path.append("/opt/2_github/python_sdk_test/http_req")
import action_req as req

sys.path.append("/opt/2_github/python_sdk_test/utils")
from config_io import read_ini_file

#test code
#test_sequence = [[], ['set_color-176 130 223'], ['set_color_temperature-5873', 'set_brightness-16'], ['set_color_temperature-2847', 'set_color-153 80 132', 'set_brightness-98']]
#test_sequence = ['set_color-169 11 18', 'set_on_off_status-1', 'set_color_temperature-4884', 'set_brightness-72', 'set_brightness-77', 'set_brightness-51']

def _get_input_from_test_cases(case):
    input_numbers = re.findall(r'\d+\.\d+|\d+', case)
    return input_numbers

def run_tests(test_cases, test_input):
    print("test_cases", test_cases)
    print("test_input", test_input)

    case_str = ''.join(re.findall(r"[A-Za-z_]+", test_cases))

    match case_str:
        case 'set_on_off_status':
            state_numbers = [ int(x) for x in test_input ]

            req.light_action_state(state_numbers[0])

        case 'set_color':

            rgb_numbers = [ int(x) for x in test_input ]

            req.light_action_color(rgb_numbers[0], rgb_numbers[1], rgb_numbers[2])

        case 'set_color_temperature':

            color_temperature_input_number = [ int(x) for x in test_input ]
            req.light_action_color_temperature(color_temperature_input_number[0])

            color_temperature = int(read_ini_file('color_temperature'))

        case 'set_brightness':

            brightness_input_number = [ int(x) for x in test_input ]
            req.light_action_brightness(brightness_input_number[0])

        case 'set_channel':
            channel = [ int(x) for x in test_input ]

            req.tv_action_channel(channel[0])

        case 'set_on_off_status_tv':
            state_numbers = [ int(x) for x in test_input ]

            req.tv_action_state(state_numbers[0])

        case 'set_volume':
            volume = [ int(x) for x in test_input ]

            req.tv_action_volume(volume[0])

        case _:
            print("Match error")

    return False

def run_test_lists(case_list):
    for test_cases in case_list:
        if 0 == len(test_cases):
            continue

        for case in test_cases:
            if None == case:
                continue

            print(str(case))
            test_input = _get_input_from_test_cases(case)
            run_tests(case, test_input)
            time.sleep(3)

    return True


def run_test_sequences(case_sequences):
    for case in case_sequences:
        if None == case:
            continue

        print(str(case))
        test_input = _get_input_from_test_cases(case)
        run_tests(case, test_input)

    return True
