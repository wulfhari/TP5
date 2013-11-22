#! /usr/bin/env python
# -*- coding:Utf-8 -*-

"""
@file: Tour.py
@author:  C. Besse

Fichier contenant la classe Tour
"""

from chess.piece import Piece

class Tour(Piece):
    '''Une tour est une pièce d'échec qui peut se déplacer selon les ligne set les colonnes'''
    
    def __init__(self,nouvPos,couleur):
        """Initialise une tour à la position nouvPos = (ligne,colonne) avec la bonne couleur 0 pour noir, 1 pour blanc"""
        super().__init__(nouvPos,couleur) # Initialisation en utilisant les données membres de la classe mère.
        
    def posFuturesPossibles(self,plateau,protective):
        l = []
        # Pour chacune des diagonales
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if abs(i) != abs(j):
                    k = 1
                    # Tant qu'on atteint pas un bord
                    while plateau.inbounds(self.pos[0]+i*k,self.pos[1]+j*k) :
                        piece = plateau.getPiece(self.pos[0]+i*k,self.pos[1]+j*k)
                        # Si on rencontre une pièce, selon l'adversité on ajoute
                        if piece != None:
                            if protective or piece.color != self.color:
                                l += [(self.pos[0]+i*k,self.pos[1]+j*k)]
                            k = 100 # et on arrete la en se propulsant hors-plateau
                        else: # Sinon on ajoute et on va voir à k+1
                                l += [(self.pos[0]+i*k,self.pos[1]+j*k)]
                                k += 1
        return l
    
    def __repr__(self):
        """ Petit truc pour l'affichage """
        if self.color != 0:
            return "\u2656"
        else:
            return "\u265C"
        
        
        