class Player:

    def __init__(self):

        # PLAYER INFO
        self.name = ""
        self.location = 'e4'
        self.game_over = False

        # PLAYER STATS
        self.hp = 100
        self.stamina = 100
        self.strength = 10
        self.money = 0
        self.inventory = []
        self.status_effects = 'none'
playerko = Player()