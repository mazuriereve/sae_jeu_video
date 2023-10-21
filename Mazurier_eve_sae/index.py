import pygame
import sys
import random
from Ennemis import *
from Personnage1 import *
from finjeu import * 

# Initialisation de Pygame
pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512)


def jeu(): 

    # Dimensions de la fenêtre
    largeur_fenetre = 1000 
    hauteur_fenetre = 800
    
    #espace a droite 
    espace_blanc_droite = 250
    image_deco = pygame.Surface((espace_blanc_droite, hauteur_fenetre))
    image_deco.fill((20,100,45))  

    image_sol = pygame.image.load("image/sol.jpg")
    image_bonne_fin = pygame.image.load('image/finjeu.jpg')


    # Fonte pour le texte
    font = pygame.font.Font("police/police.ttf", 45)
    
    # Taille grille
    taille_case = (largeur_fenetre - espace_blanc_droite) // 10 
    nombre_cases_x = 10
    nombre_cases_y = 10
    
    taille_fleche = 80 
    # Chargement des images des flèches
    image_fleche_haut = pygame.image.load('image/fleche_haut.jpg')
    image_fleche_haut = pygame.transform.scale(image_fleche_haut, (taille_fleche, taille_fleche))
    image_fleche_bas = pygame.image.load('image/fleche_bas.jpg')
    image_fleche_bas = pygame.transform.scale(image_fleche_bas, (taille_fleche, taille_fleche))
    image_fleche_gauche = pygame.image.load('image/fleche_gauche.jpg')
    image_fleche_gauche = pygame.transform.scale(image_fleche_gauche, (taille_fleche, taille_fleche))
    image_fleche_droite = pygame.image.load('image/fleche_droite.jpg')
    image_fleche_droite = pygame.transform.scale(image_fleche_droite, (taille_fleche, taille_fleche))    
    # Position 
    rect_fleche_haut = image_fleche_haut.get_rect(topleft=(largeur_fenetre - espace_blanc_droite + (espace_blanc_droite - taille_fleche) / 2, 0))
    rect_fleche_bas = image_fleche_bas.get_rect(topleft=(largeur_fenetre - espace_blanc_droite + (espace_blanc_droite - taille_fleche) / 2, taille_fleche))
    rect_fleche_gauche = image_fleche_gauche.get_rect(topleft=(largeur_fenetre - espace_blanc_droite + (espace_blanc_droite - 3 * taille_fleche) / 2, taille_fleche))
    rect_fleche_droite = image_fleche_droite.get_rect(topleft=(largeur_fenetre - espace_blanc_droite + (espace_blanc_droite + taille_fleche) / 2, taille_fleche))

    # Couleurs
    blanc = (255, 255, 255)
    noir = (0, 0, 0)
    gris = (127, 127, 127)
    noir = (0,0,0)
    marron = (50,30,25)

    # Création de la fenêtre
    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
    pygame.display.set_caption("Heartsteel")

    #images perso + fond 
    fond_menu = pygame.image.load('image/menu.png')
    image_perso1 = pygame.image.load('image/perso1.png')
    image_perso1 = pygame.transform.scale(image_perso1, (taille_case, taille_case))
    image_perso2 = pygame.image.load('image/perso2.png')
    image_perso2 = pygame.transform.scale(image_perso2, (taille_case, taille_case))
    image_perso3 = pygame.image.load('image/perso3.png')
    image_perso3 = pygame.transform.scale(image_perso3, (taille_case, taille_case))
    image_perso4 = pygame.image.load('image/perso4.png')
    image_perso4 = pygame.transform.scale(image_perso4, (taille_case, taille_case))
    
    #images des boss
    image_loup = pygame.image.load('image/loups.png')
    image_dragon = pygame.image.load('image/dragon.png')
    image_chevalier = pygame.image.load('image/chevalier.png')
    image_archer = pygame.image.load('image/archers.png')

    # Redimensionnez les images au même format que les joueurs
    image_loup = pygame.transform.scale(image_loup, (taille_case, taille_case))
    image_dragon = pygame.transform.scale(image_dragon, (taille_case, taille_case))
    image_chevalier = pygame.transform.scale(image_chevalier, (taille_case, taille_case))
    image_archer = pygame.transform.scale(image_archer, (taille_case, taille_case))
    
    #  inventaire
    image_potion = pygame.image.load('image/potion.png')
    image_inventaire = pygame.image.load('image/inventaire.jpg')
    # Position de l'image d'inventaire
    position_inventaire = image_inventaire.get_rect()
    position_inventaire.topright = (largeur_fenetre , 0 )
    # Position de l'image de la potion
    position_potion = image_potion.get_rect()
    position_potion.topright = (largeur_fenetre - 10, 10)  # Ajustez la position comme vous le souhaitez

    inventaire = []
    potion_disponible = False
    
    syn = False 
    accueil_active = True
    menu_active = True 
    while accueil_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    accueil_active = False
                    syn = True 

        fenetre.blit(fond_menu, (0, 0))

        titre_text = font.render("Bienvenue dans HEARTSTEEL !", True, blanc)
        titre_rect = titre_text.get_rect(center=(largeur_fenetre // 2, hauteur_fenetre // 4))
        jouer_text = font.render("Appuyez sur ESPACE pour jouer ou Q pour quitter", True, blanc)
        jouer_rect = jouer_text.get_rect(center=(largeur_fenetre // 2, hauteur_fenetre // 2))
        fenetre.blit(titre_text, titre_rect)
        fenetre.blit(jouer_text, jouer_rect)
        pygame.display.flip()

    # Maintenant, affichez le synopsis en dehors de la boucle accueil_active
    while syn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    syn = False 
                    menu_active = True 

        fenetre.blit(fond_menu, (0, 0))
        syn_text = font.render("Comment jouer ? " , True, noir)
        syn_rect1 = syn_text.get_rect(center=(largeur_fenetre // 2, hauteur_fenetre // 8))
        syn_text3 = font.render("Selectionnez le nombre de joueur et déplacez vous avec les flèches" , True , noir)
        syn_rect3 = syn_text3.get_rect(center=(largeur_fenetre // 2 , 2* hauteur_fenetre //6 ))
        syn_text2 = font.render("Appuyer sur I pour ouvrir l'inventaire" , True , noir)
        syn_rect2 = syn_text2.get_rect(center=(largeur_fenetre // 2, 2* hauteur_fenetre // 4))
    
        fenetre.blit(syn_text, syn_rect1)
        fenetre.blit(syn_text3, syn_rect3)
        fenetre.blit(syn_text2, syn_rect2)

        pygame.display.flip()
   
    # Menu de sélection du nombre de joueurs
    selection_text = font.render("Combien de joueurs ? 1 à 4", True, noir)
    selection_rect = selection_text.get_rect(center=(largeur_fenetre // 2, hauteur_fenetre // 2))
     
     # Initialisation des positions des joueurs
    joueurs = 1 
    joueur1_x = joueur1_y = joueur2_x = joueur2_y = 0 
    joueur3_x = joueur3_y  = 0 
    joueur4_x = joueur4_y = 1

    # Boucle principale du menu 
    while menu_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    joueurs = 1
                    menu_active = False
                elif event.key == pygame.K_2:
                    joueurs = 2
                    menu_active = False
                elif event.key == pygame.K_3:
                    joueurs = 3
                    menu_active = False
                elif event.key == pygame.K_4:
                    joueurs = 4
                    menu_active = False
     
        fenetre.blit(fond_menu, (0, 0))
        fenetre.blit(selection_text, selection_rect)
        pygame.display.flip()

        zone_grise_x = nombre_cases_x // 2 - 1  
        zone_grise_largeur = 2  # Largeur de la zone grise (2 cases)
        zone_grise_y = nombre_cases_y // 2 - 1  
        zone_grise_hauteur = 2  # Hauteur de la zone grise (2 cases)

        if joueurs == 1:
            joueur1_x = zone_grise_x + 1
            joueur1_y = zone_grise_y + 1
        elif joueurs == 2:
            joueur1_x = zone_grise_x
            joueur1_y = zone_grise_y + 1
            joueur2_x = zone_grise_x + zone_grise_largeur - 1
            joueur2_y = zone_grise_y + 1
        elif joueurs == 3:
            joueur1_x = zone_grise_x
            joueur1_y = zone_grise_y
            joueur2_x = zone_grise_x + zone_grise_largeur - 1
            joueur2_y = zone_grise_y
            joueur3_x = zone_grise_x + 1
            joueur3_y = zone_grise_y + zone_grise_hauteur - 1
        elif joueurs == 4:
            joueur1_x = zone_grise_x + 1
            joueur1_y = zone_grise_y
            joueur2_x = zone_grise_x
            joueur2_y = zone_grise_y
            joueur3_x = zone_grise_x + 1
            joueur3_y = zone_grise_y + zone_grise_hauteur - 1
            joueur4_x = zone_grise_x
            joueur4_y = zone_grise_y + zone_grise_hauteur - 1

    # --------------------------------- SALLES SPECIALES ---------------------------------
    # Liste des positions des salles spéciales
    cases_speciales = []
    # Génération des positions aléatoires pour les salles spéciales
    while len(cases_speciales) < 4:
        x = random.randint(0, nombre_cases_x - 1)
        y = random.randint(0, nombre_cases_y - 1)
        # on vérifie que le prochain emplacement de la prochaine case ne soit pas dejà pris 
        if (x, y) not in cases_speciales and (x != joueur1_x or y != joueur1_y) and (joueurs != 2 or (x != joueur2_x or y != joueur2_y)):
            cases_speciales.append((x, y))

    #--------------------------------- BOSS ---------------------------------
    # ajout des boss dans ma liste boss_positions pour gérer les combats
    boss_positions = []
    chevalier_x = random.randint(0, nombre_cases_x - 1)
    chevalier_y = random.randint(0, nombre_cases_y - 1)
    boss_positions.append((chevalier_x, chevalier_y))
    archer_x = random.randint(0, nombre_cases_x - 1)
    archer_y = random.randint(0, nombre_cases_y - 1)
    boss_positions.append((archer_x, archer_y))
    loup_x = random.randint(0, nombre_cases_x - 1)
    loup_y = random.randint(0, nombre_cases_y - 1)
    boss_positions.append((loup_x, loup_y))
    dragon_x = random.randint(0, nombre_cases_x - 1)
    dragon_y = random.randint(0, nombre_cases_y - 1)
    boss_positions.append((dragon_x, dragon_y))
        
    # ---------------------------- DECLARATION DE MES FONCTIONS ----------------------------   
    # on regarde sur le plateau si il y a un ennemi sur ma case
    def get_enemy_at_position(x, y):
        for i, (enemy_x, enemy_y) in enumerate(boss_positions):
            if x == enemy_x and y == enemy_y:
                return i  # Retourne l'indice de l'ennemi dans la liste boss_positions
        return None
    
    # on fait un combat si un ennemi est detecté
    evenements_cases_speciales = [
        "Vous avez trouvé la sortie",  #fin du jeu 
        "Vous avez trouvé la salle des gardes vous trouvez une nouvelle arme!",  # Événement pour la deuxième case speciale
        "Vous avez trouvé la salle de la sorcière vous gagnez une potion (+1 potion dans l'inventaire) !",  # Événement pour la troisième case spéciale
        "Vous avez trébuché et vous êtes blessés!"  # Événement pour la quatrième case spéciale
    ]
    
    def afficher_texte(texte, x, y, font, fenetre, couleur):
        rendu = font.render(texte, True, couleur)
        fenetre.blit(rendu, (x, y))

    
    # Initialisation des points de vie du joueur et de l'ennemi
    def afficher_popup(message, actions):
        popup_font = pygame.font.Font(None, 24)
        popup_text = popup_font.render(message, True, blanc)
        fenetre.fill(noir)
        fenetre.blit(popup_text, (50, 50))
        
        action_text = popup_font.render(actions, True, blanc)
        fenetre.blit(action_text, (50, 100))
        
        pygame.display.flip()
        

    deplacement_actif = True 
    
    def combat(font, fenetre):
        couleur = (255, 255, 255)
        vie_joueur = 100
        vie_ennemi = 100
        degats_joueur = 20
        tour_joueur = True  # Initialisez la variable tour_joueur
        combat_en_cours = True

        clock = pygame.time.Clock()

        while combat_en_cours:
            actions = "Choisissez A pour attaquer, D pour défendre"

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a and tour_joueur:
                        degats = degats_joueur
                        vie_ennemi -= degats
                        tour_joueur = False
                    elif event.key == pygame.K_d and tour_joueur:
                        vie_joueur -= degats_joueur  # Défense du joueur
                        tour_joueur = False

            if not tour_joueur:
                degats_ennemi = random.randint(2, 15)
                vie_joueur -= degats_ennemi
                tour_joueur = True

            fenetre.fill(noir)

            afficher_texte("Joueur : {} PV".format(vie_joueur), 50, 50, font, fenetre, couleur)
            afficher_texte("Ennemi : {} PV".format(vie_ennemi), 50, 100, font, fenetre, couleur)

            if vie_joueur <= 0:
                message = "Game Over - Ennemi a gagné !"
                afficher_texte(message, 50, 150, font, fenetre, couleur)
                combat_en_cours = False  # Fin du combat
                jouer_son_debut()
                finjeu()
            elif vie_ennemi <= 0:
                message = "Victoire - Joueur a gagné !"
                afficher_texte(message, 50, 150, font, fenetre, couleur)
                combat_en_cours = False  # Fin du combat

            afficher_texte("Tour {} - {}".format("Joueur" if tour_joueur else "Ennemi", actions), 50, 150, font, fenetre, couleur)

            pygame.display.flip()
            clock.tick(60)
                        
    # par défault il ya un joueur actif 
    joueur_actif = 1
    evenement_special_actuel = None
    cases_speciales_occupees = []
    running = True
    menu_fin = False
    inv = False
    
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    inv = True 
                    while inv:
                        inventaire_surface = pygame.Surface((200, 200))
                        inventaire_surface.fill((0, 0, 0))
                        inventaire_rect = inventaire_surface.get_rect()
                        inventaire_rect.topright = (largeur_fenetre, 0)
                        
                        fenetre.blit(inventaire_surface, inventaire_rect)
                        fenetre.blit(image_inventaire, position_inventaire)
                        pygame.display.update()
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                inv = False 
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_i:
                                    inv = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if joueur_actif == 1:
                    # Gérer les déplacements pour le joueur 1
                    if rect_fleche_haut.collidepoint(x, y) and joueur1_y > 0:
                        joueur1_y -= 1
                        enemy_index = get_enemy_at_position(joueur1_x, joueur1_y)
                        if enemy_index is not None:
                            deplacement_actif = False 
                            afficher_popup("Début du combat", "Choisissez A pour attaquer, D pour défendre")
                            combat(font, fenetre)
                                    
                    elif rect_fleche_bas.collidepoint(x, y) and joueur1_y < nombre_cases_y - 1:
                        joueur1_y += 1
                        enemy_index = get_enemy_at_position(joueur1_x, joueur1_y)
                        if enemy_index is not None:
                            deplacement_actif = False 
                            afficher_popup("Début du combat", "Choisissez A pour attaquer, D pour défendre")

                            combat(font, fenetre)
                    
                    elif rect_fleche_gauche.collidepoint(x, y) and joueur1_x > 0:
                        joueur1_x -= 1
                        enemy_index = get_enemy_at_position(joueur1_x, joueur1_y)
                        if enemy_index is not None:
                            deplacement_actif = False 
                            afficher_popup("Début du combat", "Choisissez A pour attaquer, D pour défendre")
                            combat(font, fenetre)
                                                  
                    elif rect_fleche_droite.collidepoint(x, y) and joueur1_x < nombre_cases_x - 1:
                        joueur1_x += 1
                        enemy_index = get_enemy_at_position(joueur1_x, joueur1_y)
                        if enemy_index is not None:
                            deplacement_actif = False 
                            afficher_popup("Début du combat", "Choisissez A pour attaquer, D pour défendre")
                            combat(font, fenetre)
                       
                    if (joueur1_x, joueur1_y) in cases_speciales and (joueur1_x, joueur1_y) not in cases_speciales_occupees:
                        indice_case_speciale = cases_speciales.index((joueur1_x, joueur1_y))
                        evenement_special_actuel = evenements_cases_speciales[indice_case_speciale]
                        cases_speciales_occupees.append((joueur1_x, joueur1_y))
                        if indice_case_speciale == 2:
                            inventaire.append("potion")
                        if indice_case_speciale == 3 :
                            vie_joueur = vie_joueur -25
                        if indice_case_speciale == 0:
                            menu_fin = True
                            while menu_fin:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()                               
                                fenetre.blit(fond_menu, (0, 0))
                                fin_text = font.render("Vous vous êtes echappé félitations !", True, blanc)
                                fin_rect = fin_text.get_rect(center=(largeur_fenetre // 2, hauteur_fenetre // 4))
                                fenetre.blit(fin_text, fin_rect)
                                pygame.display.flip()
                                
                    joueur_actif = 2 
                elif joueur_actif == 2:
                    if rect_fleche_haut.collidepoint(x, y) and joueur2_y > 0:
                        joueur2_y -= 1
                        enemy_index = get_enemy_at_position(joueur2_x, joueur2_y)
                        if enemy_index is not None:
                            deplacement_actif = False 
                            afficher_popup("Début du combat", "Choisissez A pour attaquer, D pour défendre")
                            combat(font, fenetre)
                                           
                    elif rect_fleche_bas.collidepoint(x, y) and joueur2_y < nombre_cases_y - 1:
                        joueur2_y += 1
                        enemy_index = get_enemy_at_position(joueur2_x, joueur2_y)
                        if enemy_index is not None:
                            deplacement_actif = False 
                            afficher_popup("Début du combat", "Choisissez A pour attaquer, D pour défendre")
                            combat(font, fenetre)
                                                   
                    
                    elif rect_fleche_gauche.collidepoint(x, y) and joueur2_x > 0:
                        joueur2_x -= 1
                        enemy_index = get_enemy_at_position(joueur2_x, joueur2_y)
                        if enemy_index is not None:
                            deplacement_actif = False 
                            afficher_popup("Début du combat", "Choisissez A pour attaquer, D pour défendre")
                            combat(font, fenetre)
                                                  
                    elif rect_fleche_droite.collidepoint(x, y) and joueur2_x < nombre_cases_x - 1:
                        joueur2_x += 1
                        enemy_index = get_enemy_at_position(joueur2_x, joueur2_y)
                        if enemy_index is not None:
                            deplacement_actif = False 
                            afficher_popup("Début du combat", "Choisissez A pour attaquer, D pour défendre")
                            combat(font, fenetre)
                            
                    if (joueur2_x, joueur2_y) in cases_speciales and (joueur2_x, joueur2_y) not in cases_speciales_occupees:
                        indice_case_speciale = cases_speciales.index((joueur2_x, joueur2_y))
                        evenement_special_actuel = evenements_cases_speciales[indice_case_speciale]
                        cases_speciales_occupees.append((joueur2_x, joueur2_y))
                        if indice_case_speciale == 0:
                            menu_fin = True
                            while menu_fin:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()                               
                                fenetre.blit(fond_menu, (0, 0))
                                fin_text = font.render("Vous vous êtes echappé félitations !", True, blanc)
                                fin_rect = fin_text.get_rect(center=(largeur_fenetre // 2, hauteur_fenetre // 4))
                                fenetre.blit(fin_text, fin_rect)
                                pygame.display.flip()
                        
  
                    joueur_actif = 3
                        
                elif joueur_actif == 3:
                    # Gérer les déplacements pour le joueur 3 (si joueurs >= 3)
                    if rect_fleche_haut.collidepoint(x, y) and joueur3_y > 0:
                        joueur3_y -= 1
                        enemy_index = get_enemy_at_position(joueur3_x, joueur3_y)
                        if enemy_index is not None:
                            deplacement_actif = False 
                            afficher_popup("Début du combat", "Choisissez A pour attaquer, D pour défendre")
                            combat(font, fenetre)
                                           
                    elif rect_fleche_bas.collidepoint(x, y) and joueur3_y < nombre_cases_y - 1:
                        joueur3_y += 1
                        enemy_index = get_enemy_at_position(joueur3_x, joueur3_y)
                        if enemy_index is not None:
                            deplacement_actif = False 
                            afficher_popup("Début du combat", "Choisissez A pour attaquer, D pour défendre")
                            combat(font, fenetre)       
                
                    elif rect_fleche_gauche.collidepoint(x, y) and joueur3_x > 0:
                        joueur3_x -= 1
                        enemy_index = get_enemy_at_position(joueur3_x, joueur3_y)
                        if enemy_index is not None:
                            deplacement_actif = False 
                            afficher_popup("Début du combat", "Choisissez A pour attaquer, D pour défendre")
                            combat(font, fenetre)
                                                  
                    elif rect_fleche_droite.collidepoint(x, y) and joueur3_x < nombre_cases_x - 1:
                        joueur3_x += 1
                        enemy_index = get_enemy_at_position(joueur3_x, joueur3_y)
                        if enemy_index is not None:
                            message = f"Vous avez rencontré un ennemi : {enemy_index}"
                            print(message) 
                            
                    if (joueur3_x, joueur3_y) in cases_speciales and (joueur3_x, joueur3_y) not in cases_speciales_occupees:
                        indice_case_speciale = cases_speciales.index((joueur3_x, joueur3_y))
                        evenement_special_actuel = evenements_cases_speciales[indice_case_speciale]
                        cases_speciales_occupees.append((joueur3_x, joueur3_y))
                        print(f"Case spéciale détectée : {evenement_special_actuel}")
                        if indice_case_speciale == 0:
                            menu_fin = True
                            while menu_fin:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()                               
                                fenetre.blit(fond_menu, (0, 0))
                                fin_text = font.render("Vous vous êtes echappé félitations !", True, blanc)
                                fin_rect = fin_text.get_rect(center=(largeur_fenetre // 2, hauteur_fenetre // 4))
                                fenetre.blit(fin_text, fin_rect)
                                pygame.display.flip()
                                                
                    joueur_actif = 4
                    
                elif joueur_actif == 4:
                    # Gérer les déplacements pour le joueur 3 (si joueurs >= 3)
                    if rect_fleche_haut.collidepoint(x, y) and joueur4_y > 0:
                        joueur4_y -= 1
                    elif rect_fleche_bas.collidepoint(x, y) and joueur4_y < nombre_cases_y - 1:
                        joueur4_y += 1
                    elif rect_fleche_gauche.collidepoint(x, y) and joueur4_x > 0:
                        joueur4_x -= 1
                    elif rect_fleche_droite.collidepoint(x, y) and joueur4_x < nombre_cases_x - 1:
                        joueur4_x += 1
                    joueur_actif = 1
                    
                    if (joueur4_x, joueur4_y) in cases_speciales and (joueur4_x, joueur4_y) not in cases_speciales_occupees:
                        indice_case_speciale = cases_speciales.index((joueur3_x, joueur3_y))
                        evenement_special_actuel = evenements_cases_speciales[indice_case_speciale]
                        cases_speciales_occupees.append((joueur4_x, joueur4_y))
                        print(f"Case spéciale détectée : {evenement_special_actuel}")
                        if indice_case_speciale == 0:
                            menu_fin = True
                            while menu_fin:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()                               
                                fenetre.blit(fond_menu, (0, 0))
                                fin_text = font.render("Vous vous êtes echappé félitations !", True, blanc)
                                fin_rect = fin_text.get_rect(center=(largeur_fenetre // 2, hauteur_fenetre // 4))
                                fenetre.blit(fin_text, fin_rect)
                                pygame.display.flip()
                                           
        for i, (x, y) in enumerate(boss_positions):
            if i == 0:
                boss_image = image_loup
            elif i == 1:
                boss_image = image_dragon
            elif i == 2:
                boss_image = image_chevalier
            elif i == 4:
                boss_image = image_archer
                
            fenetre.blit(boss_image, (x * taille_case, y * taille_case))
        
        fenetre.fill(blanc)
        
        # Créez une liste de couleurs spéciales
        couleurs_speciales = [(0, 0, 255), (255, 255, 0), (0, 255, 0)]

        # Utilisez un indice pour parcourir les couleurs spéciales
        indice_couleur = 0

        for indice, (x, y) in enumerate(cases_speciales):
            evenement = evenements_cases_speciales[indice]
            couleur_case = couleurs_speciales[indice_couleur]
            indice_couleur = (indice_couleur + 1) % len(couleurs_speciales)
            pygame.draw.rect(fenetre, couleur_case, (x * taille_case, y * taille_case, taille_case, taille_case))
           
        fenetre.blit(image_dragon, (dragon_x * taille_case, dragon_y * taille_case)) 
        fenetre.blit(image_loup, (loup_x * taille_case, loup_y * taille_case)) 
        fenetre.blit(image_archer, (archer_x * taille_case, archer_y * taille_case))
        fenetre.blit(image_chevalier , (chevalier_x * taille_case , chevalier_y * taille_case))

        for x in range(nombre_cases_x):
            for y in range(nombre_cases_y):
                fenetre.blit(image_sol, (x * taille_case, y * taille_case))
                        
        #Dessiner l'image "deco.jpg" à la place de l'espace blanc
        fenetre.blit(image_deco, (largeur_fenetre - espace_blanc_droite, 0))
        
        # Dessiner la grille
        for x in range(0, largeur_fenetre - espace_blanc_droite, taille_case):
            pygame.draw.line(fenetre, marron, (x, 0), (x, hauteur_fenetre))
        for y in range(0, hauteur_fenetre, taille_case):
            pygame.draw.line(fenetre, marron, (0, y), (largeur_fenetre - espace_blanc_droite, y))

        # Dessiner la zone grise
        for x in range(zone_grise_x * taille_case, (zone_grise_x + zone_grise_largeur) * taille_case, taille_case):
            for y in range(zone_grise_y * taille_case, (zone_grise_y + zone_grise_hauteur) * taille_case, taille_case):
                pygame.draw.rect(fenetre, gris, (x, y, taille_case, taille_case))
                
         # Dessiner les joueurs
        fenetre.blit(image_perso1, (joueur1_x * taille_case, joueur1_y * taille_case))
        if joueurs >= 2:
            fenetre.blit(image_perso2, (joueur2_x * taille_case, joueur2_y * taille_case))
        if joueurs >= 3:
            fenetre.blit(image_perso3, (joueur3_x * taille_case, joueur4_y * taille_case))
        if joueurs >= 4:
            fenetre.blit(image_perso4, (joueur4_x * taille_case, joueur4_y * taille_case))
            

        # Dessiner les flèches
        fenetre.blit(image_fleche_haut, rect_fleche_haut.topleft)
        fenetre.blit(image_fleche_bas, rect_fleche_bas.topleft)
        fenetre.blit(image_fleche_gauche, rect_fleche_gauche.topleft)
        fenetre.blit(image_fleche_droite, rect_fleche_droite.topleft)
                
        # Rafraîchir l'affichage
        pygame.display.flip()