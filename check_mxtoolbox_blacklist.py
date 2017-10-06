#!/usr/bin/env python

#######################################################
#
# check_mxtoolbox_blacklist.py
#
# initial:  2017-10-06, reynlds@illinois.edu
#
# This script will check the status of any host against
# the MXToolbox blacklist listing.
#
# Required variables:  an auth key and a hostname
#
#######################################################

import json, requests, argparse, re, sys
parser = argparse.ArgumentParser()
parser.add_argument('HOST', type=str, help='This is the hostname that will be checked for a blacklist entry by MXToolbox.')
parser.add_argument('AUTH', type=str, help='This is the authorization needed for the check. Most often, it will be in the form of a key string')
args = parser.parse_args()
HOST = str(args.HOST)
AUTH = str(args.AUTH)
URL = 'https://api.mxtoolbox.com/api/v1/Monitor?Authorization=' + AUTH + '&name=' + HOST
req = requests.get(URL)
result = str('Not Blacklisted' in str(json.loads(req.text)))
if result == 'True':
    print 'Not Blacklisted'
else:
    print 'Blacklisted'

