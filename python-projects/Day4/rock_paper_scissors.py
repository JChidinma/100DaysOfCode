# Create a Rock -> Paper -> Scissors game with ASCII art: https://wrpsa.com/#google_vignette

import random
rock = """
 _____         
| | | |/\       
|_|_|_|\ \       
|        /
\_______/            (  ( ) ) ( )  )
 \______\           ( ( ( ( )  )  ) )
 \       \         ( ( )) ) (   ) ( ( )
  \       \        ( (__.-.___.-.__) )                  R O C K
   \       \        /---._.---._.--- \
    \       \       \||   '  \'    ||/
     \       \       |||     _)   |||
      \       \       ||||///\\\||||
       \       \_____/ ||||\__/||||\___
        \             \ |||||||||| /   \
         \             \  ||||||  /     \
          \_____
"""

paper = """
8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,  
88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8  
88       d8 ,adPPPPP88 88       d8 8PP""""""" 88          
88b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88          
88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88          
88                     88                                 
88                     88     
"""

scissors = """
    _       ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\.
"""

game_images = [rock, paper, scissors]
users_choice = int(input(
    "What do you choose? \nType 0 for 'Rock' or 1 for 'Paper' or 2 for 'Scissors': \n"))
print(game_images[users_choice])

computer_choice = random.randint(0, 2)
print(f"Computer chose: ")
print(game_images[computer_choice])


if users_choice >= 3 or users_choice < 0:
    print("You typed and invalid number. You lose!")
elif users_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and users_choice == 2:
    print("You lose!")
elif users_choice < computer_choice:
    print('You lose!')
elif computer_choice == users_choice:
    print("It's a draw. Keep playing!")
elif users_choice > computer_choice:
    print("You win!")
else:
    print("You lose! Restart the game...")

# there's a small bug
