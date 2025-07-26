import socket

from utils.message import msg_to_midi

HOST = ""
PORT = ""


def server_connect() -> None:
    """The server end of the socket."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    msg = conn.recv(1024)
                    if not msg:
                        break
                    midi = msg_to_midi(msg)
                    print(msg)


def main() -> None:
    server_connect()


if __name__ == "__main__":
    main()
