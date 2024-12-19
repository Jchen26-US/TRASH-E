#SERVER.py: #############

import socket
import time
from inference_sdk import InferenceHTTPClient
from PIL import Image, ImageDraw



def rotateImg(Img_address):
    Origin = Image.open(Img_address)
    
    rotated = Origin.rotate(90)

    rotated.save(Img_address)

def analyze(Img_adrress, CLIENT): 
    result = CLIENT.infer(Img_adrress, model_id="trash-detection-otdmj/35")#roboflow analyzes using api
    num_objects = len(result["predictions"])
    print(num_objects)
    if num_objects != 0:
        return True
    else:
        return False
    
def drawBoundingBox(Img_address,x,y,width,height, color):#meant to be used with roboflow prediction
    Origin = Image.open(Img_address)
    shape = [(x-width/2,y-height/2), (x+width/2, y+height/2)]
    Modified = ImageDraw.Draw(Origin)
    Modified.fill = True
    Modified.rectangle(shape, color)
    Origin.save(Img_address)

def annotate_image(CLIENT, img_address, img_target):
    Image_address_unedited = img_address
    Img1 = Image.open(Image_address_unedited)
    Image_address = img_target
    Img1.copy().save(img_target)

    result = CLIENT.infer(Image_address, model_id="trash-detection-otdmj/35")
    #print(result["predictions"])
    color = [
        "red", "blue", "green", "yellow", "orange", 
        "purple", "pink", "brown", "black", "white", 
        "gray", "cyan", "magenta", "lime", "teal", 
        "indigo", "violet", "gold", "silver", "maroon"
    ]
    #idk man
    cur_color = 0
    for prediction1 in (result["predictions"]):
        drawBoundingBox(Image_address, prediction1['x'], prediction1['y'], prediction1['width'], prediction1['height'], color[cur_color])
        cur_color += 1



def saveGps():
    #code will go to saveGps data here after sent to server
    pass

STARTING_TIME = time.time()
SERVER_IP = "0.0.0.0"  # Listen on all interfaces
SERVER_PORT = 5000
SAVE_PATH = "./liveImageApp/images/received_img.jpg"
ANNOTATED_PATH = "./liveImageApp/images/annotated_img.jpg"
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="933ini7vNHkeJxSDlwba"
)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen(1)
    print(f"Server listening on {SERVER_IP}:{SERVER_PORT}")

    while True:
        print("time passed: " , time.time() - STARTING_TIME)
        STARTING_TIME = time.time()
        print("listening...")
        conn, addr = server_socket.accept()
        print(f"Connection from {addr}")
        with conn, open(SAVE_PATH, "wb") as image_file:
            while (chunk := conn.recv(1024)):
                image_file.write(chunk)
        print(f"Image saved to {SAVE_PATH}")
        
        if(analyze(SAVE_PATH, CLIENT) == True):#only use if, gps works
            print("Object detected")
            saveGps()
        else:
            print("Nothing")

        annotate_image(CLIENT, SAVE_PATH, ANNOTATED_PATH)
        
