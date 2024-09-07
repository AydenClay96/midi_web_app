import socket
import midi
import win32com.client

# Connection IP and port.
HOST = "192.168.1.191"
PORT = 65432

# Get USB devices attached.
wmi = win32com.client.GetObject("winmgmts:")
for usb in wmi.InstancesOf ("Win32_USBHub"):
    print(usb.DeviceID)

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     while True:
#         msg = "received"
#         print(msg)
