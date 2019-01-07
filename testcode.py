#!usr/bin/env python3

import requests
import base64
import logging
import httplib

# Debug logging
httplib.HTTPConnection.debuglevel = 1
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
req_log = logging.getLogger('requests.packages.urllib3')
req_log.setLevel(logging.DEBUG)
req_log.propagate = True

url = 'https://connect-shared-sandbox-2445582615332.production.gw.apicast.io/v1'
headers = {'Content-Type' : 'application/json', 'app_id' : 'fb4124da', 'app_key' : ''}

# This call returns the version and chains
r = requests.get(url, headers=headers)

print(r.text)
headers = {'Content-Type' : 'application/json', 'app_id' : 'fb4124da', 'app_key' : ''}
chain_endpoint = "https://connect-shared-sandbox-2445582615332.production.gw.apicast.io/v1/chains"

# ext_id = base64.encodestring(b'9000')
# print(ext_id)
payload = "{\"external_ids\":[\"9000\"],\"content\":\"VGhpcyBpcyB0aGUgaGlzdG9yeSBvZiBXb3JsZCBXYXIgMi4=\"}"
# create a chain
z = requests.post(chain_endpoint, headers=headers, data=payload)

print(z.text)

#query the chain
y = requests.get(chain_endpoint, headers=headers)

print(y.text)

#search for my newly created chain
payload = "{\"external_ids\":[\"9000\"]}"
q = requests.post(chain_endpoint + "/search", headers=headers, data=payload)

print("Newly created chain is " + q.text)

entry = base64.encodestring("Hi.")
#create a new entry in the chain we created (chain_id == 9000)
# payload = "{\"external_ids\":[\"1939\"],\"content\":" + entry + "}"
payload = "{\"external_ids\":[\"1939\"],\"content\":\"IlRoZSBJbnZhc2lvbiBvZiBQb2xhbmQgYnkgTmF6aSBHZXJtYW55IHN0YXJ0cyBhdCA0OjQ1IGEubS4gd2l0aCB0aGUgTHVmdHdhZmZlIGF0dGFja2luZyBzZXZlcmFsIHRhcmdldHMgaW4gUG9sYW5kLiI=\"}"
print(payload)
t = requests.post(chain_endpoint + "/9000/entries", headers=headers, data=payload)

print(t.text)

# This is erroring out and giving me a 500 Internal Server Error.
