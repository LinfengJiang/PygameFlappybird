# Pygame Beispiel
import os, sys, pygame, pygame.locals

# Initialisieren von PyGame
pygame.init()


# Fenster öffnen
screen =pygame.display.set_mode((640, 480))

# Titel für Fensterkopf
pygame.display.set_caption('Flapply Dot')

# Bildschirm Aktualisierungen einstellen
clock = pygame.time.Clock()

# solange die Variable True ist, soll das Spiel laufen
spielaktiv = True

# Spielzustand vorbereiten
x = 100
y = 240
f = 800
a1 = 800
a2 = 600
a3 = 400
a4 = 200
a5 = 0

# Schleife Hauptprogramm
while spielaktiv:

# Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT or (
                event.type == pygame.locals.KEYDOWN and event.key == pygame.locals.K_ESCAPE):
            # Spiel wird beendet!
            spielaktiv=False

# Aktualisieren des Zustands
#     if pygame.key.get_pressed()[pygame.locals.K_LEFT]:
#         x -= 1
#     elif pygame.key.get_pressed()[pygame.locals.K_RIGHT]:
#         x += 1
    if pygame.key.get_pressed()[pygame.locals.K_UP]:
        y -= 1
    elif pygame.key.get_pressed()[pygame.locals.K_DOWN]:
        y += 1
    else :
        if y > 10:
            y += 1
        else:
            y = 10
# Spiellogik hier integrieren

# Spielfeld/figur(en) zeichnen (davor Spielfeld löschen)
#    f -= 1
#     a1 = f
#     a2 = f-200
#     a3 = f-400
#     a4 = f-600
#     a5 = f-800
    a1 -= 1
    a2 -= 1
    a3 -= 1
    a4 -= 1
    a5 -= 1
    if a1 == -250:
        a1 = 800
    if a2 == -50:
        a2 = 800
    if a3 == -50:
        a3 = 800
    if a4 == -50:
        a4 = 800
    if a5 == -50:
        a5 = 800

    tupleAU = (a1,0,50,150)
    tupleAD = (a1,300,50,180)

    tupleBU = (a2, 0, 50, 200)
    tupleBD = (a2, 280, 50, 200)

    tupleCU = [a3, 0, 50, 150]
    tupleCD = [a3, 300, 50, 180]

    tupleDU = [a4, 0, 50, 150]
    tupleDD = [a4, 300, 50, 180]

    tupleEU = [a5, 0, 50, 150]
    tupleED = [a5, 300, 50, 180]

    screen.fill((64, 64, 64))  # Dark Gray
    pygame.draw.circle(screen, (192, 32, 32), (x,y), 10)

    pygame.draw.rect(screen,(32,192,32),tupleAU)
    pygame.draw.rect(screen,(32,192,32),tupleAD)
    pygame.draw.rect(screen, (32, 192, 32), tupleBU)
    pygame.draw.rect(screen, (32, 192, 32), tupleBD)
    pygame.draw.rect(screen, (32, 192, 32), tupleCU)
    pygame.draw.rect(screen, (32, 192, 32), tupleCD)
    pygame.draw.rect(screen, (32, 192, 32), tupleDU)
    pygame.draw.rect(screen, (32, 192, 32), tupleDD)
    pygame.draw.rect(screen, (32, 192, 32), tupleEU)
    pygame.draw.rect(screen, (32, 192, 32), tupleED)

# Fenster aktualisieren
    pygame.display.flip()

# Refresh-Zeiten festlegen
    clock.tick(60)

pygame.quit()