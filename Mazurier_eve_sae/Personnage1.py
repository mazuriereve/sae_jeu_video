class Personnage:
    def __init__(self, nom, points_de_vie, degats):
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.degats = degats
        self.defense = False

    def attaquer(self, cible):
        degats = self.degats
        if self.defense:
            # Réduction des dégâts en cas de défense
            degats = int(degats * 0.9)  # Réduction de 10%
        cible.points_de_vie -= degats
            
class Personnage1(Personnage):
    def __init__(self, nom, points_de_vie, degats):
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.degats = degats

