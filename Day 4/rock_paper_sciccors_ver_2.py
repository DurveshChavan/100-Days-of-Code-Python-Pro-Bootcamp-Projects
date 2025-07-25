import random

rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    Rock
'''

paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    Paper
'''

scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    Scissors
'''

# store images in list
game_images = [rock, paper, scissors]

# generate random choice for computer
computer_choice = random.randint(0, 2)

# Greetings and prompt for input
print('''
██████   ██████   ██████ ██   ██     ██████   █████  ██████  ███████ ██████      ███████  ██████ ██ ███████ ███████  ██████  ██████  ███████ 
██   ██ ██    ██ ██      ██  ██      ██   ██ ██   ██ ██   ██ ██      ██   ██     ██      ██      ██ ██      ██      ██    ██ ██   ██ ██      
██████  ██    ██ ██      █████       ██████  ███████ ██████  █████   ██████      ███████ ██      ██ ███████ ███████ ██    ██ ██████  ███████ 
██   ██ ██    ██ ██      ██  ██      ██      ██   ██ ██      ██      ██   ██          ██ ██      ██      ██      ██ ██    ██ ██   ██      ██ 
██   ██  ██████   ██████ ██   ██     ██      ██   ██ ██      ███████ ██   ██     ███████  ██████ ██ ███████ ███████  ██████  ██   ██ ███████ 
''')
users_choice = int(input("What do you choose?\n    1 for Rock.\n    2 for Paper.\n    3 for Scissors.\n    : "))

# logical Corrections
users_choice -= 1

#  Create image for users choice
if 0 <= users_choice < 3:
    print(game_images[users_choice])
else:
    print('''You typed an invalid choice.
          
        You

        ██╗      ██████╗  ██████╗ ███████╗███████╗
        ██║     ██╔═══██╗██╔═══██╗██╔════╝██╔════╝
        ██║     ██║   ██║██║   ██║███████╗█████╗  
        ██║     ██║   ██║██║   ██║╚════██║██╔══╝  
        ███████╗╚██████╔╝╚██████╔╝███████║███████╗
        ╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
    ''')
    exit(1)

# Create image for computers choice
print(f"Computer chose: {computer_choice}\n{game_images[computer_choice]}")

# Game Logic
if users_choice == computer_choice:
    print('''It's a 

        ██████╗ ██████╗  █████╗ ██╗    ██╗
        ██╔══██╗██╔══██╗██╔══██╗██║    ██║
        ██║  ██║██████╔╝███████║██║ █╗ ██║
        ██║  ██║██╔══██╗██╔══██║██║███╗██║
        ██████╔╝██║  ██║██║  ██║╚███╔███╔╝
        ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ 
    ''')
elif users_choice == 0 and computer_choice == 2:
    print('''You

        ██╗    ██╗██╗███╗   ██╗██╗
        ██║    ██║██║████╗  ██║██║
        ██║ █╗ ██║██║██╔██╗ ██║██║
        ██║███╗██║██║██║╚██╗██║╚═╝
        ╚███╔███╔╝██║██║ ╚████║██╗
         ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝
    ''')
elif users_choice == 2 and computer_choice == 0:
    print('''You

        ██╗      ██████╗  ██████╗ ███████╗███████╗
        ██║     ██╔═══██╗██╔═══██╗██╔════╝██╔════╝
        ██║     ██║   ██║██║   ██║███████╗█████╗  
        ██║     ██║   ██║██║   ██║╚════██║██╔══╝  
        ███████╗╚██████╔╝╚██████╔╝███████║███████╗
        ╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
    ''')
elif users_choice > computer_choice:
    print('''You

        ██╗    ██╗██╗███╗   ██╗██╗
        ██║    ██║██║████╗  ██║██║
        ██║ █╗ ██║██║██╔██╗ ██║██║
        ██║███╗██║██║██║╚██╗██║╚═╝
        ╚███╔███╔╝██║██║ ╚████║██╗
         ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝
    ''')
elif users_choice < computer_choice:
    print('''You

        ██╗      ██████╗  ██████╗ ███████╗███████╗
        ██║     ██╔═══██╗██╔═══██╗██╔════╝██╔════╝
        ██║     ██║   ██║██║   ██║███████╗█████╗  
        ██║     ██║   ██║██║   ██║╚════██║██╔══╝  
        ███████╗╚██████╔╝╚██████╔╝███████║███████╗
        ╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
    ''')
else:
    print("Error!")
