import json, commands, re
import pprint

machines = json.loads(commands.getstatusoutput('rs_tag -q "couchbase:cluster"')[1])

internal_addresses = []
external_addresses = []
host_string = ''

for machine,tags in machines.items():
    for tag in tags['tags']:
        if re.match('ip:internal', tag):
            ip = re.sub(r'^ip:internal=', '', tag)
            internal_addresses.append(ip)
        if re.match('ip:external', tag):
            ip = re.sub(r'^ip:external=', '', tag)
            external_addresses.append(ip)
for internal_address in internal_addresses:
    host_string = host_string + "-h " + internal_address + " "

print host_string



