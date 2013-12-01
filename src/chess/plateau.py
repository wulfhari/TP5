#! /usr/bin/env python
# -*- coding:Utf-8 -*-

"""
@file: Plateau.py
@author:  C. Besse

Fichier contenant la classe Plateau
"""
print(dir())

from src.chess.tour import Tour
from src.chess.pion import Pion
from src.chess.cavalier import Cavalier
from src.chess.fou import Fou
from src.chess.dame import Dame
from src.chess.roi import Roi

class Plateau:
    
    def __init__(self, l_lignes=[]):
        """Initialise le plateau avec un damier vide"""
        if(l_lignes == []):
            self.damierParDefaut()
        else:
            self.luDepuisFichier(l_lignes)
        
    def getPiece(self,line,col):
        """Retourne la piece à la position (line,col) ou None sinon"""
        return self.damier.get((line,col))
    
    def getRoi(self,couleur):
        """Retourne le roi de la couleur indiqué : 0=NOIR, 1=BLANC"""
        for piece in self.damier.values():
            if isinstance(piece,Roi) and piece.color == couleur:
                return piece
    
    def deplacer(self,piece,nouvPos):
        """déplace la pièce à la nouvelle position"""
        oldPos = piece.pos
        nouvPos = piece.deplacer(nouvPos,self)
        if nouvPos != oldPos: # Le deplacement fonctionne
            self.damier[nouvPos] = piece
            del(self.damier[oldPos])
            return True # On retourne vrai pour dire que tout s'est bien passé
        else:
            return False 
    
    def inbounds(self,line,col):
        '''Definit si une position est sur le plateau ou non'''
        return line >=0 and line <=7 and col >=0 and col <=7
    
    def luDepuisFichier(self,l_lignes):
        '''
        Prends un série de lignes formatées (line,col,type,couleur) pour updater le damier avec.
        '''
        self.damier.clear()
        for l in l_lignes:
            pos = (int(l[0]),int(l[1]))  
            if(l[3] == "B"):
                couleur = 1
            else:
                couleur = 0
            if(l[2] == "C"):# Cavalier
                self.damier[pos] = Cavalier(pos, couleur)
            elif(l[2] == "F"):# Fou
                self.damier[pos] = Fou(pos, couleur)            
            elif(l[2] == "T"):# Tour
                self.damier[pos] = Tour(pos, couleur)                        
            elif(l[2] == "D"):# Dame
                self.damier[pos] = Dame(pos, couleur)                        
            elif(l[2] == "R"):# Roi
                self.damier[pos] = Roi(pos, couleur)                        
            else:# Pion            
                self.damier[pos] = Pion(pos, couleur)
                              
    def pourEcrireFichier(self):
        '''
        Retourne une série de lignes formatées (line,col,type,couleur)\n
        '''
        s = ""
        for p in self.damier.values():
            if p.color == 0:
                couleur = "N"
            else:
                couleur = "B"
            if isinstance(p,Pion):
                typ = "P"
            elif isinstance(p,Cavalier):
                typ = "C"
            elif isinstance(p,Fou):
                typ = "F"
            elif isinstance(p,Tour):
                typ = "T"
            elif isinstance(p,Dame):
                typ = "D"
            else: # Roi
                typ = "R"
            s += str(p.pos[0]) + str(p.pos[1]) + typ + couleur + "\n" 
        
        return s
    
    def __repr__(self):
        """ Petit truc pour l'affichage """
        s = " +-0-+-1-+-2-+-3-+-4-+-5-+-6-+-7-+\n"
#        s += " +---+---+---+---+---+---+---+---+\n"
        for i in range(0,8):
            s+= str(i)+"| "
            for j in range(0,8):
                if (i,j) in self.damier:
                    s += str(self.damier[(i,j)])+" | "
                else:
                    s += "  | "
            s += "\n +---+---+---+---+---+---+---+---+\n"
            
        return s
            
    def damierParDefaut(self):
        '''Initialise le Damier par défaut avec la position classique de départ'''
        self.damier = {(0,0):Tour((0,0),1), 
                       (0,1):Cavalier((0,1),1), 
                       (0,2):Fou((0,2),1), 
                       (0,3):Roi((0,3),1), 
                       (0,4):Dame((0,4),1), 
                       (0,5):Fou((0,5),1), 
                       (0,6):Cavalier((0,6),1), 
                       (0,7):Tour((0,7),1), 
                       (1,0):Pion((1,0),1), 
                       (1,1):Pion((1,1),1), 
                       (1,2):Pion((1,2),1), 
                       (1,3):Pion((1,3),1), 
                       (1,4):Pion((1,4),1), 
                       (1,5):Pion((1,5),1), 
                       (1,6):Pion((1,6),1), 
                       (1,7):Pion((1,7),1), 
                       (6,0):Pion((6,0),0), 
                       (6,1):Pion((6,1),0), 
                       (6,2):Pion((6,2),0), 
                       (6,3):Pion((6,3),0), 
                       (6,4):Pion((6,4),0), 
                       (6,5):Pion((6,5),0), 
                       (6,6):Pion((6,6),0), 
                       (6,7):Pion((6,7),0), 
                       (7,0):Tour((7,0),0), 
                       (7,1):Cavalier((7,1),0), 
                       (7,2):Fou((7,2),0), 
                       (7,3):Roi((7,3),0), 
                       (7,4):Dame((7,4),0), 
                       (7,5):Fou((7,5),0), 
                       (7,6):Cavalier((7,6),0), 
                       (7,7):Tour((7,7),0)}

if __name__ == "__main__":
    p = Plateau()
    print(p)
         
        
