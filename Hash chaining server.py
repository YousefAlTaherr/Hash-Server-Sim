import socket
import hashlib

def chain_hash(msg, n):
    hashed_msg = msg
    for _ in range(n):
        hashed_msg = hashlib.sha256(hashed_msg.encode()).hexdigest()
    return hashed_msg


server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 12345)


server_socket.bind(server_address)

print("Server is waiting for a connection...")

received_hashed_message, client_address = server_socket.recvfrom(1024)
received_hashed_message = received_hashed_message.decode()

secret_message = "This is the secret message"

iterations = 10

hashed_secret_message = chain_hash(secret_message, iterations)

if hashed_secret_message == received_hashed_message:
    print("Server: Message validated successfully.")
    server_socket.sendto("Validated".encode(), client_address)
else:
    print("Server: Message validation failed.")
    server_socket.sendto("Not Validated".encode(), client_address)
