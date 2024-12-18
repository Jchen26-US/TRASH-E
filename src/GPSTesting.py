import socket
import time
#import picamzero
from gps import *

# Configuration
SERVER_IP = "192.168.4.104"  # Replace with the computer's IP address #This actually is my ip dont hack plz
SERVER_PORT = 5000  # Port for communication
INTERVAL = 10  # Time interval in seconds between image captures


#Math May not Use this section, currently unsure
def dm(x): #Converts integer into degrees and minutes
    degrees = int(x) // 100
    minutes = x - 100*degrees

    return degrees, minutes

def decimal_degrees(degrees, minutes): #Converts Degrees + minutes into Degrees
    return degrees + minutes/60 

#Rasp.py edits:
#Modified capture_image to also send GPS coordinates


gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)
def get_gps_data():#writes 
    nx = gpsd.next() #may have to replace with gpsd.read() modify as needed
    if nx['class'] == 'TFV':
        lat = getattr(nx, "lat", "Unknown")#gets latitude attribute, and returns unknown if doesnt exist
        long = getattr(nx, "lon", "Unknown")
        print(f"Current Position: latitude = {str(lat)}, longitude = {str(long)}")
        return {"lat": lat, "long": long} #returns dictionary with latitude and longitude


def capture_image(image_path, gps_path):#captures img -> image_path, gps_data -> text file
#    with picamzero.Camera() as camera:
#        camera.resolution = (640, 480)  # Set resolution
#        camera.start_preview()
#        time.sleep(2)  # Allow camera to adjust
#        camera.capture(image_path)
    with open(gps_path, "w") as gps_file: #can maybe just open gps_path forever in while loop
        gps_data = get_gps_data()
        gps_file.write(str(gps_data))


def send_image(image_path, gps_path):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            client_socket.connect((SERVER_IP, SERVER_PORT))
            with open(image_path, "rb") as image_file:
                while (chunk := image_file.read(1024)):
                    client_socket.sendall(chunk)
            print(f"Image sent to {SERVER_IP}:{SERVER_PORT}")
            with open(gps_path, "rb") as gps_file:#added
                while (chunk := gps_file.read(1024)):
                    client_socket.sendall(chunk)
        except Exception as e:
            print(f"Error sending image: {e}")
            
print (decimal_degrees(*dm(3648.5518)))