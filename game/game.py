import pygame
import sys
import os

from scripts.utils import load_image

INITIAL_SIZE_WIDTH, INITIAL_SIZE_HEIGHT = 320, 240
ASPECT_RATIO = INITIAL_SIZE_WIDTH / INITIAL_SIZE_HEIGHT
SCALE = 1

class Game:
    def __init__(self):
        pygame.init()
        
        pygame.display.set_caption('game')
        self.screen = pygame.display.set_mode((INITIAL_SIZE_WIDTH * SCALE, INITIAL_SIZE_HEIGHT * SCALE), pygame.RESIZABLE)
        self.display = pygame.Surface((INITIAL_SIZE_WIDTH, INITIAL_SIZE_HEIGHT))
        
        self.clock = pygame.time.Clock()
        
        self.movement = [False, False]
        
        self.click = False
        
        self.assets = {
            'player': load_image('entities/player/player.png'),
            'enemy': load_image('entities/enemy/enemy.png'),
            'gun': load_image('entities/gun.png'),
            'background': load_image('background.png'),
        }
        
    def run(self):
        while True:
                                
            current_width, current_height = self.screen.get_size()            
            
            self.display.fill((0, 175, 255))
            self.display.blit(self.assets['background'], (0, 0))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.click = False
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_BACKSPACE:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.KEYUP:
                    pass
                        
            display_width, display_height = self.screen.get_size()
            if self.screen.get_width() / ASPECT_RATIO < self.screen.get_height():
                display_width = current_width
                display_height = display_width / ASPECT_RATIO
            elif self.screen.get_height() * ASPECT_RATIO < self.screen.get_width():
                display_height = current_height
                display_width = display_height * ASPECT_RATIO
            
            self.screen.fill('black')
            self.screen.blit(pygame.transform.scale(self.display, (display_width, display_height)), ((current_width - display_width) / 2, (current_height - display_height) / 2))
            pygame.display.update() 
            self.clock.tick(60)
            
Game().run()
