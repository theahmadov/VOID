import os
import time
from colorama import Fore,Back,Style

def menu():
    print(Fore.BLUE+"""
    
        [+] VOID [+]

        [M] Menu
        [1] Zip Brute Forcer
    """)


def zip(path):
    print(" ")
    print(Fore.BLUE+"[+] Starting Zip Brute Forcer...")
    time.sleep(1)
    os.system(f"sudo john --format=zip {path}")
    print(" ")

def john():
    os.system("clear")

    menu()
    n = input(Fore.RED+"[+] Please Select : ")
    if n=="1":
        path = input(Fore.RED+"[+] Please input zip path : ")
        zip(path)
    if n=="M" or n == "m":
        os.system("sudo python3 main.py")


if __name__ == "__main__":
    john()