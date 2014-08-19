#!/usr/bin/python

import requests
import json

def create_initiator_group(ip, token, init_group_name):
    api_url = 'https://' + ip + "/restapi/15/" + token + "/initiatorgroup"
    #api_url = api_url + init_group_name

    api_data = 'data={"name":"' + init_group_name + '"}'

    api_headers = {'Accept':'application/json'}


    r = requests.post(api_url, api_data, verify=False, headers=api_headers)
    #print r.content
    print "Created initiator group " + init_group_name

def delete_initiator_group(ip, token, init_group_name):
    api_url = 'https://' + ip + "/restapi/15/" + token + "/initiatorgroup"
    api_url = api_url + "/" + init_group_name

    #api_data = 'data={"name":"' + init_group_name + '"}'

    api_headers = {'Accept':'application/json'}


    #r = requests.post(api_url, api_data, verify=False, headers=api_headers)
    r = requests.delete(api_url, verify=False, headers=api_headers)
    #print r.content
    print "Deleted initiator group " + init_group_name

def create_initiator(ip, token, init_group_name, init_pwwn):
    api_url = 'https://' + ip + "/restapi/15/" + token + "/initiator"

    api_data = 'data={"name":"' + init_group_name + '",'
    api_data = api_data + '"initiator":"' + init_pwwn + '"}'

    api_headers = {'Accept':'application/json'}


    r = requests.post(api_url, api_data, verify=False, headers=api_headers)
    #print r.content
    print "Created initiator " + init_pwwn + " in initiator group " + init_group_name
