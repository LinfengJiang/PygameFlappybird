# Pygame
import os, sys, pygame, pygame.locals, random

import Mulitplayer.last_score as ls  # this funktion is use to upload the score into database
import Mulitplayer.register as reg  # this funktion is use to register an account into database

try:
    reg.register('test')  # regeister as ID 'test'
except BaseException as e:
    print(e)  # print any error

# Initialisieren von PyGame


display_width = 640
display_height = 480

WHITE = (255, 255, 255)
RED = (255, 0, 0)
bg_location = 'bg.png'


pygame.init()


class Button(object):
    # 输入文字，颜色，x偏移量，y偏移量，额外参数
    def __init__(self, text, color, x=None, y=None, **kwargs):
        self.surface = font.render(text, True, color)

        self.WIDTH = self.surface.get_width()
        self.HEIGHT = self.surface.get_height()

        if 'centered_x' in kwargs and kwargs['centered_x']:   #如果有要求在x轴居中显示
            self.x = display_width // 2 - self.WIDTH // 2
        else:
            self.x = x

        if 'centered_y' in kwargs and kwargs['centered_y']:
            self.y = display_height // 2 - self.HEIGHT // 2
        else:
            self.y = y

    def display(self):
        screen.blit(self.surface, (self.x, self.y))

    def check_click(self, position):
        x_match = position[0] > self.x and position[0] < self.x + self.WIDTH
        y_match = position[1] > self.y and position[1] < self.y + self.HEIGHT

        if x_match and y_match:
            return True
        else:
            return False


def starting_screen():
    global spielaktiv    #引入全局变量方便后面修改
    screen.blit(bg, (0, 0))

    game_title = font.render('Starting Screen', True, WHITE)

    screen.blit(game_title, (display_width // 2 - game_title.get_width() // 2, 150))

    play_button = Button('Play', RED, None, 350, centered_x=True)
    exit_button = Button('Exit', WHITE, None, 400, centered_x=True)

    play_button.display()
    exit_button.display()

    pygame.display.update()

    while True:

        if play_button.check_click(pygame.mouse.get_pos()):
            play_button = Button('Play', RED, None, 350, centered_x=True)
        else:
            play_button = Button('Play', WHITE, None, 350, centered_x=True)

        if exit_button.check_click(pygame.mouse.get_pos()):
            exit_button = Button('Exit', RED, None, 400, centered_x=True)
        else:
            exit_button = Button('Exit', WHITE, None, 400, centered_x=True)

        play_button.display()
        exit_button.display()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
        if pygame.mouse.get_pressed()[0]:
            if play_button.check_click(pygame.mouse.get_pos()):
                break
            if exit_button.check_click(pygame.mouse.get_pos()):
                #pygame.quit()
                spielaktiv = False
                break


screen = pygame.display.set_mode((display_width, display_height))
bg = pygame.image.load(bg_location)
font_addr = pygame.font.get_default_font()
font = pygame.font.Font(font_addr, 36)


# Fenster öffnen
screen = pygame.display.set_mode((640, 480))

# Titel für Fensterkopf
pygame.display.set_caption('Flapply Bird')

# Bildschirm Aktualisierungen einstellen
clock = pygame.time.Clock()

# solange die Variable True ist, soll das Spiel laufen
spielaktiv = True


# Wand Geschwendigkeit
geschwendigkeit = 1

# vogel koordinate_x_y
x = 200
y = 240

# Score
score = 0

# wand_1_x ,jede Wand beginnt von rechts, Abstand 150 ,Wand Breite 50
a1 = 640

# wand_2_x +200
a2 = 840

# wand_3_x
a3 = 1040

# wand_4_x
a4 = 1240

# braucht ein random Lücke,so gibt ein random Wands Lange l
list_l = [80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320]
lA = random.choice(list_l)
lB = random.choice(list_l)
lC = random.choice(list_l)
lD = random.choice(list_l)

starting_screen()

# Schleife Hauptprogramm
while spielaktiv:

    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT or (
                event.type == pygame.locals.KEYDOWN and event.key == pygame.locals.K_ESCAPE):
            # Spiel wird beendet!
            spielaktiv = False

    # Aktualisieren des Zustands
    #     if pygame.key.get_pressed()[pygame.locals.K_LEFT]:
    #         x -= 1
    #     elif pygame.key.get_pressed()[pygame.locals.K_RIGHT]:
    #         x += 1

    # vogel mit jede ein mal K_UP nach oben 10
    if pygame.key.get_pressed()[pygame.locals.K_UP]:
        # 调整上升速度
        y -= 2  # 10 ist zu Schwier ,testing....

    # vogel fallen immer
    else:
        if y > 0:
            y += 3
    # alle Wände immer nach links bewegen
    a1 -= geschwendigkeit
    a2 -= geschwendigkeit
    a3 -= geschwendigkeit
    a4 -= geschwendigkeit

    # wenn grans Wand aus screen, nach rechts zurück und gibt es ein neue Lücke
    if a1 == -50:
        a1 = 750
        lA = random.choice(list_l)
    if a2 == -50:
        a2 = 750
        lB = random.choice(list_l)
    if a3 == -50:
        a3 = 750
        lC = random.choice(list_l)
    if a4 == -50:
        a4 = 750
        lD = random.choice(list_l)

    # Scoreboard
    # When bird pass the wall,
    # that means the coordinates for the wall is C(brid) - thickness of walls
    if a1 == 150:
        score += 1
    if a2 == 150:
        score += 1
    if a3 == 150:
        score += 1
    if a4 == 150:
        score += 1

    rectA1 = pygame.Rect(a1, 0, 50, lA)
    rectA2 = pygame.Rect(a1, lA + 100, 50, 380 - lA)

    rectB1 = pygame.Rect(a2, 0, 50, lB)
    rectB2 = pygame.Rect(a2, lB + 100, 50, 380 - lB)

    rectC1 = pygame.Rect(a3, 0, 50, lC)
    rectC2 = pygame.Rect(a3, lC + 100, 50, 380 - lC)

    rectD1 = pygame.Rect(a4, 0, 50, lD)
    rectD2 = pygame.Rect(a4, lD + 100, 50, 380 - lD)

    # macht ein list, es hat alle tupel
    list_tuple = [rectA1, rectA2, rectB1, rectB2, rectC1, rectC2, rectD1, rectD2]

    screen.fill((64, 64, 64))  # Dark Gray

    bird = pygame.Rect(x, y, 10, 10)  # get a bird( Quadrat)
    pygame.draw.rect(screen, (192, 32, 32), bird)

    pygame.draw.rect(screen, (32, 192, 32), rectA1)
    pygame.draw.rect(screen, (32, 192, 32), rectA2)
    pygame.draw.rect(screen, (32, 192, 32), rectB1)
    pygame.draw.rect(screen, (32, 192, 32), rectB2)
    pygame.draw.rect(screen, (32, 192, 32), rectC1)
    pygame.draw.rect(screen, (32, 192, 32), rectC2)
    pygame.draw.rect(screen, (32, 192, 32), rectD1)
    pygame.draw.rect(screen, (32, 192, 32), rectD2)

    # Fenster aktualisieren
    pygame.display.flip()

    # if Bird out screen,end game, und etwas ausdrüken
    if y > 480 or y <= 0:
        print('Try again')
        spielaktiv = False
        # pygame.quit()

    # Refresh-Zeiten festlegen
    clock.tick(60)

    # Bestimmen es, ob es kollidieren werden
    for i in list_tuple:
        a = pygame.Rect.colliderect(bird, i)
        # wenn kollidieren enden game
        if a == 1:
            print('100G!! Overload!!!!')
            spielaktiv = False

# Wenn end der Spielen , ausdrüken der letzt Punkte
print('Your score is:', score)
# upload the score into database
ls.insert_last_score(score)

pygame.quit()
