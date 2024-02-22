# class Player:
#     def __init__(self, name, load_image,create_cards,deal_card):
#         self.name = name
#         self.load_image = load_image
#         self.create_cards = create_cards
#         self.deal_card = deal_card
#         self.cards = []  # List to store dealt cards
#         self.total_number = 0  # Total number of points
        
#     def add_card(self, card):
#         self.cards.append(card)
#         self.total_number += card.number

# class Human(Player):
#     def __init__(self):
#         super().__init__('You')

# class Computer(Player):
#     def __init__(self):
#         super().__init__('Computer')

# # Global list to store players
# players = []

# def play():
   
#     print('Debug: play()')
#     load_image()
#     create_cards()

#     # Create instances of Human and Computer classes
#     human_player = Human()
#     computer_player = Computer()

#     # Add instances to the global list 'players'
#     players.append(human_player)
#     players.append(computer_player)

#     # Deal cards to players
#     for player in players:
#           deal_card(player)

#     # Print the cards dealt to each player (for debugging)
#     for player in players:
#         print(f"{player.name}'s cards:")
#         for card in player.cards:
#             print(card.display_name, "of", card.mark)
#         print("Total points:", player.total_number)

# play()
