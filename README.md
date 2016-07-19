# DNS-O-Matic – Update your IP Address on OpenDNS

## What
This Python script allows Meraki users to update the IP Addresses of their MR
and MX products on OpenDNS using the Meraki Provisioning API and DNS-O-Matic
API.

## Why
Why do you even need this script? Our MR and MX products update their IP
Addresses every so often. And if you use OpenDNS to describe policies for your
devices using IP Addresses, they may not act appropriately as the device IP
addresses are changing. We need to be able to update the IP Addresses of our
devices on OpenDNS. We can usually do this manually, but when we have thousands
of devices across countless networks, this can be a not-so-fun task. This script
allows us to solve this issue in an easy, automated fashion.

## How to run
In order to update the IP Addresses of your Meraki devices on OpenDNS, you will
run the above script from your command line.  

Install the modules specified in requirements.txt using [pip](https://pip.pypa.io/en/stable/installing/), a package manager
for [Python](https://www.python.org/).

    pip install -r requirements.txt

If you don't want to use the requirements.txt file, you can install the requests
module yourself as well. Using pip, try running this from the command line:

    pip install requests

After you have installed all the required modules, you can run the following
from the command line:

    python update_ip_addr_dns.py [X-Cisco-Meraki-API-Key] [DNS-O-Matic-USER]:[DNS-O-Matic-PASS] [device_type1, device_type2]

For example, when I try updating the IP Addresses of my MR devices on all of my
networks, I run the following command (the password and API key are fake):

    python update_ip_addr_dns.py 8943qjkewasdf98q34 shubhi.jain@meraki.com:mypassword MR

And voila! You will now have updated your IP Addresses for your specific devices
on OpenDNS.

## Getting Help
- [How to get a X-Cisco-Meraki-API-Key](https://documentation.meraki.com/zGeneral_Administration/Other_Topics/The_Cisco_Meraki_Provisioning_API)
- [What is OpenDNS](https://www.opendns.com/)
- [What is DNS-O-Matic](https://dnsomatic.com/)
- [What is Python](https://www.python.org/)
