import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


choice = int(input("What do you choose? Type '0' for Rock, '1' for Paper or '2' for Scissors: "))

if choice > 2 or choice < 0:
  print("You chose the wrong number. Try again!")
  exit()

game_list = [rock, paper, scissors]

your_choice = game_list[choice]

computer_random = random.randint(0, 2)
computer_choice = game_list[computer_random]

print(f"You chose: \n {your_choice}")
print(f"The computer chose: \n {computer_choice}")


if choice == 0 and computer_random == 1:
  print("You lose")
elif choice == 0 and computer_random == 2:
  print("You win")
elif choice == 1 and computer_random == 0:
  print("You win")
elif choice == 1 and computer_random == 2:
  print("You lose")
elif choice == 2 and computer_random == 0:
  print("You lose")
elif choice == 2 and computer_random == 1:
  print("You win")
else:
  print("Its a draw")