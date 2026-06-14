# gamewindow
import pygame
import input
from player import Player
from sprite import sprites, Sprite
from map import TileKind, Map
from camera import create_screen
from quest import QuestManager
pygame.init()

# setup
screen = create_screen(1200, 800, "Encantondo")

clear_color = pygame.Color(140, 214, 70)

running = True
player = Player("images/player.png", 42 * 32, 11 * 32)
tile_kinds = [

    # if true means solid but not applicable

    TileKind("grass", "images/grass.png", False), #0
    TileKind("road", "images/road.png", False), #1 and soo on
    TileKind("bush", "images/bush.png", False),
    TileKind("warmwater", "images/warmwater.png", False),
    TileKind("fencelightbrown", "images/fencelightbrown.png", False),
    TileKind("treessnow1", "images/treessnow1.png", False),
    TileKind("bahaynimorena", "images/bahaynimorena.png", False),
    TileKind("randomhouse3", "images/randomhouse3.png", False),

]
map = Map("maps/start.map", tile_kinds, 32)

bahaynimorena = Sprite("images/bahaynimorena.png", 43 * 32, 0 * 32)
randomhouse3 = Sprite("images/randomhouse3.png", 45 * 32, 15 * 32)
randomhouse1 = Sprite("images/randomhouse1.png", 4 * 32, 35 * 32)

quest_manager = QuestManager()

#game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            input.keys_down.add(event.key)
        elif event.type == pygame.KEYUP:
            input.keys_down.discard(event.key)

    #update code
    if not quest_manager.game_over:
        player.update()

    quest_manager.update(player)

    # draw
    screen.fill(clear_color)
    map.draw(screen)
    for s in sprites:
        s.draw(screen)
    quest_manager.draw_ui(screen)
    pygame.display.flip()

pygame.quit()

