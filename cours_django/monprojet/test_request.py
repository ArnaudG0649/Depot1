#!/bin/env python3

import requests

r = requests.get('http://127.0.0.1:7000/monappli/URL_de_reception')
# print(f"status_code: {r.status_code}, headers: {r.headers}")
# print(f"content-type: {r.headers['content-type']}")
# print(f"encoding: {r.encoding}")
# print(f"text: {r.text}") 

print(r.request)