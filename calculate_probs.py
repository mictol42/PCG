import sys

card_deck = sys.argv[1]

f = open(card_deck,'r')

for line in f:
    print line
