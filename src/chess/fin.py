#! /usr/bin/env python
# -*- coding:Utf-8 -*-
'''
Created on 2013-11-17

@author: C. Besse
'''

class FinDePartie(Exception):
    '''
    Exception permettant de déterminer la fin d'une partie
    '''
    
    def __init__(self, message):
        '''
        Constructor
        '''
        super().__init__()
        self.msg = message
        
    def __repr__(self):
        return "Fin de partie : " + self.msg