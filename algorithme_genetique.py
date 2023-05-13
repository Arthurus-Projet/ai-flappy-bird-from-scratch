from reseau_neuronal import ReseauNeuronal
from random import choice, randint
import numpy as np
import copy


class AlgorithmeGenetique:
    """
    Classe AlgorithmeGenetique

    Attributes:
        individus: Liste d'instance de la classe ReseauNeuronal
        nombre_individus: Nombre d'individus
    """

    def __init__(self, nombre_individus, nombre_neurone_entre, nombre_neurone_cache, nombre_neurone_sortie):
        self.individus = [ReseauNeuronal(nombre_neurone_entre, nombre_neurone_cache, nombre_neurone_sortie) for _ in range(nombre_individus)]
        self.nombre_individus = nombre_individus

    def action_individus(self, distance_horizontal, distance_vertical):
        '''
        Liste des actions des individus (saut ou non)

        Args:
            distance_horizontal (list): Distance_horizontal des oiseaux à leur tuyaux le plus proche
            distance_vertical (list): Distance_vertical des oiseaux à leur tuyaux le plus proche

        Returns:
            actions (list): Actions des individus (1=Saut, 0=Pas de saut)
        '''
        actions = []
        i = 0
        for individu in self.individus:
            action = individu.propagation([distance_horizontal[i], distance_vertical[i]])
            actions.append(action)
            i += 1
        return actions

    def element_plus_frequent(self, liste):
        '''
        Renvoi l'élément le plus fréquent d'une liste

        Args:
            liste (list): Liste

        Returns:
            element (list): L'élément le plus fréquent
        '''
        element = None
        nb_occurrences = 0
        for x in liste:
            nb = liste.count(x)
            if nb > nb_occurrences:
                element = x
                nb_occurrences = nb
        return element

    def plot_meilleur_individu(self, fitness):
        '''
        On affiche la fonction du réseau de neurone du meilleur individu

        Args:
            fitness (list): Liste du score de fitness de chaque oiseau
        '''
        liste_individus = []
        for i in range(len(self.individus)):
            for _ in range(fitness[i]):
                liste_individus.append(copy.deepcopy(self.individus[i]))

        meilleur_individu = self.element_plus_frequent(liste_individus)
        meilleur_individu.plot_fonction_reseau_de_neurone()

    def selection_meilleur_individus(self, fitness):
        '''
        Chaque oiseau a une probabilité d'être pris pour la prochaine génération de :
        Son score / Le score total des oiseaux

        Args:
            fitness (list): Liste du score de fitness de chaque oiseau
        '''
        liste_individus = []
        for i in range(len(self.individus)):
            for _ in range(fitness[i]):
                liste_individus.append(copy.deepcopy(self.individus[i]))

        for i in range(self.nombre_individus):
            self.individus[i] = copy.deepcopy(choice(liste_individus))



    def reproduction_moyenne(self):
        '''
        Les meilleurs individus qui ont été choisi grâce à la fonction selection_meilleur_individus se reproduisent en prennant la moyenne de leur poids
        Exemple : 2 individus (I1 et I2) formeront 2 nouveaux individus identique en prennant pour chaque poids : (poidsI1 + poidsI2) / 2
        '''
        for i in range(2, self.nombre_individus, 2):
            for y in range(len(self.individus[i].poids_premiere_couche)):
                for y2 in range(len(self.individus[i].poids_premiere_couche[y])):
                    self.individus[i].poids_premiere_couche[y][y2] = (self.individus[i].poids_premiere_couche[y][y2] + self.individus[i + 1].poids_premiere_couche[y][y2]) / 2
                    self.individus[i + 1].poids_premiere_couche[y][y2] = (self.individus[i].poids_premiere_couche[y][y2] + self.individus[i + 1].poids_premiere_couche[y][y2]) / 2

            for y in range(len(self.individus[i].poids_seconde_couche)):
                for y2 in range(len(self.individus[i].poids_seconde_couche[y])):
                    self.individus[i].poids_seconde_couche[y][y2] = (self.individus[i].poids_seconde_couche[y][y2] + self.individus[i + 1].poids_seconde_couche[y][y2]) / 2
                    self.individus[i + 1].poids_seconde_couche[y][y2] = (self.individus[i].poids_seconde_couche[y][y2] + self.individus[i + 1].poids_seconde_couche[y][y2]) / 2

    def mutation_bruit(self, proba, valeur_bruit):
        """
        Chaque poids a une probabilité de muté en lui rajoutant une valeur comprise entre : intervalle_bas et intervalle_haut

        Args:
            proba (int): Probabilité qu'un poids mute
            valeur_bruit (float): Valeur qui définit l'intervalle du bruit rajouté sur un poids
        """
        intervalle_bas, intervalle_haut = -valeur_bruit, valeur_bruit

        for i in range(2, self.nombre_individus, 2):

            for y in range(len(self.individus[i].poids_premiere_couche)):
                for y2 in range(len(self.individus[i].poids_premiere_couche[y])):
                    if randint(1, proba) == 1:
                        self.individus[i].poids_premiere_couche[y][y2] += np.random.uniform(intervalle_bas, intervalle_haut)
                    if randint(1, proba) == 1:
                        self.individus[i + 1].poids_premiere_couche[y][y2] = np.random.uniform(intervalle_bas, intervalle_haut)

            for y in range(len(self.individus[i].poids_seconde_couche)):
                for y2 in range(len(self.individus[i].poids_seconde_couche[y])):
                    if randint(1, proba) == 1:
                        self.individus[i].poids_seconde_couche[y][y2] += np.random.uniform(intervalle_bas, intervalle_haut)
                    if randint(1, proba) == 1:
                        self.individus[i + 1].poids_seconde_couche[y][y2] = np.random.uniform(intervalle_bas, intervalle_haut)
