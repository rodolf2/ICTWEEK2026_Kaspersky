import random

print("--- Guess the Number Game ---")
print("I am thinking of a number between 1 and 1000. Can you find it in 10 guesses or less?")
print("-----------------------------")

target = random.randint(1, 1000)
attempt = 0
while(True):
    print(target)
    guess = int(input("Enter your guess:"))
    
    attempt += 1
    if(guess > target):
        print("Result: Lower! ⬇️")
    elif(guess < target):
        print("Result: Higher! ⬆️")
    else:
        break

print("Correct! You found it in "+str(attempt)+" attempts.")