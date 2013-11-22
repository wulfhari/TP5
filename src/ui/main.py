#! /usr/bin/env python
# -*- coding:Utf-8 -*-

'''
Created on 2013-11-03

@author: C. Besse
'''
from chess.fin import FinDePartie
from chess.game import GameManagement
from chess.plateau import Plateau
from chess.roi import Roi
import random

def testP():
    print("------------------ TEST PION ------------------")
    g = GameManagement("../jeuP.txt")
    print(g)
    p1 = g.board.getPiece(1,1)
    print((4,1) not in g.aJouer[p1]) # Pos inatteignable
    p2 = g.board.getPiece(1,3)
    print(p2 not in g.aJouer.keys()) # p2 aucune option de jeu
    g.play(p2, (2,3))
    print(g)
    rn = g.board.getPiece(7,7)
    g.play(rn, (7,6))
    print(g)
    p3 = g.board.getPiece(1,0)
    g.play(p3, (2,1))
    print(g)
    
    
def testC():
    print("------------------ TEST CAVALIER ------------------")
    g = GameManagement("../jeuC.txt")
    print(g)
    c1=g.board.getPiece(0,1)
    print((2,1) not in g.aJouer[c1])
    g.play(c1, (2,2))
    print(g)
    rn = g.board.getPiece(7,7)
    g.play(rn, (7,6))
    print(g)
    g.play(c1, (4,1))
    print(g)
    
def testT():
    print("------------------ TEST TOUR ------------------")
    g = GameManagement("../jeuT.txt")
    print(g)
    t1 = g.board.getPiece(0,0)
    print((1,1) not in g.aJouer[t1]) # inatteignable
    g.play(t1, (0,3))
    print(g)
    rn = g.board.getPiece(7,4)
    print((7,3) not in g.aJouer[rn])
    t2 = g.board.getPiece(7,0)
    g.play(t2, (7,3))
    print(g)
    g.play(t1, (4,3))
    print(g)
    g.play(t2, (4,3))
    print(g)
    
def testD():
    print("------------------ TEST DAME ------------------")
    g = GameManagement("../jeuD.txt")
    print(g)
    d1 = g.board.getPiece(0,1)
    g.play(d1, (0,4))
    print(g)
    d2 = g.board.getPiece(7,5)
    g.play(d2, (7,0))
    print(g)
    print((4,0) not in g.aJouer[d1]) # inatteignable
    g.play(d1, (3,1))
    print(g)
    g.play(d2, (1,0))
    print(g)
    rb = g.board.getPiece(0,0)
    g.play(rb, (1,0))
    print(g)
    rn = g.board.getPiece(7,7)
    g.play(rn, (6,7))
    print(g)    
    try:
        g.play(d1, (3,7))
    except FinDePartie as e:
        print(e.msg)
    print(g)
    print(g.aJouer)
    
def testF():
    print("------------------ TEST FOU ------------------")
    g = GameManagement("../jeuF.txt")
    print(g)
    f1 = g.board.getPiece(0,1)
    print(f1 not in g.aJouer) # roi echec
    print(f1 not in g.aJouer) # roi echec
    rb = g.board.getPiece(0,0)
    g.play(rb, (1,0))
    print(g)
    f2 = g.board.getPiece(5,5)
    print(f2 not in g.aJouer) # inatteignable
    g.play(f2, (6,4))
    print(g)
    f3 = g.board.getPiece(2,0)
    print((6,4) not in g.aJouer[f3]) # inatteignable
    g.play(f3, (3,1))
    print(g)
    f4 = g.board.getPiece(3,4)
    g.play(f4, (5,6))
    print(g)
    print((6,7) not in g.aJouer[f1]) # inatteignable
    
def testR():
    print("------------------ TEST ROI ------------------")
    g = GameManagement("../jeuR.txt")
    print(g)
    rb = g.board.getPiece(0,3)
    db = g.board.getPiece(2,4)
    cb = g.board.getPiece(1,3)
    rn = g.board.getPiece(7,3)
    dn = g.board.getPiece(7,4)
   
    g.play(rn, (7,1))
    print(g)
    g.play(rb, (0,5))
    print(g)
    g.play(dn, (7,5))
    print(g)
    print(db not in g.aJouer) # inatteignable
    print(g.aJouer)
    g.play(cb, (2,5))
    print(g)
    g.play(dn, (7,4))
    print(g)
    try:
        g.play(db, (6,0))
    except FinDePartie as e:
        print(e.msg)
    print(g)
    
def testRpat():
    print("------------------ TEST PAT ------------------")
    g = GameManagement("../jeuRpat.txt")
    print(g)
    t = g.board.getPiece(1,6)
    try:
        g.play(t, (6,6))
    except FinDePartie as e:
        print(e.msg)
    print(g)
    



if __name__ == "__main__":
    jeu = True
    #jeu = False
    testP()
    testC()
    testT()
    testD()
    testF()
    testR()
    testRpat()
    
    
    test = 0
    while test < 10000 and jeu:# jeu:
        try:
            g = GameManagement("../jeu1.txt")
            print(g)  
            ## OLD TEST:
            aJouer = g.aJouer
            while len(aJouer) != 0:
                # Joueur fou joue les deux joueurs:
                # Choisir une pièce au hasard
                piece = random.choice(list(aJouer.keys()))
                print(g.time,": Joueur joue :",piece,":",piece.pos)
                print("possibilités :",aJouer[piece])
                pos = aJouer[piece][random.randrange(len(aJouer[piece]))]
                pieceAManger = g.board.getPiece(pos[0], pos[1])
                
                if pieceAManger != None and (piece.color == pieceAManger.color or isinstance(pieceAManger,Roi)):
                    raise ValueError("D'ou ???")
                
                print(g.time,": Joueur joue :",piece,":",piece.pos,"->",pos)
                print(g)
                
                g.play(piece,pos)
                print(g)
        except FinDePartie as e:
            print(g)
            print(e.msg)
            test+=1
     
