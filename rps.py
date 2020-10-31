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
win_counter = 0
draw_counter = 0
loss_counter = 0
total_matches = 0

def main():
    global win_counter
    global draw_counter
    global loss_counter

    cls()
    print(f"{prefix}\n")
    print(f"Total: {total_matches}")
    print(f"Wins: {win_counter} | Draws: {draw_counter} | Losses: {loss_counter}\n")

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

    if choice == "rock" and comp == "scissors":
        print(f"You: {choice}\n\nvs.\n\nComputer: {comp}")
        print("\n\nResults: You win.")
        sleep()
        win_counter += 1
        main()
    
    elif choice == "paper" and comp == "rock":
        print(f"You: {choice}\n\nvs.\n\nComputer: {comp}")
        print("\n\nResults: You win.")
        sleep()
        win_counter += 1
        main()

    elif choice == "scissors" and comp == "paper":
        print(f"You: {choice}\n\nvs.\n\nComputer: {comp}")
        print("\n\nResults: You win.")
        sleep()
        win_counter += 1
        main()
        
    elif choice == comp:
        print(f"You: {choice}\n\nvs.\n\nComputer: {comp}")
        print("\n\nResults: Draw.")
        sleep()
        draw_counter += 1
        main()

    else:
        print(f"You: {choice}\n\nvs.\n\nComputer: {comp}")
        print("\n\nResults: You lose.")
        sleep()
        loss_counter += 1
        main()

main()