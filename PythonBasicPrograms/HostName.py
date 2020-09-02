import socket
class HostName:
    def name(self):
        hostName = socket.gethostname()
        print("Host name :", hostName)

host = HostName()
host.name()