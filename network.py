import socket
import pickle

def send_message(address, message):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(address)
            s.sendall(pickle.dumps(message))
            return pickle.loads(s.recv(4096))
    except Exception:
        return None