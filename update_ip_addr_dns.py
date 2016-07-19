'''
This script updates the IP Address of dynamically updated IP Addresses for all
APs via DNS O Matic.
'''
import requests
import itertools
import sys


## CONSTANTS
USAGE = '''
CORRECT USAGE:
python update_ip_addr_dns.py [X-Cisco-Meraki-API-Key] [DNS-O-Matic-USER]:[DNS-O-Matic-PASS] [device_type1, device_type2]
e.g.
python update_ip_addr_dns.py 8943qjkewasdf98q34 shubhi.jain@meraki.com:mypassword MR,MX
'''

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(USAGE)
        exit(1)

    # USER-ENTERED
    API_KEY = sys.argv[1]
    USER_PWD = sys.argv[2]
    DEVICES = sys.argv[3].split(',')

    # FIXED
    MERAKI_URL = 'https://dashboard.meraki.com/api/v0/'
    DNS_O_URL  = 'https://' + USER_PWD + '@updates.dnsomatic.com/nic/update'

    # Grab all organizations administrated by this user
    headers = {'X-Cisco-Meraki-API-Key':API_KEY}
    orgs = requests.get(MERAKI_URL + 'organizations', headers=headers)

    # Incorrect Cisco Meraki API Key
    if orgs.status_code != 200:
        print('Incorrect X-Cisco-Meraki-API-Key')
        exit(1)
    else:
        orgs = orgs.json()

    # Grab all networks from all organizations and flatten into list of dictionaries
    networks = list(itertools.chain(*[requests.get(MERAKI_URL +
        'organizations/' + str(org['id']) + '/networks',
        headers=headers).json() for org in orgs]))

    # Grab all devices in all networks & filter on ONLY specific devices
    devices = filter(lambda x: x['model'][:2] in DEVICES,
        list(itertools.chain(*[requests.get(MERAKI_URL + 'organizations/' +
        str(net['organizationId']) + '/networks/' + str(net['id']) + '/devices',
        headers=headers).json() for net in networks])))

    # Update IP Addresses accordingly
    dns_data = {}
    headers = {'User-Agent':'Meraki - IP Update Test - 0.1'}
    for device in devices:
        # Define DNS-O-Matic GET Request headers
        dns_data['hostname'] = device['name']
        if device['model'][:2] == 'MR':
            dns_data['myip']     = device['lanIp']
        else:
            dns_data['myip']     = device['wan1Ip']
        r = requests.get(DNS_O_URL, data=dns_data, headers=headers)
        # Incorrect DNS-O-Matic Auth
        if r.text == 'badauth':
            print('Incorect DNS-O-Matic Username & Password')
            exit(1)
        # Update results
        if r.text.split(' ')[0] == 'good':
            print('%s updated its IP address to %s' % (device['name'], dns_data['myip']))
        else:
            print('%s failed to update its IP address' % device['name'])
