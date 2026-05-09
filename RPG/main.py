#RPG (Realistic Pinoy Game)
import sys
import os
import time
from map import zonemap, ZONENAME, DESC, EXAM, UTOS
from movement import player_move, movement_handler, valid_up, valid_down, valid_left, valid_right
from player import playerko

screen_width = 100

#VALID_INPUTS & List in General
valid_moves = ['walk', 'lakad', 'takbo', 'run', 'hakbang', 'hop', 'jump', 'sprint', 'go', 'move'] 
valid_options = ['new game', 'load game', 'help', 'quit']
valid_help_options = ['change name', 'how to play', 'return']
valid_up = ['north', 'hilaga', 'up', 'norte', 'go north', 'go up', 'forward', 'taas'] 
valid_down = ['south', 'timog', 'down', 'sur', 'go south', 'go down', 'backward', 'baba'] 
valid_left = ['west', 'kaliwa', 'left', 'westside', 'go west', 'go left', 'sideward left']
valid_right = ['east', 'kanan', 'right', 'eastside', 'go east', 'go right', 'sideward right']
enemies = ['Tambay', 'Rugby boy', 'Snatcher', 'Holduper', 'Tanod', 'Civilian']
boss = ['Tatay', 'Nanay', 'Kapitana', 'Lispo']
valid_tawag_kay_nanay = ['nanay', 'ma', 'mama', 'mom', 'mother', 'ermat','inay', 'nay','mommy', 'mommie']

#KEYS
HPENEMY = 0
STAMINAENEMY = 0
STRENGTHENEMY = 0
STATUS_EFFECTSENEMY = 'none'
PERANILA = 0
ITEMNILA= 'none'

kalaban = {
    'Tambay': {
        HPENEMY: 25,
        STAMINAENEMY: 25,
        STRENGTHENEMY: 5,
        STATUS_EFFECTSENEMY: 'none',
        PERANILA: 20
    },
    'Rugby boy': {
        HPENEMY: 125,
        STAMINAENEMY: 75,
        STRENGTHENEMY: 7,
        STATUS_EFFECTSENEMY: 'high',
        PERANILA: 20
    },
    'Tanod': {
        HPENEMY: 100,
        STAMINAENEMY: 100,
        STRENGTHENEMY: 10,
        STATUS_EFFECTSENEMY: 'none',
        PERANILA: 20,
        ITEMNILA: 'batuta',
    },
    'Snatcher': {
        HPENEMY: 75,
        STAMINAENEMY: 150,
        STRENGTHENEMY: 7,
        STATUS_EFFECTSENEMY: 'high',
        PERANILA: 80,
        ITEMNILA: 'running shoes',
    },
    'Holduper': {
        HPENEMY: 75,
        STAMINAENEMY: 75,
        STRENGTHENEMY: 15,
        STATUS_EFFECTSENEMY: 'high',
        PERANILA: 80,
        ITEMNILA: 'knife',
    },
    'Civilian': {
        HPENEMY: 100,
        STAMINAENEMY: 100,
        STRENGTHENEMY: 10,
        STATUS_EFFECTSENEMY: 'rage',
        PERANILA: 40,
        ITEMNILA: 'none',
    },
    'Tatay': {
        HPENEMY: 10000,
        STAMINAENEMY: 1000,
        STRENGTHENEMY: 10000,
        STATUS_EFFECTSENEMY: 'rage',
        PERANILA: 100000000000,
        ITEMNILA: 'Walis Tambo',
    },
    'Nanay': {
        HPENEMY: 10000,
        STAMINAENEMY: 10000,
        STRENGTHENEMY: 1000,
        STATUS_EFFECTSENEMY: 'rage',
        PERANILA: 100000000000,
        ITEMNILA: 'Hanger',
    },
    'Kapitana': {
        HPENEMY: 125,
        STAMINAENEMY: 150,
        STRENGTHENEMY: 7,
        STATUS_EFFECTSENEMY: 'none',
        PERANILA: 40,
        ITEMNILA: 'batuta',
    },
    'Lispo': {
        HPENEMY: 75,
        STAMINAENEMY: 150,
        STRENGTHENEMY: 15,
        STATUS_EFFECTSENEMY: 'none',
        PERANILA: 80,
        ITEMNILA: 'baril',
    },
}

def save_game():
    try:
        with open("savefile.txt", "w") as file:
            file.write(playerko.name + "\n")
            file.write(playerko.location + "\n")
            file.write(str(playerko.hp) + "\n")
            file.write(str(stamina) + "\n")
            file.write(str(strength) + "\n")
            file.write(str(money) + "\n")
            file.write(','.join(inventory) + "\n")
            file.write(str(status_effects) + "\n")
            file.write(str(UTOS) + "\n")
   
    except:
        center_block("~~Error saving game.~~")

#UI
def border():
    print('Xx'+'='*screen_width+'xX')

def center_block(text):
    for line in text.split('\n'):
        print(line.center(screen_width))

def title_screen_options():
    while True:
        option = input("> ").lower()

        if option == "new game":
            ask_name()
            start_game()
            break
        elif option == "load game":
            load_game()
            break
        elif option == "help":
            help_menu()
            break
        elif option == "quit":
            sys.exit()
        else:
            center_block("~~Invalid command. Please try again.~~")

def ask_name():
    os.system('cls')
    border()
    center_block(" ~~Sup, what should I call you homie?~~")
    border()

    playerko.name = input("> ")
    playerko.location = 'e4' 
    while playerko.name == "":
        border()
        center_block("~~No name amputek. Feeling unique yarn?~~")
        border()
        playerko.name = input("> ")
    save_game()
    border()
    center_block(f" ~~Eyyo what's trippin', {playerko.name}!~~")
    border()

def load_game():
    global hp, stamina, strength, money, inventory, status_effects, UTOS

    try:
        file = open("savefile.txt", "r")
        lines = file.readlines()
        file.close()

        if len(lines) < 9:
            raise Exception("Corrupted save file")

        playerko.name = lines[0].strip()
        playerko.location = lines[1].strip()

        if playerko.location not in zonemap:
            playerko.location = 'e4'

        hp = int(lines[2].strip() or 100)
        stamina = int(lines[3].strip() or 100)
        strength = int(lines[4].strip() or 10)
        money = int(lines[5].strip() or 0)
        inventory = lines[6].strip().split(',') if lines[6].strip() else []
        status_effects = lines[7].strip() if len(lines) > 7 and lines[7].strip() else 'none'
        UTOS = lines[8].strip() == 'True' if len(lines) > 8 else False
    

        border()
        center_block(f"~~Sup {playerko.name}! Welcome back!~~")
        border()

    except:
        center_block("~~Save file corrupted. Starting new game.~~")
        ask_name()
        return
    start_game()

def change_name():
    os.system('cls')
    border()
    center_block(" ~~What do you want your new name to be?~~")
    border()

    new_name = input("> ").strip()
    if new_name == "":
        center_block("~~No name amputek. Feeling unique yarn?~~")
        return
    playerko.name = new_name
    save_game()

    border()
    center_block(f" ~~Name changed to {playerko.name}!~~")
    border()

def how_to_play():
    os.system('cls')
    border()
    center_block("~~How to Play~~\n")
    center_block("1. Use the commands 'walk, takbo, go' followed by a direction to move around the map.")
    center_block("2. Use the command 'save game', 'help menu' or 'main menu' to access the respective menus at any time during the game.")
    center_block("3. Use the command 'gamitin ko mata ko' to look around your current location for clues and items.")
    center_block("4. Use commands to interact with the environment and characters, some common commands are 'yap with', 'stats' and 'use'.")
    center_block("5. Your goal is to explore Encantondo and discover different commands that you could use on your journey.")
    center_block("\nType 'return' to go back to the help menu.")
    border()
    choice = input("> ")
    if choice.lower() == ("return"):
        help_menu()

def help_menu_options():
    while True:
        choice = input("> ").lower()

        if choice == "how to play":
            how_to_play()
            break
        elif choice == "change name":
            change_name()
            break
        elif choice == "return":
            title_screen()
            break
        else:
            center_block("~~Invalid command. Please try again.~~")

def title_screen():
    os.system('cls')
    border()
    center_block("~~welcome to REALISTIC PINOY GAME (RPG)~~\n")
    center_block(" ~Gagawin ang lahat ng bagay maliban sa pagsunod sa utos sa'yo ng nanay mo~\n")
    center_block("| NEW GAME  |\n")
    center_block("| LOAD GAME |\n")
    center_block("|   HELP    |\n")
    center_block("|   QUIT    |\n")
    center_block("Copyright 2026 by Villamor. All rights reserved.")
    border()
    title_screen_options()

def help_menu():
    while True:
        os.system('cls')
        border()
        center_block("~~Help Menu~~\n")
        center_block(" | Change Name |\n")
        center_block("| How to Play |\n")
        center_block("|   Return    |\n")
        center_block("Copyright 2026 by Kyle Zedrick A. Villamor. All rights reserved.")
        border()
        help_menu_options()
        break

#GAME_LOOP
def start_game():
    while not playerko.game_over:
        print_location()
        prompt()
        nanay_utos_ending()
    if playerko.game_over:
        title_screen()

#DISPLAY
def print_location():
    loc = playerko.location
    print("Location:", zonemap[loc][ZONENAME])
    print('> '+zonemap[loc][DESC])

def print_status():
    border()
    center_block(f"HP: {hp} | Stamina: {stamina} | Strength: {strength} | Money: {money} | Inventory: {', '.join(inventory) if inventory else 'Empty'} | Status Effects: {status_effects}")
    border()

#PLAYER_PROMPT
def prompt():
    center_block("~~What do you want to do?~~")
    border()
    action = input("> ").lower().strip()
    words = action.split()
    if len(words) == 0:
        return
    if words[0] in valid_moves:
        if len(words) > 1:
            player_move(words[1])   
        else:
            player_move(None)
    elif action == 'gamitin ko mata ko':
        player_examine()
    elif action == 'save game':
        save_game() 
    elif action == 'help menu':
        help_menu()
    elif action == 'main menu':
        title_screen()
    elif action == 'quit':
        sys.exit()
    elif action.startswith('yap with'):
        npc = action.replace('yap with', '').strip()
        npc_interaction(npc)
    elif action == 'stats':
        print_status()
    elif action.startswith('buy'):
        item = action.replace('buy', '').strip()
        buy_item(item)
    else:
        border()
        center_block("~~Invalid command. Please try again.~~")
        border()

#EXAMINE
def player_examine():
    loc = playerko.location
    border()
    print(f"> Nakita mo na {zonemap[loc][EXAM]}")
    border()

#NPC_INTERACTION
def npc_interaction(npc):
    global money, UTOS
    if npc is None or npc == "":
        border()
        center_block("~~Sinong dadaldalin mo?~~")
        border()
        npc = input("> ").lower().strip()
    elif npc in valid_tawag_kay_nanay:
        if playerko.location == 'e4':
            if not UTOS:
                border()
                center_block(f"~~Nanay: {playerko.name}!~~")
                center_block(f"~~Nanay: {playerko.name}!!~~")
                center_block("~~Nanay: Puro ka selpon eh! Kanina pa kita tinatawag ahh?!~~")
                center_block("~~Nanay: Bili kang yelo oh, balik mo sakin yung sukli.~~")
                border()
                money += 60
                UTOS = True
                save_game()
            else:
                border()
                center_block("~~Nanay: Ano pang dinadaldal mo dyan? Bumili ka na nang makagawa na'ko ng halo-halo.~~")
                border()
        else:
            border()
            center_block("~~Sayang, 'di mo dala phone mo.~~")
            border()
    else:
        border()
        center_block(" ~~Ha? Pakiulit nga.~~")
        border()

#BUY_ITEM
def buy_item(item):
    global money, UTOS

    if playerko.location == 'b5':
        if not UTOS:
            border()
            print("> Nag-overthink ka kung ano bang bibilhin mo. Sa huli ay wala ka ring nabili.")
            border()
            return

        if item is None or item == "":
            border()
            center_block("~~What item do you want to buy?~~")
            border()
            item = input("> ").lower().strip()

        if item in ['yelo', 'ice']:
            if money >= 60:
                money -= 60
                inventory.append('yelo')
                border()
                center_block("~~Nabili mo ang yelo.~~")
                border()
                save_game()
            else:
                border()
                center_block(f"~~Saan aabot ang {money} mo?~~")
                border()
        else:
            border()
            center_block("~~Kung ano mang binibili mo, always rememeber na for school purposes lang ito.~~")
            border()
    else:
        border()
        center_block("~~'Mali ka ng binibilhan.~~")
        border()

#Nanay's Utos Ending
def nanay_utos_ending():
    global inventory, UTOS
    if playerko.location == 'e4' and 'yelo' in inventory and UTOS == True:
            os.system('cls')
            border()
            print("Nanay: Ba't ngayon ka lang? San ka galing?")
            print("Nanay: Oh siya't kadkarin mo na ang yelo at maghahanda na'ko ng baso.")
            border()
            time.sleep(8)
            center_block("~~Sa huli ay nakakain karin ng halo-halo laban sa tag-init.~~")
            time.sleep(8)
            center_block("~~Habang kumakain, naramdaman mo ang pagmamahal ng nanay mo sa'yo.~~")
            time.sleep(8)
            center_block("~~Ang simpleng pag-gawa niya ng halo-halo o kahit anong meryenda ")
            center_block("at ang simpleng pagtanong at pag-aalala niya kung saan ka pumupunta " )
            center_block("ay isa nang malaking patunay ng kanyang pagmamahal sa'yo.~~")
            time.sleep(16)
            center_block("~~Iyong napagnilay-nilay; Ba't ko nga ba gustong sawayin ang utos ng mapagmahal kong ina?~~")
            time.sleep(16)
            border()
            center_block("~~Halo-halo Ending Achieved!~~")
            border()
            time.sleep(8)
            playerko.game_over = True  

#GAME_START
title_screen()
