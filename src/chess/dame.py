#! /usr/bin/env python
# -*- coding:Utf-8 -*-

'''
Created on 2013-11-03

@author: C. Besse
Fichier contenant la classe Dame
'''

from src.chess.piece import Piece
from src.chess.tour import Tour
from src.chess.fou import Fou

class Dame(Piece):
    '''
    Un dame est une pièce d'échec qui peut se déplacer dans toutes les directions.
    '''


    def __init__(self,nouvPos,couleur):
        """Initialise un pion à la position nouvPos = (ligne,colonne) avec la bonne couleur 0 pour noir, 1 pour blanc"""
        super().__init__(nouvPos,couleur) # Initialisation en utilisant les données membres de la classe mère.
        
    def posFuturesPossibles(self,plateau,protective):
        '''
        Retourne la liste des positions possibles à partir de la position actuelle.
        '''
        t = Tour(self.pos,self.color)
        f = Fou(self.pos,self.color)
        
        lt = t.posFuturesPossibles(plateau,protective)
        lf = f.posFuturesPossibles(plateau,protective)
        
        return lt+lf

    def __repr__(self):
        """ Petit truc pour l'affichage """
        if self.color != 0:
            return "\u2655"
        else:
            return "\u265B"
