import configparser
import time
from filelock import FileLock

CONFIG_FILE = "/tmp/sinric_config.ini"

LOCK_FILE = CONFIG_FILE + ".lock"

def read_ini_file(key, section = 'light'):
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)

    if key not in config[section]:
        print(f"Key '{key}' not found in section'.")
        return None

    print("read", config[section][key])
    return config[section][key]

def set_ini_file(key, value, section = 'light'):
    lock = FileLock(LOCK_FILE)

    with lock:
        config = configparser.ConfigParser()

        config.read(CONFIG_FILE)

        config[section][key] = value

        with open(CONFIG_FILE, 'w') as configfile:
            config.write(configfile)

    time.sleep(1)

def set_ini_file_color(r, g, b):
    lock = FileLock(LOCK_FILE)

    with lock:
        config = configparser.ConfigParser()

        config.read(CONFIG_FILE)

        config['light']['r'] = str(r)
        config['light']['g'] = str(g)
        config['light']['b'] = str(b)

        with open(CONFIG_FILE, 'w') as configfile:
            config.write(configfile)

    time.sleep(1)

def set_initial_value():
    lock = FileLock(LOCK_FILE)

    with lock:
        config = configparser.ConfigParser()

        config.read(CONFIG_FILE)

        config['light']['r'] = str(-1)
        config['light']['g'] = str(-1)
        config['light']['b'] = str(-1)
        config['light']['color_temperature'] = str(-1)
        config['light']['brightness'] = str(-1)
        config['light']['color_temperature'] = str(-1)
        config['light']['power'] = str(False)
        config['tv']['power'] = str(False)
        config['tv']['volume'] = str(-1)
        config['tv']['channel'] = str(-1)

        with open(CONFIG_FILE, 'w') as configfile:
            config.write(configfile)

    time.sleep(1)



