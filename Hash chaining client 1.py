
import socket
import hashlib

def chain_hash(msg, n):
    hashed_msg = msg
    for _ in range(n):
        hashed_msg = hashlib.sha256(hashed_msg.encode()).hexdigest()
    return hashed_msg

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 12345)  # Server address and port

secret_message = "This is the secret message"

iterations = 10

hashed_secret_message = chain_hash(secret_message, iterations)

client_socket.sendto(hashed_secret_message.encode(), server_address)

validation_response, _ = client_socket.recvfrom(1024)
if validation_response.decode() == "Validated":
    print("Client: Message validated successfully.")
else:
    print("Client: Message validation failed.")
