#!/usr/bin/python

import json
import time
import datetime
import sys
import getopt
import getpass
from modules.utilities import authentication
from modules.lun import lun

ts = time.time()
timestamp_str = \
    datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
remove_script_file = "remove_script_" + timestamp_str
file_out = open(remove_script_file, 'w')

invoking_user = getpass.getuser()
desc_string = "Created via Python by " + invoking_user + " - " + timestamp_str
print desc_string

myopts, args = getopt.getopt(sys.argv[1:],
                             "c:i:u:p:s:m:v:",
                             ["config_file=",
                              "ip=",
                              "user=",
                              "pw=",
                              "source_lun=",
                              "mirror_lun=",
                              "volume_group="])

for o, a in myopts:
    if o in ("-i", "--ip"):
        invicta_ip = a
    elif o in ("-u", "--user"):
        invicta_user = a
    elif o in ("-p", "--pw"):
        invicta_pw = a
    elif o in ("-c", "--config_file"):
        config_file = a
    elif o in ("-s", "--source_lun"):
        source_lun = a
    elif o in ("-m", "--mirror_lun"):
        mirror_lun = a
    elif o in ("-v", "--volume_group"):
        lun_vg = a
    else:
        print("Usage: %s --ip <ip> --user <user_name> --pw <password>\
               [--config_file [config_file]] [--source_lun [lun]]\
               [--mirror_lun [lun_name]]" % sys.argv[0])

if 'config_fie' in locals():

    json_config_data = open(config_file)
    InvictaTemplates = json.load(json_config_data)

    for inv_temp in InvictaTemplates.keys():
        luns = InvictaTemplates[inv_temp]['luns']

        for lun_to_mirror in luns.keys():
            token = authentication.login(invicta_ip, invicta_user, invicta_pw)
            lun_vg = luns[lun_to_mirror]['mirror'].values()[0]
            new_mirror_lun = luns[lun_to_mirror]['mirror'].keys()[0]

            lun.mirror_lun(
                invicta_ip,
                token,
                lun_to_mirror,
                new_mirror_lun,
                lun_vg)
elif 'source_lun' in locals():
            token = authentication.login(invicta_ip, invicta_user, invicta_pw)

            lun.mirror_lun(
                invicta_ip,
                token,
                source_lun,
                mirror_lun,
                lun_vg)
