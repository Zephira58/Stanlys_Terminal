from colorama import Fore, Back, Style
import time, sys, os, keyboard, random

random_milis = random.randint(1,50)
random_milis = str(random_milis)
lower_keys = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
lower_random_key = random.choice(lower_keys)
print(Fore.GREEN,">-Employee #427 Instructional Prompt              v. 1.81.7+")
print("─────────────────────────────────────────────────────────────")
print("---")
print("> Please Press '"+lower_random_key+"' for",random_milis+"ms")

while True:
    if keyboard.read_key() == lower_random_key:
        random_milis = random.randint(1,50)
        random_milis = str(random_milis)
        lower_keys = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        lower_random_key = random.choice(lower_keys)
        display_key = lower_random_key.upper
        print("---")
        print("> Please Press '"+lower_random_key+"' for",random_milis+"ms")
        time.sleep(0.5)