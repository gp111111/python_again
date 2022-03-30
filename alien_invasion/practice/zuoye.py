import pygame
import sys

def blank_screen():
    """monitor the key event and show the response"""
    pygame.init()
    screen = pygame.display.set_mode((700,700))
    pygame.display.set_caption("KEY EVENTS MONITOR")

    bg_color = (168,235,18)

    while True:
        
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == 32:#点空格退出
                    sys.exit()
                print(event.key)

        screen.fill(bg_color)
        pygame.display.flip()

blank_screen()