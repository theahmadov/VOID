# Nmap Scan Tutorial

## Port Scanner

### Function Code

```py
def portscanner(url):
    print(" ")
    print(Fore.BLUE+"[+] Starting Port Scanner...")
    time.sleep(1)
    os.system(f"sudo nmap -oN output.txt {url}")
    print(" ")
    print(Fore.RED+"[+] Output saved to output.txt file!")
    print(" ")
```

### Command Guide
In Nmap we use `sudo nmap url` for scan ports of website or ip. With `-oN output.txt` you can save output to file. To read later.

```
sudo nmap -oN output.txt url.com
```

## Vulnerability Scan

```py
def vuln(url):
    print(" ")
    print(Fore.BLUE+"[+] Starting Vulnerability Scanner...")
    time.sleep(1)
    os.system(f"sudo nmap -sV -oN output.txt {url}")
    print(" ")
    print(Fore.RED+"[+] Output saved to output.txt file!")
    print(" ")
```

### Command Guide
You can just put -sV to scan vuln s of website.
```
sudo nmap -sV -oN output.txt url.com
```

## Operating System Scan (Os Scan)

```py
def oss(url):
    print(" ")
    print(Fore.BLUE+"[+] Starting OS (Operating System) Scanner...")
    time.sleep(1)
    os.system(f"sudo nmap -A -T4 -oN output.txt {url}")
    print(" ")
    print(Fore.RED+"[+] Output saved to output.txt file!")
    print(" ")
```
## Command Guide
You may put -O too but -O sometimes cant dedect os of server. So I used -A and -T4 to dedect better.
```
sudo nmap -A -T4 -oN output.txt url.com
```
