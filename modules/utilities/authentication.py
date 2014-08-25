#!/usr/bin/python

import requests
import json

def login(ip, user, password):
    login_url = 'https://' + ip + "/restapi/15/authenticate"
    login_data = 'data={"username":"' + user + '","password":"'
    login_data = login_data + password + '"}'
    login_headers = {'Accept':'application/json'}

    try:
        r = requests.post(login_url, login_data, verify=False, headers=login_headers)
        print "Successfully logged in to " + ip + " as user " + user
        return r.content[44:172]
    except LoginError:
        print("Error: Unable to login to " + ip)
