import os, sys


def obtain_web_file_path():
    path = input("input web file path(default this spec abspath >>> ")
    if not path:
        path = os.path.dirname(os.path.realpath(sys.argv[0]))
    print(path)
    return path


def obtain_zip_path():
    path = input("input web file path(default save desktop >>> ")
    if not path:
        path = get_desktop_path()
    return path


def get_desktop_path():
    """obtain desktop path"""
    return os.path.join(os.path.expanduser("~"), 'Desktop')

