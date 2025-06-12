import socket
import os

def get_device_id():
    return socket.gethostname()

def ensure_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
