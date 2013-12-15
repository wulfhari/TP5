#! /usr/bin/env python
# -*- coding:Utf-8 -*-

'''
Created on 2013-11-06

@author: C. Besse
Fichier contenant la classe GameManagement
'''
from src.chess.cavalier import Cavalier
from src.chess.dame import Dame
from src.chess.fin import FinDePartie
from src.chess.fou import Fou
from src.chess.pion import Pion
from src.chess.plateau import Plateau
from src.chess.roi import Roi
from src.chess.tour import Tour

class GameManagement:
    '''
    Pour la gestion du jeu
    '''
    def __init__(self,f_path=""):
        '''
        Constructeur du game management
        '''
        self.time = 0 # Le nombre de tours joués
        self.color = 1 # les blancs jouent toujours en premier.
        self.board = Plateau() # le plateau de jeu
        self.eaten = {} # La liste des pièce mangées selon le joueur
        self.eaten[0] = []
        self.eaten[1] = []
        self.pat = 0 # Le nombre de coups depuis la dernière prise  
        self.check = False
        if f_path != "":
            self.lireFichier(f_path)
        self.aJouer = {} # Le dictionnaire des coups possibles au prochain coup
        self.calculAJouer()
        
        print(self.aJouer)
        
    def calculAJouer(self):
        '''
        Initialse le dictionaire des coups possibles à jouer selon le tour de jeu.
        '''
        for piece in self.board.damier.values():
            if(piece.color == self.color):
                #Verifie que la piece peut être déplacée
                if not self.checkVirtuel(piece):
                    l = piece.posFuturesPossibles(self.board,False)
                    if l != []:
                        self.aJouer[piece] = l

    
    def play(self,piece,nouvPos):
        '''
        Pour jouer une partie depuis un fichier ou depuis une partie initiale classique
        '''
        # Memorisation de l'ancienne position
        oldPos = piece.pos
        
        # On regarde si on va manger une pièce si oui, on la mémorise dans "eaten"
        oldPiece = self.board.getPiece(nouvPos[0],nouvPos[1])
        if oldPiece != None and not isinstance(oldPiece,Pion):
            self.eaten[oldPiece.color] += [oldPiece]
            self.pat = 0
        else:
            self.pat += 1
            
        # Règle des 50 coups
        if self.pat == 50:
            raise FinDePartie("La partie est PAT par inaction pendant 50 coups !")
            
        if nouvPos not in self.aJouer[piece]:
            raise ValueError("Ce coup n'est pas permis ce tour-ci.")
        else:
            self.board.deplacer(piece, nouvPos)
        
        # Si ROC: le Roi a fait un déplacement de plus d'une case
        # On récupère la tour correspondante et on la déplace aussi. 
        if(isinstance(piece,Roi) and abs(oldPos[1]-nouvPos[1])>1):
            # Si le roi s'est déplacé à gauche
            if(oldPos[1]>nouvPos[1]): 
                t_roc = self.board.getPiece(oldPos[0],0)
                # On mets la tour à droite du roi
                self.board.deplacer(t_roc, (nouvPos[0],nouvPos[1]+1))
            else: # le roi s'est déplacé a droite
                t_roc = self.board.getPiece(oldPos[0],7)
                # On mets la tour à gauche du roi
                self.board.deplacer(t_roc, (nouvPos[0],nouvPos[1]-1))
        
        # On transforme le pion en plus haute pièce déjà mangée.
        # si celui ci vient d'atteindre la ligne finale.
        if isinstance(piece,Pion) :
            pionBlancAuFond = (self.color == 1) and (piece.pos[0] == 7)
            pionNoirAuFond = (self.color == 0) and (piece.pos[0] == 0)
            if pionBlancAuFond or pionNoirAuFond:
                self.transform(piece)

        # On incrémente le nombre de tours joués.    
        self.time += 1        
        # On alterne les joueurs
        self.color += 1
        self.color %= 2
        # On vide les coups possibles au prochain coup 
        self.aJouer.clear()
        # On vérifie les échecs ou MAT
        self.check,pieceEchec = self.checkCHECK()
        if not self.check: 
            # On calcule tous les coups possibles pour le prochain coup
            self.calculAJouer()
        else: # ON EST EN ECHEC !!!
            # récupération du roi du joueur à jouer
            roiCourant = self.board.getRoi(self.color)
            # Option 1 : Bouger le roi
            lf = roiCourant.posFuturesPossibles(self.board,False)
            if lf != []:
                self.aJouer[roiCourant] = lf
            # Option 2 : mettre un piece sur le chemin qui masquerait le roi aux yeux de la pièce qui fait chier
            lBetween = self.calculChemin(roiCourant, pieceEchec)
            for pos in lBetween:
                for piece in self.board.damier.values():
                    if (piece != roiCourant) and (piece.color == self.color) and pos in piece.posFuturesPossibles(self.board,False):
                        if not self.checkVirtuel(piece,pieceEchec):
                            if piece in self.aJouer:
                                self.aJouer[piece] += [pos]
                            else:
                                self.aJouer[piece] = [pos]
            # Option 3 : manger la pièce qui fait chier
            for piece in self.board.damier.values():
                if(piece.color == self.color) and pieceEchec.pos in piece.posFuturesPossibles(self.board,False):
                    if not self.checkVirtuel(piece,pieceEchec):
                        if piece in self.aJouer:
                            self.aJouer[piece] += [pieceEchec.pos]
                        else:
                            self.aJouer[piece] = [pieceEchec.pos]
            # Si aucune pièce ne peut jouer pour sortir le roi de la merde
            if len(self.aJouer) == 0 :
                if self.color == 0:
                    raise FinDePartie("Le roi Noir est MAT !")
                else:
                    raise FinDePartie("Le roi Blanc est MAT !")
        
        # Cas ou le joueur n'a pas de coup possibe mais n'est pas en échec
        if len(self.aJouer) == 0 and not self.check : # PAT!
            if self.color == 0 : 
                joueur = "noir"
            else:
                joueur = "blanc"
            raise FinDePartie("La partie est PAT car le joueur "+joueur+" ne peut plus jouer !")
        
        return self.aJouer
        
    def checkCHECK(self):
        '''
        Vérifie que la partie n'a pas un roi en échec ou qu'elle n'est pas finie par MAT ou PAT.
        '''    
        check = False
        # La couleur a déjà été alternée ici ... le self.color contient le prochain joueur à jouer.
        adverse = (self.color + 1) %2        
        # récupération du roi du joueur à jouer
        roiCourant = self.board.getRoi(self.color)
        # On doit initialiser pieceEchec au cas ou ...
        pieceEchec = None
            
        #Calcul de tous les futurs coups adverses ... mettent ils le roi courant en danger ?
        for piece in self.board.damier.values():
            if(piece.color == adverse) and roiCourant.pos in piece.posFuturesPossibles(self.board,True):
                check |= True
                pieceEchec = piece
                break # Il est en échec une fois, c'est suffisant.
        
        return check,pieceEchec
    
    def checkVirtuel(self,piece,pieceEchec=None):
        '''
        Vérifie que si on déplace la pièce, on ne mets pas le roi courant en échec.
        '''
        if pieceEchec != None:# On est déjà en échec par ailleurs, on "enleve" la piece 
            self.board.damier[pieceEchec.pos].color = self.color 
            # En fait on la change temporairement de couleur pour la rendre innofensive
            
        # Des coups possibles il faut éliminer les coups dangereux (créant l'échec)
        if not isinstance(piece,Roi):
            # Si la piece étant absente ca crée l'échec, 
            del(self.board.damier[piece.pos])
            checkVirtuel,_ = self.checkCHECK()
            self.board.damier[piece.pos] = piece
            # on ne déplace pas cette piece
            retour = checkVirtuel
        else:
            retour = False
            
        if pieceEchec != None:# On était déjà en échec par ailleurs, on "remets" la piece 
            self.board.damier[pieceEchec.pos].color = (self.color + 1)%2
            # On remet la piece dangereuse de sa couleur initiale
        
        return retour


    
    def transform(self,pion):
        '''
        Transforme un pion automatiquement dans la plus grosse pièce déjà mangée de sa couleur
        '''
        lDame = [piece for piece in self.eaten[pion.color] if isinstance(piece,Dame)]
        lTour = [piece for piece in self.eaten[pion.color] if isinstance(piece,Tour)]
        lCav = [piece for piece in self.eaten[pion.color] if isinstance(piece,Cavalier)]
        lFou = [piece for piece in self.eaten[pion.color] if isinstance(piece,Fou)]
        if len(lDame) > 0 :
            self.board.damier[pion.pos] = Dame(pion.pos, pion.color)
            for piece in self.eaten[pion.color]:
                if isinstance(piece,Dame):
                    self.eaten[pion.color].remove(piece)
                    break
        elif len(lTour) > 0 :
            self.board.damier[pion.pos] = Tour(pion.pos, pion.color)
            for piece in self.eaten[pion.color]:
                if isinstance(piece,Tour):
                    self.eaten[pion.color].remove(piece)
                    break
        elif len(lCav) > 0 :
            self.board.damier[pion.pos] = Cavalier(pion.pos, pion.color)
            for piece in self.eaten[pion.color]:
                if isinstance(piece,Cavalier):
                    self.eaten[pion.color].remove(piece)
                    break
        elif len(lFou) > 0 :
            self.board.damier[pion.pos] = Fou(pion.pos, pion.color)
            for piece in self.eaten[pion.color]:
                if isinstance(piece,Fou):
                    self.eaten[pion.color].remove(piece)
                    break
            
            
    
    def calculChemin(self,roi,chieur):
        '''
        Calcul en fonction du chieur des positions intermédiaires pouvant être occupées pour sauver le roi
        '''
        l = []
        dX = roi.pos[0] - chieur.pos[0]
        if dX != 0 : dX = dX // abs(dX)
        dY = roi.pos[1] - chieur.pos[1]
        if dY != 0 : dY = dY // abs(dY)
        
        if isinstance(chieur,Cavalier) or isinstance(chieur,Pion) :
            return []
        elif isinstance(chieur,Fou) or isinstance(chieur,Tour) or isinstance(chieur,Dame):
            k = 1
            while roi.pos[0] != chieur.pos[0]+dX*k or roi.pos[1] != chieur.pos[1]+dY*k :
                l += [(chieur.pos[0]+dX*k,chieur.pos[1]+dY*k)]
                k += 1                
                            
        return l            
    
    def lireFichier(self,f_path):
        '''
        Pour lire une partie depuis un fichier
        '''
        file = open(f_path,'r')
        l = file.readlines()
        file.close()
        info = l[0].split()
        self.time = int(info[0])
        # A qui de jouer ? selon le time stamp:
        if self.time%2 == 0:
            self.color = 1
        else:
            self.color = 0
        # On lit le fichier pour remplir le plateau
        self.board.luDepuisFichier(l[1:])
        
        # Mise à jour de l'état des Rois/Tours selon la première ligne
        for couleur in [0,1]:
            line = 7 - couleur*7 # B:0 N:7
            roi = self.board.getRoi(couleur)
            petit = 3 - couleur # B:1 N:3
            grand = 4 - couleur # B:2 N:4
            if int(info[petit]) == 0 : # Petit ROC impossible
                if int(info[grand]) == 0 :  # Grand ROC impossible
                    roi.firstMove = False
                else:  # Grand ROC possible mais pas le petit
                    for piece in self.board.damier.values():
                        if isinstance(piece,Tour) and piece.color == couleur and piece.pos != (line,7):
                            piece.firstMove = False
            else:
                if int(info[grand]) == 0 : # Petit ROC possible mais pas le grand
                    for piece in self.board.damier.values():
                        if isinstance(piece,Tour) and piece.color == couleur and piece.pos != (line,0):
                            piece.firstMove = False
                        
        # Vérification à faire ou pas:
        # ----------------------------------------------------------------------------------------FINALEMENT NON mais si vous voulez ...
#        if int(info[1]) == 1 : # petit roc blanc possible supposément
#            roi = self.board.getPiece(0, 3)
#            tour = self.board.getPiece(0, 3)
#            if not (roi != None and tour != None and isinstance(roi,Roi) and isinstance(tour,Tour)):
#                raise Exception("Les valeurs lues dans le fichier ne correspondent pas avec l'état du plateau sur le petit ROC blanc.")

        # Mise à jour de l'état des Pions selon leur position
        for piece in self.board.damier.values():
            if isinstance(piece,Pion) and piece.pos[0] != 6 - piece.color*5: # B:1 N:6
                piece.firstMove = False

    
    def EcrireFichier(self,f_path):
        '''
        Pour lire une partie depuis un fichier
        '''
        file = open(f_path,'w')
        rn = self.board.getRoi(0)
        rb = self.board.getRoi(1)
        sROC = " "
        # ETAT DES ROCS BLANCS
        if rb.firstMove:
            lTours = [self.board.getPiece(0, 0)] # tour petit roc blanc
            lTours += [self.board.getPiece(0, 7)] # tour grand roc blanc
            for i in range(2):
                if lTours[i] != None :
                    if isinstance(lTours[i],Tour) and lTours[i].firstMove:
                        sROC += "1 "
                    else:
                        sROC += "0 "
                else:
                    sROC += "0 "                       
        else:
            sROC += "0 0 "                       
            
        # ETAT DES ROCS NOIRS
        if rn.firstMove:
            lTours += [self.board.getPiece(7, 0)] # tour petit roc noir
            lTours += [self.board.getPiece(7, 7)] # tour grand roc noir
            for i in range(2):
                if lTours[i] != None :
                    if isinstance(lTours[i],Tour) and lTours[i].firstMove:
                        sROC += "1 "
                    else:
                        sROC += "0 "
                else:
                    sROC += "0 "                       
        else:
            sROC += "0 0 "                                   
        file.writelines(str(self.time)+sROC+"\n")
        file.writelines(self.board.pourEcrireFichier())
        file.close()
        
    def __repr__(self):
        s = "Pièces mangées : \n N: "+str(self.eaten[0])+"\n B: "+str(self.eaten[1])+"\nTour #"+str(self.time)
        if self.check:
            s += " Roi "+str([self.board.getRoi(self.color)])+" en ECHEC !"
        s += "\n"+str(self.board)
        return s
