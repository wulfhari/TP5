#! /usr/bin/env python
# -*- coding:Utf-8 -*-

'''
Created on 2013-11-03

@author: C. Besse
'''

class Piece:
    '''
    Une piece d'échec abstraite qui contient les attributs Couleur et 
    Position pour toutes les pièces d'échecs.
    '''


    def __init__(self,nouvPos,couleur):
        '''
        Constructeur d'une pièce avec sa position et sa couleur
        '''
        self.pos = nouvPos # Sa position
        self.color = couleur # Sa couleur ... il faudra mettre super() si on a une classe Pièce mère.
        self.firstMove = True # Définit que la pièce n'a pas encore bougé
        
    def posFuturesPossibles(self,plateau,protective):
        '''
        Retourne la liste des positions possibles à partir de la position actuelle.
        '''
        return []

    def deplacer(self,nouvPos,plateau):
        self.pos = nouvPos
        self.firstMove = False # La pièce s'est maintenant déplacée.
        return self.pos

    def __repr__(self):
        """ Petit truc pour l'affichage """
        if self.color == 0:
            return "\u2665"
        else:
            return "\u2662"
