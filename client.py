import os
import asyncio
import socket

# Define the server IP and port
SERVER_IP = "192.168.1.10"  # Replace with your server's IP
PORT = 5001

# Get the directory of the current file (where client.py is located)
LOCAL_DIR = os.path.dirname(os.path.abspath(__file__))

# Send file content to the server
async def send_file(file_path, writer):
    try:
        with open(file_path, 'rb') as f:
            file_name = os.path.relpath(file_path, LOCAL_DIR)
            writer.write(file_name.encode())  # Send the file path relative to LOCAL_DIR
            await writer.drain()  # Ensure data is written
            
            file_content = f.read()
            writer.write(file_content)  # Send file content
            await writer.drain()  # Ensure data is sent
            print(f"File sent: {file_name}")
    except Exception as e:
        print(f"Error sending file {file_path}: {e}")

# Traverse the local directory and send all files to the server
async def send_files():
    # Connect to the server
    reader, writer = await asyncio.open_connection(SERVER_IP, PORT)
    
    # Walk through the LOCAL_DIR and send all files
    for root, _, files in os.walk(LOCAL_DIR):
        for file in files:
            file_path = os.path.join(root, file)
            await send_file(file_path, writer)

    print("All files sent.")
    writer.close()
    await writer.wait_closed()

# Run the client
if __name__ == '__main__':
    asyncio.run(send_files())
