import pygame
import sprite

window = pygame.display.set_mode([1280,720])
clock = pygame.time.Clock()
running = True
bg = sprite.Sprite("../res/gfx/back.png", [0,0])
bg.edit_scale(10,10)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    bg.render(window)
    pygame.display.flip()
    clock.tick(60) 
