command = ""
started = False
while True :
   command = input(">> ").lower()
   if command == "start" :
      if started :
         print("The car already started!!")
      else : 
         started = True
         print ("The car is starting...")
   elif command == "stop" :
      if not started :
         print("The car already stopped!!")
      else:
         started = False
         print("The car is stopping...")
   elif command == "help" :
      print("Start - to start the car")
      print("Stop - to stop the car")
      print("Quit - to quit the car")
   elif command == "quit" :
      print("Closing the game. Good bye😇")
      break 
   else:
      print("Sorry I don't understand that")
    