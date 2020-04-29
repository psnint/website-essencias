import socket
import subprocess


def alive(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, int(port)))
        s.shutdown(2)
        return True
    except:
        return False


if not alive('essenciasdeportugal.pt', 42333):
    subprocess.call('screen -S catalogo-backend -dm ~/start_catalogo_backend.sh', shell=True)
