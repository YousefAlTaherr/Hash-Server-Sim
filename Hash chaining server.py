import socket
import hashlib

def chain_hash(msg, n):
    hashed_msg = msg
    for _ in range(n):
        hashed_msg = hashlib.sha256(hashed_msg.encode()).hexdigest()
    return hashed_msg

# Create a socket for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)  # Set the server address and port

# Bind the socket to the server address
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)
print("Server is waiting for a connection...")

# Accept a client connection
client_socket, client_address = server_socket.accept()
print("Server: Accepted connection from", client_address)

# Secret message to be sent
secret_message = "This is the secret message"

# Number of hash iterations (chaining)
iterations = 3

# Chain the hash multiple times
hashed_secret_message = chain_hash(secret_message, iterations)

# Send the hashed message to the client
client_socket.send(hashed_secret_message.encode())
client_socket.close()
