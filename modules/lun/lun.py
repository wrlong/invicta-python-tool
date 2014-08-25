#!/usr/bin/python

import requests
import json

def create_lun(ip, token, lun_name, lun_vg, lun_size, lun_dg, lun_striping):
    api_url = 'https://' + ip + "/restapi/15/" + token + "/lun"
    api_data = 'data={"name":"' + lun_name + '",'
    api_data = api_data + '"vg":"' + lun_vg + '",'
    api_data = api_data + '"size":' + str(lun_size) + '}'
    api_headers = {'Accept':'application/json'}

    try:
        r = requests.post(api_url, api_data, verify=False, headers=api_headers)
        print "Created lun " + lun_name + " with size " + str(lun_size) + " in volume group " + lun_vg
    except CreateLunError:
        print("Error:  Error creating lun " + lun_name)

def delete_lun(ip, token, lun_name):
    api_url = 'https://' + ip + "/restapi/15/" + token + "/lun"
    api_url = api_url + "/" + lun_name
    api_headers = {'Accept':'application/json'}

    try:
        r = requests.delete(api_url, verify=False, headers=api_headers)
        print "Deleted lun " + lun_name
    except DeleteLunError:
        print("Error:  Unable to delete LUN " + lun_name)

def map_lun(ip, token, init_group_name, lun_name, mapped_lun_id):
    api_url = 'https://' + ip + "/restapi/15/" + token + "/maplun"
    api_data = 'data={"name":"' + init_group_name + '",'
    api_data = api_data + '"lunName":"' + lun_name + '",'
    api_data = api_data + '"id":' + str(mapped_lun_id) + '}'
    api_headers = {'Accept':'application/json'}

    try:
        r = requests.post(api_url, api_data, verify=False, headers=api_headers)
        print "Mapped lun " + lun_name + " with id " + str(mapped_lun_id) + " to initiator group " + init_group_name
    except MapLunError:
        print("Error: Unable to map LUN " + lun_name)

def mirror_lun(ip, token, source_lun_name, target_lun_name, vg):
    api_url = 'https://' + ip + "/restapi/16/" + token + "/lunmirror"
    api_data = 'data={"lun":"' + source_lun_name + '",'
    api_data = api_data + '"mirror":"' + target_lun_name + '",'
    api_data = api_data + '"vg":"' + vg + '"}'
    api_headers = {'Accept':'application/json'}

    try:
        print "Mirroring lun " + source_lun_name + " to " + target_lun_name
        r = requests.post(api_url, api_data, verify=False, headers=api_headers)
        print "Completed mirroring lun " + source_lun_name + " to " + target_lun_name
    except MirrorLunError:
        print("Error:  Unable to mirror LUN " + source_lun_name)

def break_lun_mirror(ip, token, source_lun_name, break_mode="keep"):
    api_url = 'https://' + ip + "/restapi/16/" + token + "/lunmirror"
    api_url = api_url + "/" + source_lun_name
    api_data = 'data={"breakMode":"' + break_mode + '"}'
    api_headers = {'Accept':'application/json'}

    try:
        r = requests.delete(url=api_url, data=api_data, verify=False, headers=api_headers)
        print "Broke mirrored lun " + source_lun_name
    except BreakLunMirrorError:
        print("Error: Unable to break lun mirror for " + source_lun_name)
