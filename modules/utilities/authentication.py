#!/usr/bin/python

import requests
import json

def login(ip, user, password):
    login_url = 'https://' + ip + "/restapi/15/authenticate"
    login_data = 'data={"username":"' + user + '","password":"'
    login_data = login_data + password + '"}'

    login_headers = {'Accept':'application/json'}

    #print login_url
    #print login_data
    #print login_headers

    r = requests.post(login_url, login_data, verify=False, headers=login_headers)
    #print r.content
    #print r.content[44:172]
    #return r.content[44:172]
    print "Successfully logged in to " + ip + " as user " + user
    return r.content[44:172]
