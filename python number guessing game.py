#write a python pattern where computer generated random to 1-10 teh user has to guess the number the program should give hints like to high or to low until correct guess is made.
import random as r
num = r.randint(1, 10)   
while True:
    n = int(input("Enter your guess: "))
    if n == num:
        print("Correct! You guessed the number.")
        break
    elif n > num:
        print("Too high")
    else:
        print("Too low")