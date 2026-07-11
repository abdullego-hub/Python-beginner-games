box = False
coins = 0 
print("Welcome to the Treasure Box Game, where only geniuses survive👾🤖👩‍🏫")
print("You're officially in the zone. Wish you the best")
while True : 
    command = input("=> ").lower()
    if command== "open" :
        if box:
            print("The box is already opened and it's empty😞") 
        else :
            box = True 
            coins+= 10
            print("You found 10 coins")
    elif command == "shake" :
        if not box :
            print("Do you hear anything...")
        else:
            print("The box was already opened!")
    elif command == "leave" :
        if box :
            print("The box is opened already!") 
            break 
        else:
            print("Why not try your luck, the box might contain coins")
    elif command == "check" :
        print(f" You have {coins} coins")
    elif command == "help" :
        print("Open - to open the box")
        print("Shake - to shake the box and find a hint")
        print("Leave - to skip the box")
        print("Check  - to check the coins collected")
        print("Quit - to close the game")
    elif command == "quit" :
        print("Closing the game")
        break
    else :
        print("The game does not support the fucntion you pressed🚨🚩")
        print ("Type help for more information")

            
