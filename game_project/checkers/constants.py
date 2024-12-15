import pygame
#store const vals

#boards
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

#RBG vals
LIME = (235, 236, 208)
WHITE = (255, 255, 255)
BLACK = (86, 83, 81)
GREEN = (119, 149, 86)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

#crown png when promoted to king
CROWN = pygame.transform.scale(pygame.image.load('game_project/assets/kings-crown-logo-vector-PNG.png'), (50, 50))