import random
import os
import time
def show_logo():
    print("""разработчики:
██╗░░██╗███████╗████████╗░░░░░░░░░██╗░░██╗░█████╗░████████╗
██║░██╔╝██╔════╝╚══██╔══╝░░░░░░░░░██║░██╔╝██╔══██╗╚══██╔══╝
█████╔╝░█████╗░░░░░██║░░░░░░░░░░░░█████╔╝░███████║░░░██║░░░
██╔═██╗░██╔══╝░░░░░██║░░░░░░░░░░░░██╔═██╗░██╔══██║░░░██║░░░
██║░░██╗███████╗░░░██║░░░███████╗░██║░░██╗██║░░██║░░░██║░░░
╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚══════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░
""")

def clear_screen_with_logo():
    os.system("cls")  
    show_logo()



show_logo() 

while True:
    print("\rЗапуск программы...", end="")
    time.sleep(0.3)

    print("\rЗапуск программы.. ", end="") 
    time.sleep(0.5)

    print("\rЗапуск программы.  ", end="")
    time.sleep(1)

    print("\rКонец запуска программы")
    time.sleep(0.5)

    clear_screen_with_logo() 
    break

room = 1
key = False
print("ты просыпаешься в каком-то лаберинте ты видишь две развили (влево, вправо)")

stats_player = {
    "HP": 100,
    "AP": 100  # вдохновился механикой из блек солс
}
monster_HP = 150
count_room_1 = 0
count_room_2 = 0
random_room = ["влево","вправо"]
count_ded = 0
anti_cheat1 = random.choice(random_room)
anti_cheat2 = random.choice(random_room)
anti_cheat3 = random.choice(random_room)

while True:
    room_input = input("куда пойдёшь: ").lower().strip()
    if room == anti_cheat1:
        if  room_input == anti_cheat:
            room = 2
            print("ты во второй комнате. ты видишь два пути (влево, вправо) ")
        else:
            monster_hit = random.randint(1,10)
            print(f"ты увидел стену где кровью написано: БЕГИ ПОКА ОН ТЕБЯ НЕ НАСТИГ! \n Вы сильно испугались что не увидели огромную крысу которая вас укусила и нанесла {monster_hit}")
    elif room == 2:
        if room_input == anti_cheat2:
            room = 3
            if count_room_2 == 0:
                anti_cheat = random.choices(random_room)
                count_room_2 = 1
                print("Ты стоишь во второй комнате. Куда теперь? ()")
        elif room_input in ["вперёд", "прямо"]:
            os.system("cls")
            print("вы видите гоблина который на вас наподает")
            while True:
                print(f"""
================================================================
                MONSTER_HP: {monster_HP}                    
================================================================
                                                            
================================================================
    HP: {stats_player['HP']} | AP: {stats_player['AP']}      
================================================================
1.атака             (AP: 40)
2.блокировать       (AP: 10)
3.уклонится         (AP: 5)
4.пропустить        (AP: + 10, 40)
""")
                if monster_HP <= 0:
                    print("вы победили!")
                    break
                if stats_player["HP"] <= 0:
                    print("вы умерли")
                    count_ded = 1
                    break
                try:
                    player_actions = int(input("///  "))
                except ValueError:
                    print("Вводите цифрами")
                    continue
                if player_actions == 1:
                    if stats_player["AP"] >= 40:
                        evasion = random.randint(1,10)
                        if evasion == 5:
                            print("гоблин уклонился")
                        else:
                            Crete = random.randint(1,50)
                            if Crete == 30:
                                print("вы нанесли критический удар!")
                                monster_HP -= 100
                                stats_player["AP"] -= 100
                            else:
                                hit = random.randint(10,50)
                                print(f"вы нанесли {hit}")
                                stats_player["AP"] -= 40
                    else:
                        print("Не хватает AP для удара! Ты промахнулся.")
                        monster_hit = random.randint(10, 30)
                        stats_player["HP"] -= monster_hit
                        print(f"Монстр ударил на {monster_hit} HP!")
                elif player_actions == 2:
                    if stats_player["AP"] >= 10:
                        monster_hit = random.randint(10, 30)
                        shield_block_percent = 13 
                        
                        hit_sum = int(monster_hit * (1 - shield_block_percent / 100))
                        
                        stats_player["HP"] -= hit_sum
                        stats_player["AP"] -= 10
                        
                        print(f"Ты заблокировал часть урона! Вам нанесли: {hit_sum} HP")
                    else:
                        print("Не хватает AP для переката! Ты неуклюжа упал.")
                        monster_hit = random.randint(10, 30)
                        stats_player["HP"] -= monster_hit
                        print(f"Монстр ударил на {monster_hit} HP!")

                elif player_actions == 3:
                    if stats_player["AP"] >= 5:
                        dodging = random.randint(1,3)
                        if dodging == 2:
                            monster_hit = random.randint(10,30)
                            stats_player["HP"] -= monster_hit
                            print(f"вам не удалось уклонится вам нанесли: {monster_hit}")
                            stats_player["AP"] -= 5
                        else:
                            print("вы удачно уклонились!")
                            stats_player["AP"] -= 5
                    else:
                        print("Не хватает AP для укланения! Ты был настолько медленым во время переката что гоблин подумал что убагаешь.")
                        monster_hit = random.randint(15, 30)
                        stats_player["HP"] -= monster_hit
                        print(f"Монстр ударил на {monster_hit} HP!")
                elif player_actions == 4:
                    monster_hit = random.randint(10,30)
                    stats_player["HP"] -= monster_hit
                    recovery_AP = random.randint(10,40)
                    stats_player["AP"] = min(100, stats_player["AP"] + recovery_AP)
                    print(f"вы востановили себе AP: {recovery_AP}")
                else:
                    monster_hit = random.randint(10,30)
                    stats_player["HP"] -= monster_hit
                    recovery_AP = random.randint(10,40)
                    stats_player["AP"] = min(100, stats_player["AP"] + recovery_AP)
                    print(f"число вне диапозона монстр нанёс вам урон: {monster_hit} когда вы думали что сделать | но вы востановили себе AP: {recovery_AP}")
            if count_ded == 1:
                break
            print("Ты видишь тупик, но на полу лежит ключ!")
            key = True
        else:
            print("Тут нет такого пути.")

    elif room == 3:
        if room_input == anti_cheat3 and key == True:
            room = 4
            print("ты видешь белые лучи солнца")
        else:
            print("ты видишь что тут какаято дверь и она заперта возращаешься назад что-бы пересмотреть лабиринт")
            room = 1
    elif room == 4:
        print("ты выбрался")
        break

print("\nСпасибо, что поиграли в продукт от KET_KAT")
time.sleep(10)