from datetime import datetime

time_arr = []


def packet_testing(ip):
    import scapy.all as scapy
    from scapy.layers.inet import IP, ICMP

    alive_packets = 0
    dead_packets = 0

    for i in range(4):
        start_time = datetime.now()
        packet = IP(dst=str(ip), ttl=2) / ICMP()
        response = scapy.sr1(packet, timeout=1, verbose=False)
        stop_time = datetime.now()
        if response is not None:
            alive_packets += 1
        else:
            dead_packets += 1

        total_time = stop_time - start_time
        time, millisec = str(total_time).split('.')
        millisec = int(millisec)//1000
        time_arr.append(millisec)

        ratio = (dead_packets)*100/(alive_packets + dead_packets)
        #print(f"Total {packets_sent} packets were sent to {ip}.")
        print("replying from {} Total Time {}ms with {}% packet loss".format(
            ip, millisec, ratio))

    return alive_packets, dead_packets


ip = input("Enter ip to send packets: ")
alive_packets, dead_packets = packet_testing(ip)
print("Packets: Sent = {} Received = {} Lost = {}".format(
    4, alive_packets, dead_packets))
average_time = sum(time_arr)//4
print("Average round trip time: {}ms".format(average_time))
