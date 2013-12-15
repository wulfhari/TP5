#! c:/Python33 python
# -*- coding:Utf-8 -*-

'''
Created on Dec 4, 2013

@author: Simon
'''

import tkinter as tk
from tkinter import *
from tkinter import filedialog
from src.chess.game import *
from src.chess.plateau import *
from src.ui.board import Damier
from src.ui.text_box import *
from src.chess.tour import Tour
from src.chess.pion import Pion
from src.chess.cavalier import Cavalier
from src.chess.fou import Fou
from src.chess.dame import Dame
from src.chess.roi import Roi
from src.chess.piece import Piece

class Window(Frame):
    '''
    classdocs
    '''


    def __init__(self,root):
        '''
        Constructor
        
        
        '''
        
        self.root = root
        self.g = GameManagement('../jeu1.txt')
        
        ''' Initialisation des canvas '''
        # initialisation du canvas qui contient les pieces mangees
        #self.eaten = tk.Canvas(self.root, borderwidth=0, highlightthickness=0,width=512, height=128, background="white")
        #self.eaten.pack(side="top", fill="both", expand=True, padx=2, pady=2)
        #self.eaten.grid(row=26,column = 0, sticky=S)
        
        # initialisation du damier
        self.carreaux = Damier(self.root,64)
        self.carreaux.grid(row=0, column=0,rowspan=25, sticky=NSEW)
        
        
        ''' Initialisation de la zone de texte pour l'historique'''
        
        self.text = Text_Box(self.root, 25, 25)
        #self.text = Text(root, height=25, width=25, wrap=WORD)
        self.text.text_insert("Cliquez et bougez la piece a jouer\n\n", 'Historique des coups')
        self.text.text_insert('Depart', 'Arivee')
        self.text.grid(row=2,column=1,columnspan=2, rowspan=25,sticky=NSEW)
        
        
        ''' Créations des labels et des textbox '''
        Label(self.root, text="Joueur 1", width=20,anchor=W).grid(row=0, column=1, sticky=W)
        Label(self.root, text="Joueur 2", width=20,anchor=W).grid(row=0, column=2, sticky=W)
        
        
        Label(self.root, text="Nom du Fichier actif", width=20,anchor=W).grid(row=0, column=3, sticky=W)
        self.file = Entry(self.root, width=25)
        self.file.insert(0," ")
        self.file.grid(row=1, column=3, sticky=E+W)
        
        
        '''Creation des bouttons de commandes'''
        
        self.btn = Button(self.root, text="Choisir un fichier", command = lambda :self.path_dialog())
        self.btn.grid(row=2,column=3,sticky=N+E+W)
        
        
        # Jouer une nouvelle partie depuis le fichier jeu1.txt
        self.btn = Button(self.root, text="Nouvelle Partie", command = lambda :  self.nouvelle_partie())
        self.btn.grid(row=3,column=3,sticky=N+E+W)           
        
        #bouton enregistrer
        self.btn = Button(self.root, text="Enregistrer", command= lambda : self.save_game())
        self.btn.grid(row=4,column=3,sticky=N+E+W)
        
        #bouton quiter
        self.btn = Button(self.root, text="Quitter", command=quit)
        self.btn.grid(row=5,column=3,sticky=N+E+W)
        
        self.perso_state = "off"
        self.perso_btn = Button(self.root, text="Personaliser", command = lambda : self.switch_perso())
        self.perso_btn.grid(row=6, column=3, sticky=N+W+E)
        
        
        self.btn = Button(self.root, text="Effacer", command=lambda : self.clear())
        self.btn.grid(row=7,column=3,sticky=N+E+W)
        
        #bouton coup precedent
        self.btn = Button(self.root, text="Coup Precedent", command = lambda : self.previous_turn())
        self.btn.grid(row=1,column=1,sticky=E+W)
        
        self.btn = Button(self.root, text="Coup Suivant", command = lambda : self.previous_turn())
        self.btn.grid(row=1,column=2,sticky=E+W)
        
        
        ''' Radio boutons pour la personalisation des parties'''
                # radio bouton pour la couleur
        
        Label(self.root, text="Couleur a ajouter", width=20,anchor=W).grid(row=15, column=3, sticky=W)
        self.color_state = IntVar()
        self.noir = Radiobutton(self.root, text="Noir", variable=self.color_state, value=0)
        self.noir.grid(row=16, column=3, sticky=W)
        self.blanc = Radiobutton(self.root, text="Blanc", variable=self.color_state, value=1)
        self.blanc.grid(row=17, column=3, sticky=W)
        
        #radio bouton pour le choix de la piece
        
        Label(self.root, text="Piece a ajouter", width=20,anchor=W).grid(row=18, column=3, sticky=W)
        self.piece = StringVar()
        self.pion = Radiobutton(self.root, text="Pion", variable=self.piece, value='Pion')
        self.pion.grid(row=19, column=3, sticky=W)
        
        self.tour = Radiobutton(self.root, text="Tour", variable=self.piece, value='Tour')
        self.tour.grid(row=20, column=3, sticky=W)
        
        self.cavalier = Radiobutton(self.root, text="Cavalier", variable=self.piece, value='Cavalier')
        self.cavalier.grid(row=21, column=3, sticky=W)
        
        self.fou = Radiobutton(self.root, text="Fou", variable=self.piece, value='Fou')
        self.fou.grid(row=22, column=3, sticky=W)
        
        self.dame = Radiobutton(self.root, text="Dame", variable=self.piece, value='Dame')
        self.dame.grid(row=23, column=3, sticky=W)
        
        self.roi = Radiobutton(self.root, text="Roi", variable=self.piece, value='Roi')
        self.roi.grid(row=24, column=3, sticky=W)
        
        
        ''' GEstion des clicks de la sourie'''
        self.carreaux.canvas.bind("<Button-1>", self.grab_piece)
        self.carreaux.canvas.bind("<ButtonRelease-1>", self.drop_piece)
        
        
        
            
        ###############################################################
        # Debut de la section des methode de la classe Window
        ###############################################################
        '''pour actualiser le joueur actif'''
    def joueur(self):
        if self.g.color == 1:
            Label(self.root, text="Joueur 1", width=20,anchor=W,foreground="white",background="gray75").grid(row=0, column=1, sticky=W)
            Label(self.root, text="Joueur 2", width=20,anchor=W).grid(row=0, column=2, sticky=W)
        elif self.g.color ==0:
            Label(self.root, text="Joueur 1", width=20,anchor=W).grid(row=0, column=1, sticky=W)
            Label(self.root, text="Joueur 2", width=20,anchor=W,foreground="white",background="gray75").grid(row=0, column=2, sticky=W)    
        
        '''pour actualiser l'affichage'''
    def actualiser(self):
        
        self.carreaux.clear()
        pieces_list = self.g.board.pourEcrireFichier()
        for piece in pieces_list:
            pieces_list[pieces_list.index(piece)] = piece + str(pieces_list.index(piece))
        
        for piece in pieces_list:
            self.carreaux.addpiece(piece[2:],int(piece[0]),int(piece[1]))
        self.joueur()
            
        '''Pour creer une partie vierge'''
    def clear(self):
        self.g = GameManagement('../jeu2.txt')
        self.actualiser()
        ''' pour creer une partie avec les blancs en haut'''
    def nouvelle_partie(self):
        
        path = "../jeu1.txt"
        self.g = GameManagement(path)
        self.actualiser()
    
        ''' pour lire un fichier de partie'''
    def load_game(self):
        
        path = self.file.get()
        self.g = GameManagement(path)
        self.actualiser()
        
        ''' pour ecrire un fichier de partie'''
    def save_game(self):
        self.g.EcrireFichier(self.file.get())
        
        
    def next_turn(self):
        
        piece = str(self.paj.get())
        dest = str(self.dest.get())
        self.g.play(Plateau.getPiece(self.g.board.damier,piece[0],piece[1]),dest[0],dest[1])
    
        '''pour determiner la piece cliquee'''
    def grab_piece(self, event):
        self.mouseGrab = self.carreaux.grab(event)
        
    
        '''Pour jouer les coups'''
    def drop_piece(self, event):
        self.mouseDrop = self.carreaux.drop(event)
        self.next_turn
        '''Insérer ici du error handling
        if self.g == None:
            Raise ValueError('Veuillez charger une partie')
        '''
        self.g.play(self.g.board.getPiece(self.mouseGrab[0], self.mouseGrab[1]), self.mouseDrop)
        self.histo()
        self.actualiser()
        
    def add_piece(self,event):
        self.mouseGrab = self.carreaux.grab(event)
        
        
        
        if self.piece.get() == 'Pion':
            self.g.board.damier[(self.mouseGrab)]=Pion((self.mouseGrab),self.color_state.get())
        elif self.piece.get() == 'Dame':
            self.g.board.damier[(self.mouseGrab)]=Dame((self.mouseGrab),self.color_state.get())
        elif self.piece.get() == 'Roi':
            self.g.board.damier[(self.mouseGrab)]=Roi((self.mouseGrab),self.color_state.get())
        elif self.piece.get() == 'Cavalier':
            self.g.board.damier[(self.mouseGrab)]=Cavalier((self.mouseGrab),self.color_state.get())
        elif self.piece.get() == 'Fou':
            self.g.board.damier[(self.mouseGrab)]=Fou((self.mouseGrab),self.color_state.get())    
        elif self.piece.get() == 'Tour':
            self.g.board.damier[(self.mouseGrab)]=Tour((self.mouseGrab),self.color_state.get())    
                        
        self.actualiser()
        
    def del_piece(self,event):
            self.mouseGrab = self.carreaux.grab(event)
            self.g.board.damier[(self.mouseGrab)]=None
            self.actualiser()
    ''' pour choisir le fichier qui servira lors de l'ecriture et de la lecture de partie '''
    def path_dialog(self):
        self.file_path = filedialog.askopenfilename(title="Open file", filetypes=[("txt file",".txt"),("All files",".*")])
        if self.file_path != "":
            self.file.delete(0, END)
            self.file.insert(0,self.file_path)
            self.load_game()
        else:
            self.file.delete(0, END)
            self.file.insert(0,"Choisisez un fichier")
        
            
            ''' Gestion de la personalisation'''
    def switch_perso(self):
        if self.perso_state == "off":
            self.perso_btn.config(text="Terminer la personnalisation")
            self.carreaux.canvas.bind("<Button-1>", self.add_piece)
            #self.root.bind("<Button-3>", self.del_piece)
            self.perso_state = "on"
        else:
            self.perso_btn.config(text="Personaliser")
            self.carreaux.canvas.bind("<Button-1>", self.carreaux.grab)
            self.carreaux.canvas.bind("<ButtonRelease-1>", self.carreaux.drop)
            self.perso_state = "off"
            
            
            
    def histo(self):
        
        self.text.text_insert(((self.g.board.getPiece(self.mouseDrop[0], self.mouseDrop[1]),self.mouseGrab[0], self.mouseGrab[1])), (self.g.board.getPiece(self.mouseDrop[0], self.mouseDrop[1]),self.mouseDrop))
        
if __name__ == "__main__":
    root=Tk()
    win = Window(root)
    root.mainloop()
    