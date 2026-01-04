import random
import time
options =("Rock","Paper","Scissor")
uwon=0
cwon=0
for x in range(3):
    user=input("Enter your choice(Rock/Paper/Scissor):")
    cpuanswer=random.choice(options)

    if user.capitalize() == cpuanswer:
        print(f"CPU CHOSE:{cpuanswer}")
        print(f"YOU CHOSE:{user.capitalize()}")
        print("GAME TIED!!")
    elif not user.capitalize() == cpuanswer:
        if user.capitalize() =="Rock" and cpuanswer == "Paper":
            print(f"CPU CHOSE:{cpuanswer}")
            print(f"YOU CHOSE:{user.capitalize()}")
            print("CPU WON!!")
            cwon+=1
        elif user.capitalize() =="Rock" and cpuanswer == "Scissor":
            print(f"CPU CHOSE:{cpuanswer}")
            print(f"YOU CHOSE:{user.capitalize()}")
            print("YOU WON!!")
            uwon+=1
        elif user.capitalize() =="Paper" and cpuanswer =="Scissor":
            print(f"CPU CHOSE:{cpuanswer}")
            print(f"YOU CHOSE:{user.capitalize()}")
            print("CPU WON!!")
            cwon+=1
        elif user.capitalize() =="Paper" and cpuanswer == "Rock":
            print(f"CPU CHOSE:{cpuanswer}")
            print(f"YOU CHOSE:{user.capitalize()}")
            print("YOU WON!!")
            uwon+=1
        elif user.capitalize() =="Scissor" and cpuanswer == "Paper":
            print(f"CPU CHOSE:{cpuanswer}")
            print(f"YOU CHOSE:{user.capitalize()}")
            print("YOU WON!!")
            uwon+=1
        elif user.capitalize() =="Scissor" and cpuanswer == "Rock":
            print(f"CPU CHOSE:{cpuanswer}")
            print(f"YOU CHOSE:{user.capitalize()}")
            print("CPU WON!!")
            cwon+=1
time.sleep(1)
if cwon>uwon:    
    print("-----------SCORE-BOARD-----------")
    print(f"CPU:{cwon:3}")
    print(f"YOU:{uwon:3}")
    print("CPU WON THIS GAME!!")
elif cwon==uwon:
    print("-----------SCORE-BOARD-----------")
    print(f"CPU:{cwon:3}")
    print(f"YOU:{uwon:3}")
    print("GAME TIED!!")
else:
    print("-----------SCORE-BOARD-----------")
    print(f"CPU:{cwon:3}")
    print(f"YOU:{uwon:3}")
    print("YOU WON THIS GAME!!")
    