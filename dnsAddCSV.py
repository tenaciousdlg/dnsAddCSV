#!/usr/bin/env python
# Script to import DNS records from a CSV file. Your CSV should be in the following format:
## type,key,value
#-----------------------------------------
## EXAMPLE:
# A,tom.atxflare.cf.,1.1.1.1
# CNAME,jerry.atxflare.cf,mouse.example.com
#-----------------------------------------

import csv
import CloudFlare

values = []
with open('./test.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        values.append(row)

keys = ['type', 'name', 'content']
dnsRecords = []

for value in values:
    dnsRecords.append(dict(zip(keys, value)))

zone_name = 'example.com'
cf = CloudFlare.CloudFlare()
zone = cf.zones.get(params={'zone_name': "[domain]",'per_page': 1})
zone_id = zone[0]["id"]

for record in dnsRecords:
    r = cf.zones.dns_records.post(zone_id, data = record)

exit(0)
