#####Simulates website recieving live entries


import os
import time
from PIL import Image,ImageDraw
from inference_sdk import InferenceHTTPClient

def drawBoundingBox(Img_address,x,y,width,height, color):#meant to be used with roboflow prediction
    Origin = Image.open(Img_address)
    shape = [(x-width/2,y-height/2), (x+width/2, y+height/2)]
    Modified = ImageDraw.Draw(Origin)
    Modified.fill = True
    Modified.rectangle(shape, color)
    Origin.save(Img_address)

def analyze_image(CLIENT, img_address, img_target):
    color = [
        "red", "blue", "green", "yellow", "orange", 
        "purple", "pink", "brown", "black", "white", 
        "gray", "cyan", "magenta", "lime", "teal", 
        "indigo", "violet", "gold", "silver", "maroon"
    ]
    
    Image_address_unedited = img_address
    Img1 = Image.open(Image_address_unedited)
    Image_address = img_target
    

    result = CLIENT.infer(Image_address_unedited, model_id="trash-detection-otdmj/35")
    #print(result["predictions"])
    #idk man
    cur_color = 0
    Img1.copy().save(img_target)
    for prediction1 in (result["predictions"]):
        drawBoundingBox(Image_address, prediction1['x'], prediction1['y'], prediction1['width'], prediction1['height'], color[cur_color])
        cur_color += 1

def main():
    
    CLIENT = InferenceHTTPClient(
        api_url="https://detect.roboflow.com",
        api_key="933ini7vNHkeJxSDlwba"
    )

    #only used when image_path1 and image_path2 are not automatically updating from server.py file
    image_set1 = os.listdir("../valid/images")
    image_set2 = os.listdir("../valid/Annotated")
    
    target_path1 = "./images/received_img.jpg"
    target_path2 = "./images/annotated_img.jpg"
    
    

    for x in range(0, len(image_set1) - 1):

        target_file1 = open(target_path1, "wb")
        target_file2 = open(target_path2, "wb") 

        path1 = "../valid/images/" + image_set1[x]

        with open(path1, "rb") as image_file1:
            target_file1.write(image_file1.read())
        analyze_image(CLIENT, path1 , target_path2)
        print(image_set1[x])
        print(f"set #{x}: image updated")
        time.sleep(5)
        

main()