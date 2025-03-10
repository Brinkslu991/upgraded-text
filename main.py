# Pygame game template

import pygame
import sys
import config # Import the config module

def init_game ():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def draw_text(screen, font_pose, text='No text', font_size=10, font_name='DejaVuSans.ttf', font_color= (0,0,0), italic=False, bold=False):
    pygame.font.init()
    font = pygame.font.Font(font_name, font_size)
    font.set_italic(italic)
    font.set_bold(bold)
    img = font.render(text, False, font_color)
    screen.blit(img, font_pose)

  

def handle_events ():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True
def main():
    screen = init_game()
    clock = pygame.time.Clock() # Initialize the clock here

    running = True
    while running:
        running = handle_events()
        screen.fill(config.WHITE) # Use color from config

        draw_text(screen, [100,100], 'Lucas Brinks', 30, bold=True)

        draw_text(screen, [200,200], 'GOD PLEASE NOOOO', 30, italic=True)

        draw_text(screen, [300,300], 'This is FINE', 30)


        pygame.display.flip()
        
        # Limit the frame rate to the specified frames per second (FPS)
        clock.tick(config.FPS) # Use the clock to control the frame rate

        

    pygame.quit()

    sys.exit()

if __name__ == "__main__":
    main()
