import random
import time
import sys



print("You awaken in a room. There is a dimly lit torch on a wall to your left side, but otherwise there is no lighting. There is a door in front of you as well as one to your left.")

#Room 1
def Room1():
    print("Select a decision!\n 1. Look Around\n 2. open the door in front of you \n 3. Open the door to yor left\n 4. sit\n 5. Quit")
    commands = input()
    while True:
          if commands == "Look Around":
               Choices()
          if commands == "Open the door in front of you":
               TheRoominFront()
          if commands == "Open the door to your left":
               leftroom()
          if commands == "sit":
                print("You have sat down on the damp cold floor.")
                time.sleep(5)
                print("You have stood up after to long on the grimey floor.")
          if commands == "Quit":
                Exit_Program()
          else: 
               print("Invalid Command")
               Room1()
     
#LIST
     #Choices for option 1
Choice_list = ["There is a few rocks but nothing much.","You spy an odd looking stick","There doesn't seem to be anything.Try looking again."]
     #Events for the stick
Events_lst = ["BOOM, ZAP, BAM, THIS STICK IS A WAND!","It does nothing it is a stick.","It broke in half."]
     #Rocks event list
Events_lst2 = ["You throw the rock at the wall, the wall breaks.","Nothing Happens","The rock disappears"]
     #Sound Investigate
Investigate_lst = ["There is a cute rat.","There is a terrifying rat, he bites you and you fall unconscious. You wake back up in the first room.","There is nothing it must be your imagination."]
#Functions
     #Stuff to do with the stick
def Stick_list ():
    print("Do you want to interact with the stick? Type N or No to chose No or type Y or Yes for Yes")
    player_choice = input()
    if player_choice == "Y" or player_choice == "yes":
        choice = random.randint(1,3)
        if choice == 1:
             print(Events_lst[0])
             Room1()
        elif choice == 2:
             print(Events_lst[1])
             Room1()
        elif choice == 3:
             print(Events_lst[2])
             Room1()
    if player_choice == "N" or player_choice ==  "No":
         print("You're lame! Here lays a cool stick and you toss it away like its nothing.")
         Room1()
    else:
         print("Invalid Selection! Please try again.")
         Stick_list()
#The Room in front of player
def TheRoominFront ():
     print("The room is larger than that of the last, the lighting is similar aswell except fot the dim light of the moon driftig in from a window on the wall")
     print("Select a decision!\n 1. Look Around\n 2. Exit to previous Room \n 3. Jump out the window\n 4. sit\n 5. Quit")
     commands = input()
     while ():
          if commands == "Look Around":
               Choices()
          if commands == "Exit to previous Room":
               Room1()
          if commands == "Jump out window":
               print("Glass shattered as you threw your entire body into the window. You proceeded to fall 157 floors. Your story is over")
               Exit_Program()
          if commands == "sit":
                print("You have sat down on the damp cold floor.")
                time.sleep(5)
                print("You have stood up after to long on the grimey floor.")
          if commands == "Quit":
                Exit_Program()
          else: 
               print("Invalid Command")
               TheRoominFront()
#Rocks Options
def Rocks():
    print("Would you like to interact with thye sticks?")
    player_choice = input()
    if player_choice == "Y" or player_choice == "yes":
        choice = random.randint(1,3)
        if choice == 1:
             print(Events_lst2[0])
             Room1()
        elif choice == 2:
             print(Events_lst2[1])
             Room1()
        elif choice == 3:
             print(Events_lst2[2])
             Room1()
    if player_choice == "N" or player_choice ==  "No":
         print("You're lame!")
         Room1()
    else:
         print("Invalid Selection! Please try again.")
         Stick_list()
#Exit Command
def Exit_Program():
    sys.exit(0)
#Room to your left
def leftroom():
     print("The door opens and a strange noice comes from the corner.")
     print("Would you like to investigate the sound?")
     player_choice = input()
     if player_choice == "Y" or player_choice == "Yes":
        choice = random.randint(1,3)
        if choice == 1:
             print(Investigate_lst[0])
        elif choice == 2:
             print(Investigate_lst[1])
             Room1()
        elif choice == 3:
             print(Investigate_lst[2])
             leftroom()
     if player_choice == "N" or player_choice ==  "No":
         print("Thats probably the right choice!")
         leftroom()
     else:
         print("Invalid Selection! Please try again.")
         leftroom()

#Choice Selection
def Choices():
    choice = random.randint(1,3)
    if choice == 1:
         print(Choice_list[0])   

    elif choice == 2:
        print(Choice_list[1])
        Stick_list()
    elif choice == 3:
        print(Choice_list[2])
        Room1()

Room1()



















        