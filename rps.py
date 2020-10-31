import os
import time
import random

# rps game made by splars#1252
cls = lambda: os.system("cls" if os.name == "nt" else "clear")
sleep = lambda: os.system("timeout 3 >nul" if os.name == "nt" else time.sleep(3))
os.system("title rps game made by splars#1252" if os.name == "nt" else "pass")
os.system("color c" if os.name == "nt" else "pass")

rps = ["rock", "paper", "scissors"]
prefix = "rps game v1.2"

def main():
    cls()
    print(f"{prefix}\n")

    print("A: Rock")
    print("B: Paper")
    print("C: Scissors")

    choice = input("\n>> ").lower()
    if not choice:
        main()

    if choice == "a":
        choice = "rock"
    elif choice == "b":
        choice = "paper"
    elif choice == "c":
        choice = "scissors"

    if choice not in rps:
        print("\nYou did not make a valid selection.")
        sleep()
        main()

    comp = random.choice(rps)

    if   choice == "rock" and comp == "scissors":
        print(f"You: {choice}\n\nvs.\n\nComputer: {comp}")
        print("\n\nResults: You win.")
        sleep()
        main()
    
    elif choice == "paper" and comp == "rock":
        print(f"You: {choice}\n\nvs.\n\nComputer: {comp}")
        print("\n\nResults: You win.")
        sleep()
        main()

    elif choice == "scissors" and comp == "paper":
        print(f"You: {choice}\n\nvs.\n\nComputer: {comp}")
        print("\n\nResults: You win.")
        sleep()
        main()
        
    elif choice == comp:
        print(f"You: {choice}\n\nvs.\n\nComputer: {comp}")
        print("\n\nResults: Draw.")
        sleep()
        main()

    else:
        print(f"You: {choice}\n\nvs.\n\nComputer: {comp}")
        print("\n\nResults: You lose.")
        sleep()
        main()

main()