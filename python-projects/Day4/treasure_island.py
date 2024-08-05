print(
    """
                 .
             |~
            /|\
           |-.-|
           '-:-'
            [|]
            [|]
            [|]
            [|]
            [|]
           .[|].
           :/|\:
           [/|\]
           [/|\]
         .:_#|#_:.
         |_ '-' _|
         /\:-.-:/\
        /\|_[|]_|/\
      _/\|~ [|] ~|/\_
      [''=-.[|].-='']
      :-._   |   _.-:
      //\;::-:-::;/\\
     /\.'-\\/|\//-'./\
   .'\/'   :\|/:   '\/'.
 .//\('    [\|/]    ')/\\.
'':][\.'  .[\|/].  './][:''
    ''    :/\|/\:    ''
         .[\/|\/].
           '.|.'
             '
    """
)
print("""Welcome to Treasure Island!\n
Your mission to find the treasure!\n""")
direction = str(input("What way do you want to go? Type 'Left' or 'Right':\n"))
water_activity = str(input("What do you want to do? \nSwim or Wait:\n"))
door = str(input("Choose what door to pass thru? Red or Blue or Yellow:\n"))

direction = direction.lower()
water_activity = water_activity.lower()
door = door.lower()

if direction == "left":
    print("You have landed on a lake. To get to the Olympic 2024 island, Type: 'Swim' or 'Wait'.\n")

    if water_activity == "wait":
        if door == "red":
            print("You have been burned by fire.\nGame Over!")
        elif door == "blue":
            print("You have been eaten by a beast! \nGame Over!")

        elif door == "yellow":
            print("You Win!!! Here is your treasure!\n")
        else:
            print("You chose a door that doesn't exist. Game Over!\n")
    else:
        print("Game Over! \nYou have been eaten by an angry Trout!\n")
else:
    print(f"Game Over! \nYou fell into a hole!")
