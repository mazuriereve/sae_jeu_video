class Ennemi:
    def __init__(self, hp, damage):
        self.hp = hp
        self.damage = damage

    def attaquer(self, cible):
        # Calcul des dégâts infligés à la cible
        degats_infliges = self.damage
        cible.defense(degats_infliges)  # Appel à la méthode de défense de la cible

    def defense(self, degats):
        # Réduire les points de vie en fonction des dégâts
        self.hp -= degats

    def is_alive(self):
        return self.hp > 0

class Chevaliers(Ennemi):
    def __init__(self):
        super().__init(niveau=75, points_de_vie=20)

class Chevaliers(Ennemi):
    def __init__(self):
        super().__init(75, 20)

class Archers(Ennemi):
    def __init__(self):
        super().__init(50, 30)

class Dragon(Ennemi):
    def __init__(self):
        super().__init(150, 50)
