
import socket

attacker_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 12345)

# BLIND REPLAY ATTACK ATTEMPT
received_hashed_message = "f7e18f8b843b3a95f09a8b84d3d4b7ec9a6a227e"

attacker_socket.sendto(received_hashed_message.encode(), server_address)

validation_response, _ = attacker_socket.recvfrom(1024)

if validation_response.decode() == "Validated":
    print("Client 2 (Attacker): Successfully executed a blind replay attack.")
else:
    print("Client 2 (Attacker): Blind replay attack failed.")
