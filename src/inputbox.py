# A program to get user input, allowing backspace etc
# shown in a box in the middle of the screen
# Called by:
# import inputbox
# answer = inputbox.ask(screen, "Your name")
#
# Only near the center of the screen is blitted to

import pygame
import pygame.font
import pygame.event
import pygame.draw
import string
from pygame.locals import *
from refresh import *

def get_key() :
    while True :
        event = pygame.event.poll()
        if event.type == KEYDOWN :
            return event.key
        elif event.type == QUIT :
            exit()
        else:
            pass

def display_box(screen, message) :
    fontobject = pygame.font.Font(None,18)
    pygame.draw.rect(screen, (0,0,0),
                   ((screen.get_width() / 2) - 150,
                    (screen.get_height() / 2) - 10,
                    300,20), 0)
    pygame.draw.rect(screen, (255,255,255),
                  ((screen.get_width() / 2) - 152,
                    (screen.get_height() / 2) - 12,
                    304,24), 1)
    if len(message) != 0:
        screen.blit(fontobject.render(message, 1, (255,255,255)),
                ((screen.get_width() / 2) - 150, (screen.get_height() / 2) - 10))
    pygame.display.flip()

digits = (K_0,K_1,K_2,K_3,K_4,K_5,K_6,K_7,K_8,K_9,
    K_KP0,K_KP1,K_KP2,K_KP3,K_KP4,K_KP5,K_KP6,K_KP7,K_KP8,K_KP9)

def ask(screen, question) :
    pygame.font.init()
    current_string = []
    display_box(screen, question + ": " + string.join(current_string,""))

    done = False
    cont = 0
    ans = 0

    while not done:
        inkey = get_key()
        
        if inkey == K_BACKSPACE :
            current_string = current_string[0:-1]

            if cont>0 :
                cont = cont-1
                ans /= 10
        elif inkey == K_RETURN :
            
            if cont>0 :
                done = True
                break
        elif inkey in digits :
            
            if cont<6 :
                current_string.append(chr(inkey))
                cont = cont+1
                
                if K_0 <= inkey <= K_9 :
                    ans = ans*10+(inkey-K_0)
                if K_KP0 <= inkey <= K_KP9 :
                    ans = ans*10+(inkey-K_KP0)
        
        display_box(screen, question + ": " + string.join(current_string,""))
    
    return ans
