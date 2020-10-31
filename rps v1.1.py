from os import system
import time
import random

# made by splars#1252

system("title rps v1.1")
system("color c")
rps = ["rock", "paper", "scissors"]

prefix = "game made by splars#1252\nrps game v1.1"
spacer = "\n"

def main():
    system("cls")
    print(prefix)
    print(spacer)

    print("Rock")
    print("Paper")
    print("Scissors")

    x = input("\n>> ").lower()
    comp = random.choice(rps)

    if x == "rock" and comp == "scissors":
        print("You: " + str(x) + "\n\nvs\n\n" + "Computer: " + str(comp))
        print("\n\nResults: You win.")
        time.sleep(3)
        main()
    
    elif x == "paper" and comp == "rock":
        print("You: " + str(x) + "\n\nvs\n\n" + "Computer: " + str(comp))
        print("\n\nResults: You win.")
        time.sleep(3)
        main()

    elif x == "scissors" and comp == "paper":
        print("You: " + str(x) + "\n\nvs\n\n" + "Computer: " + str(comp))
        print("\n\nResults: You win.")
        time.sleep(3)
        main()
        
    elif x == comp:
        print("You: " + str(x) + "\n\nvs\n\n" + "Computer: " + str(comp))
        print("\n\nResults: Draw.")
        time.sleep(3)
        main()

    else:
        print("You: " + str(x) + "\n\nvs\n\n" + "Computer: " + str(comp))
        print("\n\nResults: You lose.")
        time.sleep(3)
        main()

main()