import random, sys
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
list_letter = 'aoгентип'

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
#Буква О

def letter_draw_U(x, y, koof_size=1, ):
    pygame.draw.line(screen, (255, 55, 0), (x - x // 4, y + y // 2), (x - x // 4, y - y // 2), 20)
    pygame.draw.line(screen, (255, 55, 0), (x - x // 4, y - y // 2), (x + x // 4, y - y // 2), 20)
#Буква Г

def letter_draw_E(x, y, koof_size=1, ):
    pygame.draw.line(screen, (255, 55, 0), (x - x // 4, y + y // 2), (x - x // 4, y - y // 2), 20)
    pygame.draw.line(screen, (255, 55, 0), (x - x // 4, y - y // 2), (x + x // 3, y - y // 2), 20)
    pygame.draw.line(screen, (255, 55, 0), (x - x // 4, y + y // 2), (x + x // 3, y + y // 2), 20)
    pygame.draw.line(screen, (255, 55, 0), (x - x // 4, y), (x + x // 5, y), 20)
#Буква Е

def letter_draw_N(x, y, koof_size=1, ):
    pygame.draw.line(screen, (255, 55, 0), (x - x // 4, y + y // 2), (x - x // 4, y - y // 2), 20)
    pygame.draw.line(screen, (255, 55, 0), (x - x // 4, y), (x + x // 5, y), 20)
    pygame.draw.line(screen, (255, 55, 0), (x + x // 4, y + y // 2), (x + x // 4, y - y // 2), 20)
#Буква Н

def letter_draw_T(x, y, koof_size=1, ):
    pygame.draw.line(screen, (255, 55, 0), (x, y + y // 2), (x, y - y // 2), 20)
    pygame.draw.line(screen, (255, 55, 0), (x - x // 3, y - y // 2), (x + x // 3, y - y // 2), 20)
#Буква Т

def letter_draw_B(x, y, koof_size=1, ):
    pygame.draw.line(screen, (255, 55, 0), (x - x // 4, y + y // 2), (x - x // 4, y - y // 2), 20)
    pygame.draw.line(screen, (255, 55, 0), (x - x // 4, y + y // 2), (x + x // 4, y - y // 2), 20)
    pygame.draw.line(screen, (255, 55, 0), (x + x // 4, y + y // 2), (x + x // 4, y - y // 2), 20)
#Буква И

def letter_draw_G(x, y, koof_size=1, ):
    pygame.draw.line(screen, (255, 55, 0), (x - x // 4, y + y // 2), (x - x // 4, y - y // 2), 20)
    pygame.draw.line(screen, (255, 55, 0), (x - x // 4, y - y // 2), (x + x // 4, y - y // 2), 20)
    pygame.draw.line(screen, (255, 55, 0), (x + x // 4, y + y // 2), (x + x // 4, y - y // 2), 20)
#Буква П

def letter(l1):
    return random.choice(l1)


# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

abc = {'a': letter_draw_A,
       'o': letter_draw_O,
       'г': letter_draw_U,
       'е': letter_draw_E,
       'н': letter_draw_N,
       'т': letter_draw_T,
       'и': letter_draw_B,
       'п': letter_draw_G
       }
key_dict = {'a': pygame.K_f,
            'o': pygame.K_j,
            'г': pygame.K_u,
            'е': pygame.K_t,
            'н': pygame.K_y,
            'т': pygame.K_n,
            'и': pygame.K_b,
            'п': pygame.K_g
            }
symbal = letter(list_letter)
abc[symbal](center_x, center_y)
while not done:

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == key_dict[symbal]:
                screen.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
                symbal = letter(list_letter)
                abc[symbal](center_x, center_y)
    pygame.display.update()
    clock.tick(30)

    pygame.display.flip()

# Be IDLE friendly
pygame.quit()
