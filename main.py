# Pygame game template

import pygame
import sys
import config # Import the config module

def init_game ():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def show_name(first_name, last_name, middle_name=None):
    if middle_name:
        output = f"{first_name} {middle_name} {last_name}"
    else:
        output = f"{first_name} {last_name}"
    return output

def draw_text(screen):
    draw_text(screen)

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

    font_name = "FreeMono.ttf"
    font_color1 = config.DARKRED  
    font_color2 = config.PALETURQUOISE
    font_color3 = config.SAPPHIRE
    font_size_normal = 36
    font_size_bold_italic = 30
    font_size_custom = 48

    custom_font_name = 'DejaVuSans.ttf'

    text_position_1 = [50, 50]
    text_position_2 = [225, 135]
    text_position_3 = [220, 370]

    running = True
    while running:
        running = handle_events()
        screen.fill(config.WHITE) # Use color from config

        draw_text(screen, 'Hello, World', font_size_normal, font_name, font_color1, text_position_1, italic=True)

        draw_text(screen, "The Better Looking Text", font_size_bold_italic, custom_font_name, font_color2, text_position_2, italic=True, bold=True)

        print(show_name('Lucas', 'Brinks'))

        pygame.display.flip()
        
        # Limit the frame rate to the specified frames per second (FPS)
        clock.tick(config.FPS) # Use the clock to control the frame rate

        

    pygame.quit()

    sys.exit()

if __name__ == "__main__":
    main()
