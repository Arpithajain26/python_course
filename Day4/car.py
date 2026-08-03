
command=""
started=False
while True:
    command=input("")
    if command.lower()=="start":
        if started:
            print("car is already started")
        else:
            started=False
        
        print("car started")
    elif command.lower()=="stop":
        print("car stopped")
    elif command=='quit':
        break
    elif command=='help':
        print("""
start-to start the car
stop- to stop the car
quit-to quit """)
    else:
        print("sorry,I dont understand that")