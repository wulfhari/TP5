'''
Created on Dec 4, 2013

@author: Simon
'''

from tkinter import *
from src.chess.game import *
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
        Label(root, text="Joueur 1", width=20,anchor=W).grid(row=0, column=1, sticky=W)
        Label(root, text="Joueur 2", width=20,anchor=W).grid(row=0, column=2, sticky=W)
        
        Label(root, text="Pièce à jouer", width=20,anchor=W).grid(row=0, column=3, sticky=W)
        self.sb = Entry(root, width=25)
        self.sb.insert(0,"")
        self.sb.grid(row=1, column=3, sticky=E+W)
        
        
        Label(root, text="Destination", width=20,anchor=W).grid(row=2, column=3, sticky=W)
        self.na = Entry(root, width=25)
        self.na.insert(0, "" )
        self.na.grid(row=3, column=3, sticky=E+W)
        
        Label(root, text="Nom du Fichier", width=20,anchor=W).grid(row=4, column=3, sticky=W)
        self.file = Entry(root, width=25)
        self.file.insert(0,"../jeu1.txt")
        self.file.grid(row=5, column=3, sticky=E+W)
        
        
        # Création du bouton effacant le text
        self.btn = Button(root, text="Personaliser")
        self.btn.grid(row=6,column=3,sticky=E+W)           
        # Création du bouton déclanchant le calcul
        self.btn = Button(root, text="Nouvelle Partie")
        self.btn.grid(row=7,column=3,sticky=E+W)           
        
        self.btn = Button(root, text="Charger une partie")
        self.btn.grid(row=8,column=3,sticky=E+W)
        
        self.btn = Button(root, text="Enregistrer")
        self.btn.grid(row=9,column=3,sticky=E+W)
        
        self.btn = Button(root, text="Quitter")
        self.btn.grid(row=10,column=3,sticky=E+W)
        
        self.btn = Button(root, text="Coup Précédent")
        self.btn.grid(row=1,column=1,sticky=E+W)
        
        self.btn = Button(root, text="Coup Suivant")
        self.btn.grid(row=1,column=2,sticky=E+W)
        
        # Création de l'affichage
        self.txt = Text(root, height=25, width=25, wrap=WORD)
        self.txt.grid(row=2,column=1,columnspan=2, rowspan=25,sticky=NSEW)
        # Création de la scrollbar
#         sc = Scrollbar(root,orient=VERTICAL) 
#         ## association du déplacement de la glissière des scrollbar avec la position visible dans 
#         ## le widget Text et inversement.              
#         sc.config(command = self.txt.yview)
#         self.txt.config(yscrollcommand = sc.set)
#         self.txt.pack(sc)
        
        self.damier = Damier(root,64)
        self.damier.grid(row=0, column=0,rowspan=25, sticky=NSEW)
        # Maintient de l'affichage
        root.mainloop()
        
        
        
        
if __name__ == "__main__":
    win = Window()