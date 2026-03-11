import requests
import os
import json
import time
from colorama import Fore, init

init(autoreset=True)

AUTH_SERVER = "https://tabbo-auth.vercel.app/api/auth"
LOOKUP_API = "https://tabbo-proxy.vercel.app/api/search?mobile="

USERS_FILE = "users.json"
HISTORY_FILE = "history.json"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def load_json(file):
    try:
        with open(file) as f:
            return json.load(f)
    except:
        return []


def save_json(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=2)


def banner(user, credits):

    clear()

    print(Fore.RED + """

╔══════════════════════════════════════════════════════╗
║                                                      ║
║        ████████╗ █████╗ ██████╗ ██████╗  ██████╗      ║
║        ╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔═══██╗     ║
║           ██║   ███████║██████╔╝██████╔╝██║   ██║     ║
║           ██║   ██╔══██║██╔══██╗██╔══██╗██║   ██║     ║
║           ██║   ██║  ██║██████╔╝██████╔╝╚██████╔╝     ║
║           ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═════╝  ╚═════╝      ║
║                                                      ║
║              🔎 TABBO NUMBER INFO TOOL 🔎           ║
║                                                      ║
╚══════════════════════════════════════════════════════╝
""")

    print(Fore.YELLOW + "⭐ CREDIT BY TABBO\n")

    print(Fore.CYAN + "╔════════════ USER INFO ════════════╗")
    print(Fore.GREEN + f"   👤 USER     : {user}")
    print(Fore.GREEN + f"   💳 CREDITS  : {credits}")
    print(Fore.CYAN + "╚═══════════════════════════════════╝\n")

    print(Fore.YELLOW + "══════ MENU ══════\n")


def login():

    clear()

    print(Fore.CYAN + """
╔════════════════════════════════╗
            🔐 LOGIN
╚════════════════════════════════╝

Telegram : @tabbo73
""")

    print(Fore.YELLOW + "Password : ", end="")
    password = input()

    try:

        r = requests.get(AUTH_SERVER, params={"pass": password}).json()

        if r.get("status") != "ok":

            print(Fore.RED + "❌ Invalid Password")
            exit()

    except:

        print(Fore.RED + "Server Error")
        exit()


def show_results(data, number):

    print(Fore.MAGENTA + f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📱 RESULTS FOR : {number}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

    if not isinstance(data, dict) or len(data) == 0:

        print(Fore.RED + "\n❌ DATA NOT FOUND\n")
        return

    for i, key in enumerate(data, 1):

        r = data[key]

        print(Fore.BLUE + "╔══════════════════════════════╗")
        print(Fore.BLUE + f"         RECORD {i}")
        print(Fore.BLUE + "╚══════════════════════════════╝")

        if r.get("name"):
            print(Fore.YELLOW + "👤 Name : " + Fore.CYAN + r["name"])

        if r.get("fname"):
            print(Fore.YELLOW + "👨 Father : " + Fore.CYAN + r["fname"])

        if r.get("address"):

            print(Fore.GREEN + "\n🏠 ADDRESS DETAILS")

            addr = r["address"].split("!")

            labels = [
                "Relation",
                "Village",
                "City",
                "District",
                "State",
                "Pincode"
            ]

            for i, part in enumerate(addr):

                part = part.strip()

                if part and i < len(labels):

                    print(
                        Fore.YELLOW + "   " + labels[i] +
                        Fore.MAGENTA + " : " +
                        Fore.CYAN + part
                    )

        if r.get("circle"):
            print(Fore.GREEN + "\n📡 Circle : " + Fore.CYAN + r["circle"])

        if r.get("alt"):
            print(Fore.YELLOW + "📞 Alternate : " + Fore.CYAN + r["alt"])

        if r.get("id"):
            print(Fore.MAGENTA + "🆔 ID : " + Fore.CYAN + r["id"])

        print(Fore.RED + """
────────────────────────────────────
📩 Telegram : @tabbo73
⭐ Credit By TABBO
────────────────────────────────────
""")


def search(user, users):

    if users[user] <= 0:

        print(Fore.RED + """

❌ YOUR CREDITS FINISHED

📩 Contact Admin For More Credits
Telegram : @tabbo73

""")

        input("Press Enter...")
        return

    number = input("📱 Enter Mobile Number : ")

    print("🔎 Searching...\n")
    time.sleep(1)

    try:

        r = requests.get(LOOKUP_API + number)

        data = r.json()

        show_results(data, number)

        history = load_json(HISTORY_FILE)
        history.append(number)
        save_json(HISTORY_FILE, history)

    except:
        pass

    users[user] -= 1
    save_json(USERS_FILE, users)

    print(Fore.YELLOW + f"\n💳 Remaining Credits : {users[user]}")

    input("Press Enter...")


def history():

    data = load_json(HISTORY_FILE)

    print(Fore.CYAN + "\n📜 SEARCH HISTORY\n")

    if len(data) == 0:
        print("No history")

    for i, n in enumerate(data, 1):
        print(Fore.YELLOW + f"{i}. {n}")

    input("\nPress Enter...")


def clear_history():

    save_json(HISTORY_FILE, [])

    print("History cleared")

    input()


def guide():

    print(Fore.GREEN + """

📖 GUIDE

1 Enter mobile number
2 Tool shows database info
3 Each search costs 1 credit

""")

    input()


def about():

    print(Fore.YELLOW + """

TABBO NUMBER INFO TOOL

Developer : TABBO
Telegram  : @tabbo73

""")

    input()


def menu(user, users):

    while True:

        banner(user, users[user])

        print(Fore.GREEN + "1️⃣  Search Number")
        print(Fore.CYAN + "2️⃣  History")
        print(Fore.MAGENTA + "3️⃣  Clear History")
        print(Fore.BLUE + "4️⃣  Guide")
        print(Fore.YELLOW + "5️⃣  About")
        print(Fore.RED + "6️⃣  Exit\n")

        op = input("Select Option : ")

        if op == "1":
            search(user, users)

        elif op == "2":
            history()

        elif op == "3":
            clear_history()

        elif op == "4":
            guide()

        elif op == "5":
            about()

        elif op == "6":
            exit()


login()

users = load_json(USERS_FILE)

username = os.getlogin()

if username not in users:
    users[username] = 5

save_json(USERS_FILE, users)

menu(username, users)
