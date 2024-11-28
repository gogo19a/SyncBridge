import os
import asyncio
import socket
import shutil

# Define the server's IP and port
HOST = '0.0.0.0'  # Listen on all available network interfaces
PORT = 5001

# Destination directory for storing received files
DESTINATION_DIR = os.path.dirname(os.path.abspath(__file__))

# Handle receiving and saving files
async def handle_client(reader, writer):
    # Get the client address
    addr = writer.get_extra_info('peername')
    print(f"Connected to {addr}")

    try:
        # Read data sent by the client
        data = await reader.read(100)
        while data:
            file_path = os.path.join(DESTINATION_DIR, data.decode())
            file_dir = os.path.dirname(file_path)
            
            # Create directories if they don't exist
            if not os.path.exists(file_dir):
                os.makedirs(file_dir)
            
            # Read the actual file content
            file_content = await reader.read(1000000)  # Adjust size as needed
            with open(file_path, 'wb') as f:
                f.write(file_content)
            
            print(f"File received and saved: {file_path}")
            data = await reader.read(100)
    except Exception as e:
        print(f"Error while receiving file: {e}")
    finally:
        writer.close()
        await writer.wait_closed()

# Start the server to listen for incoming connections
async def main():
    server = await asyncio.start_server(handle_client, HOST, PORT)
    print(f"Serving on {HOST}:{PORT}")

    async with server:
        await server.serve_forever()

# Run the server
if __name__ == '__main__':
    asyncio.run(main())
