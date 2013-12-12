#! c:/Python33 python
# -*- coding:Utf-8 -*-

'''
Created on Dec 4, 2013

@author: Simon
'''

import tkinter as tk
from tkinter import *
from src.chess.game import *
from src.chess.plateau import *
from src.ui.board import Damier
from src.ui.text_box import *

class Window(Frame):
    '''
    classdocs
    '''


    def __init__(self,root):
        '''
        Constructor
        
        
        '''
        
        self.root = root
        self.g = None
        
        ''' Initialisation des canvas '''
        # initialisation du canvas qui contient les pieces mangees
        self.eaten = tk.Canvas(self.root, borderwidth=0, highlightthickness=0,width=512, height=128, background="white")
        self.eaten.pack(side="top", fill="both", expand=True, padx=2, pady=2)
        self.eaten.grid(row=26,column = 0, sticky=S)
        # initialisation du damier
        self.carreaux = Damier(self.root,64)
        self.carreaux.grid(row=0, column=0,rowspan=25, sticky=NSEW)
        
        
        ''' Initialisation de la zone de texte pour l'historique'''
        
        self.text = Text_Box(self.root, 25, 25)
        #self.text = Text(root, height=25, width=25, wrap=WORD)
        self.text.grid(row=2,column=1,columnspan=2, rowspan=25,sticky=NSEW)
        
        
        self.mouseGrab = None
        self.mouseDrop = None
        self.root.bind("<Button-1>", self.grab_piece)
        self.root.bind("<ButtonRelease-1>", self.drop_piece)
        
        
        ''' Créations des labels et des textbox '''
        Label(self.root, text="Joueur 1", width=20,anchor=W).grid(row=0, column=1, sticky=W)
        Label(self.root, text="Joueur 2", width=20,anchor=W).grid(row=0, column=2, sticky=W)
        
        Label(self.root, text="Piece a jouer", width=20,anchor=W).grid(row=0, column=3, sticky=W)
        self.paj = Entry(self.root, width=25)
        self.paj.insert(0,"46")
        self.paj.grid(row=1, column=3, sticky=E+W)
        
        
        Label(self.root, text="Destination", width=20,anchor=W).grid(row=2, column=3, sticky=W)
        self.dest = Entry(self.root, width=25)
        self.dest.insert(0, "44" )
        self.dest.grid(row=3, column=3, sticky=E+W)
        
        Label(self.root, text="Nom du Fichier", width=20,anchor=W).grid(row=4, column=3, sticky=W)
        self.file = Entry(self.root, width=25)
        self.file.insert(0,"../jeuC.txt")
        self.file.grid(row=5, column=3, sticky=E+W)
        
        
        '''Creation des bouttons de commandes'''
        
        #bouton personaliser
        self.btn = Button(self.root, text="Personaliser")
        self.btn.grid(row=6,column=3,sticky=E+W)           
        
        # Jouer une nouvelle partie depuis le fichier jeu2.txt
        self.btn = Button(self.root, text="Nouvelle Partie", command = lambda :  self.nouvelle_partie())
        self.btn.grid(row=7,column=3,sticky=E+W)           
        
        #bouton charger une partie
        self.btn = Button(self.root, text="Charger une partie", command= lambda : self.load_game())
        self.btn.grid(row=8,column=3,sticky=E+W)
        
        #bouton enregistrer
        self.btn = Button(self.root, text="Enregistrer", command= lambda : self.save_game())
        self.btn.grid(row=9,column=3,sticky=E+W)
        
        #bouton quiter
        self.btn = Button(self.root, text="Quitter", command=quit)
        self.btn.grid(row=10,column=3,sticky=E+W)
        
        #bouton coup precedent
        self.btn = Button(self.root, text="Coup Precedent", command = lambda : self.previous_turn())
        self.btn.grid(row=1,column=1,sticky=E+W)
        
        
        
        ###############################################################
        # Debut de la section des methode de la classe Window
        ###############################################################
    def actualiser(self):
        
        self.carreaux.clear()
        pieces_list = self.g.board.pourEcrireFichier()
        for piece in pieces_list:
            pieces_list[pieces_list.index(piece)] = piece + str(pieces_list.index(piece))
        
        print(pieces_list)
        for piece in pieces_list:
            self.carreaux.addpiece(piece[2:],int(piece[0]),int(piece[1]))
            
    
    def nouvelle_partie(self):
        
        path = "../jeu2.txt"
        self.g = GameManagement(path)
        self.actualiser()
    
    
    def load_game(self):
        
        path = self.file.get()
        self.g = GameManagement(path)
        self.actualiser()
        
        
    def save_game(self):
        self.g.EcrireFichier(self.file.get())
        
        
    def next_turn(self):
        pass
        piece = str(self.paj.get())
        dest = str(self.dest.get())
        self.g.play(Plateau.getPiece(self.g.board.damier,piece[0],piece[1]),dest[0],dest[1])
    
        
    def grab_piece(self, event):
        self.mouseGrab = self.carreaux.grab(event)
        
    
        
    def drop_piece(self, event):
        self.mouseDrop = self.carreaux.drop(event)
        self.next_turn
        '''Insérer ici du error handling
        if self.g == None:
            Raise ValueError('Veuillez charger une partie')
        '''
        self.g.play(self.g.board.getPiece(self.mouseGrab[0], self.mouseGrab[1]), self.mouseDrop)
        self.actualiser()
        
        
    def previous_turn(self):
        pass
    
    
    
    
    '''self.btn = Button(root, text="Coup Suivant", command = lambda : next_turn())
    self.btn.grid(row=1,column=2,sticky=E+W)
    '''
    
    '''Pour jouer les coups'''
        
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    win = Window(root)
    root.mainloop()
    