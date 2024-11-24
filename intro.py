import pygame,random,os

pygame.init()
win  = pygame.display.set_mode((1300,750))
pygame.display.set_caption("Login")
win.fill((0,0,0))
clock = pygame.time.Clock()
x = -1
y = 10
x1 = x
y1 = y
count = 0
t = 0
nev = False
music = pygame.mixer.music.load(os.getcwd()+"\data\wall.mp3")
pygame.mixer.music.play(1)

for i in range(0,1000):
    x = -1
    y  = int(random.random()*750)
    x1 = x
    y1 = y
    t += 20
    if count >= 255:
        count = 255
        nev = True
    if count < 0:
        count = 0
        nev = False
    c = 255-count
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        if nev == False:
            count += 1
        else:
            count -= 1
        if count >= 255:
            count = 255
            nev = True
        if count < 0:
            count = 0
            nev = False
        c = 255-count
        clock.tick(t)
        x = x1
        y = y1
        x1 += 15
        if count % 2 == 0:
            y1 += int(random.random()*10)
        else:
            y1 -= int(random.random()*10)
        pygame.draw.aalines(win,(int(random.random()*255),int(random.random()*255),int(random.random()*255)),False,((x,y),(x1,y1)),blend = 1)
        
        if x1 >= 1300:
            break

        pygame.display.update()

pygame.quit()
quit()
