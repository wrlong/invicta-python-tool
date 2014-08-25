invicta_python_tool
===============

A simple UCS Invicta configuration tool that interacts with the RESTful Invicta API for configuration and integration.

It modularizes key functions for the UCS Invicta API, supporting configuration via a JSON structured configuration file for simplified manipulation. 
 
### Important source files
- build_invicta.py - Main file to build a UCS Invicta environment.
- invicta_config<>.json - JSON configuraiton file required for build_invicta.py; Uses JSON format specifying Invicta constructs such as storage targets, LUNs, and initiator groups.
- remove_invicta.py - Main file to remove a UCS Invicta environment with JSON configuration file as input.

### Usage
#### To build:
build_invicta.py -i `ip` -u `user` -p `password` -c `json config file`
```bash
$ build_invicta.py -i 192.168.10.10 -u admin -p cisco123 -c invicta_config-2xESX.json 
```
#### To remove:
remove_invvicta.py -i `ip` -u `user` -p `password` -c `json config file`
```bash
$ remove_invicta.py -i 192.168.10.10 -u admin -p cisco123 -c invicta_config-2xESX.json 
```
