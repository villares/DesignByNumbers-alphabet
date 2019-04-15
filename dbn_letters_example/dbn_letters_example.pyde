"""
s18019 - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day

Converting some of Maeda's Design by Number
dbnletters.dbn code -> Processing

This draws a sample using code in dbn_letters.py
"""

from dbn_letters import *

def setup():
    size(200, 200)
    noLoop()
    noSmooth()

def draw():
    #scale(4, 4)
    dbn_sample()
    saveFrame("dbn_letters_example.png")

def dbn_sample():
    for y in range(0, 5):
        for x in range(1, 6):
            dbn_letter[x + y * 5](x * 12, -20 - y * 12)
    dbn_letterZ(x * 12 + 12, -32 - y * 12)
