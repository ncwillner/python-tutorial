# DECISION GAME
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "help":
        print("""
- start: start car
- stop: stop car
- quit : exit
           """)
    elif command == 'start':
        if started:
            print("car is already started!")
        else:
            started = True
            print("car started...")
    elif command == 'stop':
        if not started:
             print("car is already stopped...")
        else:
            started = False
            print("car stopped.")
    elif command == 'quit':
        print('EXIT, bye')
        break
    else:
        print("i don't understand...")