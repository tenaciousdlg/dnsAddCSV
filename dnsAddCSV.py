#!/usr/bin/env python
import csv
import CloudFlare
import argparse
import time #testing

parser = argparse.ArgumentParser(description='DNS Records from CSV')
parser.add_argument("-i", default=None, required=True, type=str, help="Relative location of CSV file. Example: -i ./test.csv")
parser.add_argument("-z", default=None, required=True, type=str, help="Name of Cloudflare domain such as example.com")
parser.add_argument("-a", required=True, type=str, help="Name of the Cloudflare account that the zone is in such as Example Sites")
args = parser.parse_args()

file = args.i
zone = args.z
account = args.a

values = []
with open(file) as f:
    reader = csv.reader(f)
    for row in reader:
        values.append(row)

keys = ['type', 'name', 'content']
dnsRecords = []
for value in values:
    dnsRecords.append(dict(zip(keys, value)))

cf = CloudFlare.CloudFlare()

accountData = cf.accounts.get(params = {'name': account,'per_page':1})
accountId = accountData[0]['id']
accountName = accountData[0]['name']
print('Using ' + accountName + ' for the account.') #testing
time.sleep(5) #testing

zoneData = cf.zones.get(params = {'name':zone,'account.id':accountId,'per_page':1})
zoneId = zoneData[0]['id']
zoneName = zoneData[0]['name']
print('Using ' + zoneName + ' as the zone we are adding the records to.') #testing
time.sleep(5) #testing

try:
    for record in dnsRecords:
        r = cf.zones.dns_records.post(zoneId, data = record)
except CloudFlare.exceptions.CloudFlareAPIError as e:
    exit('/zones.get %d %s - api call failed' % (e, e))
except Exception as e:
    exit('/zones.get - %s - api call failed' % (e))
exit(0)
