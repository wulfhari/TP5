#! c:/Python33 python
# -*- coding:Utf-8 -*-

'''
Created on Dec 4, 2013

@author: Simon
'''

from tkinter import *
from src.chess.game import *
from src.chess.plateau import *
from src.ui.board import Damier
from src.ui.text_box import *

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
        
        ''' Créations des labels et des textbox '''
        Label(root, text="Joueur 1", width=20,anchor=W).grid(row=0, column=1, sticky=W)
        Label(root, text="Joueur 2", width=20,anchor=W).grid(row=0, column=2, sticky=W)
        
        Label(root, text="Piece a jouer", width=20,anchor=W).grid(row=0, column=3, sticky=W)
        self.paj = Entry(root, width=25)
        self.paj.insert(0,"46")
        self.paj.grid(row=1, column=3, sticky=E+W)
        
        
        Label(root, text="Destination", width=20,anchor=W).grid(row=2, column=3, sticky=W)
        self.dest = Entry(root, width=25)
        self.dest.insert(0, "44" )
        self.dest.grid(row=3, column=3, sticky=E+W)
        
        Label(root, text="Nom du Fichier", width=20,anchor=W).grid(row=4, column=3, sticky=W)
        self.file = Entry(root, width=25)
        self.file.insert(0,"../jeuC.txt")
        self.file.grid(row=5, column=3, sticky=E+W)
        
        
        self.btn = Button(root, text="Personaliser")
        self.btn.grid(row=6,column=3,sticky=E+W)           
        
        
        self.g = None
        self.carreaux = Damier(root,64)
        self.carreaux.grid(row=0, column=0,rowspan=25, sticky=NSEW)
        
        self.text = Text_Box(root, 25, 25)
        
        #self.text = Text(root, height=25, width=25, wrap=WORD)
        self.text.grid(row=2,column=1,columnspan=2, rowspan=25,sticky=NSEW)
        
        
        def actualiser():
            
            self.carreaux.clear()
            pieces_list = self.g.board.pourEcrireFichier()
            for piece in pieces_list:
                pieces_list[pieces_list.index(piece)] = piece + str(pieces_list.index(piece))
            
            print(pieces_list)
            for piece in pieces_list:
                self.carreaux.addpiece(piece[2:],int(piece[0]),int(piece[1]))
                
        
        def nouvelle_partie():
            
            path = "../jeu2.txt"
            self.g = GameManagement(path)
            actualiser()
        
        
        def load_game():
            
            path = self.file.get()
            self.g = GameManagement(path)
            actualiser()
            
            
        def save_game():
            self.g.EcrireFichier(self.file.get())
            
            
        def next_turn():
            pass
            piece = str(self.paj.get())
            dest = str(self.dest.get())
            self.g.play(Plateau.getPiece(self.g.board.damier,piece[0],piece[1]),dest[0],dest[1])
        
        
        def previous_turn():
            pass
        
        ''' Jouer une nouvelle partie depuis le fichier jeu2.txt'''
        self.btn = Button(root, text="Nouvelle Partie", command = lambda :  nouvelle_partie())
        self.btn.grid(row=7,column=3,sticky=E+W)           
                
        self.btn = Button(root, text="Charger une partie", command= lambda : load_game())
        self.btn.grid(row=8,column=3,sticky=E+W)
        
        self.btn = Button(root, text="Enregistrer", command= lambda : save_game())
        self.btn.grid(row=9,column=3,sticky=E+W)
        
        self.btn = Button(root, text="Quitter", command=quit)
        self.btn.grid(row=10,column=3,sticky=E+W)
        
        self.btn = Button(root, text="Coup Precedent", command = lambda : previous_turn())
        self.btn.grid(row=1,column=1,sticky=E+W)
                
        self.btn = Button(root, text="Coup Suivant", command = lambda : next_turn())
        self.btn.grid(row=1,column=2,sticky=E+W)
        
        # Creation de l'affichage du texte de la suite des coups


        
        root.mainloop()
        
        
if __name__ == "__main__":
    win = Window()
    