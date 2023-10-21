import pygame
import sys
import time
import random

# Initialisation de Pygame
pygame.init()
pygame.mixer.init()  # Initialisation du module de musique

def jouer_son_debut():
    pygame.mixer.init()  # Initialisation du module de musique
    son_debut = pygame.mixer.Sound("son/fin.mp3")  # Remplacez le nom du fichier son par le vôtre
    son_debut.play()


def finjeu():
    # Dimensions de la fenêtre
    largeur, hauteur = 800, 600
    fenetre = pygame.display.set_mode((largeur, hauteur))
    pygame.display.set_caption("Fin")

    # Charger l'image et le son à la fin
    image_fin = pygame.image.load("image/fin.jpg")
    image_fin = pygame.transform.scale(image_fin, (largeur, hauteur))  # Redimensionne l'image

    # Charger le son
    son_fin = pygame.mixer.Sound("son/fin.mp3")

    # Couleurs
    blanc = (0, 0, 0)

    # Fonction pour afficher le texte des points de vie
    def compteur(points):
        font = pygame.font.Font(None, 36)
        texte = font.render(f" {points}", True, blanc)
        fenetre.blit(texte, (10, 10))

    # Fonction principale du jeu
    Compteur = random.randint(5, 20)
    temps_debut = time.time()
    while Compteur > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        fenetre.fill((0, 0, 0))

        temps_actuel = time.time()
        temps_ecoule = temps_actuel - temps_debut

        if temps_ecoule >= 1:
            Compteur -= 1
            temps_debut = time.time()

        compteur(Compteur)

        pygame.display.flip()

    son_fin.play()  # Joue le son
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        fenetre.blit(image_fin, (0, 0))
        pygame.display.flip()

if __name__ == "__main__":
    jouer_son_debut()
    finjeu()
