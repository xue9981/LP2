inp=int(input("I'm thinking of a number! Try to guess the number I'm thinking of:"))
str='yes'
answer=42
while str=='yes':
    if inp > answer:
        inp=int(input("Too low! Guess again:"))
    elif inp < answer:
        inp=int(input("Too high! Guess again:"))
    else:
        str=input("That's it! Would you like to play again? (yes/no):")

print("Thank for playing!")
