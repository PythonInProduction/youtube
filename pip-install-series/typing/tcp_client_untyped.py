import socket

HOST = "127.0.0.1"  # Server IP or hostname
PORT = 5000         # Server port

def tcp_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        print(f"Connected to {HOST}:{PORT}")

        message = "Hello from client"
        client.sendall(message.encode("utf-8"))

        response = client.recv(1024)
        print("Server replied:", response.decode("utf-8"))

if __name__ == "__main__":
    tcp_client()
