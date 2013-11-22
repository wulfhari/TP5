#! /usr/bin/env python
# -*- coding:Utf-8 -*-

'''
Created on 2013-11-03

@author: C. Besse
Fichier contenant la classe Piece
'''

from chess.piece import Piece

class Cavalier(Piece):
    '''
    Un cavalier est une pièce d'échec qui peut se déplacer de deux cases 
    en avancant puis d'une case sur le côté dans les 4 directions. 
    Soit 8 déplacements possibles au maximum
    '''


    def __init__(self,nouvPos,couleur):
        """Initialise un pion à la position nouvPos = (ligne,colonne) avec la bonne couleur 0 pour noir, 1 pour blanc"""
        super().__init__(nouvPos,couleur) # Initialisation en utilisant les données membres de la classe mère.
        
    def posFuturesPossibles(self,plateau,protective):
        '''
        Retourne la liste des positions possibles à partir de la position actuelle.
        '''
        l = []
        
        for i in [-2,-1,1,2]:
            for j in [-2,-1,1,2]:
                # Pour les 8 positions autour possibles
                if abs(i) != abs(j) :
                    if plateau.inbounds(self.pos[0]+i,self.pos[1]+j) :
                        piece = plateau.getPiece(self.pos[0]+i,self.pos[1]+j)
                        # Si on rencontre une pièce, selon l'adversité on ajoute
                        if piece != None:
                            if protective or piece.color != self.color:
                                l += [(self.pos[0]+i,self.pos[1]+j)]
                        else: # Sinon on ajoute 
                                l += [(self.pos[0]+i,self.pos[1]+j)]
        
        return l

    def __repr__(self):
        """ Petit truc pour l'affichage """
        if self.color != 0:
            return "\u2658"
        else:
            return "\u265E"
