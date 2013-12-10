#! /usr/bin/env python
# -*- coding:Utf-8 -*-

'''
Created on Dec 4, 2013

@author: Simon
'''

from tkinter import *
from src.chess.game import *
from src.chess.plateau import *
from src.ui.board import Damier

class Window(Frame):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        
        
        '''
        g = GameManagement()

        root = Tk()
        
        self.damier = Damier(root,64)
        self.damier.grid(row=0, column=0,rowspan=25, sticky=NSEW)
        # Maintient de l'affichage
        def addNouveauJeu(board):
            # Le blancs
            board.addpiece("TB1", 0, 0)
            board.addpiece("CB1", 0, 1)
            board.addpiece("FB1", 0, 2)
            board.addpiece("KB", 0, 3)
            board.addpiece("QB", 0, 4)
            board.addpiece("FB2", 0, 5)
            board.addpiece("CB2", 0, 6)
            board.addpiece("TB2", 0, 7)
            board.addpiece("PB1", 1, 0)
            board.addpiece("PB2", 1, 1)
            board.addpiece("PB3", 1, 2)
            board.addpiece("PB4", 1, 3)
            board.addpiece("PB5", 1, 4)
            board.addpiece("PB6", 1, 5)
            board.addpiece("PB7", 1, 6)
            board.addpiece("PB8", 1, 7)
            # Les noirs
            board.addpiece("TN1", 7, 0)
            board.addpiece("CN1", 7, 1)
            board.addpiece("FN1", 7, 2)
            board.addpiece("KN", 7, 3)
            board.addpiece("QN", 7, 4)
            board.addpiece("FN2", 7, 5)
            board.addpiece("CN2", 7, 6)
            board.addpiece("TN2", 7, 7)
            board.addpiece("PN1", 6, 0)
            board.addpiece("PN2", 6, 1)
            board.addpiece("PN3", 6, 2)
            board.addpiece("PN4", 6, 3)
            board.addpiece("PN5", 6, 4)
            board.addpiece("PN6", 6, 5)
            board.addpiece("PN7", 6, 6)
            board.addpiece("PN8", 6, 7)
        
        
        Label(root, text="Joueur 1", width=20,anchor=W).grid(row=0, column=1, sticky=W)
        Label(root, text="Joueur 2", width=20,anchor=W).grid(row=0, column=2, sticky=W)
        
        Label(root, text="Piece a jouer", width=20,anchor=W).grid(row=0, column=3, sticky=W)
        self.paj = Entry(root, width=25)
        self.paj.insert(0,"77")
        self.paj.grid(row=1, column=3, sticky=E+W)
        
        
        Label(root, text="Destination", width=20,anchor=W).grid(row=2, column=3, sticky=W)
        self.dest = Entry(root, width=25)
        self.dest.insert(0, "77" )
        self.dest.grid(row=3, column=3, sticky=E+W)
        
        Label(root, text="Nom du Fichier", width=20,anchor=W).grid(row=4, column=3, sticky=W)
        self.file = Entry(root, width=25)
        self.file.insert(0,"../jeu1.txt")
        self.file.grid(row=5, column=3, sticky=E+W)
        
        # Cr�ation du bouton effacant le text
        self.btn = Button(root, text="Personaliser")
        self.btn.grid(row=6,column=3,sticky=E+W)           
        # Cr�ation du bouton d�clanchant le calcul
        self.btn = Button(root, text="Nouvelle Partie",command=addNouveauJeu(self.damier))
        self.btn.grid(row=7,column=3,sticky=E+W)           
        
        board = Plateau()
        
        self.btn = Button(root, text="Charger une partie", command=g.lireFichier(self.file.get()))
        self.btn.grid(row=8,column=3,sticky=E+W)
        
        self.btn = Button(root, text="Enregistrer", command=g.EcrireFichier(self.file.get()))
        self.btn.grid(row=9,column=3,sticky=E+W)
        
        self.btn = Button(root, text="Quitter", command= quit)
        self.btn.grid(row=10,column=3,sticky=E+W)
        
        self.btn = Button(root, text="Coup Precedent")
        self.btn.grid(row=1,column=1,sticky=E+W)
        
        piece = str(self.paj.get())
        
        self.btn = Button(root, text="Coup Suivant")
        #, command=g.play(Plateau.getPiece(board.damier,piece[0],piece[1]),self.dest.get()))
        self.btn.grid(row=1,column=2,sticky=E+W)
        
        # Cr�ation de l'affichage
        self.txt = Text(root, height=25, width=25, wrap=WORD)
        self.txt.grid(row=2,column=1,columnspan=2, rowspan=25,sticky=NSEW)
        # Cr�ation de la scrollbar
#         sc = Scrollbar(root,orient=VERTICAL) 
#         ## association du d�placement de la glissi�re des scrollbar avec la position visible dans 
#         ## le widget Text et inversement.              
#         sc.config(command = self.txt.yview)
#         self.txt.config(yscrollcommand = sc.set)
#         self.txt.pack(sc)
        
        
        
        
        
        root.mainloop()
        
        
        
        
        
        
if __name__ == "__main__":
    win = Window()
    