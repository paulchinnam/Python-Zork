room = 1
print("--------------------------------")
print("Welcome to Zork")

while True:
    while room == 1:
        if room == 1:
            print("--------------------------------")
            print("You are standing in an open field west of a white house, with a boarded front door.")
            print("(A secret path leads southwest into the forest.")
            print("There is a Small Mailbox.")
            second = input("What do you do? ")
        if second.lower() == "open mailbox":
            print("--------------------------------")
            print("Opening the mailbox reveals a leaflet")
        elif second.lower() == "take mailbox":
            print("--------------------------------")
            print("the mailbox is securely fastened")
        elif second.lower() == ("go east"):
	    print("---------------------------------------------------------")
	    print("The door is boarded and you cannot remove the boards.")
	elif second.lower() == ("open door"):
	    print("---------------------------------------------------------")
	    print("The door cannot be opened.")
	elif second.lower() == ("take boards"):
	    print("---------------------------------------------------------")
	    print("The boards are securely fastened.")
	elif second.lower() == ("look at house"):
	    print("---------------------------------------------------------")
	    print("The house is a beautiful colonial house which is painted white. It is clear that the owners must have been extremely wealthy.")
	elif second.lower() == ("go southwest"):
	    room = 2
	elif second.lower() == ("read leaflet"):
	    print("---------------------------------------------------------")
	    print("Welcome to the Unofficial Python Version of Zork. Your mission is to find a Jade Statue.")
	else:
	    print("---------------------------------------------------------")
    while room == 2:
        if room == 2:
            print("---------------------------------------------------------")
            print("This is a forest, with trees in all directions. To the east, there appears to be sunlight.")
	    forest_inp = input("What do you do? ")
        if forest_inp.lower() == ("go west"):
	    print("---------------------------------------------------------")
	    print("You would need a machete to go further west.")
	elif forest_inp.lower() == ("go north"):
	    print("---------------------------------------------------------")
	    print("The forest becomes impenetrable to the North.")
	elif forest_inp.lower() == ("go south"):
	    print("---------------------------------------------------------")
	    print("Storm-tossed trees block your way.")
	elif forest_inp.lower() == ("go east"):
	    room = 3
	else:
	    print("---------------------------------------------------------")
    while room == 3:
        if room == 3:
            last_inp = ("What do you want to do? ")
        if last_inp.lower() == 'open trunk':
            print("You found the statue and completed your quest")
        else:
            print("---------------------------------------------------------")


        exit_inp = input("do you want to exit the game? ")
        if exit_inp == 'yes':
            exit()
        else:
            room = 1
