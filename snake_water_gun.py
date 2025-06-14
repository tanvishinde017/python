import random

def snake_water_gun():
    print("Welcome to Snake-Water-Gun Game!")
    print("Choose:\n's' for Snake\n'w' for Water\n'g' for Gun")

    user = input("Your choice (s/w/g): ").lower()
    if user not in ['s', 'w', 'g']:
        print("Invalid input. Please enter s, w, or g.")
        return

    computer = random.choice(['s', 'w', 'g'])

    print(f"\nYou chose: {user.upper()} | Computer chose: {computer.upper()}")

    if user == computer:
        print("Result: It's a draw!")
    elif (user == 's' and computer == 'w') or \
         (user == 'w' and computer == 'g') or \
         (user == 'g' and computer == 's'):
        print("Result: You win! ")
    else:
        print("Result: Computer wins! ")


snake_water_gun()
