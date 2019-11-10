import random

gamePositions = list(range(1,10))
availablePositions = list(range(1,10))

# print(gamePositions[8])

userChoice = input("What do you want to use (X or 0) : ")

cpuChoice = "0" if userChoice == "X" else "X"

userTurn = random.choice([True, False])
print("UserTurn is ", userTurn)

gameTurn = 0

while True:

    if gameTurn >= 5:
        if gamePositions[0] == gamePositions[1] == gamePositions[2]:
            print('user won') if gamePositions[0] == userChoice else print("cpu won")

    print( "Next turn is of user" ) if userTurn else print( "Next turn is of cpu" )
    print('''
    {} | {} | {}
    ---------
    {} | {} | {}
    ---------
    {} | {} | {}'''.format(gamePositions[0], gamePositions[1], gamePositions[2], gamePositions[3], gamePositions[4], gamePositions[5], gamePositions[6], gamePositions[7], gamePositions[8]))

    if userTurn:
        userInput = int(input(f"Where do you want to place your {userChoice} : "))
        if userInput not in availablePositions:
            print("Invalid choice")
            continue
        availablePositions.remove(userInput)
        userInput -= 1
        gamePositions[userInput] = userChoice
        gameTurn += 1
        userTurn = False
        continue
    cpuInput = random.choice(availablePositions)
    print("Cpu input is ", cpuInput)
    availablePositions.remove(cpuInput)
    cpuInput -= 1
    gamePositions[cpuInput] = cpuChoice
    gameTurn += 1
    userTurn = True

    # print(gamePositions)