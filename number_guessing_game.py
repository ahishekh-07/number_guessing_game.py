import random

#declaring a number guessing introduction
def number_guessing():
    print("hello this is Number guessing game")
    print("choose the Number between 1 to 100")
#giving the target number by the random library50

    target_number = random.randint(1 ,100)
# defining the attempts
    attempt = 10
    print(f"you have only {attempt} to guess the Number")
#using ht nested if for the logic 
    for attempt in range (1,attempt +1):
        guess = int(input(f"attempt {attempt} :guess the NUMBER :-"))
        try:
            if (guess < target_number):
                print("too small! wrong guess")
            elif(guess> target_number):
                print("too big! wrong guess")
            else:
                print(f"congratulations!!,You guessed the {target_number} in {attempt} attempts")
                break
        except ValueError:
            print("pls enter the valid number")

            if attempt == attempt:
                print(f"you are out pf attempt the number was {target_number} ")

number_guessing()                
