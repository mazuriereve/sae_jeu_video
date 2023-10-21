import pygame

class Cases:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def action(self):
        # Mettez en œuvre le comportement spécifique ici, par exemple, afficher une fenêtre de fin de jeu
        fenetre_fin = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
        fenetre_fin.fill(noir)
        pygame.display.flip()
        pygame.time.delay(2000)  # Attendre pendant 2 secondes avant de quitter le jeu
        pygame.quit()
        sys.exit()
