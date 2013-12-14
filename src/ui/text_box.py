#! c:/Python33 python
# -*- coding:Utf-8 -*-

'''
Created on Dec 11, 2013

@author: Simon
'''
import tkinter as tk
from tkinter import *

class Text_Box(tk.Frame,):
    '''
    classdocs
    '''


    def __init__(self,parent, sizeX, sizeY):
        '''
        Constructor
        '''
    # Cr�ation de l'affichage
        
        tk.Frame.__init__(self, parent)
        self.text = Text(parent, height=sizeX, width=sizeY, wrap=WORD)
        self.text.grid(row=2,column=1,columnspan=2, rowspan=25,sticky=NSEW)
        # Creation de la scrollbar
        sc = Scrollbar(parent,orient=VERTICAL) 
        ## association du deplacement de la glissiere des scrollbar avec la position visible dans 
        ## le widget Text et inversement.              
        sc.config(command = self.text.yview)
        self.text.config(yscrollcommand = sc.set)
        sc.grid(row=5,column=2,sticky=NSEW)
        
    def clear(self):
        # On efface le text widget
        self.text.delete(1.0, END)
        
    def text_insert(self, x,y):
        self.text.insert(END,"{0:8}{1:>20}\n".format(x,y))