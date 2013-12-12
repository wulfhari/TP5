#! /usr/bin/env python
# -*- coding:Utf-8 -*-

import tkinter as tk

class Damier(tk.Frame):
    '''
    Classe permettant l'affichage d'un damier
    @author: Bryan Oakley
    '''

    def __init__(self, parent,size):
        '''size est la taille d'un cote d'une case en pixel.'''
        # Definition du damier
        self.rows = 8
        self.columns = 8
        self.size = size
        self.color1 = "white"
        self.color2 = "gray"
        self.pieces = {}
        # Calcul de la taille du dessin
        canvas_width = self.columns * self.size
        canvas_height = self.rows * self.size
        # Initialisation de la fenetre parente contenant le canvas
        tk.Frame.__init__(self, parent)
        # Initialisation du canvas
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,
                                width=canvas_width, height=canvas_height, background="white")
        # "Pack" le tout.
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)
        self.pack(side="top", fill="both", expand=True, padx=4, pady=4)

        # Fais en sorte que le redimensionnement de la fenetre redimensionne le damier
        self.canvas.bind("<Configure>", self.refresh)
        self.canvas.bind("<Button-1>",self.grab)
        self.canvas.bind("<ButtonRelease-1>",self.drop)
        
        

    def addpiece(self, name, row=0, column=0):
        '''Ajoute une piece sur le damier'''
        # Caracteres unicode des pieces
        dic_pieces = {'TB': '\u2656','CB': '\u2658','FB': '\u2657','RB': '\u2654','DB': '\u2655','PB': '\u2659',
                      'TN': '\u265C','CN': '\u265E','FN': '\u265D','RN': '\u265A','DN': '\u265B','PN': '\u265F',}
        tempfont = ('Helvetica',self.size//2)
        text = dic_pieces[name[0:2]]
        # On "dessine" le nom
        self.canvas.create_text(row, column, text=text, tags=(name, "piece"),font=tempfont)
        # On place la piece pour le rafraichissement
        self.pieces[name] = (row, column)
        self.placepiece(name, row, column)
        
        
    def placepiece(self, name, row, column):
        '''Place une piece a la position donnee row/column'''
        x0 = (column * self.size) + int(self.size / 2)
        y0 = (row * self.size) + int(self.size / 2)
        self.canvas.coords(name, x0, y0)

    def refresh(self, event):
        '''Redessine le damier lorsque la fenetre est redimensionnee'''
        # Calcul de la nouvelle taille du damier
        xsize = int((event.width - 1) / self.columns)
        ysize = int((event.height - 1) / self.rows)
        self.size = min(xsize, ysize)
        # On efface les cases
        self.canvas.delete("case")
        # On les redessine
        color = self.color2
        for row in range(self.rows):
            color = self.color1 if color == self.color2 else self.color2
            for col in range(self.columns):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="case")
                color = self.color1 if color == self.color2 else self.color2
        # On redessine les pieces
        for name in self.pieces:
            self.placepiece(name, self.pieces[name][0], self.pieces[name][1])
        # On mets les pieces au dessus des cases
        self.canvas.tag_raise("piece")
        self.canvas.tag_lower("case")
        
    def clear(self):
        self.canvas.delete("piece")
        
    def grab(self,event):
        x = event.x // self.size
        y = event.y // self.size
        print(y,x)
        return y,x
    
            
    def drop(self,event):
        x = event.x // self.size
        y = event.y // self.size
        print(y,x)
        return y,x
    

def addNouveauJeu(board):
        # Le blancs
        board.addpiece("TB1", 0, 0)
        board.addpiece("CB1", 0, 1)
        board.addpiece("FB1", 0, 2)
        board.addpiece("RB", 0, 3)
        board.addpiece("DB", 0, 4)
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
        board.addpiece("RN", 7, 3)
        board.addpiece("DN", 7, 4)
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

if __name__ == "__main__":
    root = tk.Tk()
    board = Damier(root,64)
    addNouveauJeu(board)
    root.mainloop()        
