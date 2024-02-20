import requests
import cv2 as cv
import numpy as np

card_images = []

def load_image():
    image_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcScKDX9BRB4wMhtx5hTqQ2fj88_T4wIqTmjDA&usqp=CAU'

    response = requests.get(image_url)
    image_array = np.frombuffer(response.content, np.uint8)
    img = cv.imdecode(image_array, cv.IMREAD_COLOR)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    vsplit_number = 4
    hsplit_number = 13
    h, w = img.shape[:2]
    crop_img = img[:h // vsplit_number * vsplit_number, :w // hsplit_number * hsplit_number]

    card_images.clear()
    for h_image in np.vsplit(crop_img, vsplit_number):
        for v_image in np.hsplit(h_image, hsplit_number):
            card_images.append(v_image)

class Card:
    def __init__(self, mark, display_name, number, image):
        self.mark = mark
        self.display_name = display_name
        self.number = number
        self.image = image

def play():
    print('Debug: play()')
    load_image()

play()
