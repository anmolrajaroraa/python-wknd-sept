#pip3 install pygame

import pygame,random
pygame.init()

width = 500
height = 300
white = 255,255,255
red = 255,0,0
green = 0,255,0
blue = 0,0,255
x = 0
y = 0
x2 = random.randint(0,width - 50)
y2 = random.randint(0,height - 50)
moveX = 0
moveY = 0
frog = pygame.image.load('assets/frog.png')
sound = pygame.mixer.Sound("assets/point.wav")
counter = 0
snakeWidth = 50
snakeList = []
snakeLength = 1

screen = pygame.display.set_mode((width,height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                moveY = 1
                moveX = 0
            elif event.key == pygame.K_UP:
                moveY = -1
                moveX = 0
            elif event.key == pygame.K_LEFT:
                moveX = -1
                moveY = 0
            elif event.key == pygame.K_RIGHT:
                moveX = 1
                moveY = 0

    screen.fill(white)

    #screen, color, (x,y,width,height)
    rect1 = pygame.draw.rect(screen, red, (x,y,snakeWidth,50))
    rect2 = pygame.draw.rect(screen, white, (x2,y2,50,50))
    screen.blit(frog, (x2,y2))

    if rect1.colliderect(rect2):
        # print("Collision!!")
        x2 = random.randint(0,width - 50)
        y2 = random.randint(0,height - 50)
        sound.play()
        counter += 1
        snakeLength += 10
        # snakeWidth += 10

    msg = f"Score : {counter}"
    font = pygame.font.SysFont(None, 25, True, True)
    score = font.render(msg, True, red, None)
    screen.blit(score, (0,0))

    snakeList.append((x,y))
    if len(snakeList) > snakeLength:
        del snakeList[0]
    print(snakeList)

    for bodyPart in snakeList:
        pygame.draw.rect(screen, red, (bodyPart[0], bodyPart[1], 50,50))

    x = x + moveX
    y = y + moveY

    if x > width:
        x = -50
    elif y > height:
        y = -50
    elif x < -50:
        x = width
    elif y < -50:
        y = height

    pygame.display.update()