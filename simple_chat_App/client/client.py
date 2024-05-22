import socket
import threading
from cryptography.fernet import Fernet

# Client configuration
HOST = '127.0.0.1'
PORT = 12345

def receive_messages(client_socket, cipher_suite):
    """Receive and print messages from the server."""
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                decrypted_message = cipher_suite.decrypt(message)
                print(decrypted_message.decode('utf-8'))
            else:
                break
        except Exception as e:
            print(f"Error: {e}")
            break

def authenticate(client_socket, cipher_suite):
    """Handle user authentication."""
    while True:
        action = input("Do you want to 'register' or 'login'? ").strip()
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        credentials = f"{action}:{username}:{password}"
        encrypted_credentials = cipher_suite.encrypt(credentials.encode('utf-8'))
        client_socket.send(encrypted_credentials)
        response = client_socket.recv(1024).decode('utf-8')
        print(response)
        if 'successful' in response:
            break

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    # Receive encryption key from the server
    key = client_socket.recv(1024)
    cipher_suite = Fernet(key)

    authenticate(client_socket, cipher_suite)

    print("Connected to the chat server!")
    threading.Thread(target=receive_messages, args=(client_socket, cipher_suite)).start()

    while True:
        message = input()
        if message:
            encrypted_message = cipher_suite.encrypt(message.encode('utf-8'))
            client_socket.send(encrypted_message)
        else:
            break

if __name__ == "__main__":
    main()
