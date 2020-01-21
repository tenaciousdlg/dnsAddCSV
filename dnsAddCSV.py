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
import argparse

parser = argparse.ArgumentParser(description='DNS Records from CSV')
parser.add_argument("-i", default=None, required=True, type=str, help="Relative location of CSV file. Example: -i ./test.csv")
parser.add_argument("-z", default=None, required=True, type=str, help="Name of Cloudflare domain such as example.com")
args = parser.parse_args()

file = args.i
zone = args.z

values = []
with open(file) as f:
    reader = csv.reader(f)
    for row in reader:
        values.append(row)

keys = ['type', 'name', 'content']
dnsRecords = []
for value in values:
    dnsRecords.append(dict(zip(keys, value)))

zone_name = zone
cf = CloudFlare.CloudFlare()
zone_data = cf.zones.get(params={'zone_name': "[domain]",'per_page': 1})
zone_id = zone_data[0]["id"]

for record in dnsRecords:
    r = cf.zones.dns_records.post(zone_id, data = record)

exit(0)
