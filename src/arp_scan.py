#! /usr/bin/env python
from scapy.all import *

def arp_monitor_callback(pkt):
    if ARP in pkt and pkt[ARP].op in (1,2): #who-has or is-at
        return pkt.sprintf("%ARP.hwsrc% %ARP.psrc%")


print("capturing packets, press ctl-c to open in wireshark and continue capturing in background, press ctl-z to exit")
packets = sniff(prn=arp_monitor_callback, filter="arp")

wireshark(packets)
