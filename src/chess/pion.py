#! /usr/bin/env python
# -*- coding:Utf-8 -*-

'''
Created on 2013-11-03

@author: C. Besse
Fichier contenant la classe Pion
'''

from chess.piece import Piece

class Pion(Piece):
    '''
    Un pion est une pièce d'échec qui peut se déplacer que d'une case en avancant,
    ou de deux cases lors de son premier coup,
    ne peut manger qu'en diagonale, 
    et peut (peut-être) se transformer en arrivant sur la ligne de fond adverse.
    '''


    def __init__(self,nouvPos,couleur):
        """Initialise un pion à la position nouvPos = (ligne,colonne) avec la bonne couleur 0 pour noir, 1 pour blanc"""
        super().__init__(nouvPos,couleur) # Initialisation en utilisant les données membres de la classe mère.
        
    def posFuturesPossibles(self,plateau,protective):
        '''
        Retourne la liste des positions possibles à partir de la position actuelle.
        '''
        l = []
        # Si on est blanc on avance selon les x sinon selon les -x
        if self.color == 1:
            avance = 1
        else:
            avance = -1
        
        # Avance de 1
        if plateau.inbounds(self.pos[0]+avance,self.pos[1]) :
            piece = plateau.getPiece(self.pos[0]+avance,self.pos[1])
            if piece == None:
                l += [(self.pos[0]+avance,self.pos[1])]
        # Avance de 2
        if self.firstMove and plateau.inbounds(self.pos[0]+avance+avance,self.pos[1]):
            piece = plateau.getPiece(self.pos[0]+avance+avance,self.pos[1])
            if piece == None:
                l += [(self.pos[0]+avance+avance,self.pos[1])]
        # Mange à droite
        if plateau.inbounds(self.pos[0]+avance,self.pos[1]+1) :
            piece = plateau.getPiece(self.pos[0]+avance,self.pos[1]+1)
            if (piece != None and piece.color != self.color) or protective:
                l += [(self.pos[0]+avance,self.pos[1]+1)]
        # Mange à gauche
        if plateau.inbounds(self.pos[0]+avance,self.pos[1]-1) :
            piece = plateau.getPiece(self.pos[0]+avance,self.pos[1]-1)
            if (piece != None and piece.color != self.color) or protective:
                l += [(self.pos[0]+avance,self.pos[1]-1)]                
        return l

    def __repr__(self):
        """ Petit truc pour l'affichage """
        if self.color != 0:
            return "\u2659"
        else:
            return "\u265F"
