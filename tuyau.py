from random import randint, random


class Tuyau:
    """
    Classe Tuyau

    Attributes:
        position_x_tuyau: Liste des positions horizontales des tuyaux
        position_y_tuyau: Position verticale commune à tous les tuyaux
        hauteur_tuyau: Liste de la hauteur des tuyaux
        largeur_tuyau: Largeur de chaque tuyau
        distance_entre_tuyau: Distance horizontale entre chaque tuyau
        tuyau_monte: Liste de variables booléennes indiquant si chaque tuyau monte ou non
        vitesse: Liste des vitesses de montée ou de descente de chaque tuyau
        longueur_deplacement: Longueur de déplacement vertical des tuyaux lorsqu'ils atteignent leur limite
        longueur_deplacement_tuyau: Nombre de pixel vertical qu'il reste au tuyau pour monter ou baisser
    """

    def __init__(self):
        #Initialise une instance de la classe Tuyau.
        self.position_x_tuyau = [400, 700, 1000]
        self.position_y_tuyau = 0
        self.hauteur_tuyau = [200, 350, 300]
        self.largeur_tuyau = 100
        self.distance_entre_tuyau = 250
        self.tuyau_monte = [randint(0, 1), randint(0, 1), randint(0, 1)] # 1 Le tuyau monte, 0 il ne monte pas
        self.vitesse = [0.5 + random() , random() + 0.5, random() + 0.5]
        self.longueur_deplacement = 50
        self.longueur_deplacement_tuyau = [self.longueur_deplacement, self.longueur_deplacement, self.longueur_deplacement]

    def indice_tuyau_que_le_joueur_peut_toucher(self, x_oiseau):
        '''
        Indice du tuyau le plus proche du joueur

        Args:
            x_oiseau (int): Distance horizontal de l'oiseau

        Returns:
            indice_min_tuyau (int): Indice du tuyau le plus proche du joueur
        '''
        indice_tuyau, valeur_tuyau = 0, self.position_x_tuyau[0]

        for  i in range(1, len(self.position_x_tuyau)):
            if self.position_x_tuyau[i] < valeur_tuyau:
                indice_tuyau, valeur_tuyau = i, self.position_x_tuyau[i]

        if valeur_tuyau + self.largeur_tuyau < x_oiseau:
            return indice_tuyau - 2
        return indice_tuyau

    def nouveau_tuyau(self, i):
        '''
        Création d'un nouveau tuyau

        Args:
            i (int): Indice où l'on veut créer ce nouveau tuyau
        '''
        self.position_x_tuyau[i] = 250 + self.position_x_tuyau[i - 1]
        self.hauteur_tuyau[i] = randint(110, 290)
        self.tuyau_monte[i] = randint(0, 1)
        self.vitesse[i] = random() + 0.5
        self.longueur_deplacement_tuyau[i] = randint(30, 60)

    def tuyau_bouge(self):
        # Déplace les tuyaux
        for i in range(len(self.hauteur_tuyau)):
            if self.tuyau_monte[i]:
                self.hauteur_tuyau[i] -= self.vitesse[i]
            else:
                self.hauteur_tuyau[i] += self.vitesse[i]

            self.longueur_deplacement_tuyau[i] -= self.vitesse[i]

            if self.longueur_deplacement_tuyau[i] <= 0:
                self.longueur_deplacement_tuyau[i] = self.longueur_deplacement
                self.tuyau_monte[i] = not self.tuyau_monte[i]
