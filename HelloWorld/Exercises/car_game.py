help = "start = The car gets started. \nstop = The car stops. \nquit = The user quits the game." 
while help.lower() != "hello":
    user_input = input("> ")
    if user_input == "help" or user_input == "HELP":
        print (help)
    elif user_input == "start":
        print("Yay the car has started.")
    elif user_input == "stop":
        print("The car has been stopped.")
    elif user_input == "quit":
        break
    else:
        print("I dont understand that.....")
        
