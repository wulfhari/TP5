#! /usr/bin/env python
# -*- coding:Utf-8 -*-

'''
Created on 2013-11-03

@author: C. Besse
Fichier contenant la classe Roi
'''

from src.chess.piece import Piece
from src.chess.pion import Pion
from src.chess.tour import Tour

class Roi(Piece):
    '''
    Un roi est une pièce d'échec qui peut se déplacer dans toutes les directions d'une seule case.
    '''

    def __init__(self,nouvPos,couleur):
        """Initialise un pion à la position nouvPos = (ligne,colonne) avec la bonne couleur 0 pour noir, 1 pour blanc"""
        super().__init__(nouvPos,couleur) # Initialisation en utilisant les données membres de la classe mère.
        

    def posFuturesPossibles(self,plateau,protective):
        '''
        Retourne la liste des positions possibles à partir de la position actuelle.
        '''
        l= []
        # Pour toutes les cases autour du roi
        for i in [-1,0,1]:
            for j in [-1,0,1]: # on ajoute :
                if plateau.inbounds(self.pos[0]+i,self.pos[1]+j) :
                    if i != 0 or j !=0: # Si ce n'est pas la case ou est le roi
                        piece = plateau.getPiece(self.pos[0]+i,self.pos[1]+j)
                        if piece == None : # S'il n'y'a pas de piece
                            l += [(self.pos[0]+i,self.pos[1]+j)]
                        elif piece.color != self.color or protective: # ou si c'est une piece adverse
                            l += [(self.pos[0]+i,self.pos[1]+j)]
        
        # Si on cherche juste a savoir les endroits atteignables
        # on ne considère pas le ROC ni les cases inaccessibles (on est en support)
        if protective:
            return l
        
        # Il faut également ajouter le petit ROC et le grand ROC si possibles
        if self.firstMove :
            line = self.pos[0]
            t_petit = plateau.getPiece(line,0)
            t_grand = plateau.getPiece(line,7)
            # Petit ROC
            if t_petit != None and t_petit.firstMove and plateau.getPiece(line,1) == None and plateau.getPiece(line,2) == None:
                l += [(line,1)] # On indique la possibilité du Petit ROC
            # Grand ROC
            if t_grand != None and t_grand.firstMove and plateau.getPiece(line,4) == None and plateau.getPiece(line,5) == None and plateau.getPiece(line,6) == None:
                l += [(line,5)] # On indique la possibilité du Grand ROC                
                        
        # Une fois ca fait il faut filtrer les cases accessibles aux pièces adverses.
        lAdverse = []
        del(plateau.damier[self.pos]) # On calcule toutes les positions adverses comme si le roi était absent
        for p in plateau.damier.values():
            lAdverse +=  [pos for pos in p.posFuturesPossibles(plateau,True) if p.color != self.color]
        plateau.damier[self.pos] = self # On remets le roi ensuite    
            
        lfiltree = [pos for pos in l if pos not in lAdverse]    
                        
        # On retourne ensuite l
        return lfiltree

    def __repr__(self):
        """ Petit truc pour l'affichage """
        if self.color != 0:
            return "\u2654"
        else:
            return "\u265A"
