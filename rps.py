import os
import time
import random

# made by splars#1252
cls = lambda: os.system("cls" if os.name == "nt" else "clear")
os.system("title rps v1.2" if os.name == "nt" else "pass")
os.system("color c" if os.name == "nt" else "pass")

rps = ["rock", "paper", "scissors"]

prefix = "rps game made by splars#1252\nrps game v1.2"

def main():
    os.system("cls")
    print(f"{prefix}\n")

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