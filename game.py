import pygame, sys
import os

pygame.init()
screen = pygame.display.set_mode((432, 768)) # double the size of the existing backgroud image

# # Get the directory where your game.py file is located
# current_dir = os.path.dirname(os.path.abspath(__file__))
# # Build the path to the assets folder
# assets_dir = os.path.join(current_dir, 'assets')

# Set FPS
clock = pygame.time.Clock()

# Set Background Image
# bg = pygame.image.load(os.path.join(assets_dir, 'background-night.png'))
bg = pygame.image.load('assets/background-night.png')

# Loop that load background image for long term use
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(bg, (0, 0)) # (0, 0) is the top left corner
    pygame.display.update()
    clock.tick(120) # 120 FPS
