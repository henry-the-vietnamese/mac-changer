#!/usr/bin/env python3

#
# File:         main.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         4/10/2021
# Description:  Change the machine's current MAC address.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.
#

"""
The first module is to access the terminal for inputting user commands.
The second module contains the function required to generate a new MAC address.
"""

import subprocess
import new_mac 

# Specify the network interface.
interface = 'eth0'

# Inform user of the change.
print(f'[+] Changing the MAC address for {interface} to {new_mac.NewMac()}.')

# The process of changing the current MAC address.
subprocess.call(f'ifconfig {interface} down', shell=True)
subprocess.call(f'ifconfig eth0 hw ether {new_mac.NewMac()}', shell=True)
subprocess.call(f'ifconfig {interface} up', shell=True)
