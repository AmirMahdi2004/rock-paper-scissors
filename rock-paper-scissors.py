import random

username = input("Enter your User name : ")
skg = ['S', 'K', 'G']
player_selection = str
player_points, system_score, equality, i = 0, 0, 0, 0
while i >= 0:
    player_selection = input("Enter your choice : ")
    system_selection = random.choice(skg)
    print(f"{username} : {player_selection} system : {system_selection} ")
    if player_points > 2 or system_score > 2:
        break
    elif player_selection == system_selection:
        equality += 1
        print("equality")
    elif player_selection == "G" and system_selection == "S":
        system_score += 1
        print("los")
    elif player_selection == "S" and system_selection == "K":
        system_score += 1
        print("los")
    elif player_selection == "K" and system_selection == "G":
        system_score += 1
        print("los")
    elif player_selection == "S" and system_selection == "G":
        player_points += 1
        print("win")
    elif player_selection == "K" and system_selection == "S":
        player_points += 1
        print("win")
    elif player_selection == "G" and system_selection == "K":
        player_points += 1
        print("win")
    elif player_selection != "G" or player_selection != "S" or player_selection != "K":
        print("wrong choice try agin Please S or K or G ")
        i = 0
    i += 1

if player_points > system_score:
    print(
        f"{username} victory \n your score :{player_points}  System score :{system_score} equality :{equality} round :{i}")
else:
    print(
        f"{username} lost \nyour score :{player_points}  System score :{system_score} equality :{equality} round :{i}")
