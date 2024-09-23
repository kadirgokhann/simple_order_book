import socket
import struct

# Multicast group details
MULTICAST_GROUP = '239.0.0.1'  # Replace with actual multicast group
PORT = 5000  # Replace with actual port

# Create the UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind to the port
sock.bind(('', PORT))

# Add the socket to the multicast group
mreq = struct.pack("4sl", socket.inet_aton(MULTICAST_GROUP), socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

# Listen for incoming data
while True:
    data, _ = sock.recvfrom(1024)  # Buffer size of 1024 bytes
    print(f"Received data: {data}")