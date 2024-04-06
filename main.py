### Made By Unkel // Licensed in Licence.txt

from colorama import Fore, Style 
import os
import webbrowser
import time
import ipinfo

RED = Fore.RED
BLUE = Fore.BLUE
GREEN = Fore.GREEN
CYAN = Fore.CYAN
BLACK = Fore.BLACK
WHITE = Fore.WHITE

### Change Title :
os.system('title Unkel Multitool Example')
print(" Star : https://github.com/unkelr/Unkel-MultiTool-Example/ ")
time.sleep(2)


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

### Change the ascii art if you want to! website : https://patorjk.com/software/taag/#p=testall&f=Graffiti&t=UNKEL

def intro():
    print(RED + f"""

╦ ╦╔╗╔╦╔═╔═╗╦  
║ ║║║║╠╩╗║╣ ║  
╚═╝╝╚╝╩ ╩╚═╝╩═╝

Welcome to Unkel MultiTool!

""")
intro()
### You can change "RED" to any of the colors listed above.
time.sleep(2)
cls()

def menu():
    print(RED + """


                                                     ╦ ╦╔╗╔╦╔═╔═╗╦  
                                                     ║ ║║║║╠╩╗║╣ ║  
                                                     ╚═╝╝╚╝╩ ╩╚═╝╩═╝
                   ║══════════════════════════════════════════════════════════════════════════════════║

                                            1. IP LOOKUP                    4.

                                            2. Discord                      5.

                                            3. Github                       6. Exit

                    ║══════════════════════════════════════════════════════════════════════════════════║
""")
menu()

def iplookup():
    access_token = 'cb657df67f619c'
    handler = ipinfo.getHandler(access_token)

    while True:
        choice = input("                                >> ")

        if choice == "1":
            ip_address = input(f"                             IP >> ")
            details = handler.getDetails(ip_address)
            print("                                 IP:", details.ip)
            print("                                 City:", details.city)
            print("                                 Region:", details.region)
            print("                                 Country:", details.country)
            print("                                 Organization:", details.org)
            print("                                 Latitude:", details.latitude)
            print("                                 Longitude:", details.longitude)
            time.sleep(5)
            cls()
            menu()

        
        ### change this to your dicsord server if you want. or make it something else!
        elif choice == "2":
            webbrowser.open_new_tab("https://discord.gg/unkelmarket")
            cls()
            menu()

        elif choice == "3":
            webbrowser.open_new_tab("https://github.com/unkelr/Unkel-MultiTool-Example/")

        elif choice == "4":
            webbrowser.open_new_tab("")

        elif choice == "5":
            webbrowser.open_new_tab("")

        elif choice == "6":
            print("                                Cya Next Time! github.com/unkelr/")
            time.sleep(1)
            break






# Calling the function to execute the IP lookup process
iplookup()
            

    




