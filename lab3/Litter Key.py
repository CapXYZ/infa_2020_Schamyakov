import random
import pygame

pygame.init()

# Define the colors we will use in RGB format
color_dict = dict(
    BLACK=(0, 0, 0),
    WHITE=(255, 255, 255),
    BLUE=(0, 0, 255),
    GREEN=(0, 255, 0),
    RED=(255, 0, 0)
)
list_letter = 'aoг'

# Set the height and width of the screen
size = [400, 400]
screen = pygame.display.set_mode(size)

center = (200, 200)
center_x, center_y = center

pygame.display.set_caption("Учимся печатать")

def letter_draw_O(x, y, koof_size=1, ):
    pygame.draw.ellipse(screen, (255, 55, 0), (x - x // 2, y // 3,
                                               x, y + y // 3), 20)


def letter_draw_A(x, y, koof_size=1, ):
    pygame.draw.line(screen, (255, 55, 0), (x - x // 2, y + y // 2), (x, y - y // 2), 20)
    pygame.draw.line(screen, (255, 55, 0), (x, y - y // 2), (x + x // 2, y + y // 2), 20)
    pygame.draw.line(screen, (255, 55, 0), (x - x // 4, y), (x + x // 4, y), 20)


def letter_draw_G(x, y, koof_size=1, ):
    pygame.draw.line(screen, (255, 55, 0), (x - x // 4, y + y // 2), (x - x // 4, y - y // 2), 20)
    pygame.draw.line(screen, (255, 55, 0), (x - x // 4, y - y // 2), (x + x // 4, y - y // 2), 20)


def letter(l1):
    return random.choice(l1)

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

abc = {'a': letter_draw_A,
       'o': letter_draw_O,
       'г': letter_draw_G
       }

while not done:

    clock.tick(1)


    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    screen.fill((55, 255, 55))

    abc[letter(list_letter)](center_x, center_y)

    pygame.display.flip()

# Be IDLE friendly
pygame.quit()
