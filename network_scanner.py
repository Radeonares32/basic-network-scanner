from click import argument
import scapy.all as scapy
import optparse as parse


def user_input():
    parse_object = parse.OptionParser()
    parse_object.add_option("-i", "--ipaddress",
                            dest="ip_address_varrib", help="Enter IP Address")
    (user_inp, arguments) = parse_object.parse_args()

    if not user_inp.ip_address_varrib:
        print("Enter IP Address")
    return user_inp
def scan(ip):
    arp_request_packet = scapy.ARP(pdst=ip)

    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    combined_packet = broadcast_packet/arp_request_packet

    (answer, unaswered) = scapy.srp(combined_packet, timeout=1)

    answer.summary()

user_ip_address = user_input()
scan(user_ip_address.ip_address_varrib)

# scapy.ls(scapy.Ether())
# scapy.ls(scapy.ARP())
