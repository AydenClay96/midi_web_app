import socket
import pygame
from pygame import midi

# Connection IP and port.
HOST = "192.168.1.191"
PORT = 65432

# Get Midi device.
pygame.init()
midi.init()

devices = []
for i in range(32):
    dev = midi.get_device_info(i)
    if dev:
        devices.append(dev)

inputs = {}
outputs = {}
for index, device in enumerate(devices):
    name = device[1]
    if device[2] == 1:
        inputs[name] = index
    else:
        outputs[name] = index

print(inputs)
midi_device = midi.Input(inputs[b'Roland Digital Piano'])

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        if midi_device.poll():
            msg = midi_device.read(1)[0]
            print(msg)
            data = msg[0]
            time = msg[1]
            msg_str = "".join([str(e) for e in data])
            msg_str += str(time)
            s.sendall(str.encode(msg_str))
