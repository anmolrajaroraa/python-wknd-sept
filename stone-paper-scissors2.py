import random

gameChoices = ["stone", "paper", "scissors"]

cpuScore = 0
userScore = 0
draw = 0

while True:
    print("Stone Paper Scissors".center(100))

    #print("Score -> User : {}, CPU : {}, Draw : {}, Total matches played : {}".format(userScore, cpuScore, draw, userScore + cpuScore + draw).center(100))
    print(f"Score -> User : {userScore}, CPU : {cpuScore}, Draw : {draw}, Total matches played : {userScore + cpuScore + draw}".center(100 ) )

    if cpuScore == 3 or userScore == 3:
        print("Game Finish!")
        break

    print('''
    1. Stone
    2. Paper
    3. Scissors''')
    userInput = int(input("Enter your choice : "))
    userInput -= 1
    userInput = gameChoices[userInput]

    if userInput not in gameChoices:
        print("Invalid choice")
        continue

    cpuInput = random.choice(gameChoices)
    print(cpuInput)

    if userInput == cpuInput:
        print("Game draw!")
        draw += 1
        continue

    if userInput == "stone":
        if cpuInput == "paper":
            print("Cpu won")
            # cpuScore = cpuScore + 1
            cpuScore += 1
        else:
            print("User won")
            userScore += 1


    elif userInput == "paper":
        if cpuInput == "stone":
            print("User won")
            userScore += 1
        else:
            print("Cpu won")
            cpuScore += 1

    else:
        if cpuInput == "stone":
            print("Cpu won")
            cpuScore += 1
        else:
            print("User won")
            userScore += 1
