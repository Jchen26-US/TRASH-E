#Used for testing Roboflow and also evalutating the model's accuracy
from inference_sdk import InferenceHTTPClient
from PIL import Image, ImageDraw
import os


def rotateImg(Img_address):#not used in this program currently, but is useful if you recieve a rotated image
    Origin = Image.open(Img_address)
    
    rotated = Origin.rotate(90)

    rotated.save(Img_address)
    #Image.open("Rotated", 'w')
def drawBoundingBox(Img_address,x,y,width,height, color):#meant to be used with roboflow prediction
    Origin = Image.open(Img_address)
    shape = [(x-width/2,y-height/2), (x+width/2, y+height/2)]
    Modified = ImageDraw.Draw(Origin)
    Modified.fill = True
    Modified.rectangle(shape, color)
    Origin.save(Img_address)


def analyze_image(CLIENT, img_address, img_target):
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

def analyze_directory(CLIENT, Image_directory, Target_directory):
    try:
        os.mkdir(Target_directory)
        print(f"Directory {Target_directory} created")
    except FileExistsError:
        for filename in os.listdir(Target_directory):
            file_path = os.path.join(Target_directory, filename)
            os.remove(file_path)
            print(f"Deleted file: {filename} from {Target_directory}")
        print(f"{Target_directory} is now clear")
    
    for filename in os.listdir(Image_directory):
        filenamewdir = Image_directory + "/" + filename #filename with directory
        analyze_image(CLIENT, filenamewdir, Target_directory + "/" + filename)
        print(f"analyzed {filename}")
    
    print("\n\nDone")

    


def main():
    CLIENT = InferenceHTTPClient(
        api_url="https://detect.roboflow.com",
        api_key="933ini7vNHkeJxSDlwba"
    )

    analyze_directory(CLIENT, "./src/valid/images", "./src/valid/Annotated")
    
    


main()