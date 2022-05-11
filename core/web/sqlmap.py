import os
import time
from colorama import Fore,Back,Style

def menu():
    print(Fore.BLUE+"""
        
        [+] VOID [+]

        [M] Main
        [1] List information about the existing databases 
        [2] List information about tables present in a particular database 

    """)

def listdb(url):
    print(" ")
    print(Fore.BLUE+"[+] Listing information about the existing databases...")
    time.sleep(1)
    os.system(f"sudo sqlmap -u {url} --dbs")
    print(" ")


def listtb(url):
    print(" ")
    print(Fore.BLUE+"[+] Listing information about the Tables present in a particular Database ...")
    time.sleep(1)
    os.system(f"sudo sqlmap -u {url} -D acuart --tables ")
    print(" ")
    
def sql():
    os.system("clear")
    menu()
    n = input(Fore.RED+"[+] Please Select : ")
    if n=="1":
        url = input(Fore.RED+"[+] Please input url to list information of existing databases : ")
        listdb(url)
    elif n=="2":
        url = input(Fore.RED+"[+] Please input url to list information of existing databases : ")
        listtb(url)

    elif n=="M" or n == "m":
        os.system("sudo python3 main.py")


if __name__ == "__main__":
    sql()