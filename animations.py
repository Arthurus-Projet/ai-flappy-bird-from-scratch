import pygame

class animation:
    """
    Classe animation

    Attributes:
        time_next_frame (float): Temps (en secondes) avant le prochain changement de frame de l'animation
        x (float): Position horizontale de l'animation
        y (float): Position verticale de l'animation
        number_image (int): Nombre total d'images dans l'animation
        time (float): Temps écoulé depuis le dernier changement de frame de l'animation
        frame (int): Numéro de la frame actuelle de l'animation
    """

    def __init__(self, time_next_frame, x, y, number_image):
        """
        Initialise une instance de la classe Animation.

        Args:
            time_next_frame (float): Temps (en secondes) avant le prochain changement de frame de l'animation
            x (float): Position horizontale de l'animation
            y (float): Position verticale de l'animation
            number_image (int): Nombre total d'images dans l'animation
        """
        self.time_next_frame = time_next_frame
        self.time = time_next_frame
        self.number_image = number_image
        self.x = x
        self.y = y
        self.frame = 0


    def get_frame(self, clock):
        """
        Obtient la valeur de la frame actuelle de l'animation.

        Args:
            clock (float): Temps écoulé depuis la dernière mise à jour de l'animation.

        Returns:
            int: Numéro de la frame actuelle.
        """
        self.time -= clock
        if self.time < 0:
            self.time += self.time_next_frame
            self.frame = (self.frame + 1) % self.number_image

        return self.frame

    def set_time(self, clock):
        """
        Met à jour le temps écoulé de l'animation.

        Args:
            clock (float): Temps écoulé depuis la dernière mise à jour de l'animation.
        """
        self.time -= clock
