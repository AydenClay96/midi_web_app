import socket
from typing import List

HOST = "192.168.1.191"
PORT = 65432


def msg_to_midi(msg: str) -> List[int]:
    """Converts messages from the client to midi message in pygame.midi.Input format.

    Parameters
    ----------
    msg : str
        format is b"TTTNNNVVVSSSS"

    Returns
    -------
    List:
        [[type, note, velocity], timestamp]
    """
    msg_list = str(msg).split(",")
    type, note, velocity, timestamp = msg_list
    type = type[2:]
    timestamp = int(timestamp[:-1])
    midi = [int(type), int(note), int(velocity)]
    return [midi, timestamp]


def server_connect() -> None:
    """The server end of the socket."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        # While on and listening.
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    # While connected infinitely await data.
                    msg = conn.recv(1024)
                    if not msg:
                        break
                    # Send the data back.
                    midi = msg_to_midi(msg)
                    print(midi)
                    conn.sendall(msg)

def main() -> None:
    server_connect()

if __name__ == "__main__":
    main()
