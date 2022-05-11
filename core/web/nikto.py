import os
import time
from colorama import Fore,Back,Style

def menu():
    print(Fore.BLUE+"""
        
        [+] VOID [+]

        [M] Main
        [1] Scan a Domain with SSL Enabled

    """)

def ssl(url):
    print(" ")
    print(Fore.BLUE+"[+] Scanning A Domain With SSL Enabled...")
    time.sleep(1)
    os.system(f"sudo nikto -h {url} -ssl")
    print(" ")

def nikto():
    os.system("clear")

    menu()
    n = input(Fore.RED+"[+] Please Select : ")
    if n=="1":
        url = input(Fore.RED+"[+] Please input url to domain scanner (without https://) : ")
        ssl(url)
    if n=="2":
        os.system("sudo python3 ./core/web/nikto.py")
    if n=="M" or n == "m":
        os.system("sudo python3 main.py")


if __name__ == "__main__":
    nikto()