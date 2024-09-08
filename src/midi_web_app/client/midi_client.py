import socket
import pygame
from pygame import midi


HOST = "192.168.1.191"
PORT = 65432
MIDI = b'Roland Digital Piano'


def find_devices() -> midi.Input:
    """Finds the midi devices connected to the client machine."""
    pygame.init()
    midi.init()
    # Find all midi devices connected.
    devices = []
    for i in range(32):
        dev = midi.get_device_info(i)
        if dev:
            devices.append(dev)

    # Organize them into input and output devices.
    inputs = {}
    outputs = {}
    for index, device in enumerate(devices):
        name = device[1]
        if device[2] == 1:
            inputs[name] = index
        else:
            outputs[name] = index

    # Find the Roland device that I own.
    return midi.Input(inputs[MIDI])

def client_connect(midi_device: midi.Input) -> None:
    """connects the client midi device to the server socket.

    Parameters
    ----------
    midi_device : midi.Input
        from pygame, a midi input device.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect via the socket.
        s.connect((HOST, PORT))
        # While connected:
        while True:
            # If there is data yet to send.
            if midi_device.poll():
                # Read the first message on the buffer.
                msg = midi_device.read(1)[0]
                data = msg[0]
                time = msg[1]
                msg_str = ",".join([str(e) for e in data])
                msg_str += str(time)
                # Sends a byte-string of the entire data stream:
                # [[type, note, velocity], timestamp]
                print(f"{msg} = {msg_str}")
                s.sendall(str.encode(msg_str))

def main():
    midi = find_devices()
    client_connect(midi)

if __name__ == "__main__":
    main()
