import random as rd
import colorama

choices = ["rock", "paper", "scissor"]

print(colorama.Style.BRIGHT, colorama.Fore.GREEN + "\n\nPLAY ROCK PAPER SCISSOR : \n\n" + colorama.Fore.WHITE)
a = input(colorama.Fore.RED + "Y/n\n").strip().lower()

if a not in ("", "y", "yes"):
    print("selected not to play")
else:
    while True:
        random_ch = rd.choice(choices)
        user_choice = input(
            colorama.Fore.YELLOW
            + "rock(1), paper(2), or scissor(3) (write your choice)\n\n"
        )

        try:
            g = int(user_choice)
        except ValueError:
            print(colorama.Fore.RED + "Invalid input. Please choose 1, 2, or 3.\n")
            continue

        if g == 1 and random_ch == "scissor" or g == 2 and random_ch == "rock" or g == 3 and random_ch == "paper":
            print(colorama.Fore.GREEN + "you win")
        elif g == 1 and random_ch == "rock" or g == 2 and random_ch == "paper" or g == 3 and random_ch == "scissor":
            print(colorama.Fore.WHITE + "draw")
        else:
            print(colorama.Fore.RED + "you loose\n")

        ret = input(colorama.Style.DIM + "press enter to retry")
        if ret != "":
            break
print(colorama.Fore.WHITE)
 