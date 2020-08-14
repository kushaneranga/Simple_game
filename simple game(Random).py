import random

random_num = random.randint(1, 100)
print(random_num)
user_num = int(input("Guess an integer number from 1 to 100: "))
guess = []
if 1 <= user_num <= 100:
    guess.append(user_num)
    while user_num != random_num:
        if user_num > random_num:
            print("Try a lower number!!!")
        else:
            print("Try a higher number!!!")
        user_num = int(input("Guess an integer number from 1 to 100: "))
        guess.append(user_num)

    else:
        if len(guess) <= 5:
            print("You have won congrats!!!")
        else:
            print("You have tried " + format(len(guess)) + " times. You lost it.")
else:
    print("Your Value is out of range!!!")
