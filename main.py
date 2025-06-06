import random

def results():
    print(f"Player: {player}")
    print(f"Computer: {computer}")

options = ("rock", "paper", "scissors")
player = None

print("------Rock-Paper-Scissors-Game------")
print("---------------------------------------")
while player not in options or player == computer:
    computer = random.choice(options)
    player = input("Choose between one rock, paper and scissors: ")
    results()

if player == "rock" and computer == "scissors":
    print("You Win!")
elif player == "rock" and computer == "paper":
    print("You Lose!")
elif player == "scissors" and computer == "rock":
    print("You Lose!")
elif player == "scissors" and computer == "paper":
    print("You Win!")
elif player == "paper" and computer == "rock":
    print("You Win!")
elif player == "paper" and computer == "scissors":
    print("You Lose!")
