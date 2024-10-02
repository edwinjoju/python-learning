from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# Pick a random number from 1 to 3
num = randint(1,3)

# Turn that random number into the computer's RPS move
if num == 1:
    c_move= "rock"
elif num ==2:
    c_move= "paper"
elif num == 3:
    c_move = "scissors"

# Ask a user to enter their move

user = input("Enter you move: ")
# Print the rock, paper, or scissors ASCII art that corresponds to the player's move
print("-------------------USER-------------------")
if(user=="rock"):
    print(rock)
elif(user=="paper"):
    print(paper)
elif(user=="scissors"):
    print(scissors)

# Print the rock, paper, or scissors ASCII art that corresponds to the computer's move
print("-------------------COMPUTER-------------------")
if c_move =="rock":
    print(rock)
elif c_move =="paper":
    print(paper)
elif c_move =="scissors":
    print(scissors)
# Figure out who wins and print the result!

if(c_move==user):
    print("draw")
elif user=="rock" and c_move=="paper":#paper
    print("Computer Wins")
elif user =="paper" and c_move == "rock":#rock
    print("user wins")
elif user =="scissors" and c_move == "rock":#rock
    print("Computer Wins")
elif user =="rock" and c_move == "scissors":#scissors
    print("User Wins")
elif user == "scissor" and c_move == "paper":
    print("User Wins")
elif user =="paper" and c_move =="scissors":
        print("Computer wins")
