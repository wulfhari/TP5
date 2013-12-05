'''
Created on Dec 4, 2013

@author: Simon
'''

if __name__ == '__main__':
    
    from src.ui.board import *

    root = tk.Tk()
    board = Damier(root,64)
    addNouveauJeu(board)
    root.mainloop()