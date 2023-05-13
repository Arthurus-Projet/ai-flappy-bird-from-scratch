from random import randint
import pygame
from  algorithme_genetique import AlgorithmeGenetique
from animations import *
from tuyau import Tuyau

# Initialisation de Pygame
pygame.init()

# Couleur jaune en rgb
JAUNE = (255, 255, 0)

LONGUEUR_FENETRE = 800
LARGEUR_FENETRE = 600

# Définition de la taille de la fenêtre
TAILLE_FENETRE = (LARGEUR_FENETRE, LONGUEUR_FENETRE)
ecran = pygame.display.set_mode(TAILLE_FENETRE)

# Nom de la fenêtre
pygame.display.set_caption("Flappy bird")

tuyau = Tuyau()

MULTIPLICATEUR = 1
TAILLE_FLAPPY_BIRD = 50 * MULTIPLICATEUR

image_bird_1 = pygame.image.load("illustrations/1.png").convert_alpha()
image_bird_1 = pygame.transform.scale(image_bird_1, (51*MULTIPLICATEUR, 50*MULTIPLICATEUR))

image_bird_2 = pygame.image.load("illustrations/2.png").convert_alpha()
image_bird_2 = pygame.transform.scale(image_bird_2, (51*MULTIPLICATEUR, 50*MULTIPLICATEUR))

image_bird_3 = pygame.image.load("illustrations/3.png").convert_alpha()
image_bird_3 = pygame.transform.scale(image_bird_3, (51*MULTIPLICATEUR, 50*MULTIPLICATEUR))

image_tuyau = pygame.image.load("illustrations/tuyau.png").convert_alpha()
image_tuyau_bas = pygame.image.load("illustrations/tuyau_haut.png").convert_alpha()

fond = pygame.image.load("illustrations/fond.jpg").convert_alpha()
fond_bas = pygame.image.load("illustrations/fond_bas.jpg").convert_alpha()

images_bird = [image_bird_1, image_bird_2, image_bird_3]
bird_animation = animation(100, 51, 50, 3)

# Horloge pour la gestion du temps
horloge = pygame.time.Clock()

# Algo génétique
NOMBRE_INDIVIDUS = 100
nombre_generation = 1 # variable qui indique à quel génération on est
x_oiseau = [randint(10, 400) for i in range(NOMBRE_INDIVIDUS)]
individus = AlgorithmeGenetique(NOMBRE_INDIVIDUS, 2, 4, 1)

angle_rotation = [0 for i in range(NOMBRE_INDIVIDUS)]
nombre_restant_saut = [0 for i in range(NOMBRE_INDIVIDUS)]

for _ in range(200): # Nombre de génération qu'on crée
    compteur_individu_morts = 0
    score = 0
    tuyau.position_x_tuyau = [400, 700, 1000]
    fitness = [-1 for i in range(NOMBRE_INDIVIDUS)]
    y_individus = [500 for i in range(NOMBRE_INDIVIDUS)]

    # Boucle de jeu
    en_cours_de_jeu = True
    while en_cours_de_jeu:

        # Limitation du taux de rafraîchissement de la boucle de jeu à 60 fps
        temps = horloge.tick(60)

        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                en_cours_de_jeu = False
            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_c:
                    # Lorsque l'on appuie sur c, on plot la fonction d'activation du meilleur individu
                    for i in range(len(fitness)):
                        if fitness[i] == -1:
                            fitness[i] = score
                    individus.plot_meilleur_individu(fitness)
                    en_cours_de_jeu = False
                if evenement.key == pygame.K_m:
                    for i in range(len(fitness)):
                        if fitness[i] == -1:
                            fitness[i] = score
                    en_cours_de_jeu = False

        ecran.blit(fond, (0, 0))

        tuyau.tuyau_bouge()
        indices_tuyaux = [tuyau.indice_tuyau_que_le_joueur_peut_toucher(x) for x in x_oiseau]

        for i in range(NOMBRE_INDIVIDUS):
            if fitness[i] == -1: # on test seulement les individus en vie (si un oiseau a comme fitness -1, cela veut dire qu'il est encore en vie)
                # Test collision en haut à gauche du joueur :
                if tuyau.position_x_tuyau[indices_tuyaux[i]] < x_oiseau[i] < tuyau.position_x_tuyau[indices_tuyaux[i]] + tuyau.largeur_tuyau and tuyau.position_y_tuyau < y_individus[i] < tuyau.position_y_tuyau + tuyau.hauteur_tuyau[indices_tuyaux[i]]:
                    fitness[i] = score
                    compteur_individu_morts += 1
                # Test collision en haut à droite
                elif tuyau.position_x_tuyau[indices_tuyaux[i]] < x_oiseau[i] + TAILLE_FLAPPY_BIRD < tuyau.position_x_tuyau[indices_tuyaux[i]] + tuyau.largeur_tuyau and tuyau.position_y_tuyau < y_individus[i] < tuyau.position_y_tuyau + tuyau.hauteur_tuyau[indices_tuyaux[i]]:
                    fitness[i] = score
                    compteur_individu_morts += 1
                # Test collision en bas à gauche
                elif tuyau.position_x_tuyau[indices_tuyaux[i]] < x_oiseau[i] < tuyau.position_x_tuyau[indices_tuyaux[i]] + tuyau.largeur_tuyau and tuyau.position_y_tuyau + tuyau.hauteur_tuyau[indices_tuyaux[i]] + tuyau.distance_entre_tuyau < y_individus[i] + TAILLE_FLAPPY_BIRD < tuyau.position_y_tuyau + tuyau.hauteur_tuyau[indices_tuyaux[i]] + tuyau.distance_entre_tuyau + LONGUEUR_FENETRE:
                    fitness[i] = score
                    compteur_individu_morts += 1
                # Test collision en bas à droite
                elif tuyau.position_x_tuyau[indices_tuyaux[i]] < x_oiseau[i] + TAILLE_FLAPPY_BIRD < tuyau.position_x_tuyau[indices_tuyaux[i]] + tuyau.largeur_tuyau and tuyau.position_y_tuyau + tuyau.hauteur_tuyau[indices_tuyaux[i]] + tuyau.distance_entre_tuyau < y_individus[i] + TAILLE_FLAPPY_BIRD < tuyau.position_y_tuyau + tuyau.hauteur_tuyau[indices_tuyaux[i]] + tuyau.distance_entre_tuyau + LONGUEUR_FENETRE:
                    fitness[i] = score
                    compteur_individu_morts += 1
                # Test collision mur haut
                elif y_individus[i] < 0:
                    fitness[i] = score - 5
                    compteur_individu_morts += 1
                # Test collision mur bas
                elif y_individus[i] > LONGUEUR_FENETRE - TAILLE_FLAPPY_BIRD:
                    fitness[i] = score - 5
                    compteur_individu_morts += 1


        # Affichage de flappy bird
        for i in range(NOMBRE_INDIVIDUS):
            if fitness[i] == -1: # on affiche seulement les oiseaux vivants
                frame = bird_animation.get_frame(temps)
                image_rotate = pygame.transform.rotate(images_bird[frame], angle_rotation[i])
                ecran.blit(image_rotate, (x_oiseau[i], y_individus[i]))

        score += 1

        # On définit la police d'écriture
        police = pygame.font.Font(None, 36)

        texte_score = police.render(str(score), True, JAUNE)
        texte_generation = police.render("generation : " + str(nombre_generation), True, JAUNE)
        texte_individus = police.render("individus : " + str(NOMBRE_INDIVIDUS - compteur_individu_morts), True, JAUNE)

        # On affiche le score du jeu
        ecran.blit(texte_score, (530, 20))

        # Gravité des oiseaux qui ne sont pas en train de sauter
        for i in range(len(fitness)):
            if nombre_restant_saut[i] == 0:
                y_individus[i] += 3

        # Affichage du réseau de neurone
        for i in range(len(fitness)):
            if fitness[i] == -1: # on affiche le réseau de neurone d'un oiseau en vie
                individus.individus[i].plot_graphique_reseau_de_neurone(ecran, [tuyau.position_x_tuyau[indices_tuyaux[i]] + tuyau.largeur_tuyau - x_oiseau[i], y_individus[i] - tuyau.hauteur_tuyau[indices_tuyaux[i]]])
                break

        # Chaque oiseau va sauter ou non
        actions = individus.action_individus([tuyau.position_x_tuyau[indices_tuyaux[i]] + tuyau.largeur_tuyau - x_oiseau[i] for i in range(len(fitness))], [y_individus[i] - tuyau.hauteur_tuyau[indices_tuyaux[i]] for i in range(len(fitness))])
        for i in range(len(actions)):
            if actions[i][0] == 1:
                nombre_restant_saut[i] = 6

        # Affiche les tuyaux
        for i in range(len(tuyau.position_x_tuyau)):
            ecran.blit(image_tuyau_bas, (tuyau.position_x_tuyau[i], -500 + tuyau.hauteur_tuyau[i]))
            ecran.blit(image_tuyau, (tuyau.position_x_tuyau[i], tuyau.hauteur_tuyau[i] + tuyau.distance_entre_tuyau))
            tuyau.position_x_tuyau[i] -= 3

            if tuyau.position_x_tuyau[i] + tuyau.largeur_tuyau < 0:
                tuyau.nouveau_tuyau(i)

        ecran.blit(texte_generation, (30, 20))
        ecran.blit(texte_individus, (30, 58))

        # Saut des oiseaux
        for i in range(len(nombre_restant_saut)):
            if nombre_restant_saut[i] > 0:

                y_individus[i] -= 14
                if nombre_restant_saut[i] >= 6:
                    angle_rotation[i] = 0
                angle_rotation[i] += 10
                nombre_restant_saut[i] -= 1
            else:
                if angle_rotation[i] > -90:
                    angle_rotation[i] -= 3

        ecran.blit(fond_bas, (0, LONGUEUR_FENETRE - 101))

        # Mise à jour de l'écran
        pygame.display.flip()

        # Si tous les individus sont morts, on passe à la génaration suivante
        if compteur_individu_morts == NOMBRE_INDIVIDUS:
            en_cours_de_jeu = False

    # On crée la prochaine génération:
    individus.selection_meilleur_individus(fitness)
    individus.reproduction_moyenne()
    individus.mutation_bruit(10, 0.01)
    nombre_generation += 1

# Fermeture de Pygame
pygame.quit()
