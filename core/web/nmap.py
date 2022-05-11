import os
import time
from colorama import Fore,Back,Style

def menu():
    print(Fore.BLUE+"""
        
        [+] VOID [+]

        [M] Main
        [1] Port Scanner
        [2] Vulnerability Scanner
        [3] OS (Operating System) Scanner

    """)

def portscanner(url):
    print(" ")
    print(Fore.BLUE+"[+] Starting Port Scanner...")
    time.sleep(1)
    os.system(f"sudo nmap -oN output.txt {url}")
    print(" ")
    print(Fore.RED+"[+] Output saved to output.txt file!")
    print(" ")

def vuln(url):
    print(" ")
    print(Fore.BLUE+"[+] Starting Vulnerability Scanner...")
    time.sleep(1)
    os.system(f"sudo nmap -sV -oN output.txt {url}")
    print(" ")
    print(Fore.RED+"[+] Output saved to output.txt file!")
    print(" ")

def oss(url):
    print(" ")
    print(Fore.BLUE+"[+] Starting OS (Operating System) Scanner...")
    time.sleep(1)
    os.system(f"sudo nmap -A -T4 -oN output.txt {url}")
    print(" ")
    print(Fore.RED+"[+] Output saved to output.txt file!")
    print(" ")

def nmap():
    os.system("clear")
    menu()
    n = input(Fore.RED+"[+] Please Select : ")
    if n=="1":
        url = input(Fore.BLUE+"[+] Please input url to port scanner (without https://) : ")
        portscanner(url)
    elif n=="2":
        url = input(Fore.BLUE+"[+] Please input url to vulnerability scanner (without https://) : ")
        vuln(url)
    elif n=="3":
        url = input(Fore.BLUE+"[+] Please input url to os scanner (without https://) : ")
        oss(url)
    elif n=="M" or n == "m":
        os.system("sudo python3 main.py")


if __name__ == "__main__":
    nmap()