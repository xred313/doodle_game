

import pygame
import random

pygame.init()

# screen settings
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("doodle noodle")

# set colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)



# icon images for eraser, pen and colouring
done_icon = pygame.image.load("done_icon.png")
#draw_icon = pygame.image.load("draw_icon.png")
erase_icon = pygame.image.load("rubber_icon.png")
colour_icon = pygame.image.load("colour_icon.png")

# icon images n size
icon_size = (50, 50)
done_icon = pygame.transform.scale(done_icon, icon_size)
#draw_icon = pygame.transform.scale(draw_icon, icon_size)
erase_icon = pygame.transform.scale(erase_icon, icon_size)
colour_icon = pygame.transform.scale(colour_icon, icon_size)

# icon positons
icon_margin = 20
done_icon_pos = (icon_margin, icon_margin * 4 + icon_size[1] * 3)
#draw_icon_pos = (icon_margin, icon_margin)
erase_icon_pos = (icon_margin, icon_margin * 2 + icon_size[1])
colour_icon_pos = (icon_margin, icon_margin * 3 + icon_size[1] * 2)

# Function to read a text file and return one randomly picked word from the file which contains a list of 1o words
def load_from_txt(filename):
    with open(filename, 'r') as file:
        words = file.readlines()
    return words

# function that picks a random word :)


def pick_random_word(words):
    return random.choice(words)




print("Hello, welcome to my program!")
filename = "ordlista.txt"
words = load_from_txt(filename)
random_word = pick_random_word(words).rstrip()
print("slumpmässigt valt ord:", random_word)

font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render(random_word, True, BLACK, WHITE)

textRect = text.get_rect()
textRect.center = (screen_width // 2, 25)



def main():
    # drawing and mouse code
    # variable to track drawing
    colour = 0
    colours = [(0, 0, 0), (0, 0, 255), (0, 255, 0), (255, 0, 0), (255, 255, 255)]
    drawing = False
    last_pos = None
    drawn_lines = [] # list to store the lines
    clock = pygame.time.Clock()    # frame rate

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left mouse button
                    if erase_icon_rect.collidepoint(event.pos):
                        drawing = False
                        drawn_lines = []

                    if done_icon_rect.collidepoint(event.pos):
                            running = False

                    elif colour_icon_rect.collidepoint(event.pos):
                        # implement colour selection logic here
                        colour = colour + 1
                        colour = colour % len(colours)    # modulo so the list repeats and you can switch between colours




                    else:
                        drawing = True
                        last_pos = event.pos
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing = False
                    last_pos = None
            elif event.type == pygame.MOUSEMOTION:
                if drawing:
                    current_pos = event.pos
                    if last_pos:
                        pygame.draw.line(screen, colours[colour], last_pos, current_pos, 30) # mouse n drawing line settings
                        drawn_lines.append((last_pos, current_pos, colours[colour]))
                    last_pos = current_pos



        for line in drawn_lines:
            pygame.draw.line(screen, line[2], line[0], line[1], 5)

    # draw a line from last_pos to current_pos
        # draw icons
       # screen.blit(draw_icon, draw_icon_pos)
        screen.blit(done_icon, done_icon_pos)
        screen.blit(erase_icon, erase_icon_pos)
        screen.blit(colour_icon, colour_icon_pos)
        pygame.draw.rect(screen, colours[colour], pygame.Rect(icon_margin, icon_margin, 65, 65 ))
        screen.blit(text, textRect)


        # define icon rectangles for collision detection
       # draw_icon_rect = draw_icon.get_rect(topleft = draw_icon_pos)
        done_icon_rect = done_icon.get_rect(topleft=done_icon_pos)
        erase_icon_rect = erase_icon.get_rect(topleft=erase_icon_pos)
        colour_icon_rect = colour_icon.get_rect(topleft = colour_icon_pos)


        pygame.display.flip()
        # Draw game elements here
        screen.fill(WHITE)
        clock.tick(60)


    pygame.quit()

if __name__ == "__main__":
    main()
