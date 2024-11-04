from scapy.all import sniff, IP, ICMP

def receive_icmp(packet):
    if IP in packet and ICMP in packet:
        if packet[IP].ttl == 1 and packet[ICMP].type == 8:  
            packet.show()

if __name__ == "__main__":
    print("Listening for ICMP packets...")
    sniff(filter="icmp", prn=receive_icmp)
