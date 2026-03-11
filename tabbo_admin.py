import json
import os
from colorama import Fore, init

init(autoreset=True)

USERS_FILE = "users.json"

ADMIN_ID = "admin"
ADMIN_PASS = "tabbo123"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def load_users():

    try:
        with open(USERS_FILE) as f:
            return json.load(f)
    except:
        return {}


def save_users(data):

    with open(USERS_FILE,"w") as f:
        json.dump(data,f,indent=2)


def banner():

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
║                 👑 ADMIN CONTROL PANEL               ║
║                                                      ║
╚══════════════════════════════════════════════════════╝
""")


def login():

    banner()

    print(Fore.YELLOW + "🔐 ADMIN LOGIN\n")

    admin = input("Admin ID : ")
    password = input("Password : ")

    if admin != ADMIN_ID or password != ADMIN_PASS:

        print("❌ Invalid admin login")
        exit()


def total_users():

    users = load_users()

    print(Fore.GREEN + f"\n👥 Total Users : {len(users)}\n")

    input("Press Enter...")


def show_users():

    users = load_users()

    print(Fore.CYAN + "\n📋 USERS LIST\n")

    for u in users:

        print(Fore.YELLOW + f"User : {u}")
        print(Fore.GREEN + f"Credits : {users[u]}")
        print("──────────────")

    input("\nPress Enter...")


def give_credits():

    users = load_users()

    user = input("Enter Username : ")

    if user not in users:

        print("User not found")
        input()
        return

    credit = int(input("Credits to add : "))

    users[user] += credit

    save_users(users)

    print("✅ Credits Added")

    input()


def menu():

    while True:

        banner()

        print(Fore.GREEN + """

1️⃣  Total Users
2️⃣  Show Users
3️⃣  Add Credits
4️⃣  Exit

""")

        op = input("Select Option : ")

        if op == "1":
            total_users()

        elif op == "2":
            show_users()

        elif op == "3":
            give_credits()

        elif op == "4":
            exit()


login()
menu()
