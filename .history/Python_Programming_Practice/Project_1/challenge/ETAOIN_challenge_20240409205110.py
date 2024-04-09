"""Map letters from string into dictionary & print bar chart of frequency."""

import sys
import pprint
from collections import defaultdict

# Note: text should be a short phrase for bars to fit in IDLE window
TEXT = 'Como o castelo no seu canto num jogo medieval, prevejo problemas \
    terriveis e fico aqui na mesma.'

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

# defaultdict module lets you build dictionary keys on the fly!
mapped = defaultdict(list)
in_character = ''
for character in TEXT:
    character = character.lower()
    if character in ALPHABET:
        mapped[character].append(character)
        in_character += character

for character in ALPHABET:
    if character not in ALPHABET:
        

# pprint lets you print stacked output
print("\nYou may need to stretch console window if text wrapping occurs.\n")
print("text = ", end='')
print(f"{TEXT}\n", file=sys.stderr)
pprint.pprint(mapped, width=110)
