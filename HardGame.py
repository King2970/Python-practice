import random
import pygame
import cv2 as cv
import numpy as np

pygame.init()

screen = pygame.display.set_mode((699,729))
clock = pygame.time.Clock()
pygame.display.set_caption("Test")

Running = True
Moving = False
Timer = 200
round = 0
score = 0

font = pygame.font.SysFont('Ariel', 30)

def makeColor():
    color = (random.randint(1,255),random.randint(1,255),random.randint(1,255))

    return color

colorA = makeColor()
colorB = makeColor()
colorC = makeColor()
colorD = makeColor()
colorE = makeColor()
colorF = makeColor()
colorG = makeColor()
colorH = makeColor()
winner = random.randint(1,8)

def generateScore(round,time):
    if time < 100:
        generatedScore = 5*round
    elif time < 200:
        generatedScore = 3*round
    elif time < 1000:
        generatedScore = 2*round
    else:
        generatedScore = 10*round

    return generatedScore

while(Running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                Moving = True
        if event.type == pygame.K_RIGHT:
            Moving = True
        if event.type == pygame.K_LEFT:
            Moving = True
        if event.type == pygame.K_UP:
            Moving = True

    screen.fill((255, 255, 255))
    keys = pygame.key.get_pressed()
    roundnumber =0

    # Draws the board
    RectCenter = pygame.draw.rect(screen, (155, 155, 155), (233, 233, 233, 233))
    pygame.draw.rect(screen, colorA, (233, 0, 233, 233))
    pygame.draw.rect(screen, colorB, (0, 233, 233, 233))
    pygame.draw.rect(screen, colorC, (233, 466, 233, 233))
    pygame.draw.rect(screen, colorD, (466, 233, 233, 233))
    pygame.draw.rect(screen, colorE, (0, 0, 233, 233))
    pygame.draw.rect(screen, colorF, (466, 0, 233, 233))
    pygame.draw.rect(screen, colorG, (0, 466, 233, 233))
    pygame.draw.rect(screen, colorH, (466, 466, 233, 233))

    # Where player is
    character_rect = pygame.draw.circle(screen, (1, 1, 1), (350, 350), 50, -1)

    # Player move
    if keys[pygame.K_LEFT]:
        character_rect.x -= 233
    if keys[pygame.K_RIGHT]:
        character_rect.x += 233
    if keys[pygame.K_UP]:
        character_rect.y -= 233
    if keys[pygame.K_DOWN]:
        character_rect.y += 233

    # draw player
    if (winner == 1):
        pygame.draw.circle(screen, colorA, (character_rect.x, character_rect.y), 50)
    if (winner == 2):
        pygame.draw.circle(screen, colorB, (character_rect.x, character_rect.y), 50)
    if (winner == 3):
        pygame.draw.circle(screen, colorC, (character_rect.x, character_rect.y), 50)
    if (winner == 4):
        pygame.draw.circle(screen, colorD, (character_rect.x, character_rect.y), 50)
    if (winner == 5):
        pygame.draw.circle(screen, colorE, (character_rect.x, character_rect.y), 50)
    if (winner == 6):
        pygame.draw.circle(screen, colorF, (character_rect.x, character_rect.y), 50)
    if (winner == 7):
        pygame.draw.circle(screen, colorG, (character_rect.x, character_rect.y), 50)
    if (winner == 8):
        pygame.draw.circle(screen, colorH, (character_rect.x, character_rect.y), 50)
    pygame.draw.circle(screen, (1, 1, 1), (character_rect.x, character_rect.y), 50, 10)

    #Win states
    if (character_rect.y == 117) and (character_rect.x == 350) and winner == 1:
        colorA = makeColor()
        colorB = makeColor()
        colorC = makeColor()
        colorD = makeColor()
        colorE = makeColor()
        colorF = makeColor()
        colorG = makeColor()
        colorH = makeColor()
        new_winner = random.randint(1, 8)
        while (winner == new_winner):
            new_winner = random.randint(1, 8)
        winner = new_winner
        round += 1
        Timer += 50
        print(round)
        score += generateScore(round,Timer)

    if (character_rect.y == 350) and (character_rect.x == 117) and winner == 2:
        colorA = makeColor()
        colorB = makeColor()
        colorC = makeColor()
        colorD = makeColor()
        colorE = makeColor()
        colorF = makeColor()
        colorG = makeColor()
        colorH = makeColor()
        new_winner = random.randint(1, 8)
        while (winner == new_winner):
            new_winner = random.randint(1, 8)
        winner = new_winner
        round += 1
        Timer += 50
        print(round)
        score += generateScore(round,Timer)

    if (character_rect.y == 583) and (character_rect.x == 350) and winner == 3:
        colorA = makeColor()
        colorB = makeColor()
        colorC = makeColor()
        colorD = makeColor()
        colorE = makeColor()
        colorF = makeColor()
        colorG = makeColor()
        colorH = makeColor()
        new_winner = random.randint(1, 8)
        while (winner == new_winner):
            new_winner = random.randint(1, 8)
        winner = new_winner
        round += 1
        Timer += 50
        print(round)
        score += generateScore(round,Timer)

    if (character_rect.y == 350) and (character_rect.x == 583) and winner == 4:
        colorA = makeColor()
        colorB = makeColor()
        colorC = makeColor()
        colorD = makeColor()
        colorE = makeColor()
        colorF = makeColor()
        colorG = makeColor()
        colorH = makeColor()
        new_winner = random.randint(1, 8)
        while (winner == new_winner):
            new_winner = random.randint(1, 8)
        winner = new_winner
        round += 1
        Timer += 50
        print(round)
        score += generateScore(round,Timer)

    if (character_rect.y == 117) and (character_rect.x == 117) and winner == 5:
        colorA = makeColor()
        colorB = makeColor()
        colorC = makeColor()
        colorD = makeColor()
        colorE = makeColor()
        colorF = makeColor()
        colorG = makeColor()
        colorH = makeColor()
        new_winner = random.randint(1, 8)
        while (winner == new_winner):
            new_winner = random.randint(1, 8)
        winner = new_winner
        round += 1
        Timer += 50
        print(round)
        score += generateScore(round,Timer)

    if (character_rect.y == 117) and (character_rect.x == 583) and winner == 6:
        colorA = makeColor()
        colorB = makeColor()
        colorC = makeColor()
        colorD = makeColor()
        colorE = makeColor()
        colorF = makeColor()
        colorG = makeColor()
        colorH = makeColor()
        new_winner = random.randint(1, 8)
        while (winner == new_winner):
            new_winner = random.randint(1, 8)
        winner = new_winner
        round += 1
        Timer += 50
        print(round)
        score += generateScore(round,Timer)

    if (character_rect.y == 583) and (character_rect.x == 117) and winner == 7:
        colorA = makeColor()
        colorB = makeColor()
        colorC = makeColor()
        colorD = makeColor()
        colorE = makeColor()
        colorF = makeColor()
        colorG = makeColor()
        colorH = makeColor()
        new_winner = random.randint(1, 8)
        while (winner == new_winner):
            new_winner = random.randint(1, 8)
        winner = new_winner
        round += 1
        Timer += 50
        print(round)
        score += generateScore(round,Timer)

    if (character_rect.y == 583) and (character_rect.x == 583) and winner == 8:
        colorA = makeColor()
        colorB = makeColor()
        colorC = makeColor()
        colorD = makeColor()
        colorE = makeColor()
        colorF = makeColor()
        colorG = makeColor()
        colorH = makeColor()
        new_winner = random.randint(1, 8)
        while (winner == new_winner):
            new_winner = random.randint(1, 8)
        winner = new_winner
        round += 1
        Timer += 50
        print(round)
        score += generateScore(round,Timer)


    #Bottom screen info
    Timer_text = 'Timer: ' + str(Timer)
    text_surface = font.render(Timer_text, False, (0,0,0))
    screen.blit(text_surface, (0,699))
    Round_text = 'Round: ' + str(round)
    text_surface = font.render(Round_text, False, (0,0,0))
    screen.blit(text_surface, (233,699))
    Score_text = 'Score: ' + str(score)
    text_surface = font.render(Score_text, False, (0,0,0))
    screen.blit(text_surface, (466,699))

    #lose condition
    if (Timer == 0):
        #Camilla Jumpscare
        cap = cv.VideoCapture('Sprites/fire-emblem-camilla.mp4')
        fps = cap.get(cv.CAP_PROP_FPS)
        while cap.isOpened():
            ret, frame = cap.read()

            if not ret:
                pygame.quit()
                break
            frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

            frame_surface = pygame.surfarray.make_surface(np.rot90(frame))
            screen.blit(frame_surface, (35, 145))
            pygame.display.update()
            pygame.display.flip()
            clock.tick(fps)
        pygame.quit()
        exit(0)

    pygame.display.flip()
    Timer -= 1
    clock.tick(60)

pygame.quit()