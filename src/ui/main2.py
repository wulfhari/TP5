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
        

        root = Tk()
        
        
        # Maintient de l'affichage
        
        
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
        
        
        g = GameManagement(self.file.get())
        self.carreaux = Damier(root,64)
        self.carreaux.grid(row=0, column=0,rowspan=25, sticky=NSEW)
        
        
        def actualiser():
            pass
        
        
        def print_piece():
            for piece in g.board.pourEcrireFichier():
                self.carreaux.addpiece(piece[2:],int(piece[0]),int(piece[1]))
        
        def load_game():
            g.lireFichier(self.file.get())
            
        def save_game():
            g.EcrireFichier(self.file.get())
            
        def next_turn():
            pass
            #piece = str(self.paj.get())
            #g.play(Plateau.getPiece(board.damier,piece[0],piece[1]),self.dest.get()))
        
        def previous_turn():
            pass
        
        self.btn = Button(root, text="Nouvelle Partie", command = lambda :  print_piece())
        self.btn.grid(row=7,column=3,sticky=E+W)           
                
        self.btn = Button(root, text="Charger une partie", command= lambda : load_game())
        self.btn.grid(row=8,column=3,sticky=E+W)
        
        self.btn = Button(root, text="Enregistrer", command= lambda : save_game())
        self.btn.grid(row=9,column=3,sticky=E+W)
        
        self.btn = Button(root, text="Quitter", command= quit)
        self.btn.grid(row=10,column=3,sticky=E+W)
        
        self.btn = Button(root, text="Coup Precedent", command = previous_turn())
        self.btn.grid(row=1,column=1,sticky=E+W)
        
        
        self.btn = Button(root, text="Coup Suivant", command = next_turn())
        
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
    