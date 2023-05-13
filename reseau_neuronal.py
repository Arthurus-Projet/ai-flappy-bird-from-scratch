import numpy as np
import matplotlib.pyplot as plt
import pygame


class ReseauNeuronal:
    """
    Classe ReseauNeuronal

    Attributes:
        poids_premiere_couche: Poids de la première couche du réseau de neurone
        poids_seconde_couche: Poids de la seconde couche du réseau de neurone
        nombre_neurone_sortie: Nombre de neurone caché
        valeur_premiere_couche: Valeur de la première couche du réseau de neurone
        valeur_seconde_couche: Valeur de la seconde couche du réseau de neurone
    """

    def __init__(self, nombre_neurone_entre, nombre_neurone_cache, nombre_neurone_sortie):
        self.poids_premiere_couche = np.array([[np.random.uniform(-0.1, 0.1) for _ in range(nombre_neurone_cache)] for _ in range(nombre_neurone_entre + 1)])
        self.poids_seconde_couche = np.array([[np.random.uniform(-0.1, 0.1)  for _ in range(nombre_neurone_sortie )] for _ in range(nombre_neurone_cache +1)])
        self.nombre_neurone_cache = nombre_neurone_cache
        self.valeur_premiere_couche = None
        self.valeur_seconde_couche = None

    def print_weight(self):
        # Permet d'afficher les poids de la première couche
        print("Poids première couche :")
        print(self.poids_premiere_couche)

    def print_weight_second(self):
        # Permet d'afficher les seconds poids
        print("Poids seconde couche :")
        print(self.poids_seconde_couche)

    def print_first_layer(self):
        # Permet d'afficher les valeurs de sortie de la première couche
        print(self.valeur_premiere_couche)

    def print_second_layer(self):
        # Permet d'afficher les valeurs de sortie de la seconde couche
        print(self.valeur_seconde_couche)

    def relu(self, x):
        # Fonction d'activation relu
        return max(0, x)

    def sigmoid(self, x):
        # Fonction d'activation sigmoid
        return 1 / (1 + np.exp(-x))

    def seuil(self, x):
        # Fonction d'activation seuil
        if x > 0:
            return 1
        return 0

    def value_first_layer(self, input_value):
        '''
        Produit matricielle des valeurs d'entrés multiplié par les poids de la première couche

        Args:
            input_value (liste): Liste des valeurs d'entrés
        '''
        input_value.append(1) # On rajoute 1 pour le biais
        self.valeur_premiere_couche = [self.sigmoid(elem) for elem in input_value@self.poids_premiere_couche]
        self.valeur_premiere_couche.append(1) # biais pour les résultats de sortie de la couche de sortie
        return self.valeur_premiere_couche

    def value_second_layer(self):
        # Produit matricielle des valeurs de la couche caché par les poids de la seconde couche
        self.valeur_seconde_couche = [self.seuil(elem) for elem in self.valeur_premiere_couche@self.poids_seconde_couche]
        return self.valeur_seconde_couche

    def propagation(self, input_value):
        '''
        On prend les valeurs d'entrés et on renvoie une sortie binaire, 1 pour un saut ou 0 pour l'absence de saut

        Args:
            input_value (liste): Liste des valeurs d'entrés
        '''
        self.value_first_layer(input_value)
        return self.value_second_layer()

    def plot_fonction_reseau_de_neurone(self):
        # Affichage de la fonction du réseaud de neurone
        n = 500
        n2 = 200
        distance_horizontal = np.linspace(0, n, n + 1)
        distance_vertical = np.linspace(-n2, n2 * 4, (n2*5) + 1)

        # Liste de liste de tous les cas possible (saut ou non) pour x et y
        Y = []
        print("< Graphique en cours de traitement ... >")
        for x in range(len(distance_horizontal)):
            l = []
            for y in range(len(distance_vertical)):
                l.append(self.propagation([distance_horizontal[x], distance_vertical[y]]))
            Y.append(l)

        x_red, y_red, x_blue, y_blue = [], [], [], []

        for i in range(len(distance_horizontal)):
            for i2 in range(len(distance_vertical)):
                if Y[i][i2] == [1]:
                    x_red.append(-distance_horizontal[i])
                    y_red.append(-distance_vertical[i2])
                else:
                    x_blue.append(-distance_horizontal[i])
                    y_blue.append(-distance_vertical[i2])

        plt.scatter(x_red, y_red, marker="s", color='red')
        plt.scatter(x_blue, y_blue, color='blue')
        plt.show()


    def plot_graphique_reseau_de_neurone(self, ecran, input_value):
        '''
        Visualisation du réseau de neurone

        Args:
            ecran (pygame.display.set_mode): Fenêtre graphique pour l'affichage du jeu
            input_value (liste): Liste des valeurs d'entrés
        '''
        rayon = 10
        largeur = 3
        position = (400, 400)
        valeur_premiere_couche = self.value_first_layer(input_value)[0:self.nombre_neurone_cache] # on supprime le biais qui vaut 1
        valeur_seconde_couche = self.value_second_layer()
        couleur_valeur_premiere_couche = []

        for i in range(len(valeur_premiere_couche)):
            if valeur_premiere_couche[i] > 1:
                couleur_valeur_premiere_couche.append((255, 255, 0)) # couleur jaune
            else:
                couleur_valeur_premiere_couche.append((255, 255, 255 - (valeur_premiere_couche[i]*255)))

        couleur_valeur_seconde_couche = (255, 255, 255 - (valeur_seconde_couche[0]*255)) # jaune si l'oiseau saut (255, 255, 0), blanc si il ne saute pas (255, 255, 255)
        if valeur_seconde_couche[0] == 1:
            couleur_valeur_seconde_couche = (0, 0, 0)
        else:
            couleur_valeur_seconde_couche = (255, 255, 255)

        # connexion premier input
        pos = [-35, 0, 35, 70]
        for p in pos:
            pygame.draw.line(ecran, (255, 255, 255), (position[0], position[1]), (position[0] + 50, position[1] + p), largeur)

        # connexion deuxième input
        for p in pos:
            pygame.draw.line(ecran, (255, 255, 255), (position[0], position[1] + 35), (position[0] + 50, position[1] + p), largeur)

        # connexion au neurone de sortie
        for p in pos:
            pygame.draw.line(ecran, (255, 255, 255), (position[0] + 50, position[1] + p), (position[0] + 100, position[1] + 17.5), largeur)

        # les 2 neurones d'entrés
        pygame.draw.circle(ecran, (255, 255, 255), (position[0], position[1]), rayon)
        pygame.draw.circle(ecran, (255, 255, 255), (position[0], position[1] + 35), rayon)

        # les 4 neurones cachés
        for i in range(len(pos)):
            pygame.draw.circle(ecran, couleur_valeur_premiere_couche[i], (position[0] + 50, position[1] + pos[i]), rayon)

        # le neurone de sortie
        pygame.draw.circle(ecran, couleur_valeur_seconde_couche, (position[0] + 100, position[1] + 17.5), rayon)
