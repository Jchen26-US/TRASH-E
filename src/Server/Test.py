from inference_sdk import InferenceHTTPClient
import os
from PIL import Image
from pathlib import Path
def main():
    CLIENT = InferenceHTTPClient(
        api_url="https://detect.roboflow.com",
        api_key="933ini7vNHkeJxSDlwba"
    )

    new_directory = "Reformatted"
    # List of common image extensions

    # List of common image extensions
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff')
    #clears summary file
    WriteTo = open("..\summary.txt", "w")
    WriteTo.write("")
    WriteTo.close()
    
    #opens file
    WriteTo = open("..\summary.txt", 'a')

    #opens annoted images directory
    SummaryDir = os.open("..\annotated_images", dir_fd)
    

    #result = CLIENT.infer("metal_759.jpg", model_id="trash-detection-otdmj/35")
    # Loop through all files in the current directory
    for filename in os.listdir():
        if filename.lower().endswith(image_extensions):
            print(f"Found image: {filename}")
            #IMG = Image.open(filename)
            #IMG.show()
            result = CLIENT.infer(filename, model_id="trash-detection-otdmj/35")
            num_objects = len(result["predictions"])
            if(num_objects != 0):
                print(f"Number of Objects in {filename}: {num_objects}")
            else:
                print(f"No Objects in {filename}")
            WriteTo.write(str(filename + ",\n" + "number of objects: " + str(num_objects) + ",\n" + "Predictions: " + str(result["predictions"]) + ",\n\n"))
            print("added to summary")

            
    print("done")

main()