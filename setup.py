import os


def setup():
    os.system("clear")
    print("""
        [+] VOID [-]

        [1] Debian Based Os (Kali Linux,Parrot,Kde)
        [2] Arch Based Os (Arch Linux,Archcraft,ArcoLinux)

    """)
    n = input("[+] Please Select : ")

    if n=="1":
        os.system("sudo bash ./core/debian.sh")
    elif n=="2":
        os.system("sudo bash ./core/arch.sh")
    else:
        print("[-] Please Select Correct One (1 or 2) : ")

if __name__ == "__main__":
    setup()