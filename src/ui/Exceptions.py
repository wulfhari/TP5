Fichier sur les Exceptions


    Class Exc_depl_pions(Exceptions):

        '''Exceptions qui va gerer les contraintes concernant les deplacememnts
            possibles des pions.'''

        def__init__(self, message):

             '''Constructor'''

             super().__init__()
             self.message = message


        def__repr__(self):

            return "Erreur de deplacement du pions: " + self.msg
        


        Class Exc_depl_roi(Exceptions):

            '''
         Exception qui va gerer les contraintes concernant les deplacements
         possibles du roi.'''


        def__init__(self, message):

             '''Constructor'''

             super().__init__()
             self.message = message


        def__repr__(self):

            return "Erreur de deplacement du roi: " + self.msg


          Class Exc_depl_dame(Exception)

          ''' Exceptions qui va etre gerer les contraintes concernant
               les deplacements possibles de la dame.'''

           def__init__(self, message):

             '''Constructor'''

             super().__init__()
             self.message = message


        def__repr__(self):

            return "Erreur de deplacement de la dame: " + self.msg


        Class Exc_depl_tour(Exception):

            '''Excpeption qui va gerer les contraintes concernant
            les deplacements possibles de la tour.'''

            
        def__init__(self, message):

             '''Constructor'''

             super().__init__()
             self.message = message


        def__repr__(self):

            return "Erreur de deplacement de la tour: " + self.msg


    Class Exc_depl_cavalier(Exception):

            '''Exception qui va gerer les contraintes concernant les
              deplacements possibles du cavalier'''

        def__init__(self, message)

           '''Constructor'''

           super().__init__()
           self.msg = message

        delf__repr__(self):
            return "Erreur de deplacement du cavalier: " + self

    Class_Exc_depl_fou(Exception):

            '''Exception qui va gerer les contraintes concernant les deplacemnts
               possibles du fou. '''

        def__init__(self, message):

            '''constructor
            '''
            super().__init__()
            self.message = message

       def__repr__(self):
           return "Erreur de deplacemnt du fou: " + self.msg


        Class Exc_couleur_pieces(Exceptions):

            '''Exception qui va gerer si le joueur joue les pieces adverses.'''

            def__init__(self, message):

                ''' Constructor
                '''
                super().__init__()
                self.msg = message

            def__repr__(self):
                return " Action interdite: " + self.msg
