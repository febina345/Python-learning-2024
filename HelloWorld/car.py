command = ""
started=False
while True:
    command = input("> ").lower()
    if command == "help":
        print("""
start - car started
stop- car stopped 
quit -To quit
        """)
    elif command == "start":
        if started:
            print("car started already")
        else:
            started=True
            print("car started")
    elif command == "stop":
        if not started:
            print("car stopped already")
        else:
            started=False
            print("Car stopped")
    elif command == "quit":
        break
    else:
        print("sorry I don't understand ")




