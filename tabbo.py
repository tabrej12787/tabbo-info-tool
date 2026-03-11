import requests
import sys
from colorama import Fore, Style, init

init()

AUTH_SERVER = "https://tabbo-auth.vercel.app/api/auth"
LOOKUP_API = "https://tabbo-info.vercel.app/api/lookup?key=tabbo02&mobile="

def banner():

    print(Fore.CYAN + """
████████╗ █████╗ ██████╗ ██████╗ 
╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗
   ██║   ███████║██████╔╝██████╔╝
   ██║   ██╔══██║██╔══██╗██╔══██╗
   ██║   ██║  ██║██████╔╝██████╔╝
   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═════╝

TABBO INFO TOOL
Credit ❤️ tabbo73
Contact tg @tabbo73
""")

def verify_password():

    password = input("🔒 Enter Tool Password: ")

    try:

        r = requests.get(AUTH_SERVER, params={"pass": password})
        data = r.json()

        if data.get("status") != "ok":

            print(Fore.RED + "❌ Invalid password")
            sys.exit()

        print(Fore.GREEN + "✅ Access granted\n")

    except:

        print("❌ Server connection failed")
        sys.exit()

def lookup():

    while True:

        number = input("📱 Enter mobile number (or 'exit'): ")

        if number.lower() == "exit":
            break

        try:

            r = requests.get(LOOKUP_API + number)

            print("\n📊 RESULT\n")

            print(r.text)

            print("\n━━━━━━━━━━━━━━━━━━━━\n")

        except:

            print("❌ API error")

def main():

    banner()

    verify_password()

    lookup()

main()
