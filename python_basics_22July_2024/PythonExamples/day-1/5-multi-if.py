number = 25
guess = int(input("Enter the number: "))

if guess == number:
    print("Congratulations, you guessed it.")
elif guess < number:
    print("No, it is a little higher than that")
else:
    print("No, it is a little lower than that")
print("Done")