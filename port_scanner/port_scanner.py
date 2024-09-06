import socket

def port_scan(host, start_port, end_port):
    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host, port))
            print(f"Port {port} is open")
            sock.close()
        except socket.error:
            print(f"Port {port} is closed")

host = input("Enter the host IP: ")
start_port = int(input("Enter the start port: "))
end_port = int(input("Enter the end port: "))
port_scan(host, start_port, end_port)