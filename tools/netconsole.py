import argparse
import signal
import socket
import sys
import threading

# Default configurations
DEFAULT_PORT = 6666
PROMPT = ""  # Configurable prompt

# Store device addresses
devices = {}

# Event to signal program exit
exit_event = threading.Event()

# Trap for handling Ctrl+C (SIGINT) and Ctrl+D (EOF)
def signal_handler(sig, frame):
    if sig == signal.SIGINT:  # Ctrl+C
        # Send Ctrl+C to all devices
        print("\nCtrl+C detected. Sending Ctrl+C to devices.")
        for addr in devices:
            devices[addr].sendto(b'\x03', addr)  # Sending interrupt signal to the device

# Set up signal traps
signal.signal(signal.SIGINT, signal_handler)

def udp_listener(port):
    """Listen for incoming UDP messages."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", port))
    print(f"Listening on UDP port {port}...")

    while not exit_event.is_set():
        try:
            sock.settimeout(0.1)  # Timeout to allow checking the exit event periodically
            data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
            if addr not in devices:
                devices[addr] = sock
                print(f"New device detected: {addr}")
            print(data.decode('utf-8'), end="")
        except socket.timeout:
            continue  # Timeout used to keep checking the exit_event
        except Exception as e:
            print(f"Error: {e}")
            break

def input_handler(devices):
    """Handle user input and send to the specified device."""
    while not exit_event.is_set():
        try:
            user_input = input(PROMPT) + "\n"
            if user_input == "":
                continue
            # Send input to the device
            for addr, sock in devices.items():
                sock.sendto(user_input.encode('utf-8'), addr)
        except EOFError:  # Ctrl+D
            print("\nCtrl+D detected. Closing connection.")
            exit_event.set()
            break
        except Exception as e:
            print(f"Error sending data: {e}")
            exit_event.set()

def main():
    # Argument parser for custom port
    parser = argparse.ArgumentParser(description="Netconsole UDP listener.")
    parser.add_argument(
        "-p", "--port", type=int, default=DEFAULT_PORT, help="Port to listen on (default: 6666)"
    )
    args = parser.parse_args()

    # Start UDP listener in a separate thread
    listener_thread = threading.Thread(target=udp_listener, args=(args.port,))
    listener_thread.daemon = True
    listener_thread.start()

    input_thread = threading.Thread(target=input_handler, args=(devices,))
    input_thread.daemon = True
    input_thread.start()

    # Keep main thread alive and check for exit_event
    while not exit_event.is_set():
        try:
            listener_thread.join(timeout=1)  # Join the listener thread periodically
        except Exception as e:
            print(f"Error: {e}")
            break

    print("Application exiting...")

if __name__ == "__main__":
    main()
