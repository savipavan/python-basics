number = 25
running = True
print('print 0 to exit')

while running:
    guess = int(input("Enter the number: "))
    if guess == number:
        print("Congratulations, you guessed it.")
        running = False
    elif guess == 0:
        break
    elif guess < number:
        print("No, it is a little higher than that")
    else:
        print("No, it is a little lower than that")
else:
    print('game over')