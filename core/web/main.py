import os
import time
from colorama import Fore,Back,Style

def menu():
    print(Fore.BLUE+"""
        
        [+] VOID [+]

        [M] Main
        [1] Nmap Scan
        [2] Nikto Scan
        [3] SQLMap Scan

    """)


def web():
    os.system("clear")

    menu()
    n = input(Fore.RED+"[+] Please Select : ")
    if n=="1":
        os.system("sudo python3 ./core/web/nmap.py")
    if n=="2":
        os.system("sudo python3 ./core/web/nikto.py")
    if n=="3":
        os.system("sudo python3 ./core/web/sqlmap.py")
    if n=="M" or n == "m":
        os.system("sudo python3 main.py")


if __name__ == "__main__":
    web()