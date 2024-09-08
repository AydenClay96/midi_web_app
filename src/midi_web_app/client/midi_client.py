import socket
from time import sleep

import pygame
from pygame import midi

from utils.message import midi_to_msg

HOST = "192.168.1.191"
PORT = 65432
MIDI = b"Roland Digital Piano"


def find_devices() -> midi.Input:
    """
    Finds the midi device in the MIDI global variable.
    Will return None if not found.
    """
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

    # Find the device listed in the global MIDI variable.
    try:
        return midi.Input(inputs[MIDI])
    except KeyError:
        print(f"Could not find {MIDI}")
        return None


def client_connect(midi_device: midi.Input) -> None:
    """connects the client midi device to the server socket.
    note: if no midi device found, will send test msg.

    Parameters
    ----------
    midi_device : midi.Input
        from pygame, a midi input device.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            if midi_device:
                if midi_device.poll():
                    msg = midi_device.read(1)[0]
                    msg_str = midi_to_msg(msg)
                    s.sendall(str.encode(msg_str))
            else:
                msg = [[144, 35, 50], 500]
                msg_str = midi_to_msg(msg)
                s.sendall(str.encode(msg_str))
                sleep(1)


def main():
    midi = find_devices()
    client_connect(midi)


if __name__ == "__main__":
    main()
