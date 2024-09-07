import socket
import midi
import serial

# Connection IP and port.
HOST = "192.168.1.191"
PORT = 65432

# Get serial ports and find midi device.
ports = ['COM%s' % (i + 1) for i in range(256)]
result = []
for port in ports:
    try:
        s = serial.Serial(port)
        s.close()
        result.append(port)
    except (OSError, serial.SerialException):
        pass
print(result)

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     while True:
#         msg = "received"
#         print(msg)
