import sys

card_deck = sys.argv[1]

f = open(card_deck,'r')

deck = []

for line in f:
    words = line.split()
    deck.append((words[0],words[1]))

print deck
