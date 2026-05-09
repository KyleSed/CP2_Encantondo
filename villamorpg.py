#RPG (Realistic Pinoy Game)
import sys
import os
import random
import time

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
ZONENAME = "name"
DESC = "desc"
EXAM = "exam"
NORTH = "north"
SOUTH = "south"
WEST = "west"
EAST = "east"
HPENEMY = 0
STAMINAENEMY = 0
STRENGTHENEMY = 0
STATUS_EFFECTSENEMY = 'none'
PERANILA = 0
ITEMNILA= 'none'
UTOS = False

#MAP
zonemap = {
        'a1': {
            ZONENAME: 'Construction Supply Store',
            DESC: 'A place where you can buy construction materials and tools.',
            EXAM: 'may rugby sa shelves.',
            NORTH: '', 
            SOUTH: 'b1', 
            WEST: '', 
            EAST: 'a2', 
        },
        'a2': {
            ZONENAME: 'Tattoo Parlor',
            DESC: 'A place where you can get tattoos done.',
            EXAM: 'may nagru-rugby sa gilid ng parlor.',
            NORTH: '', 
            SOUTH: 'b2', 
            WEST: 'a1', 
            EAST: 'a3', 
        },
        'a3': {
            ZONENAME: 'Bahay ni Tita',
            DESC: 'Bahay ng tita mo na may maliit na farm sa gilid.',
            EXAM: 'sinisenyasan ka ng tita mo na lumapit ka sa kanya. Uutusan ka yata.',
            NORTH: '', 
            SOUTH: 'b3', 
            WEST: 'a2', 
            EAST: 'a4', 
        },
        'a4': {
            ZONENAME: 'Church',
            DESC: 'A place of worship where you can pray and reflect.',
            EXAM: 'may krus sa altar.',
            NORTH: '', 
            SOUTH: 'b4', 
            WEST: 'a3', 
            EAST: 'a5', 
        },
        'a5': {
            ZONENAME: 'Encantondo Hill',
            DESC: 'A scenic hill with a beautiful view of the town (tambak ng buhangin at bato).',
            EXAM: 'madulas ang daan papunta sa tuktok ng burol. Sarap paring puntahan ng tuktok',
            NORTH: '', 
            SOUTH: 'b5', 
            WEST: 'a4', 
            EAST: '', 
        },
        'b1': {
            ZONENAME: 'Motorcycle Dealership',
            DESC: 'A place where you can buy and repair motorcycles.',
            EXAM: 'may motor na naka-stored sa loob ng tindahan.',
            NORTH: 'a1', 
            SOUTH: 'c1', 
            WEST: '', 
            EAST: 'b2', 
        },
        'b2': {
            ZONENAME: 'Encantondo Daycare Center',
            DESC: 'A place where children are cared for during the day.',
            EXAM: 'may mga teacher na nagtuturo sa loob ng daycare center.',
            NORTH: 'a2', 
            SOUTH: 'c2', 
            WEST: 'b1', 
            EAST: 'b3', 
        },
        'b3': {
            ZONENAME: 'Encantondo Covered Court',
            DESC: 'A covered court where people can gather and play.',
            EXAM: 'tao na masasama ang tingin sa iyo sa labas ng court',
            NORTH: 'a3', 
            SOUTH: 'c3', 
            WEST: 'b2', 
            EAST: 'b4', 
        },
        'b4': {
            ZONENAME: 'BDO',
            DESC: 'A bank where you can deposit and withdraw money.',
            EXAM: 'may tao na naglalakad sa labas ng BDO. May hawak ng wallet ang isa sa kanila.',
            NORTH: 'a4', 
            SOUTH: 'c4', 
            WEST: 'b3', 
            EAST: 'b5', 
        },
        'b5': {
            ZONENAME: 'Dali Store',
            DESC: 'A small store where you can buy snacks and drinks.',
            EXAM: 'may freezer sa loob ng tindahan. Mukhang may yelo silang tinda.',
            NORTH: 'a5', 
            SOUTH: 'c5', 
            WEST: 'b4', 
            EAST: '', 
        },
        'c1': {
            ZONENAME: 'Naka-park na E-Bike sa Daan',
            DESC: 'Kapal, buong bike nakaparking sa kalahati ng kalsada.',
            EXAM: 'walang tow truck na papunta, sayang.',
            NORTH: 'b1', 
            SOUTH: 'd1', 
            WEST: '', 
            EAST: 'c2', 
        },
        'c2': {
            ZONENAME: 'Encantondo Plaza',
            DESC: 'A bustling plaza where people gather and socialize.',
            EXAM: 'may stall sa paligid ng plaza. Mukhang may mga pagkain at inumin na binebenta roon.',
            NORTH: 'b2', 
            SOUTH: 'd2', 
            WEST: 'c1', 
            EAST: 'c3', 
        },
        'c3': {
            ZONENAME: 'Encontondo University',
            DESC: 'A prestigious university where students come to learn and grow.',
            EXAM: 'ang leader mo sa final project na sinisenyasan ka. Mukhang may sasabihin yata sa iyo.',
            NORTH: 'b3', 
            SOUTH: 'd3', 
            WEST: 'c2', 
            EAST: 'c4', 
        },
        'c4': {
            ZONENAME: 'Encantondo Police Station',
            DESC: 'A police station where law enforcement officers are stationed.',
            EXAM: 'minumukhaan ka nila. Mukhang may nagawa kang mali.',
            NORTH: 'b4', 
            SOUTH: 'd4', 
            WEST: 'c3', 
            EAST: 'c5', 
        },
        'c5': {
            ZONENAME: 'Mr. Donuts',
            DESC: 'A small donut shop where you can buy fresh donuts.',
            EXAM: 'may butternut, favourite flavour ni crush.',
            NORTH: 'b5', 
            SOUTH: 'd5', 
            WEST: 'c4', 
            EAST: '', 
        },
        'd1': {
            ZONENAME: 'Bigbrew Coffee Shop',
            DESC: 'A cozy coffee shop where you can enjoy a good cup of coffee.',
            EXAM: 'problemado ang bantay sa coffee shop, mukhang kinukulang sila ng sangkap',
            NORTH: 'c1', 
            SOUTH: 'e1', 
            WEST: '', 
            EAST: 'd2', 
        },
        'd2': {
            ZONENAME: 'Novo',
            DESC: 'A small market where you can buy various items.',
            EXAM: 'masama ang tingin sa iyo nung isang lalaki sa tapat ng store.',
            NORTH: 'c2', 
            SOUTH: 'e2', 
            WEST: 'd1', 
            EAST: 'd3', 
        },
        'd3': {
            ZONENAME: 'Encantondo Doctors',
            DESC: 'A medical clinic where you can receive healthcare services.',
            EXAM: 'mukhang amoy alcohol sa tapat ng hospital.',
            NORTH: 'c3', 
            SOUTH: 'e3', 
            WEST: 'd2', 
            EAST: 'd4', 
        },
        'd4': {
            ZONENAME: 'Pandayan Bookstore',
            DESC: 'A bookstore where you can buy various books.',
            EXAM: 'may bond paper sa loob ng bookstore.',
            NORTH: 'c4', 
            SOUTH: 'e4', 
            WEST: 'd3', 
            EAST: 'd5', 
        },
        'd5': {
            ZONENAME: 'Bakal Gym',
            DESC: 'A place where you can exercise and stay fit.',
            EXAM: 'pamilyar sa iyo ang bantay ng gym.',
            NORTH: 'c5', 
            SOUTH: 'e5', 
            WEST: 'd4', 
            EAST: '', 
        },
        'e1': {
            ZONENAME: 'Encantondo Seaside',
            DESC: 'A beautiful seaside where you can relax and enjoy the view (kanal na punong-puno ng basura).',
            EXAM: 'mukhang mabaho. May kademonyohan kang nasa isip.',
            NORTH: 'd1', 
            SOUTH: '', 
            WEST: '', 
            EAST: 'e2', 
        },
        'e2': {
            ZONENAME: 'Bahay na Violet',
            DESC: 'A cozy house and bahay ni crush.',
            EXAM: 'nakatambay si crush sa biranda ng bahay nila. Mukhang may ginagawa siya sa cellphone niya.',
            NORTH: 'd2', 
            SOUTH: '', 
            WEST: 'e1', 
            EAST: 'e3', 
        },
        'e3': {
            ZONENAME: 'Bahay na Green',
            DESC: 'A cozy house and bahay ng tropa mo.',
            EXAM: 'ang tropa mo na kasama ang ea niya. Mukhang may ibubulong yata sa iyo ang tropa mo.',
            NORTH: 'd3', 
            SOUTH: '', 
            WEST: 'e2', 
            EAST: 'e4', 
        },
        'e4': {
            ZONENAME: 'Home',
            DESC: 'Your humble abode where you can rest and recover.',
            EXAM: 'may sinasabi ang nanay mo, uutusan ka yata sa bahay.',
            NORTH: 'd4', 
            SOUTH: '', 
            WEST: 'e3', 
            EAST: 'e5', 
            UTOS: False
        },
        'e5': {
            ZONENAME: 'Encantondo Town Hall',
            DESC: 'The local government building where you can handle various administrative tasks.',
            EXAM: 'masama ang tingin sa iyo nung isang tanod, mukhang may nagawa kang mali.',
            NORTH: 'd5', 
            SOUTH: '', 
            WEST: 'e4', 
            EAST: '', 
        }
    }

#Player Stats
hp = 100
stamina = 100
strength = 10
money = 0
inventory = []
status_effects = 'none'


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
            file.write(str(hp) + "\n")
            file.write(str(stamina) + "\n")
            file.write(str(strength) + "\n")
            file.write(str(money) + "\n")
            file.write(','.join(inventory) + "\n")
            file.write(str(status_effects) + "\n")
            file.write(str(UTOS) + "\n")
   
    except:
        center_block("~~Error saving game.~~")

#PLAYER
class Player:
    def __init__(player):
        player.location = 'e4'
        player.game_over = False

playerko = Player()

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

#PLAYER_MOVE
def player_move(direction):
    if direction is None:
        border()
        center_block("~~Where do you want to go?~~")
        border()
        direction = input('> ').lower().strip()
    if direction in valid_up:
        destination = zonemap[playerko.location][NORTH]
    elif direction in valid_down:
        destination = zonemap[playerko.location][SOUTH]
    elif direction in valid_left:
        destination = zonemap[playerko.location][WEST]
    elif direction in valid_right:
        destination = zonemap[playerko.location][EAST]
    else:
        border()
        center_block("~~Wrong spelling ka siguro. Pakiulit.~~")
        border()
        return
    if destination == '':
        border()
        center_block("~~Dead End ka sah. Hanap kang ibang daan.~~")
        border()
    else:
        movement_handler(destination)

#MOVE_HANDLER
def movement_handler(destination):
    playerko.location = destination
    border()
    center_block(f"~~You moved to {zonemap[destination][ZONENAME]} ~~")
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
testing = true
changes na gagawin sa game loop:
- add more npc interactions - add more items to buy and more shops to buy them from - add more commands to use in the game (e.g. 'use [item]', 'check inventory', 'talk to [npc]', etc.) - add more locations to explore and more things to examine in each location - add more endings based on different choices and interactions in the game - add a combat system for encounters with enemies - add a leveling system for the player to improve their stats and abilities - add a quest system for the player to complete tasks and earn rewards - add a day/night cycle                    