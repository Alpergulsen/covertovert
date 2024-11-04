from scapy.all import IP, ICMP, send

def send_icmp():
    packet = IP(dst="receiver", ttl=1) / ICMP()
    send(packet)
    print("ICMP packet sent with TTL=1")

if __name__ == "__main__":
    send_icmp()
