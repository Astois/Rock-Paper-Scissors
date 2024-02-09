def main():
    import random
    RPSO = ("R","P","S")
    while True:
        BOTA = random.choice(RPSO)
        RPSOU = input("Enter (R)Rock, (P)Paper or (S)Scissors: ")
        if RPSOU == BOTA:
            print(f"BOT chose{BOTA}!")
            print("DRAW!")
        elif  RPSOU in ["r", "R"] and BOTA ==  "S":
            print(f"BOT chose {BOTA}!")
            print("YOU WIN!")
        elif  RPSOU in ["s", "S"] and BOTA ==  "R":
            print(f"BOT chose {BOTA}!")
            print("YOU LOSE!")
        elif RPSOU  in ["P", "p"] and BOTA == "R":
            print(f"BOT chose {BOTA}!")
            print("YOU WIN!")
        elif  RPSOU in ["r", "R"] and BOTA ==  "P":
            print(f"BOT chose {BOTA}!")
            print("YOU LOSE!")
        elif  RPSOU in ["s", "S"] and BOTA ==  "P":
            print(f"BOT chose {BOTA}!")
            print("YOU WIN!")
        elif  RPSOU in ["p", "P"] and BOTA ==  "S":
            print(f"BOT chose {BOTA}!")
            print("YOU LOSE!")

        
        PlayAgain = input("Do you want to play again? Y/N: ")
        if PlayAgain not in { "y", "Y",}:
            break
main()

