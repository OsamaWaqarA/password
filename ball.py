import pygame,random,os

pygame.init()
win  = pygame.display.set_mode((1300,750))
pygame.display.set_caption("Login")
win.fill((0,0,0))
clock = pygame.time.Clock()
font = pygame.font.SysFont('Calibri ',20)
lock = pygame.image.load(os.getcwd()+"\data\lock.png")


fps = 0
cfps = 0
sec = 0
oldsec = 0
x = 0
y = 0

add = 5

while True:
    import time
    date = str(time.ctime(time.time()))
    sec = date[17:20]
    if sec == oldsec:
        cfps += 1
    if sec != oldsec:
        oldsec = sec
        fps = cfps
        cfps = 0
    
    clock.tick(240)
    win.blit(lock,((150,200)))
    pygame.draw.rect(win,(0,0,0),(600,690,100,50))
    x = 0
    for i in range(0,1300):
        pygame.draw.rect(win,((int(random.random()*255)),(int(random.random()*255)),(int(random.random()*255))),(x,y,1,1))
        pygame.draw.rect(win,((int(random.random()*255)),(int(random.random()*255)),(int(random.random()*255))),(x,y+1,1,1))
        pygame.draw.rect(win,((int(random.random()*255)),(int(random.random()*255)),(int(random.random()*255))),(x,y+2,1,1))
        pygame.draw.rect(win,((int(random.random()*255)),(int(random.random()*255)),(int(random.random()*255))),(x,y+3,1,1))
        pygame.draw.rect(win,((int(random.random()*255)),(int(random.random()*255)),(int(random.random()*255))),(x,y+4,1,1))
        x += 1
    y += 5
    win.blit(font.render(("FPS "+str(fps)),True,(255,255,255)),(600,690))
  
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
    if y >= 750:
        break
