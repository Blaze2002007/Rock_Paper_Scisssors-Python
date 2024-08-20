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

# Write your code below this line 👇


print("Welcome to the Rock, Paper, Scissors game!")
choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
if choice == "0":
    print("You choose Rock")
    print(rock)
    random_choice = random.randint(0, 2)
    print(f"Computer choose {random_choice}")
    if random_choice == 0:
        print(rock)
        print("Its draw")
    elif random_choice == 1:
        print(paper)
        print("You Lose")
    elif random_choice == 2:
        print(scissors)
        print("You Win")
if choice == "1":
    print("You choose Paper")
    print(paper)
    random_choice = random.randint(0, 2)
    print(f"Computer choose {random_choice}")
    if random_choice == 0:
        print(rock)
        print("You win")
    elif random_choice == 1:
        print(paper)
        print("Its draw")
    elif random_choice == 2:
        print(scissors)
        print("You lose")
if choice == "2":
    print("You choose scissors")
    print(scissors)
    random_choice = random.randint(0, 2)
    print(f"Computer choose {random_choice}")
    if random_choice == 0:
        print(rock)
        print("You lose")
    elif random_choice == 1:
        print(paper)
        print("You win")
    elif random_choice == 2:
        print(scissors)
        print("Its draw")




