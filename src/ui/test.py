#! c:/Python33 python
# -*- coding:Utf-8 -*-

'''
Created on Dec 9, 2013

@author: Simon
'''

###  Pour afficher un damier de boutton
#########################################################
# from tkinter import *
# 
# root = Tk()
# coup = 0
# joueurCouleur = ["white", "grey"]
# for x in range(7):
#     Grid.columnconfigure(root,x,weight=1)
# for y in range(7):
#     Grid.rowconfigure(root,y,weight=1)
# for i in range(7):
#     for j in range(7):
#         b = Button(root,bg=joueurCouleur[coup % 2])
# #dict[(i,j)] = b
#         b.grid(row=i, column=j, sticky=N+S+E+W)
# coup += 1
# root.mainloop()

#############################################################
from src.chess.game import GameManagement

g = GameManagement("../jeu1.txt")


for i in g.board.pourEcrireFichier():
    print(i[1])





