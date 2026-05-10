from map import zonemap, NORTH, SOUTH, WEST, EAST, ZONENAME, DESC, EXAM, UTOS
from main import border, playerko, center_block, valid_up, valid_down, valid_left, valid_right
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