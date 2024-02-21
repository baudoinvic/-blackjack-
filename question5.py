import requests
import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np
import random

card_images = []
cards = []

class Card:
    def __init__(self, mark, display_name, number, image):
        self.mark = mark
        self.display_name = display_name
        self.number = number
        self.image = image

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []  # List to store dealt cards
        self.total_number = 0  # Total number of points
        
    def add_card(self, card):
        self.cards.append(card)
        self.total_number += card.number

def load_image():
    image_name = 'cards.jpg'
    vsplit_number = 4
    hsplit_number = 13
  
    if not os.path.isfile(image_name):
        response = requests.get('http://3156.bz/techgym/cards.jpg', allow_redirects=False)
        with open(image_name, 'wb') as image:
            image.write(response.content)
   
    img = cv.imread('./'+image_name)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
 
    h, w = img.shape[:2]
    crop_img = img[:h // vsplit_number * vsplit_number, :w // hsplit_number * hsplit_number]
  
    card_images.clear()
    for h_image in np.vsplit(crop_img, vsplit_number):
        for v_image in np.hsplit(h_image, hsplit_number):
            card_images.append(v_image)

def create_cards():
    cards.clear()
    marks = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
    display_names = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    numbers = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    for i, mark in enumerate(marks):
        for j, number in enumerate(numbers):
            cards.append( Card(mark, display_names[j], number, card_images[i*len(numbers)+j]) )

def deal_card(player):
    # Select a random card
    random_card = random.choice(cards)
    
    # Add the card to the player's hand
    player.add_card(random_card)

def play():
    print('Debug: play()')
    load_image()
    create_cards()

    # Create players
    player1 = Player("You")
    computer = Player("Computer")
    
    # Deal cards to players
    deal_card(player1)
    deal_card(computer)
    
    # Print the cards dealt to each player (for debugging)
    print("Player 1's cards:")
    for card in player1.cards:
        print(card.display_name, "of", card.mark)
    print("Total points:", player1.total_number)
    
    print("\nComputer's cards:")
    for card in computer.cards:
        print(card.display_name, "of", card.mark)
    print("Total points:", computer.total_number)

play()
