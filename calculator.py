import platform
import os

def Calculator():
    print("""

     #####   #####   #       #####  #     #  #        #####   #######  #####   ######
    #       #     #  #      #       #     #  #       #     #     #    #     #  #     #
    #       #######  #      #       #     #  #       #######     #    #     #  ######
    #       #     #  #      #       #     #  #       #     #     #    #     #  #     #
     #####  #     #  ######  #####   #####   ######  #     #     #     #####   #      #

                                                                    Made By: Saad Ahmed
    """)

    X = "#" * 31
    Y = "=" * 29
    global greeting
    greeting = " " + X + "\n# " + Y + " #\n#  Thanks For Using Calculator  #\n# " + Y + " #\n " + X

    userX = int(input("Enter 1st No: "))
    userY = int(input("Enter 2nd No: "))

    print("\nPlease Enter Operator\n\n\t 1 = +\n\t 2 = -\n\t 3 = x \n\t 4 = /\n")

    operator = int(input("_: "))

    if (operator == 1):
        print("\n\t Result => {} \n".format(userX + userY))

    elif (operator == 2):
        print("\n\t Result => {} \n".format(userX - userY))

    elif (operator == 3):
        print("\n\t Result => {} \n".format(userX * userY))

    elif (operator == 4):
        print("\n\t Result => {} \n".format(userX / userY))

Calculator()

def runAgain():
    userInput = input("Want To Run Again Y/n: ")
    if (userInput == "y" or userInput == "Y"):
        if(platform.system() == "Linux"):
            print(os.system('clear'))
        else:
            print(os.system('cls'))
        Calculator()
        runAgain()
    else:
        print("\n"+greeting+"\n")

runAgain()