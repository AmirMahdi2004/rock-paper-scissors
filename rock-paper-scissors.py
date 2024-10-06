import random

username = input("Enter your User name : ")
skg = ['S', 'K', 'G']
us = str
u, s, i, m = 0,0,0,0
while i >= 0:
    us = input("Enter your choice : ")
    sis = random.choice(skg)
    print(f"{username} : {us} sis : {sis} ")
    if u > 2 or s > 2:
        break
    elif us == sis:
        m += 1
        print("mosav")
    elif us == "G" and sis == "S":
        s += 1
        print("los")
    elif us == "S" and sis == "K":
        s += 1
        print("los")
    elif us == "K" and sis == "G":
        s += 1
        print("los")
    elif us == "S" and sis == "G":
        u += 1
        print("win")
    elif us == "K" and sis == "S":
        u += 1
        print("win")
    elif us == "G" and sis == "K":
        u += 1
        print("win")
    elif us != "G" or us != "S" or us != "K":
        print("wrong choice try agin Please S or K or G ")
        i = 0
    i += 1

if u > s:
    print(f"{username} winner \n you point :{u}  Sistem point :{s} mosav :{m} rund :{i}")
else:
    print(f"{username} los \nyou point :{u}  Sistem point :{s} mosav :{m} rund :{i}")
