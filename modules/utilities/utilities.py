#!/usr/bin/python

import time
import datetime
import getpass

def pad_zeros(int_as_string, num_digits):
    return int_as_string.zfill(num_digits)

def int_to_string(int_to_convert):
    return str(int_to_convert)

def timestamp_str():
    return datetime.datetime.fromtimestamp(current_time()).strftime('%Y-%m-%d-%H-%M-%S')

def current_time():
    return time.time()

def invoking_user():
    return getpass.getuser()

def unique_description():
    return "Created via Python by " + invoking_user() + \
           " - " + timestamp_str()

