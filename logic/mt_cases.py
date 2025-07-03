import random
import colorsys

def _rgb_to_hsl(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return h * 360, s * 100, l * 100

def _hsl_to_rgb(h, s, l):
    h, s, l = h / 360.0, s / 100.0, l / 100.0
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    return int(r * 255), int(g * 255), int(b * 255)

def _analogous_colors(rgb, angle = 90):
    h, s, l = _rgb_to_hsl(*rgb)
    hue = (h + angle) % 360
    rgb = _hsl_to_rgb(hue, s, l)

    return rgb

def switch_mrs(cases, initial_state):
    if "On" == initial_state:
        cases.append("set_on_off_status-0")
        cases.append("set_on_off_status-1")
    elif "Off" == initial_state:
        cases.append("set_on_off_status-1")
        cases.append("set_on_off_status-0")

    return

def switch_mr_tv(cases, initial_state):
    if "On" == initial_state:
        cases.append("set_on_off_status_tv-0")
        cases.append("set_on_off_status_tv-1")
    elif "Off" == initial_state:
        cases.append("set_on_off_status_tv-1")
        cases.append("set_on_off_status_tv-0")

    return

def color_flip(cases, raw_r, raw_g, raw_b):
    flip_color_r = 255 - raw_r
    flip_color_g = 255 - raw_g
    flip_color_b = 255 - raw_b

    append_info = "set_color-" + str(flip_color_r) + " " + str(flip_color_g) + " " + str(flip_color_b)
    cases.append(append_info)

    mt_color_r = 255 - flip_color_r
    mt_color_g = 255 - flip_color_g
    mt_color_b = 255 - flip_color_b

    append_info = "set_color-" + str(mt_color_r) + " " + str(mt_color_g) + " " + str(mt_color_b)
    cases.append(append_info)

    return

def color_analogous(cases, raw_r, raw_g, raw_b):
    angle = 360

    h, s, l = _rgb_to_hsl(raw_r, raw_g, raw_b)
    hue = (h + angle) % 360
    r, g, b = _hsl_to_rgb(hue, s, l)
    append_info = "set_color-" + str(r) + " " + str(g) + " " + str(b)
    cases.append(append_info)

    return

    for _ in range(3):
        h, s, l = _rgb_to_hsl(r, g, b)
        hue = (h + angle) % 360
        r, g, b = _hsl_to_rgb(hue, s, l)
        append_info = "set_color-" + str(r) + " " + str(g) + " " + str(b)
        cases.append(append_info)
    return

def volume_adjust(cases, current_volume):
    delta = 3
    up = current_volume + delta
    up_up = up + delta
    down = up_up - delta
    down_down = down - delta

    cases.append(f"set_volume-{up}")
    cases.append(f"set_volume-{up_up}")
    cases.append(f"set_volume-{down}")
    cases.append(f"set_volume-{down_down}")

    return

def channel_adjust(cases, current_channel):
    next1 = current_channel + 1
    next2 = current_channel + 2

    cases.append(f"set_channel-{next1}")
    cases.append(f"set_channel-{next2}")
    cases.append(f"set_channel-{current_channel}")

    return

def add_random_mt_to_test_sequences(cases, r, g, b, switch, index):
    #rand = random.randint(0, 2)
    rand = index % 3

    match rand:
        case 0:
            switch_mrs(cases, switch)
        case 1:
            color_flip(cases, r, g, b)
        case 2:
            color_analogous(cases, r, g, b)
        case _:
            return

    return

def add_random_tv_mt_to_test_sequences(cases, switch, channel, volume, index):
    rand = index % 3

    match rand:
        case 0:
            switch_mr_tv(cases, switch)
        case 1:
            volume_adjust(cases, volume)
        case 2:
            channel_adjust(cases, channel)
        case _:
            return


    return
