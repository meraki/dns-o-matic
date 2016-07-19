# DNS-O-Matic – Update your IP Address on OpenDNS

## What
This Python script allows Meraki users to update the IP Addresses of their MR
and MX products on OpenDNS using the Meraki Provisioning API and DNS-O-Matic
API.

## How to run
Install the modules specified in requirements.txt using [pip](https://pip.pypa.io/en/stable/installing/), a package manager
for Python.

    pip install -r requirements.txt

If you don't want to use the requirements.txt file, you can install the requests
module yourself as well. Using pip, try running this from the command line:

    pip install requests

After you have installed all the required modules, you can run the following
from the command line:

    python update_ip_addr_dns.py [X-Cisco-Meraki-API-Key] [DNS-O-Matic-USER]:[DNS-O-Matic-PASS] [device_type1, device_type2]

And voila! You will now have updated your IP Addresses for your specific devices
on OpenDNS.
