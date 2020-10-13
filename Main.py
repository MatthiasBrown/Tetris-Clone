import pygame, pygame.locals, sys
#from Tetromino import *
#from Helpers import *


mainClock = pygame.time.Clock()
pygame.init()
# fps = 30
# fpsclock = pygame.time.Clock()  # The FPS our game will run at.


window = pygame.display.set_mode((500, 800)) # Intializing the Window
pygame.display.set_caption("Tetris Clone")

class button():

    def __init__ (self, button_color, x2, y2, width2, height2, text ''):  # constructor for the buttom variables

        self.button_color = button_color
        self.x2 = x2
        self.y2 = y2
        self.width2 = width2
        self.height2 = height2
        self.text = text"

        def draw( self, win, outline = None):

            if outline:
                pygame.draw.rect( win, outline, (self.x2-2, self.y2-2, self.width2+4, self.height+4))
            pygame.draw.rect( win,self.button_color, (self.x2, self.y2, self.width2, self.height )

            if self.text != '':
                font = pygame.font.Sysfont('Comicsnas', 60):
                text = font.render(self.text, 1, (0, 0, 0))
                win.blit(text, (self.x2 + (self.width2 /2 -text.get_width()/2), self.y2 +(self.height2/2 - text.get_height()/2)))


        def isOver(self, pos):

            if pos[0] > self.x2 and pos[0] < self.x2 + self.width2:
                if pos[1] > self.y2 and pos[1] < self.y2 + self.height2:
                    return True

            return False

def game():

    running = True
    while running:
        draw_text('game', font, ])
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN: # If we've intialized the game to 30 fps that means we have to hold for 30 frames which is a second
                if key_input[pygame.K_q] and pygame.KMOD_CTRL :    # Control_Q is standard app exit on Arch based OS, and other tiling DE
                    run = False      


# run = True     # Starting the intial window run.
# while run:
#     key_input = pygame.key.get_pressed()
#     pygame.time.delay(100)
#     window.fill((0, 0, 0)) # TODO: Must fix this call
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#              run = False
#         #elif event.type == pygame.KEYDOWN: # If we've intialized the game to 30 fps that means we have to hold for 30 frames which is a second
#         if key_input[pygame.K_q] and pygame.KMOD_CTRL :    # Control_Q is standard app exit on Arch based OS, and other tiling DE
#                 run = False

#     pygame.draw.rect(window, ( 255, 0, 0), (x, y , width, height))
#     pygame.display.update()
pygame.quit()
