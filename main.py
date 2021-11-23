"""
Change your Ethernet interface quickly static|dhcp

Author: Christian M. Fulton
Date: 23.Nov.2021
"""


def main():
    """
    exe
    """

def set_iface():
    """
    func to set interface
    """
    interface = input('Set interface to Static or DHCP?')
    if interface.lower() == 'static':
        # ask for the address and subnet
        pass
    elif interface.lower() == 'dhcp':
        # use netsh to set interface to dhcp
        pass

def set_static(address, subnet):
    """
    set the static ip address
    """
    NotImplementedError