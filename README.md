
# SyncBridge

A simple yet powerful file synchronization tool for developers to transfer files between a client (e.g., your local machine) and a server (e.g., a remote deployment server). This tool supports preserving the folder structure and is perfect for automating file updates during development.

---

## Features
- **Automatic folder structure preservation:** Files maintain their original hierarchy when transferred to the server.
- **Lightweight and asynchronous:** Uses Python's `asyncio` for efficient file transfer.
- **Cross-platform:** Works seamlessly between different operating systems (e.g., macOS and Windows).
- **Customizable and extensible:** Easy to modify and integrate into other workflows.

---

## How It Works
1. **Server-side script**: Receives files from the client and saves them in the same structure as sent.
2. **Client-side script**: Sends all files from a specified directory and its subdirectories to the server.

---

## Installation

### Prerequisites
- Python 3.7 or higher.
- Basic understanding of running Python scripts.

### Step 1: Clone the repository
```bash
git clone https://github.com/gogo19a/SyncBridge.git
cd SyncBridge
```

### Step 2: Install dependencies
No external dependencies are required; only Python's standard library is used.

---

## Usage

### 1. **Set up the server**
Run the server script (`server.py`) on the destination machine where files will be stored:
```bash
python server.py
```
By default, the server:
- Listens on all available IPs (`0.0.0.0`).
- Uses port `5001`.
- Stores received files in the same directory as `server.py`.

You can modify the `HOST` and `PORT` variables in `server.py` if needed.

---

### 2. **Set up the client**
Run the client script (`client.py`) on the source machine where files are located:
```bash
python client.py
```
The client script:
- Automatically detects the directory where it is located and sends all files within that directory and its subdirectories to the server.
- You must update the `SERVER_IP` variable in `client.py` to the IP address of your server.

Example:
```python
SERVER_IP = "192.168.1.10"  # Replace with your server's IP
```

---

### Example Workflow
1. Place `server.py` on your remote server and run it.
2. Place `client.py` in your project folder on your local machine.
3. Run `client.py` to sync your project files to the server.

---

## Security Considerations
- Ensure the server port (default: `5001`) is accessible through your firewall.
- For production environments, consider securing the connection using SSH or a VPN.

---

## Contribution
Contributions are welcome! To contribute:
1. Fork this repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -m 'Add a new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a pull request.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact
For questions, suggestions, or issues, feel free to contact me via:
- **GitHub Issues**: [Open an Issue](https://github.com/gogo19a/SyncBridge/issues)
- **Email**: gogo19a@gmail.com
