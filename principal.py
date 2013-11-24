#! /usr/bin/env python
# -*- coding:Utf-8 -*-

'''
Created on 2013-11-22

@author: Admin
'''

if __name__ == '__main__':


import Tkinter as tk

class Damier(tk.Frame):
    '''
    Classe permettant l'affichage d'un damier
    @author: Bryan Oakley & Camille Besse
    '''

        def __init__(self, parent,taille_case):
            '''size est la taille d'un cote d'une case en pixel.'''
            # Definition du damier : # de cases
            self.lignes = 8
            self.colonnes = 8
    
            # Definition du damier : taille des cases
            self.taille_case = taille_case
    
            # Definition du damier : couleur de cases
            self.couleur1 = "white"
            self.couleur2 = "gray"
    
            # Pièces sur le damier
            self.pieces = {}
    
            # Calcul de la taille du dessin
            canvas_width = self.colonnes * self.taille_case
            canvas_height = self.lignes * self.taille_case
    
            # Initialisation de la fenêtre parente contenant le canvas
            tk.Frame.__init__(self, parent)
    
            # Initialisation du canvas
            self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,
                                    width=canvas_width, height=canvas_height,
                                    background="white")
    
            # "Pack" le tout.
            self.canvas.pack(expand=True, fill="both", padx=2, pady=2)
            self.pack(expand=True, fill="both", padx=4, pady=4)
    
            # Fais en sorte que le redimensionnement de la fenetre redimensionne le damier
            self.canvas.bind("<Configure>", self.actualiser)
    
        def ajouter_piece(self, nom_piece, ligne=0, colonne=0):
            '''Ajoute une piece sur le damier'''
            # Caractères unicode des pièces
            caracteres_unicode_pieces = {'TB': '\u2656',
                                         'CB': '\u2658',
                                         'FB': '\u2657',
                                         'KB': '\u2654',
                                         'QB': '\u2655',
                                         'PB': '\u2659',
                                         'TN': '\u265C',
                                         'CN': '\u265E',
                                         'FN': '\u265D',
                                         'KN': '\u265A',
                                         'QN': '\u265B',
                                         'PN': '\u265F',}
            tempfont = ('Helvetica',self.taille_case//2)
            piece_unicode = caracteres_unicode_pieces[nom_piece[0:2]]
            # On "dessine" le nom
            self.canvas.create_text(ligne, colonne, text=piece_unicode,
                                    tags=(nom_piece, "piece"),font=tempfont)
            # On place la piece pour le rafraichissement
            self.pieces[nom_piece] = (ligne, colonne)
            self.placer_piece(nom_piece, ligne, colonne)
    
        def placer_piece(self, nom_piece, ligne, colonne):
            '''Place une piece a la position donnee row/column'''
            # Placer les pieces au centre des cases
            x0 = (colonne * self.taille_case) + int(self.taille_case / 2)
            y0 = (ligne * self.taille_case) + int(self.taille_case / 2)
            self.canvas.coords(nom_piece, x0, y0)
    
        def actualiser(self, event):
            '''Redessine le damier lorsque la fenetre est redimensionnee'''
    
            # Calcul de la nouvelle taille du damier
            xsize = int((event.width - 1) / self.colonnes)
            ysize = int((event.height - 1) / self.lignes)
            self.taille_case = min(xsize, ysize)
    
            # On efface les cases
            self.canvas.delete("case")
    
            # On les redessine
            color = self.couleur2
            for row in range(self.lignes):
                #Alternance des couleurs
                if color == self.couleur2:
                    color = self.couleur1
                else:
                    color = self.couleur2
    
                for col in range(self.colonnes):
                    x1 = col * self.taille_case
                    y1 = row * self.taille_case
                    x2 = x1 + self.taille_case
                    y2 = y1 + self.taille_case
                    self.canvas.create_rectangle(x1, y1, x2, y2,
                                                 outline="black", fill=color, tags="case")
    
                    #Alternance des couleurs
                    if color == self.couleur2:
                        color = self.couleur1
                    else:
                        color = self.couleur2
    
            # On redessine les pieces
            for name in self.pieces:
                self.placer_piece(name, self.pieces[name][0], self.pieces[name][1])
    
            # On mets les pieces au dessus des cases
            self.canvas.tag_raise("piece")
            self.canvas.tag_lower("case")
    
    
    def initialise_jeu(plateau):
            # Le blancs
            plateau.ajouter_piece("TB1", 0, 0)
            plateau.ajouter_piece("CB1", 0, 1)
            plateau.ajouter_piece("FB1", 0, 2)
            plateau.ajouter_piece("KB", 0, 3)
            plateau.ajouter_piece("QB", 0, 4)
            plateau.ajouter_piece("FB2", 0, 5)
            plateau.ajouter_piece("CB2", 0, 6)
            plateau.ajouter_piece("TB2", 0, 7)
            plateau.ajouter_piece("PB1", 1, 0)
            plateau.ajouter_piece("PB2", 1, 1)
            plateau.ajouter_piece("PB3", 1, 2)
            plateau.ajouter_piece("PB4", 1, 3)
            plateau.ajouter_piece("PB5", 1, 4)
            plateau.ajouter_piece("PB6", 1, 5)
            plateau.ajouter_piece("PB7", 1, 6)
            plateau.ajouter_piece("PB8", 1, 7)
            # Les noirs
            plateau.ajouter_piece("TN1", 7, 0)
            plateau.ajouter_piece("CN1", 7, 1)
            plateau.ajouter_piece("FN1", 7, 2)
            plateau.ajouter_piece("KN", 7, 3)
            plateau.ajouter_piece("QN", 7, 4)
            plateau.ajouter_piece("FN2", 7, 5)
            plateau.ajouter_piece("CN2", 7, 6)
            plateau.ajouter_piece("TN2", 7, 7)
            plateau.ajouter_piece("PN1", 6, 0)
            plateau.ajouter_piece("PN2", 6, 1)
            plateau.ajouter_piece("PN3", 6, 2)
            plateau.ajouter_piece("PN4", 6, 3)
            plateau.ajouter_piece("PN5", 6, 4)
            plateau.ajouter_piece("PN6", 6, 5)
            plateau.ajouter_piece("PN7", 6, 6)
            plateau.ajouter_piece("PN8", 6, 7)
    
    if __name__ == "__main__":
        root = tk.Tk()
    
        plateau = Damier(root,64)
    
        initialise_jeu(plateau)
    
        root.mainloop()        
