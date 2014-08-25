#!/usr/bin/python

import json
import getopt
import sys
from modules.utilities import authentication
from modules.utilities import utilities
from modules.lun import lun
from modules.initiator import initiator

if __name__ == '__main__':

    time_start = utilities.current_time()
    desc_string = utilities.unique_description()


    try:
        myopts, args = getopt.getopt(sys.argv[1:], "c:i:u:p:", ["config_file=","ip=","user=","pw="])
    except getopt.GetoptError:
        print("Usage: %s --ip <ip> --user <user_name> --pw <password> --config_file <config_file>" % sys.argv[0])

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

    try:
        json_config_data = open(config_file)
        InvictaTemplates = json.load(json_config_data)
    except JsonLoadException:
        print("Error: Error loading JSON file for import.")

    for inv_temp in InvictaTemplates.keys():
        init_groups = InvictaTemplates[inv_temp]['initiator_groups']
        luns = InvictaTemplates[inv_temp]['luns']

        for init_group in init_groups.keys():
            token = authentication.login(invicta_ip, invicta_user, invicta_pw)

            initiator.create_initiator_group(
                invicta_ip,
                token,
                init_group)

            for wwpn in init_groups[init_group].values():
                initiator.create_initiator(
                    invicta_ip,
                    token,
                    init_group,
                    wwpn)

        for lun_to_create in luns.keys():
            token = authentication.login(invicta_ip, invicta_user, invicta_pw)
            lun_vg = luns[lun_to_create]['volume_group']
            lun_size = int(luns[lun_to_create]['size'])
            lun_init_groups = luns[lun_to_create]['initiator_groups']

            lun.create_lun(
                invicta_ip,
                token,
                lun_to_create,
                lun_vg,
                lun_size,
                "testvg01",
                "true")

            for lun_init_group in lun_init_groups.keys():
                lun_id = lun_init_groups[lun_init_group]

                lun.map_lun(
                    invicta_ip,
                    token,
                    lun_init_group,
                    lun_to_create,
                    lun_id)
