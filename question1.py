import os
import requests
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def load_image():
    image_name = 'cards.jpg'

    if not os.path.isfile(image_name):
        try:
            response = requests.get('http://3156.bz/techgym/cards.jpg', allow_redirects=False)
            if response.status_code == 200:
                with open(image_name, 'wb') as image:
                    image.write(response.content)
            else:
                raise Exception("Failed to download image")
        except Exception as e:
            print("Error downloading image:", e)
            return []

    try:
        img = cv.imread(image_name)
        if img is None:
            raise Exception("Failed to load image")

        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        plt.imshow(img)
        plt.axis('off')
        plt.show()

    except Exception as e:
        print("Error processing image:", e)

# Test the function
if __name__ == "__main__":
    load_image()
