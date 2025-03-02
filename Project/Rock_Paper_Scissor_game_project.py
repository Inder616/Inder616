import random

ascii_art = {
    "Rock": """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """,
    "Paper": """
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """,
    "Scissor": """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """
}

user = int(input("What do you choose ? write 0 For Rock, 1 For Paper or 2 For Scissor: "))

if user not in [0, 1, 2]:
    print("Invalid input. Please enter 0 for Rock, 1 for Paper, or 2 for Scissor.")
    exit()

computer = random.randint(0, 2)

choices = ["Rock", "Paper", "Scissor"]

print(f"You chose {choices[user]}")
print(ascii_art[choices[user]])

print(f"Computer chose {choices[computer]}")
print(ascii_art[choices[computer]])

if user == computer:
    print("It's a tie!")
elif (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
    print("You won!")  
else:
    print("You lost!")
