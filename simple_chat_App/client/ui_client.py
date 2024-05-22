import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
from cryptography.fernet import Fernet

# Client configuration
HOST = '127.0.0.1'
PORT = 12345

def receive_messages(client_socket, text_area, cipher_suite):
    """Receive and display messages from the server."""
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                decrypted_message = cipher_suite.decrypt(message)
                text_area.config(state=tk.NORMAL)
                text_area.insert(tk.END, decrypted_message.decode('utf-8') + '\n')
                text_area.config(state=tk.DISABLED)
                text_area.yview(tk.END)
            else:
                break
        except Exception as e:
            print(f"Error: {e}")
            break

def authenticate(client_socket, cipher_suite, action, username, password, login_label):
    """Send authentication data to the server."""
    credentials = f"{action}:{username}:{password}"
    encrypted_credentials = cipher_suite.encrypt(credentials.encode('utf-8'))
    client_socket.send(encrypted_credentials)
    response = client_socket.recv(1024).decode('utf-8')
    login_label.config(text=response)
    return 'successful' in response

def on_send_message(client_socket, entry, text_area, cipher_suite):
    """Send message to the server."""
    message = entry.get()
    if message:
        encrypted_message = cipher_suite.encrypt(message.encode('utf-8'))
        client_socket.send(encrypted_message)
        entry.delete(0, tk.END)

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    # Receive encryption key from the server
    key = client_socket.recv(1024)
    cipher_suite = Fernet(key)

    root = tk.Tk()
    root.title("Chat Application")

    login_frame = tk.Frame(root)
    login_frame.pack()

    tk.Label(login_frame, text="Username").pack(side=tk.LEFT)
    username_entry = tk.Entry(login_frame)
    username_entry.pack(side=tk.LEFT)

    tk.Label(login_frame, text="Password").pack(side=tk.LEFT)
    password_entry = tk.Entry(login_frame, show='*')
    password_entry.pack(side=tk.LEFT)

    login_label = tk.Label(login_frame, text="")
    login_label.pack(side=tk.LEFT)

    def on_login():
        username = username_entry.get()
        password = password_entry.get()
        if authenticate(client_socket, cipher_suite, 'login', username, password, login_label):
            login_frame.pack_forget()
            chat_frame.pack()

    tk.Button(login_frame, text="Login", command=on_login).pack(side=tk.LEFT)

    chat_frame = tk.Frame(root)

    text_area = scrolledtext.ScrolledText(chat_frame, state=tk.DISABLED)
    text_area.pack()

    entry = tk.Entry(chat_frame)
    entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

    tk.Button(chat_frame, text="Send", command=lambda: on_send_message(client_socket, entry, text_area, cipher_suite)).pack(side=tk.LEFT)

    threading.Thread(target=receive_messages, args=(client_socket, text_area, cipher_suite)).start()

    root.mainloop()

if __name__ == "__main__":
    main()
