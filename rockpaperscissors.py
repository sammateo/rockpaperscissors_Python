# once your code above is working copy it to this cell and make it more interactive

import random

def name_to_number3(name):
    # delete the following pass statement and fill in your code below
    options={"rock":0,"paper":1,"scissors":2}
    return options[name]

def number_to_name3(number):
    # delete the following pass statement and fill in your code below
    options={0:"rock",1:"paper",2:"scissors"}
    return options[number]

def choice3():
    player_choice = input("rock , paper,scissors\n")
    # print a blank line to separate consecutive games
    print("Player chooses {}\n".format(player_choice))
    # print out the message for the player's choice
    player_num = name_to_number3(player_choice)
    # convert the player's choice to player_number using the function name_to_number()
    comp_number = random.randint(0,2)
    # compute random guess for comp_number using random.randrange() or random.randint()
    comp_choice = number_to_name3(comp_number)
    # convert comp_number to comp_choice using the function number_to_name()
    print("Computer chooses {}\n".format(comp_choice))
    # print out the message for computer's choice
    dif = (player_num - comp_number)%3
    # compute difference of comp_number and player_number modulo five
    # use if/elif/else to determine winner, print winner message
    if(dif==0):
        print("It's a tie\n")
    elif (dif<2):
        print("Player wins\n")
    else:
        print("Computer Wins\n")


def name_to_number5(name):
    # delete the following pass statement and fill in your code below
    options={"rock":0,"Spock":1,"paper":2,"lizard":3,"scissors":4}
    return options[name]
    # convert name to number using a dictionary
    # don't forget to return the result!



def number_to_name5(number):
    # delete the following pass statement and fill in your code below
    options={0:"rock",1:"Spock",2:"paper",3:"lizard",4:"scissors"}
    return options[number]

    # convert number to a name using a dictionary
    # don't forget to return the result!


def choice5():
    player_choice = input("rock , Spock, paper,lizard,scissors\n")
    # print a blank line to separate consecutive games
    print("Player chooses {}\n".format(player_choice))
    # print out the message for the player's choice
    player_num = name_to_number5(player_choice)
    # convert the player's choice to player_number using the function name_to_number()
    comp_number = random.randint(0,4)
    # compute random guess for comp_number using random.randrange() or random.randint()
    comp_choice = number_to_name5(comp_number)
    # convert comp_number to comp_choice using the function number_to_name()
    print("Computer chooses {}\n".format(comp_choice))
    # print out the message for computer's choice
    dif = (player_num - comp_number)%5
    # compute difference of comp_number and player_number modulo five
    # use if/elif/else to determine winner, print winner message
    if(dif==0):
        print("It's a tie\n")
    elif ((dif>0)and(dif<3)):
        print("Player wins\n")
    else:
        print("Computer Wins\n")
    
    

def name_to_number7(name):
    # delete the following pass statement and fill in your code below
    options={"rock":0,"fire":1,"scissors":2,"sponge":3,"paper":4,"air":5,"water":6}
    return options[name]
    # convert name to number using a dictionary
    # don't forget to return the result!



def number_to_name7(number):
    # delete the following pass statement and fill in your code below
    options={0:"rock",1:"fire",2:"scissors",3:"sponge",4:"paper",5:"air",6:"water"}
    return options[number]

    # convert number to a name using a dictionary
    # don't forget to return the result!


def choice7():
    player_choice = input("rock , fire,scissors,sponge, paper,air,water\n")
    # print a blank line to separate consecutive games
    print("Player chooses {}\n".format(player_choice))
    # print out the message for the player's choice
    player_num = name_to_number7(player_choice)
    # convert the player's choice to player_number using the function name_to_number()
    comp_number = random.randint(0,6)
    # compute random guess for comp_number using random.randrange() or random.randint()
    comp_choice = number_to_name7(comp_number)
    # convert comp_number to comp_choice using the function number_to_name()
    print("Computer chooses {}\n".format(comp_choice))
    # print out the message for computer's choice
    dif = (player_num - comp_number)%7
    # compute difference of comp_number and player_number modulo five
    # use if/elif/else to determine winner, print winner message
    print(dif)
    if(dif==0):
        print("It's a tie\n")
    elif (dif>3):
        print("Player wins\n")
    else:
        print("Computer Wins\n")


def name_to_number15(name):
    # delete the following pass statement and fill in your code below
    options={"rock":0,"fire":1,"scissors":2,"snake":3,"human":4,"tree":5,"wolf":6,"sponge":7,"paper":8,"air":9,"water":10,"dragon":11,"devil":12,"lightning":13,"gun":14}
    return options[name]
    # convert name to number using a dictionary
    # don't forget to return the result!



def number_to_name15(number):
    # delete the following pass statement and fill in your code below
    options={0:"rock",1:"fire",2:"scissors",3:"snake",4:"human",5:"tree",6:"wolf",7:"sponge",8:"paper",9:"air",10:"water",11:"dragon",12:"devil",13:"lightning",14:"gun"}
    return options[number]

    # convert number to a name using a dictionary
    # don't forget to return the result!


def choice15():
    player_choice = input("rock , fire,scissors,snake,human,tree,wolf,sponge,paper,air,water,dragon,devil,lightning,gun\n")
    # print a blank line to separate consecutive games
    print("Player chooses {}\n".format(player_choice))
    # print out the message for the player's choice
    player_num = name_to_number15(player_choice)
    # convert the player's choice to player_number using the function name_to_number()
    comp_number = random.randint(0,14)
    # compute random guess for comp_number using random.randrange() or random.randint()
    comp_choice = number_to_name15(comp_number)
    # convert comp_number to comp_choice using the function number_to_name()
    print("Computer chooses {}\n".format(comp_choice))
    # print out the message for computer's choice
    dif = (player_num - comp_number)%15
    # compute difference of comp_number and player_number modulo five
    # use if/elif/else to determine winner, print winner message
    print(dif)
    if(dif==0):
        print("It's a tie\n")
    elif (dif>7):
        print("Player wins\n")
    else:
        print("Computer Wins\n")


def rps():

    print("")
    which = int(input("Which of the four variants do you want to play (the original 3 choices version, the 5 choices RPSLS, the 7 choices or the 15 choices versions?\n"))
    long = int(input("How many rounds do you want to play?\n"))
    if(which == 5):
        for i in range(long):
            choice5()
    elif(which == 3):
        for i in range(long):
            choice3()
    elif (which == 7):
        for i in range(long):
            choice7()
    elif (which == 15):
        for i in range(long):
            choice15()


rps()





