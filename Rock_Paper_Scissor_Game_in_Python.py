##################### Day 4 project: Developing a Rock, Paper, Scissor Game in PYthon#################


#importing module
import random

#Welcome message for Player in game

print("Welcome to the Rock, Paper, Scissors Game!")

player_name = input("Write your name first : ")
# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


comp_choice = [rock,paper,scissors]

#Player input
player_choose = int(input("Which one you choose? 0 for ROCK, 1 for PAPER, 2 for SCISSORS: "))

#Computer input
comp_choose = random.randint(0,2)


#Conditions and Results

#If both the player and the computer choose the same option, it's a tie.
if player_choose == comp_choose:
    print(f"{player_name} you choose {comp_choice[player_choose]}.")
    print(f"Computer choose {comp_choice[comp_choose]}.")
    print("GAME TIE!")

#Rock beats Scissors(Rock crushes Scissors)
elif player_choose == 0 and comp_choose == 2:
    print(f"{player_name} you choose {comp_choice[player_choose]}.")
    print(f"Computer choose {comp_choice[comp_choose]}.")
    print(f"{player_name} you win!")

#Paper beats Rock(Paper covers Rock)
elif player_choose == 0 and comp_choose == 1:
    print(f"You choose {comp_choice[player_choose]}.")
    print(f"Computer choose {comp_choice[comp_choose]}.")
    print("Computer win!")

#Scissors beats Paper(Scissors cut Paper)
elif player_choose == 1 and comp_choose == 2:
    print(f"You choose {comp_choice[player_choose]}.")
    print(f"Computer choose {comp_choice[comp_choose]}.")
    print("Computer win!")

#Paper beats Rock(Paper covers Rock)
elif player_choose == 1 and comp_choose == 0:
    print(f"{player_name} you choose {comp_choice[player_choose]}.")
    print(f"Computer choose {comp_choice[comp_choose]}.")
    print(f"{player_name} you win!")

#Rock beats Scissors(Rock crushes Scissors)
elif player_choose == 2 and comp_choose == 0:
    print(f"You choose {comp_choice[player_choose]}.")
    print(f"Computer choose {comp_choice[comp_choose]}.")
    print("Computer win!")

#Scissors beats Paper(Scissors cut Paper)
elif player_choose == 2 and comp_choose == 1:
    print(f"{player_name} you choose {comp_choice[player_choose]}.")
    print(f"Computer choose {comp_choice[comp_choose]}.")
    print(f"{player_name} you win!")

#For wrong entries
else:
    print(f"{player_name} you choose a wrong choice.Try again!")

######Game Over###################
