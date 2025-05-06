
import random
import time

class Robot:
    def __init__(self, name, power, hp, deff, inputMet):
        self.name = name
        self.power = power
        self.hp = hp
        self.maxHp = hp
        self.deff = deff
        self.defending = False
        self.stunned = False
        self.inputMet = inputMet

    def __str__(self):
        return f"Name: {self.name}, Power: {self.power}, HP: {self.hp}, Def: {self.deff}"

    def attack(self, opponent):
        
        hit = 0
        
        if self.stunned:
            print(f"{self.name} is stunned and cannot attack this round!")
            self.stunned = False  # Status stun hilang setelah giliran
            return

        if opponent.defending:
            hit = random.randint(1, self.power) * 0.5
            opponent.hp -= hit
            print(f"{self.name} hit {hit} but {opponent.name} defended! Damage reduced.")
        else:
            hit = random.randint(10, self.power)
            opponent.hp -= hit
            print(f"{self.name} hit {hit:.2f} damage to {opponent.name}!")

        if random.random() < 0.25:  # 25% peluang untuk stun
            opponent.stunned = True
            print(f"{opponent.name} is stunned!")
        
        opponent.defending = False

    def defend(self):
        self.defending = True
        print(f"{self.name} is defending! Incoming damage will be reduced.")

    def regenerate(self):
        regen = random.randint(1, int(self.maxHp * 0.35))
        if self.hp + regen > self.maxHp:
            self.hp = self.maxHp
            print(f"{self.name}'s HP is full!")
        else:
            self.hp += regen
            print(f"{self.name} regenerated {regen} HP!")

    def give_up(self):
        self.hp = 0
        print(f"{self.name} has given up!")

    def choose_move(self, available_choices):
        print(f"{self.name}: [a]ttack, [d]efend, [r]egen, [g]ive UP?")
        mv_choice = self.inputMet(available_choices)

        if mv_choice == 'a':
            return 'attack'
        elif mv_choice == 'd':
            return 'defend'
        elif mv_choice == 'r':
            return 'regen'
        else:
            return 'give_up'


class Game:
    def __init__(self, player_1, player_2):
        self.players = [player_1, player_2]
        self.round = 1

    def start_round(self):
        print(f"\nRound {self.round}")
        actions = []

        for player in self.players:
            if player.hp > 0:
                print(player)
                action = player.choose_move(['a', 'd', 'r', 'g'])
                actions.append((player, action))

        # Eksekusi aksi dari setiap pemain
        for player, action in actions:
            if action == 'attack':
                opponent = self.get_opponent(player)
                player.attack(opponent)
            elif action == 'defend':
                player.defend()
            elif action == 'regen':
                player.regenerate()
            else:
                player.give_up()

        self.round += 1

    def get_opponent(self, player):
        """ Mengambil lawan dari player yang sedang giliran bertindak """
        return self.players[1] if self.players[0] == player else self.players[0]

    def check_winner(self):
        """ Mengecek apakah ada pemain yang menang """
        for player in self.players:
            if player.hp > 0:
                return player
        return None

    def play(self):
        while True:
            self.start_round()
            winner = self.check_winner()
            if self.players[0].hp <= 0 or self.players[1].hp <= 0:
                winner = self.check_winner()
                if winner:
                    print(f"\n** {winner.name} wins! **")
                    break


# Fungsi input untuk manusia
def human_input(choices):
    choice = input(f"player Choose: {', '.join(choices)}: ")
    while choice not in choices:
        print('Invalid choice. Try again!')
        choice = input(f"player choose: {', '.join(choices)}: ")
    return choice

def com_input(choices):
    time.sleep(1)
    
    choice = random.choice(choices)
    print(f"bot choose : {choice}")
    return choice 


# Setup pemain
player_1 = Robot('Dafa', 90, 50, 50, human_input)

player_2 = Robot('Bot', 70, 60, 100, human_input)

# Setup permainan
game = Game(player_1, player_2)
game.play()

