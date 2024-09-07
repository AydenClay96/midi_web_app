import socket
import mido

HOST = "192.168.1.191"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        with mido.open_input() as inport:
            for msg in inport:
                print(msg)
