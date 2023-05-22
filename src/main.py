import pygame
import sprite
import tile

window = pygame.display.set_mode([1280,720])
clock = pygame.time.Clock()
running = True
bg = sprite.Sprite("res/gfx/back.png", [0,0])
bg.edit_scale(10,10)
tile_positions = [(100,400)]
tiles = tile.Tile("res/gfx/tile1.png", [200,400], True)
tiles.edit_scale(3,3)
tile1 = tile.Tile("res/gfx/tile1.png", [40,500]  , True)
tile1.edit_scale(3,3)
player = sprite.Sprite("res/gfx/pawn.png", [60,473])
player.edit_scale(1.5,1.5)
compass = sprite.Sprite("res/gfx/compass1.png", [1280 - 32*5, 32])
compass.edit_scale(4,4)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player.rect[0] = 220
        player.rect[1] = 375

    bg.render(window)
    compass.render(window)
    tiles.render(window)
    tile1.render(window)
    player.render(window)
    pygame.display.flip()
    clock.tick(60) 
