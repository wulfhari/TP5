#

#jouer
#Il faut ajouter le bouton "Jouer" pour pouvoir lancer le code a partir des donnees des deux "entry"

def playinter(self):
    pos=self.sb.get
    piece=g.plateau.getPiece(pos)
    destination=self.sn.get
    g.play(piece,destination)
    
command=playinter
    
#Nouvelle partie
command=addNouveauJeu
 
#Charger une partie
def loadGame(self):
    path=self.file.get
    g.lireFicher(path)
     
command=loadGame
     
#Enregistrer une partie
def saveGame(self):
    path=self.file.get
    g.EcrirreFichier(path)
    
command=saveGame

#Quitter
def quitter(self):
    root.destroy()
    
command=quitter

#ajouter les command=... dans les caracteristiques des boutons
#il faut un autre interface pour le bouton "personnaliser", je suggere un "Entry" pour la position de la piece, combo box pour choisir la sorte de piece, bouton ajouter, bouton effacer, bouton enregistrer, bouton retour, et bien sur, le damier

