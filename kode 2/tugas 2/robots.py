
import random
import time

class Move:
    def __init__(self, player, opp=None):
        self.player = player
        self.opp = opp

    def execute(self):
        pass

class Attack(Move):
    def __init__(self, player, opp):
        super().__init__(player, opp)

    def execute(self):
        self.player.defending = False
        hit = 0
        
        if self.opp.defending:
            # If the opponent is defending, reduce the damage significantly
            hit = random.randint(1, self.player.power) * 0.5
            self.opp.deff += hit
            print(f"{self.player.name} hit but {self.opp.name} defended! Damage reduced.")
        else:
            # Normal attack
            hit = random.randint(10, self.player.power) / (self.opp.deff * 0.1)
            self.opp.hp -= hit
            print(f"{self.player.name} hit {hit:.2f} damage to {self.opp.name}!")
        
        self.opp.defending = True

class Defend(Move):
    def __init__(self, player, opp):
        super().__init__(player, opp)

    def execute(self):
        self.player.defending = True
        print(f"{self.player.name} is defending! Incoming damage will be reduced.")

class Regen(Move):
    def __init__(self, player, opp):
        super().__init__(player, opp)

    def execute(self):
        regen = random.randint(1, int(self.player.maxHp * 0.35))
        if self.player.hp + regen > self.player.maxHp:
            self.player.hp = self.player.maxHp
            print(f"{self.player.name}'s HP is full!")
        else:
            self.player.hp += regen
            print(f"{self.player.name} regenerated {regen} HP!")

class GiveUp(Move):
    def __init__(self, player, opp):
        super().__init__(player, opp)

    def execute(self):
        self.player.hp = 0
        print(f"{self.player.name} has given up!")

class Robot:
    robots = []

    def __init__(self, name, power, hp, deff, inputMet):
        self.name = name
        self.power = power
        self.hp = hp
        self.maxHp = hp
        self.deff = deff
        self.defending = False
        self.inputMet = inputMet
        Robot.robots.append(self)
    
    def __str__(self):
        return f"Name: {self.name}, Power: {self.power}, HP: {self.hp}, Def: {self.deff}"

    @classmethod
    def get_next_p(cls, p):
        curr_idx = cls.robots.index(p)
        curr_idx = (curr_idx + 1) % len(cls.robots)
        while cls.robots[curr_idx].hp < 1:
            curr_idx = (curr_idx + 1) % len(cls.robots)
        return cls.robots[curr_idx]

    def choose_move(self):
        print(f"{self.name}: [a]ttack, [d]efend, [r]egen, [g]ive UP?")
        mv_choice = self.inputMet(['a', 'd', 'r', 'g'])

        if mv_choice == 'a':
            opp = Robot.get_next_p(self)
            return Attack(self, opp)
        elif mv_choice == 'd':
            return Defend(self, None)
        elif mv_choice == 'r':
            return Regen(self, None)
        else:
            return GiveUp(self, None)

def human_input(choices):
    choice = input()
    while choice not in choices:
        print('Invalid choice. Try again!')
        choice = input()
    return choice

def com_input(choices):
    time.sleep(1)
    choice = random.choice(choices)
    print(f"Bot chose: {choice}")
    return choice

# Game setup
player_1 = Robot('Dafa', 100, 80, 50, human_input)
player_2 = Robot('Bot', 70, 90, 100, human_input)

curr_ply = Robot.robots[0]
playing = True

# Main game loop
while playing:
    actions = []
    for p in Robot.robots:
        if p.hp > 0:
            print(p, end='\n\n')
            action = p.choose_move()
            actions.append(action)

    for action in actions:
        action.execute()
        time.sleep(1)

    if len([p for p in Robot.robots if p.hp > 0]) <= 1:
        playing = False

# Endgame - print winner
for p in Robot.robots:
    if p.hp > 0:
        print(f'** {p.name} wins! **')
        break

