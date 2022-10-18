import os
from scapy.all import *
def showPacket(packet):
    #a = packet.show()
    #print(a)
    packet.display()
    print('#####################################################')

def sniffing(filter):
    sniff(filter = filter, prn = showPacket, count = 10)

if __name__ == '__main__':
    filter = None
  # can use protocol list == ['icmp', 'arp', 'rarp', 'tcp', 'udp'] and also can use 'or' sign / if filter == none, it can detact llc(ieee 802.3)
    sniffing(filter)
    
os.system('pause')




