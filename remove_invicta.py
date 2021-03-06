#!/usr/bin/python

import json
import time
import datetime
import sys
import getopt
import getpass
from modules.utilities import authentication
from modules.lun import lun
from modules.initiator import initiator

ts = time.time()
timestamp_str = \
    datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
remove_script_file = "remove_script_" + timestamp_str
file_out = open(remove_script_file, 'w')

invoking_user = getpass.getuser()
desc_string = "Created via Python by " + invoking_user + " - " + timestamp_str
print desc_string

config_file = "invicta_config-2xESXjson"

myopts, args = getopt.getopt(sys.argv[1:], "c:i:u:p:", ["config_file=","ip=","user=","pw="])

for o, a in myopts:
    if o in ("-i", "--ip"):
        invicta_ip = a
    elif o in ("-u", "--user"):
        invicta_user = a
    elif o in ("-p", "--pw"):
        invicta_pw = a
    elif o in ("-c", "--config_file"):
        config_file = a
    else:
        print("Usage: %s --ip <ip> --user <user_name> --pw <password> --config_file <config_file>" % sys.argv[0])

json_config_data = open(config_file)
InvictaTemplates = json.load(json_config_data)

for inv_temp in InvictaTemplates.keys():
    init_groups = InvictaTemplates[inv_temp]['initiator_groups']
    luns = InvictaTemplates[inv_temp]['luns']

    for init_group in init_groups.keys():
        token = authentication.login(invicta_ip, invicta_user, invicta_pw)

        initiator.delete_initiator_group(
            invicta_ip,
            token,
            init_group)

    for lun_to_delete in luns.keys():
        token = authentication.login(invicta_ip, invicta_user, invicta_pw)

        lun.delete_lun(
            invicta_ip,
            token,
            lun_to_delete)
