"""
Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day
This code was generated by dbn_generate_polys.py
Converting some of Maeda's Design by Number
dbnletters.dbn code -> Processing
"""
dbn_p_letter = {}  # Dict of functions

# A
def dbn_p_letterA(h, v, debug_poly=False):
    pushMatrix()
    scale(1, -1)
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h,v)
    vertex(h,v+7)
    # vertex(h,v+7)
    vertex(h+3,v+10)
    # vertex(h+3,v+10)
    vertex(h+10,v+3)
    # vertex(h+10,v+3)
    vertex(h+10,v)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h,v+3)
    vertex(h+10,v+3)
    endShape()
    popMatrix()
dbn_p_letter['A'] = dbn_p_letterA
dbn_p_letter[1] = dbn_p_letterA
# B
def dbn_p_letterB(h, v, debug_poly=False):
    pushMatrix()
    scale(1, -1)
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h,v)
    vertex(h,v+10)
    # vertex(h,v+10)
    vertex(h+5,v+10)
    # vertex(h+5,v+10)
    vertex(h+8,v+7)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h,v+6)
    vertex(h+7,v+6)
    # vertex(h+7,v+6)
    vertex(h+10,v+3)
    # vertex(h+10,v+3)
    vertex(h+10,v+1)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h,v)
    vertex(h+9,v)
    endShape()
    popMatrix()
dbn_p_letter['B'] = dbn_p_letterB
dbn_p_letter[2] = dbn_p_letterB
# C
def dbn_p_letterC(h, v, debug_poly=False):
    pushMatrix()
    scale(1, -1)
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h+4,v)
    vertex(h+10,v)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h+4,v)
    vertex(h,v+4)
    # vertex(h,v+4)
    vertex(h,v+9)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h+1,v+10)
    vertex(h+9,v+10)
    endShape()
    popMatrix()
dbn_p_letter['C'] = dbn_p_letterC
dbn_p_letter[3] = dbn_p_letterC
# D
def dbn_p_letterD(h, v, debug_poly=False):
    pushMatrix()
    scale(1, -1)
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h,v)
    vertex(h,v+10)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h,v)
    vertex(h+8,v)
    # vertex(h+8,v)
    vertex(h+10,v+2)
    # vertex(h+10,v+2)
    vertex(h+10,v+6)
    # vertex(h+10,v+6)
    vertex(h+6,v+10)
    # vertex(h+6,v+10)
    vertex(h,v+10)
    endShape()
    popMatrix()
dbn_p_letter['D'] = dbn_p_letterD
dbn_p_letter[4] = dbn_p_letterD
# E
def dbn_p_letterE(h, v, debug_poly=False):
    pushMatrix()
    scale(1, -1)
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h,v+3)
    vertex(h,v+10)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h,v+3)
    vertex(h+3,v)
    # vertex(h+3,v)
    vertex(h+10,v)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h,v+6)
    vertex(h+9,v+6)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h,v+10)
    vertex(h+9,v+10)
    endShape()
    popMatrix()
dbn_p_letter['E'] = dbn_p_letterE
dbn_p_letter[5] = dbn_p_letterE
# F
def dbn_p_letterF(h, v, debug_poly=False):
    pushMatrix()
    scale(1, -1)
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h,v)
    vertex(h,v+10)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h,v+6)
    vertex(h+8,v+6)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h,v+10)
    vertex(h+10,v+10)
    endShape()
    popMatrix()
dbn_p_letter['F'] = dbn_p_letterF
dbn_p_letter[6] = dbn_p_letterF
# G
def dbn_p_letterG(h, v, debug_poly=False):
    pushMatrix()
    scale(1, -1)
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h+4,v)
    vertex(h+9,v)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h+4,v)
    vertex(h,v+4)
    # vertex(h,v+4)
    vertex(h,v+9)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h+1,v+10)
    vertex(h+9,v+10)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h+10,v+1)
    vertex(h+10,v+5)
    # vertex(h+10,v+5)
    vertex(h+6,v+5)
    endShape()
    popMatrix()
dbn_p_letter['G'] = dbn_p_letterG
dbn_p_letter[7] = dbn_p_letterG
# H
def dbn_p_letterH(h, v, debug_poly=False):
    pushMatrix()
    scale(1, -1)
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h,v)
    vertex(h,v+10)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h,v+4)
    vertex(h+10,v+4)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h+10,v)
    vertex(h+10,v+10)
    endShape()
    popMatrix()
dbn_p_letter['H'] = dbn_p_letterH
dbn_p_letter[8] = dbn_p_letterH
# I
def dbn_p_letterI(h, v, debug_poly=False):
    pushMatrix()
    scale(1, -1)
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h,v)
    vertex(h+10,v)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h+5,v)
    vertex(h+5,v+10)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h,v+10)
    vertex(h+9,v+10)
    endShape()
    popMatrix()
dbn_p_letter['I'] = dbn_p_letterI
dbn_p_letter[9] = dbn_p_letterI
# J
def dbn_p_letterJ(h, v, debug_poly=False):
    pushMatrix()
    scale(1, -1)
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h,v+3)
    vertex(h+3,v)
    # vertex(h+3,v)
    vertex(h+9,v)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h+10,v+1)
    vertex(h+10,v+10)
    endShape()
    popMatrix()
dbn_p_letter['J'] = dbn_p_letterJ
dbn_p_letter[10] = dbn_p_letterJ
# K
def dbn_p_letterK(h, v, debug_poly=False):
    pushMatrix()
    scale(1, -1)
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h,v)
    vertex(h,v+10)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h,v+1)
    vertex(h+9,v+10)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h+5,v+5)
    vertex(h+10,v)
    endShape()
    popMatrix()
dbn_p_letter['K'] = dbn_p_letterK
dbn_p_letter[11] = dbn_p_letterK
# L
def dbn_p_letterL(h, v, debug_poly=False):
    pushMatrix()
    scale(1, -1)
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h,v)
    vertex(h,v+10)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h,v)
    vertex(h+10,v)
    endShape()
    popMatrix()
dbn_p_letter['L'] = dbn_p_letterL
dbn_p_letter[12] = dbn_p_letterL
# M
def dbn_p_letterM(h, v, debug_poly=False):
    pushMatrix()
    scale(1, -1)
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h,v)
    vertex(h,v+10)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    #vertex(h,v+10)
    vertex(h+2,v+10)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h+1,v+10)
    vertex(h+5,v+6)
    # vertex(h+5,v+6)
    vertex(h+9,v+10)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h+10,v+10)
    vertex(h+10,v)
    endShape()
    popMatrix()
dbn_p_letter['M'] = dbn_p_letterM
dbn_p_letter[13] = dbn_p_letterM
# N
def dbn_p_letterN(h, v, debug_poly=False):
    pushMatrix()
    scale(1, -1)
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h,v)
    vertex(h,v+10)
    # vertex(h,v+10)
    vertex(h+3,v+10)
    # vertex(h+3,v+10)
    vertex(h+10,v+3)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h+10,v+10)
    vertex(h+10,v)
    endShape()
    popMatrix()
dbn_p_letter['N'] = dbn_p_letterN
dbn_p_letter[14] = dbn_p_letterN
# O
def dbn_p_letterO(h, v, debug_poly=False):
    pushMatrix()
    scale(1, -1)
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h+4,v)
    vertex(h+9,v)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h+4,v)
    vertex(h,v+4)
    # vertex(h,v+4)
    vertex(h,v+9)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h+1,v+10)
    vertex(h+7,v+10)
    # vertex(h+7,v+10)
    vertex(h+10,v+7)
    # vertex(h+10,v+7)
    vertex(h+10,v+1)
    endShape()
    popMatrix()
dbn_p_letter['O'] = dbn_p_letterO
dbn_p_letter[15] = dbn_p_letterO
# P
def dbn_p_letterP(h, v, debug_poly=False):
    pushMatrix()
    scale(1, -1)
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h,v)
    vertex(h,v+10)
    # vertex(h,v+10)
    vertex(h+7,v+10)
    # vertex(h+7,v+10)
    vertex(h+10,v+7)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h+10,v+6)
    vertex(h+8,v+4)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h,v+4)
    vertex(h+8,v+4)
    endShape()
    popMatrix()
dbn_p_letter['P'] = dbn_p_letterP
dbn_p_letter[16] = dbn_p_letterP
# Q
def dbn_p_letterQ(h, v, debug_poly=False):
    pushMatrix()
    scale(1, -1)
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h+4,v)
    vertex(h+8,v)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h+4,v)
    vertex(h,v+4)
    # vertex(h,v+4)
    vertex(h,v+9)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h+1,v+10)
    vertex(h+7,v+10)
    # vertex(h+7,v+10)
    vertex(h+10,v+7)
    # vertex(h+10,v+7)
    vertex(h+10,v+2)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h+6,v+4)
    vertex(h+10,v)
    endShape()
    popMatrix()
dbn_p_letter['Q'] = dbn_p_letterQ
dbn_p_letter[17] = dbn_p_letterQ
# R
def dbn_p_letterR(h, v, debug_poly=False):
    pushMatrix()
    scale(1, -1)
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h,v)
    vertex(h,v+10)
    # vertex(h,v+10)
    vertex(h+7,v+10)
    # vertex(h+7,v+10)
    vertex(h+10,v+7)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h+10,v+6)
    vertex(h+8,v+4)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h,v+4)
    vertex(h+8,v+4)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h+6,v+4)
    vertex(h+10,v)
    endShape()
    popMatrix()
dbn_p_letter['R'] = dbn_p_letterR
dbn_p_letter[18] = dbn_p_letterR
# S
def dbn_p_letterS(h, v, debug_poly=False):
    pushMatrix()
    scale(1, -1)
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h,v+2)
    vertex(h+2,v)
    # vertex(h+2,v)
    vertex(h+9,v)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h+10,v+1)
    vertex(h+10,v+4)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h+9,v+5)
    vertex(h+2,v+5)
    # vertex(h+2,v+5)
    vertex(h,v+7)
    # vertex(h,v+7)
    vertex(h,v+9)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h+1,v+10)
    vertex(h+9,v+10)
    # vertex(h+9,v+10)
    vertex(h+10,v+9)
    endShape()
    popMatrix()
dbn_p_letter['S'] = dbn_p_letterS
dbn_p_letter[19] = dbn_p_letterS
# T
def dbn_p_letterT(h, v, debug_poly=False):
    pushMatrix()
    scale(1, -1)
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h,v+10)
    vertex(h+10,v+10)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h+5,v+10)
    vertex(h+5,v)
    endShape()
    popMatrix()
dbn_p_letter['T'] = dbn_p_letterT
dbn_p_letter[20] = dbn_p_letterT
# U
def dbn_p_letterU(h, v, debug_poly=False):
    pushMatrix()
    scale(1, -1)
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h,v+10)
    vertex(h,v+3)
    # vertex(h,v+3)
    vertex(h+3,v)
    # vertex(h+3,v)
    vertex(h+9,v)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h+10,v+1)
    vertex(h+10,v+10)
    endShape()
    popMatrix()
dbn_p_letter['U'] = dbn_p_letterU
dbn_p_letter[21] = dbn_p_letterU
# V
def dbn_p_letterV(h, v, debug_poly=False):
    pushMatrix()
    scale(1, -1)
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h,v+10)
    vertex(h,v+5)
    # vertex(h,v+5)
    vertex(h+5,v)
    # vertex(h+5,v)
    vertex(h+10,v+5)
    # vertex(h+10,v+5)
    vertex(h+10,v+10)
    endShape()
    popMatrix()
dbn_p_letter['V'] = dbn_p_letterV
dbn_p_letter[22] = dbn_p_letterV
# W
def dbn_p_letterW(h, v, debug_poly=False):
    pushMatrix()
    scale(1, -1)
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h,v+10)
    vertex(h,v+3)
    # vertex(h,v+3)
    vertex(h+3,v)
    # vertex(h+3,v)
    vertex(h+6,v+3)
    # vertex(h+6,v+3)
    vertex(h+9,v)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h+10,v+1)
    vertex(h+10,v+10)
    endShape()
    popMatrix()
dbn_p_letter['W'] = dbn_p_letterW
dbn_p_letter[23] = dbn_p_letterW
# X
def dbn_p_letterX(h, v, debug_poly=False):
    pushMatrix()
    scale(1, -1)
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h,v+10)
    vertex(h,v+9)
    # vertex(h,v+9)
    vertex(h+4,v+5)
    # vertex(h+4,v+5)
    vertex(h+6,v+5)
    # vertex(h+6,v+5)
    vertex(h+10,v+9)
    # vertex(h+10,v+9)
    vertex(h+10,v+10)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h,v)
    vertex(h,v+1)
    # vertex(h,v+1)
    vertex(h+4,v+5)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h+6,v+5)
    vertex(h+10,v+1)
    # vertex(h+10,v+1)
    vertex(h+10,v)
    endShape()
    popMatrix()
dbn_p_letter['X'] = dbn_p_letterX
dbn_p_letter[24] = dbn_p_letterX
# X
def dbn_p_letterX(h, v, debug_poly=False):
    pushMatrix()
    scale(1, -1)
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h,v)
    vertex(h+10,v+10)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h,v+10)
    vertex(h+10,v)
    endShape()
    popMatrix()
dbn_p_letter['X'] = dbn_p_letterX
dbn_p_letter[24] = dbn_p_letterX
# Y
def dbn_p_letterY(h, v, debug_poly=False):
    pushMatrix()
    scale(1, -1)
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h,v+10)
    vertex(h,v+7)
    # vertex(h,v+7)
    vertex(h+3,v+4)
    # vertex(h+3,v+4)
    vertex(h+10,v+4)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h+10,v+10)
    vertex(h+10,v+1)
    endShape()
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h+9,v)
    vertex(h+2,v)
    # vertex(h+2,v)
    vertex(h,v+2)
    endShape()
    popMatrix()
dbn_p_letter['Y'] = dbn_p_letterY
dbn_p_letter[25] = dbn_p_letterY
# Z
def dbn_p_letterZ(h, v, debug_poly=False):
    pushMatrix()
    scale(1, -1)
    if debug_poly: stroke(random(256),200, 200)
    beginShape()
    vertex(h,v+10)
    vertex(h+10,v+10)
    # vertex(h+10,v+10)
    vertex(h,v)
    # vertex(h,v)
    vertex(h+10,v)
    endShape()
    popMatrix()
dbn_p_letter['Z'] = dbn_p_letterZ
dbn_p_letter[26] = dbn_p_letterZ