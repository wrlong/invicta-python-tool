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
    luns = InvictaTemplates[inv_temp]['luns']
    break_mode = "keep"

    for source_lun in luns.keys():
        token = authentication.login(invicta_ip, invicta_user, invicta_pw)
        lun_vg = luns[source_lun]['mirror'].values()[0]
        new_mirror_lun = luns[source_lun]['mirror'].keys()[0]

        lun.break_lun_mirror(
            invicta_ip,
            token,
            source_lun,
            break_mode)
