#Rasp.py################

import socket
import time
import picamzero #error may arise if you try to "pip install picamzero"

# Configuration
SERVER_IP = "your IP"  # Replace with the computer's IP address
SERVER_PORT = 5000  # Port for communication
INTERVAL = 10  # Time interval in seconds between image captures

# Function to capture an image and save it temporarily
def capture_image(image_path):
    with picamzero.Camera() as camera:
        camera.resolution = (640, 480)  # Set resolution
        camera.start_preview()
        time.sleep(2)  # Allow camera to adjust
        camera.capture(image_path)

# Function to send the image to the server
def send_image(image_path):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            client_socket.connect((SERVER_IP, SERVER_PORT))
            with open(image_path, "rb") as image_file:
                while (chunk := image_file.read(1024)):
                    client_socket.sendall(chunk)
            print(f"Image sent to {SERVER_IP}:{SERVER_PORT}")
        except Exception as e:
            print(f"Error sending image: {e}")

# Main loop
def main():
    image_path = "image.jpg"  # Temporary file path for the image

    while True:
        try:
#            capture_image(image_path)
            send_image(image_path)
        except Exception as e:
            print(f"Error: {e}")

        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()
