"""
GAME : ODD-EVE
BASIC RULES : GAME SHOULD BE TWO MODE GAME

CPU VS PLAYER
PLAYER VS PLAYER

TOSS : BOTH PLAYER PLAY ODD-EVE GAME TAHT IS ,
PLAYER WILL CHOOSE NUMBER FORM 1 TO 10
AND ALSO EVEN OR ODD
THEN, BOTH THE NUMBER WILL BE ADDED IF THE RESULT IS EVEN OR ODD IT WILL BE MATCHED WITH PLAYER SELECTION.

NOW IF THE PLAYER WINS, PLAYER WILL DECIDE THE BATTING OR BOWLING

IN BOTH THE OPTION PLAYER AND CPU WILL CHOSE SOME RANDOM NUMBERS FORM 1 TO 10 

THE BATTER(CPU OR PLAYER) WILL SELECT NUMBERS AS RUNS 

THE FIRST INNING(PLAYER OR CPU'S BATTING) WILL END ONLY WHEN THE BOWLER AND PLAYER'S NUMBER(RUNS) IS MATCHED.
IT IS SAID THAT PLAYER GOT OUT WHEN BOTH NUMBER IS MATCHED.

AND THEN THE TARGET WILL BE RUN SCORED + 1 BY THE BATTER.

OTHER PLAYER HAVE TO SCORE LIKE THIS ONLY UNTIL THE NUMBERS OF BOTH PLAYER GOT MATCHED.

"""
import random
import time
print("-----PYTHON ODD-EVE GAME----")
print("-----------SELECT-----------")
print("---------1 -> START--------")
print("---------2 -> RULES--------")
select=int(input("YOUR OPTION -> "))

user_toss_dict={1:"Batting",2:"Bowling"}
cpu_toss_list=["Batting","Bowling"]



# function for cpu batting and user bowling in return


# function for countdown of 3 seconds
def countdown():
    print("GAME STARTS IN ",end="")
    time.sleep(0.7)
    for x in range(3,0,-1):
        print(x,end=" ")
        time.sleep(0.5)
    print("START!!")
    print()


if select == 2:
    print("Rules goes form here.")

elif select == 1:
    yourname=input("Enter Your Name -> ")
    print()
    print(f"HELLO {yourname.upper()}!!")
    print()
    print("TOSS TIME!!")
    eveodd_select=input("Choose EVEN or ODD -> ")          #user chose
    u_toss_number=int(input("Choose Number form 1 - 10 -> "))
    cpu_toss_number=random.randint(1,10)
    print()
    print(f"YOU CHOSE:{u_toss_number:3}")
    print(f"CPU CHOSE:{cpu_toss_number:3}")
    print()
    total=u_toss_number+cpu_toss_number

    if total%2==0:
        toss_answer="even"
    else:
        toss_answer="odd"
    
    if eveodd_select==toss_answer:
        print("------YOU WON THE TOSS------")
        print()
        print("-----------SELECT-----------")
        print("--------1 -> BATTING--------")
        print("--------2 -> BOWLING--------")
        batbowl_select=int(input("Your Option -> "))
        print()
        print(f"You CHOSE {user_toss_dict.get(batbowl_select)}")
        print()
        time.sleep(1)
        print("ENTER NUMBER FORM 1 TO 10 TO ADD UP YOUR SCORE.")
        time.sleep(1)
        print("ENTER 0 TO KNOW THE SCOREBOARD ANYTIME.")
        time.sleep(1)
        print()

        countdown() # function for three second countdown

        if batbowl_select==1:
        #start of USER-BATTING 
            user_bat_add=0
            cpubowl=random.randint(1,10)
            userbat=int(input("YOU -> "))
            #print(cpubowl)
            print(f"CPU -> {cpubowl}")
            user_bat_add+=userbat
            while not userbat==cpubowl:
                cpubowl=random.randint(1,10)
                userbat=int(input("YOU -> "))

                if userbat==0:
                    print("--------SCOREBOARD--------")
                    print(f"---PLAYER SCCORED {user_bat_add} RUNS---")
                    userbat=int(input("YOU -> "))

                if userbat>10 or userbat<0:
                    print("Enter a valid number between 1 to 10.")
                    userbat=int(input("YOU -> "))

                print(f"CPU -> {cpubowl}")
                user_bat_add+=userbat
            print()
            print(f"<<<<< {yourname} OUT!! >>>>>")
            print()
            print("--------SCOREBOARD--------")
            print(f"---PLAYER SCCORED {user_bat_add} RUNS---")
            print(f"----TARGET FOR CPU IS {user_bat_add+1}----")
            print()
        #end of USER-BATTING

            y=input("PRESS ENTER FOR CPU BATTING ->")

            while not y=="":
                y=input("PRESS ENTER FOR CPU BATTING ->")
            if y=="":
                
                countdown()     
                
            # start of CPU-BATTING
                cpu_bat_add=0
                userbowl=int(input("YOU -> "))
                cpubat=random.randint(1,10)
                print(f"CPU -> {cpubat}")
                cpu_bat_add+=cpubat
                while not cpubat==userbowl and not cpu_bat_add>=user_bat_add:
                    cpubat=random.randint(1,10)
                    userbowl=int(input("YOU -> "))
                    
                    if userbowl==0:
                        print("--------SCOREBOARD--------")
                        print(f"---CPU SCCORED {cpu_bat_add} RUNS---")
                        userbowl=int(input("YOU -> "))

                    if userbowl>10 or userbowl<0:
                        print("Enter a valid number between 1 to 10.")
                        userbowl=int(input("YOU -> "))

                    print(f"CPU -> {cpubat}")
                    cpu_bat_add+=cpubat

                if cpu_bat_add>=user_bat_add:
                    print("--------------------------")
                    print("---------CPU WON!!--------")
                    print(f"--------{yourname} LOST!!--------")
                else:
                    print("--------------------------")
                    print("<<<<<<<<<< OUT!! >>>>>>>>>")
                    print("--------------------------")
                    print("--------SCOREBOARD--------")
                    print(f"---CPU SCCORED {cpu_bat_add} RUNS---")
                    print(f"--CPU LOST FROM {yourname} BY {user_bat_add-cpu_bat_add} RUNS--")
                    print()
    
        # end of CPU-BATTING
            
        #elif batbowl_select==2:
            #user_bowling()  




    else:
        print("------CPU WON THE TOSS------")
        print(f"CPU CHOSE {random.choice(cpu_toss_list)}")

    









