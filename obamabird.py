import pygame
from random import randint

white = 255, 255, 255
black = 0, 0, 0
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255

try:
    pygame.init()
    pygame.font.init()
except:
    print("O modulo pygame nao foi inicializado com sucesso")

size = width, height = 1800, 900
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Obamium")

obama_seen = pygame.image.load("obama.png")
obama_hitbox = pygame.transform.scale(obama_seen, (100, 118))
trump = pygame.image.load("trump.png")
def text(msg, color, siz, x , y):
    font = pygame.font.SysFont(None, siz)
    text1 = font.render(msg, True, color)
    screen.blit(text1, [x, y])

def scene():
    pygame.draw.rect(screen, black, [0, 0, 1800, 50])
    pygame.draw.rect(screen, black, [0, 850, 1800, 50])
    
def game():
    placar = 0
    obsX_1 = 400
    obsX_2 = 1400
    vel_X1 = 5
    vel_X2 = -5
    colorect = red
    playing = True
    endgame = False
    obamarect = obama_seen.get_rect()
    obamarect_col = obama_hitbox.get_rect()
    obamarect.x = width/2 - 75
    obamarect.y = height/2 - 88.5
    obamarect_col.x = width/2 - 50
    obamarect_col.y = height/2 - 59
    speed = [3.5, 3.5]
    trumprect = trump.get_rect()
    trumprect.x = randint(150, 1650)
    trumprect.y = randint(150, 750)
    while playing:
        while endgame:
            screen.fill(white)
            placar = 0
            text("you lose, dumbass, press C to play again", red, 50, width/2-300, height/2)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False
                    endgame = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        playing = True
                        endgame = False
                        placar = 0
                        obsX_1 = 400
                        obsX_2 = 1400
                        vel_X1 = 5
                        vel_X2 = -5
                        colorect = red
                        game()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and (speed[1]) != -3:
                    speed[1] = -3
                if event.key == pygame.K_DOWN and (speed[1]) != 3:
                    speed[1] = 3
        obamarect = obamarect.move(speed)
        obamarect_col = obamarect_col.move(speed)
        if obamarect.left < 0 or obamarect.right > width:
            speed[0] = -speed[0]
        if obamarect.top < 50 or obamarect.bottom > 850:
            speed[1] = 0
        if obamarect_col.colliderect(trumprect):
            trumprect.x = randint(150, 1650)
            trumprect.y = randint(150, 750)
            placar += 1
        screen.fill(blue)
        screen.blit(trump, trumprect)
        screen.blit(obama_hitbox, obamarect_col)
        screen.blit(obama_seen, obamarect)
        top1 = pygame.draw.rect(screen, colorect, [obsX_1-200, 50, 50, 50])
        top2 = pygame.draw.rect(screen, colorect, [obsX_2-200, 50, 50, 50])
        bot1 = pygame.draw.rect(screen, colorect, [obsX_1+200, 800, 50, 50])
        bot2 = pygame.draw.rect(screen, colorect, [obsX_2+200, 800, 50, 50])
        mid1 = pygame.draw.rect(screen, colorect, [obsX_1, 425, 50, 50])
        mid2 = pygame.draw.rect(screen, colorect, [obsX_2, 425, 50, 50])
        if obsX_1 < 0 or obsX_1 == (obsX_2-50):
            if  placar != 0 and placar != 1 and placar != 2:
                if placar % 5 == 0 or (placar - 1) % 5 == 0 or (placar - 2) % 5 == 0:
                    if vel_X1 > 0:
                        vel_X1 = -7
                    elif vel_X1 < 0:
                        vel_X1 = 7
                else:   
                    if vel_X1 > 0:
                        vel_X1 = -5
                    elif vel_X1 < 0:
                        vel_X1 = 5
            else:   
                if vel_X1 > 0:
                    vel_X1 = -5
                elif vel_X1 < 0:
                    vel_X1 = 5
            colorect = randint(0, 255), randint(0, 255), randint(0, 255)
        if obsX_2 > (width-50) or obsX_2 == (obsX_1+50):
            if  placar != 0 and placar != 1 and placar != 2:
                if placar % 5 == 0 or (placar - 1) % 5 == 0 or (placar - 2) % 5 == 0:
                    if vel_X2 > 0:
                        vel_X2 = -7
                    elif vel_X2 < 0:
                        vel_X2 = 7
                else:   
                    if vel_X2 > 0:
                        vel_X2 = -5
                    elif vel_X2 < 0:
                        vel_X2 = 5
            else:   
                if vel_X2 > 0:
                    vel_X2 = -5
                elif vel_X2 < 0:
                    vel_X2 = 5
            colorect = randint(0, 255), randint(0, 255), randint(0, 255)
        obsX_1 += vel_X1
        obsX_2 += vel_X2
        scene()
        pygame.draw.rect(screen, white, [1730, 10, 60, 30])
        text("{}".format(placar), black, 30, 1755, 16)
        if obamarect_col.colliderect(top1) or obamarect_col.colliderect(top2) or obamarect_col.colliderect(bot1) or obamarect_col.colliderect(bot2) or obamarect_col.colliderect(mid1) or obamarect_col.colliderect(mid2):
            endgame = True
        pygame.display.flip()
game()
