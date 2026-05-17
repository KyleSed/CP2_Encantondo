# gamewindow
import pygame
import input
from player import Player
from sprite import sprites, Sprite
from map import TileKind, Map
from camera import create_screen
pygame.init()

# setup
screen = create_screen(800, 600, "Encantondo")

clear_color = pygame.Color(0, 0, 0)

running = True
player = Player("images/player.png", 10 * 32, 10 * 32)
tile_kinds = [
    # if true means solid

    TileKind("grass", "images/grass.png", False), #0
    TileKind("tree", "images/treessnow1.png", True), #1
    TileKind("bush", "images/bush.png", False),
    TileKind("road", "images/road.png", False),

]
map = Map("maps/start.map", tile_kinds, 32)


new_tree = Sprite("images/treessnow1.png", 7 * 32, 3 * 32)
new_tree = Sprite("images/treessnow1.png", 8 * 32, 5 * 32)

constructionsupplystore = Sprite("images/constuctionsupplystore.png", 15 * 32, 4 * 32)

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
    player.update()

    # draw
    screen.fill(clear_color)
    map.draw(screen)
    for s in sprites:
        s.draw(screen)
    pygame.display.flip()



pygame.quit()

