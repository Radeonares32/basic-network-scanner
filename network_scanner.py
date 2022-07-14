import scapy.all as scapy

arp_request_packet = scapy.ARP(pdst="192.168.8.1/24")

broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")


combined_packet = broadcast_packet/arp_request_packet

(answer,unaswered) =scapy.srp(combined_packet,timeout=1)

answer.summary()


#scapy.ls(scapy.Ether())
#scapy.ls(scapy.ARP())