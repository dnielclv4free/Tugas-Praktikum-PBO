from robots import Robot
from games import Game
dendelus = Robot('dendelus', 100, 100, 50)  # object
eteris = Robot('eteris', 50, 100, 80)

robots= [dendelus, eteris]

while True:
    print("ROBOT WARZZZ")
    print("Menu : ")
    print("1. Start")
    print("2. Exit")
    
    select = input("Choose 1/2 : ")

    if select == '1' :
        print("Select your Robot: ")
        
        for index, robot in enumerate(robots):
            print(f"{index + 1}. {robot}")

        plyr_choice = int(input("Choose your robot (1/2) : ")) - 1 
        plyr_robot = robots[plyr_choice]

        print("Select opponent Robot: ")

        for index, robot in enumerate(robots):
            if index != plyr_choice:
                print(f"{index + 1}. {robot}")

        opp_choice = int(input("Choose opponent robot (1/2): ")) - 1
        opp_robot = robots[opp_choice]
            
        cur_game=Game()
        
        while not cur_game.gameOver:
            cur_game.newRound()
            print("1. Attack, 2. Defense, 3. Regen")
            plyr_move=input(f"{plyr_robot.name} Select your move (1/2/3) : ")
            opp_move=input(f"{opp_robot.name} Select your move (1/2/3) : ")
            if plyr_move == '1':
                plyr_robot.attack(opp_robot)
            if opp_move=='1':
                opp_robot.attack(plyr_robot)
            if plyr_move=='2':
                plyr_robot.defense()
            if opp_move=='2':
                opp_robot.defense()
            if opp_move=='3':
                opp_robot.regenHP(15)
            if plyr_move == '3':
                plyr_robot.regenHP(15)
            cur_game.checkWin(plyr_robot,opp_robot)

    if select == '2' :
        break
    
        


print(dendelus.__dict__)
print(eteris.__dict__)

print(dendelus.name)



# Menampilkan jumlah robot yang telah dibuat

