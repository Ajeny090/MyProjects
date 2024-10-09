import random

from selenium.webdriver.common.devtools.v127.fetch import continue_response

print("Welcome to the game of guessing a number")
response = input("Do you want to play the game, YES or No? ").lower()

if response == "yes":
    print("Go ahead")
else:
    print("Thank you, you can play another time.")
    exit()

min = 1
max = 7

number = random.randint(1,100)
print("You have 7 attempts to answer the question.")
while min < max:
    guess = int(input("Enter a number between 1 to 100: "))
    if guess < number:
        print("Your guess is low, try again!")
    elif guess > number:
        print("Your guess is above, try again!")
    elif guess == number:
        print("Congratulation, you won !!!")
    min+=1
    remaining = max - min
    print("The remaining attempts is", remaining)

print("You exceeded your attempts, try again later.")
