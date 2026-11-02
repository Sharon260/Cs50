import random 

cards = ["jack", "queen", "king", "ace", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
random.shuffle(cards)
for card in cards: 
    print(card)