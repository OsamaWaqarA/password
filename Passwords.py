import pygame, os, pyperclip, random, time,qrcode#add playsound
from cryptography.fernet import Fernet

pygame.init()

info = open(os.getcwd()+"\data\Ü¥¦äæáÖãÜÒÝÚ×ãÒØÚÝÚäåÚÜÖéáÚÒÝÚØÖåÚäÔÙ.txt","rb")
key = info.readline()
ans = info.readline()
info.close
f = Fernet(key)
ans = ans = f.decrypt(ans)
ans = ans.decode()
enter = True
strike = 0

ran = int(ans[0:6])
master = int(ans[6:12])
master = master - ran

mon = (time.ctime()[4:7])#month
date = int(time.ctime()[8:11])#date
year = int(time.ctime()[22:24])#year

mon_lower = mon.lower()


if mon_lower == "jan":
    month_number = 1
elif mon_lower == "feb":
    month_number = 2
elif mon_lower == "mar":
    month_number = 3
elif mon_lower == "apr":
    month_number = 4
elif mon_lower == "may":
    month_number = 5
elif mon_lower == "jun":
    month_number = 6
elif mon_lower == "jul":
    month_number = 7
elif mon_lower == "aug":
    month_number = 8
elif mon_lower == "sep":
    month_number = 9
elif mon_lower == "oct":
    month_number = 10
elif mon_lower == "nov":
    month_number = 11
elif mon_lower == "dec":
    month_number = 12

if date > int(str(master)[2:4]) and int(str(master)[4:6]) == int(month_number) and year >= int(str(master)[0:2]):
    enter = False
if int(month_number) > int(str(master)[4:6]) or year > int(str(master)[0:2]):
    enter = False
if int(str(master)[0:2]) > (year + 2):
    music = pygame.mixer.music.load(os.getcwd()+"\data\smart.mp3")
    pygame.mixer.music.play(1)
    enter = False
    pygame.time.delay(5000)







if enter == True:

    free = pygame.font.SysFont('ink free',50)
    s_free = pygame.font.SysFont('ink free',25)
    font = pygame.font.SysFont('Agency FB',25)
    big_font = pygame.font.SysFont('Agency FB',100)

    run = True
    login = False
    storage = ["Store:"]
    detail = ["","","",""]
    user = False
    word = False
    search = ""
    pass_show = ""

    win  = pygame.display.set_mode((1300,750))
    pygame.display.set_caption("Login")
    win.fill((0,0,0))

    l_man = free.render("Password Manager",True,(255,140,0))
    s_man = s_free.render("Password Manager",True,(255,140,0))
    username = font.render("Username :",True,(255,255,255))
    password = font.render("Password :",True,(255,255,255))
    log = font.render("Login",True,(255,100,0))
    fgot = font.render("Forgot you password",True,(255,100,0))
    new = font.render("Are you new",True,(255,100,0))
    c_user = font.render("Create New Username",True,(255,255,255))
    c_password = font.render("Create New Password",True,(255,255,255))
    c_date = font.render("What is date of your birth (DD)",True,(255,255,255))
    c_luck = font.render("What is your favourite number",True,(255,255,255))
    create = font.render("Create Account",True,(255,255,255))
    f_user = font.render("What is your Username",True,(255,255,255))
    recover = font.render("Recover Account",True,(200,255,200))
    add = big_font.render("+",True,(255,0,0))
    main_user = font.render("Lenght of password",True,(255,255,255))
    main_lenght =font.render("Name of password",True,(255,255,255))
    main_create = font.render("Create Password",True,(255,255,255))


    square = pygame.image.load(os.getcwd()+"\data\square.png")
    squareL = pygame.image.load(os.getcwd()+"\data\square_l.png")
    squareM = pygame.image.load(os.getcwd()+"\data\square_m.png")

    win.blit(l_man,(620,333))
    pygame.display.update()
    pygame.time.delay(1)
    clock = pygame.time.Clock()

    def forgot():
        detail = ["","","",""]
        detail_show = [font.render("",True,(255,255,255)),font.render("",True,(255,255,255)),font.render("",True,(255,255,255)),font.render("",True,(255,255,255))]
        run = True
        listen = False
        count = 0
        while run:
            clock.tick(60)

            if count != 0:
                count+=1
                if count >= 120:
                    count = 0

            if listen == False:
                op = 4
            
            for i in range(0,4):
                detail_show[i] = font.render(detail[i],True,(255,255,255))
            
            pygame.display.update()
            win.fill((50,50,50))
            
            win.blit(s_man,(10,10))
            win.blit(f_user,(390,150))
            win.blit(c_password,(400,300))
            win.blit(c_date,(325,450))
            win.blit(c_luck,(325,600))

            win.blit(detail_show[0],(600,150))
            win.blit(detail_show[1],(600,300))
            win.blit(detail_show[2],(600,450))
            win.blit(detail_show[3],(600,600))

            pygame.draw.rect(win,((255,255,255)),(900,650,150,30),1)
            win.blit(recover,(905,657))
        
            if op == 0:
                pygame.draw.rect(win,((255,0,0)),(600,150,200,20),1)
            else:
                pygame.draw.rect(win,((255,255,255)),(600,150,200,20),1)
            if op == 1:
                pygame.draw.rect(win,((255,0,0)),(600,300,200,20),1)
            else:
                pygame.draw.rect(win,((255,255,255)),(600,300,200,20),1)
            if op == 2:
                pygame.draw.rect(win,((255,0,0)),(600,450,200,20),1)
            else:
                pygame.draw.rect(win,((255,255,255)),(600,450,200,20),1)
            if op == 3:
                pygame.draw.rect(win,((255,0,0)),(600,600,200,20),1)
            else:
                pygame.draw.rect(win,((255,255,255)),(600,600,200,20),1)

            click1,click2,click3 = pygame.mouse.get_pressed()
            if click1 == True:
                pos = pygame.mouse.get_pos()
                line = str(pos)
                coma = int(line.find(","))
                fbracket = int(line.find("("))
                lbracket = int(line.find(")"))
                x = int(line[fbracket + 1:coma])
                y = int(line[coma+2:lbracket])
                if x >= 600 and x <= 800:
                    if y >= 150 and y <= 180:
                        op = 0
                        listen = True
                        pygame.mouse.set_visible(0)
                if x >= 600 and x <= 800:
                    if y >= 300 and y <= 320:
                        op = 1
                        listen = True
                        pygame.mouse.set_visible(0)
                if x >= 600 and x <= 800:
                    if y >= 450 and y <= 480:
                        op = 2
                        listen = True
                        pygame.mouse.set_visible(0)
                if x >= 600 and x <= 800:
                    if y >= 600 and y <= 620:
                        op = 3
                        listen = True
                        pygame.mouse.set_visible(0)
                if x >= 900 and x <= 1050:
                    if y >= 650 and y <= 680:
                        count = 0
                        for i in range(0,2):
                            if len(detail[i]) >= 5:
                                count += 1
                        if len(detail[2]) > 0 and len(detail[3]) > 0:
                            count += 2
                        if count == 4:
                            search = ""
                            
                            for i in range(0,len(detail[0])):
                                search += chr(ord(detail[0][i:i+1])+113)
                                
                            try:
                                search = search+".txt"
                                info = open(os.getcwd()+"\data\Ü¥¦"+search,"rb")
                            except FileNotFoundError:
                                music = pygame.mixer.music.load(os.getcwd()+"\data\gone_for_good.mp3")
                                pygame.mixer.music.play(1)
                                pygame.time.delay(6500)
                                pygame.quit()
                                quit
                            key = info.readline()
                            real = info.readline()
                            dob = info.readline()
                            fav = info.readline()
                            store = info.readline()
                            info.close()

                            f = Fernet(key)
                            real = real = f.decrypt(real)
                            real = real.decode()

                            dob = dob = f.decrypt(dob)
                            dob = dob.decode()

                            fav = fav = f.decrypt(fav)
                            fav = fav.decode()

                            store = store = f.decrypt(store)
                            store = store.decode()

                            if dob == detail[2] and fav == detail[3]:
                                key = key = Fernet.generate_key()
                                f = Fernet(key)

                                
                                detail[1] = detail[1].encode()
                                detail[1] = f.encrypt(detail[1])

                                dob = dob.encode()
                                dob = f.encrypt(dob)

                                fav = fav.encode()
                                fav = f.encrypt(fav)

                                store = store.encode()
                                store = f.encrypt(store)
                                
                                info = open(os.getcwd()+"\data\Ü¥¦"+search,"wb")
                                
                                info.write(key)
                                info.write(b'\n')
                                info.write(detail[1])
                                info.write(b'\n')
                                info.write(dob)
                                info.write(b'\n')
                                info.write(fav)
                                info.write(b'\n')
                                info.write(store)

                                info.close()
                                pygame.quit()
                                quit
                        else:
                            music = pygame.mixer.music.load(os.getcwd()+"\data\long.mp3")
                            pygame.mixer.music.play(1)
                            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if listen == True:
                        if event.key == pygame.K_RETURN:
                            listen = False
                            pygame.mouse.set_visible(1)
                        elif event.key == pygame.K_BACKSPACE:
                            detail[op] = detail[op][0:-1]
                        else:
                            detail[op] += event.unicode
                        if len(detail[op]) > 20:
                            detail[op] = detail[op][0:-1]
                            if count == 0:
                                music = pygame.mixer.music.load(os.getcwd()+"\data\limit.mp3")
                                pygame.mixer.music.play(1)
                                count += 1
                            
                        
                            
    def newaccount():
        detail = ["","","","","Store:"]
        detail_show = [font.render("",True,(255,255,255)),font.render("",True,(255,255,255)),font.render("",True,(255,255,255)),font.render("",True,(255,255,255))]
        run = True
        listen = False
        count = 0
        while run:
            clock.tick(60)

            if count != 0:
                count+=1
                if count >= 120:
                    count = 0

            if listen == False:
                op = 4
            
            for i in range(0,4):
                detail_show[i] = font.render(detail[i],True,(255,255,255))
            
            pygame.display.update()
            win.fill((50,50,50))
            
            win.blit(s_man,(10,10))
            win.blit(c_user,(400,150))
            win.blit(c_password,(400,300))
            win.blit(c_date,(325,450))
            win.blit(c_luck,(325,600))

            win.blit(detail_show[0],(600,150))
            win.blit(detail_show[1],(600,300))
            win.blit(detail_show[2],(600,450))
            win.blit(detail_show[3],(600,600))

            pygame.draw.rect(win,((255,255,255)),(900,650,150,30),1)
            win.blit(create,(910,657))
        
            if op == 0:
                pygame.draw.rect(win,((255,0,0)),(600,150,200,20),1)
            else:
                pygame.draw.rect(win,((255,255,255)),(600,150,200,20),1)
            if op == 1:
                pygame.draw.rect(win,((255,0,0)),(600,300,200,20),1)
            else:
                pygame.draw.rect(win,((255,255,255)),(600,300,200,20),1)
            if op == 2:
                pygame.draw.rect(win,((255,0,0)),(600,450,200,20),1)
            else:
                pygame.draw.rect(win,((255,255,255)),(600,450,200,20),1)
            if op == 3:
                pygame.draw.rect(win,((255,0,0)),(600,600,200,20),1)
            else:
                pygame.draw.rect(win,((255,255,255)),(600,600,200,20),1)

            click1,click2,click3 = pygame.mouse.get_pressed()
            if click1 == True:
                pos = pygame.mouse.get_pos()
                line = str(pos)
                coma = int(line.find(","))
                fbracket = int(line.find("("))
                lbracket = int(line.find(")"))
                x = int(line[fbracket + 1:coma])
                y = int(line[coma+2:lbracket])
                if x >= 600 and x <= 800:
                    if y >= 150 and y <= 180:
                        op = 0
                        listen = True
                        pygame.mouse.set_visible(0)
                if x >= 600 and x <= 800:
                    if y >= 300 and y <= 320:
                        op = 1
                        listen = True
                        pygame.mouse.set_visible(0)
                if x >= 600 and x <= 800:
                    if y >= 450 and y <= 480:
                        op = 2
                        listen = True
                        pygame.mouse.set_visible(0)
                if x >= 600 and x <= 800:
                    if y >= 600 and y <= 620:
                        op = 3
                        listen = True
                        pygame.mouse.set_visible(0)
                if x >= 900 and x <= 1050:
                    if y >= 650 and y <= 680:
                        count = 0
                        for i in range(0,2):
                            if len(detail[i]) >= 5:
                                count += 1
                        if len(detail[2]) > 0 and len(detail[3]) > 0:
                            count += 2
                        if count == 4:
                            search = ""
                            key = key = Fernet.generate_key()
                            f = Fernet(key)
                            for i in range(1,5):
                                detail[i] = detail[i].encode()
                                detail[i] = f.encrypt(detail[i])
                            
                            for i in range(0,len(detail[0])):
                                search += chr(ord(detail[0][i:i+1])+113)
                            search += ".txt"
                            info = open(os.getcwd()+"\data\Ü¥¦"+search,"ab")
                            info.write(key)
                            for i in range(1,5):
                                info.write(b'\n')
                                info.write(detail[i])
                            info.close()
                            music = pygame.mixer.music.load(os.getcwd()+"\data\successfully.mp3")
                            pygame.mixer.music.play(1)
                            #playsound.playsound("successfully.mp3")
                            pygame.time.delay(2000)
                            pygame.quit()
                            quit
                        else:
                            music = pygame.mixer.music.load(os.getcwd()+"\data\long.mp3")
                            pygame.mixer.music.play(1)
                                

                

                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if listen == True:
                        if event.key == pygame.K_RETURN:
                            listen = False
                            pygame.mouse.set_visible(1)
                        elif event.key == pygame.K_BACKSPACE:
                            detail[op] = detail[op][0:-1]
                        else:
                            detail[op] += event.unicode
                        if len(detail[op]) > 20:
                            detail[op] = detail[op][0:-1]
                            if count == 0:
                                music = pygame.mixer.music.load(os.getcwd()+"\data\limit.mp3")
                                pygame.mixer.music.play(1)
                                count += 1
            
            

    def drawpass(user,word,logbutton):
        box1 = font.render(detail[0],True,(255,255,255))
        box2 = font.render(pass_show,True,(255,255,255))
        win.fill((100,50,50))
        win.blit(s_man,(10,10))
        win.blit(username,((400,300)))
        win.blit(password,((400,400)))
        win.blit(box1,((500,303)))
        win.blit(box2,((501,405)))

        #pygame.draw.rect(win,((255,255,255)),(680,485,188,60),1)
        win.blit(squareL,((578,413)))
        win.blit(fgot,((688,505)))

        #pygame.draw.rect(win,((255,255,255)),(355,485,140,60),1)
        win.blit(squareM,((278,413)))
        win.blit(new,((375,505)))
        
        if user == True:
            pygame.draw.rect(win,((255,0,0)),(500,300,200,20),1)
        else:
            pygame.draw.rect(win,((255,255,255)),(500,300,200,20),1)
        if word == True:
            pygame.draw.rect(win,((255,0,0)),(500,400,200,20),1)
        else:
            pygame.draw.rect(win,((255,255,255)),(500,400,200,20),1)
            
        if logbutton == True:
            #pygame.draw.rect(win,((255,255,255)),(530,485,93,60),1)
            win.blit(square,((478,413)))
            win.blit(log,((552,505)))
        pygame.display.update()
    while run:
        clock.tick(60)
        click1,click2,click3 = pygame.mouse.get_pressed()
        if click1 == True:
            pos = pygame.mouse.get_pos()
            line = str(pos)
            coma = int(line.find(","))
            fbracket = int(line.find("("))
            lbracket = int(line.find(")"))
            x = int(line[fbracket + 1:coma])
            y = int(line[coma+2:lbracket])
            if x >= 500 and x <= 700:
                if y >= 300 and y <= 320:
                    user = True
                    pygame.mouse.set_visible(0)
            if x >= 500 and x <= 700:
                if y >= 400 and y <= 420:
                    word = True
                    pygame.mouse.set_visible(0)



            if x >= 680 and x <= 868:#pygame.draw.rect(win,((255,255,255)),(680,485,188,60),1)  forget
                if y >= 485 and y <= 545:
                    forgot()
                    
            if x >= 355 and x <= 495:#pygame.draw.rect(win,((255,255,255)),(355,485,140,60),1)  new
                if y >= 485 and y <= 545:
                    newaccount()


                    
            if x >= 530 and x <= 623:
                if y >= 485 and y <= 545:
                    if logbutton == True:
                        search = ""
                        for i in range(0,len(detail[0])):
                            search += chr(ord(detail[0][i:i+1])+113)
                            
                        try:
                            search = search+".txt"
                            info = open(os.getcwd()+"\data\Ü¥¦"+search,"rb")
                        except FileNotFoundError:
                            music = pygame.mixer.music.load(os.getcwd()+"\data\wrong.mp3")
                            pygame.mixer.music.play(1)
                            win.fill((50,54,133))
                            win.blit((free.render("The username or password password is incorrect",True,(205,201,122))),(200,450))
                            pygame.display.update()
                            pygame.time.delay(5000)
                            pygame.quit()
                            quit
                        key = info.readline()
                        real = info.readline()
                        dob = info.readline()
                        fav = info.readline()
                        store = info.readline()
                        info.close()

                        f = Fernet(key)
                        real = real = f.decrypt(real)
                        real = real.decode()

                        dob = dob = f.decrypt(dob)
                        dob = dob.decode()

                        fav = fav = f.decrypt(fav)
                        fav = fav.decode()

                        store = store = f.decrypt(store)
                        store = store.decode()

                        if "\n" in real:
                            real = real[0:-1]

                        if "\n" in dob:
                            dob = dob[0:-1]

                        if "\n" in fav:
                            fav = fav[0:-1]

                        if "\n" in store:
                            store = store[0:-1]

                        if real == detail[1]:
                            login = True
                        else:
                            login = False
                        run = False

                        storage = [""]
                        storage[0] = store

                        key = key = Fernet.generate_key()
                        f = Fernet(key)

                        real = real.encode()
                        real = f.encrypt(real)

                        dob = dob.encode()
                        dob = f.encrypt(dob)

                        fav = fav.encode()
                        fav = f.encrypt(fav)

                        store = store.encode()
                        store = f.encrypt(store)
                        
                        info = open(os.getcwd()+"\data\Ü¥¦"+search,"wb")
                        
                        info.write(key)
                        info.write(b'\n')
                        info.write(real)
                        info.write(b'\n')
                        info.write(dob)
                        info.write(b'\n')
                        info.write(fav)
                        info.write(b'\n')
                        info.write(store)

                        info.close()


                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    word = False
                    user = False
                    pygame.mouse.set_visible(1)
                if user == True and len(detail[0]) < 20:
                    detail[0] += event.unicode
                if word == True and len(detail[1]) < 27:
                    detail[1] += event.unicode
                    pass_show += "*"
                if event.key == pygame.K_BACKSPACE and user == True:
                    detail[0] = detail[0][0:-2]
                if event.key == pygame.K_BACKSPACE and word == True:
                    detail[1] = detail[1][0:-2]
                    pass_show = pass_show[0:-2]

        if len(detail[0]) >= 5 and len(detail[1]) >= 5:
            logbutton = True
        else:
            logbutton = False
                    
        drawpass(user,word,logbutton)

    #______________________________________________________________________________________________________________--------------------------------------_______________________________________----------------------------------_________________________________

    run = True
    op = 0
    size = [0,0]
    storage_show = []
    select = 61
    choose = 2
    count = 0
    detail = ["",""]
    warn = [False,False]
    detail_show = [font.render("",True,(255,255,255)),font.render("",True,(255,255,255)),font.render("",True,(255,255,255)),font.render("",True,(255,255,255))]
    listen = False

    if len(storage[0]) != 6:
        storage[0] = storage[0].replace("Store:","")
        while run:
            if "," in storage[0]:
                coma = int(storage[0].find(","))
                storage.append(storage[0][0:coma])
                storage[0] = storage[0][coma+1:len(storage[0])]
            else:
                run = False
        x = 50
        y = 100
        r = 255
        g = 0
        b = 155
        for i in range(0,len(storage)):
            storage_show.append(font.render(storage[i],True,(255,255,255)))
            r += 20
            g += 20
            b += 20
            if r >= 255:
                r = 0
            if g >= 255:
                g = 0
            if b >= 255:
                b = 0

    run = True
        
        

    def draw():
        clock.tick(60)
        win.blit(s_man,(10,10))
        pygame.display.update()
        win.fill((100,150,165))

    if login == True:
        while run:
            draw()
            for i in range(0,2):
                detail_show[i] = font.render(detail[i],True,(255,255,255))
            win.blit(detail_show[0],(600,150))
            win.blit(detail_show[1],(600,300))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if listen == True:
                        if event.key == pygame.K_RETURN:
                            listen = False
                            pygame.mouse.set_visible(1)
                        elif event.key == pygame.K_BACKSPACE:
                            detail[choose] = detail[choose][0:-1]
                        else:
                            detail[choose] += event.unicode 
                        if len(detail[choose]) > 20:
                            detail[choose] = detail[choose][0:-1]
                            if count == 0:
                                music = pygame.mixer.music.load(os.getcwd()+"\data\limit.mp3")
                                pygame.mixer.music.play(1)
                                count += 1
            if op == 1:
                if detail[1] != "":
                    if int(detail[1]) > 1500 and warn[0] == False and int(detail[1]) <= 2300:
                        music = pygame.mixer.music.load(os.getcwd()+"\data\hard.mp3")
                        pygame.mixer.music.play(1)
                        warn[0] = True
                    if int(detail[1]) > 2300 and warn[1] == False:
                        music = pygame.mixer.music.load(os.getcwd()+"\data\disable.mp3")
                        pygame.mixer.music.play(1)
                        warn[0] = True
                        warn[1] = True
                win.blit(main_lenght,(420,150))
                win.blit(main_user,(420,300))
                pygame.draw.rect(win,((255,255,255)),(900,650,150,30),1)
                win.blit(main_create,(905,657))
                if listen == False:
                    choose = 2
                if count != 0:
                    count+=1
                    if count >= 120:
                        count = 0
                if  choose == 0:
                    pygame.draw.rect(win,((255,0,0)),(600,150,200,20),1)
                else:
                    pygame.draw.rect(win,((255,255,255)),(600,150,200,20),1)
                if choose == 1:
                    pygame.draw.rect(win,((255,0,0)),(600,300,200,20),1)
                else:
                    pygame.draw.rect(win,((255,255,255)),(600,300,200,20),1)
                click1,click2,click3 = pygame.mouse.get_pressed()
                if click1 == True:
                    pos = pygame.mouse.get_pos()
                    line = str(pos)
                    coma = int(line.find(","))
                    fbracket = int(line.find("("))
                    lbracket = int(line.find(")"))
                    x = int(line[fbracket + 1:coma])
                    y = int(line[coma+2:lbracket])
                    if x >= 600 and x <= 800:
                        if y >= 150 and y <= 180:
                            choose = 0
                            listen = True
                            pygame.mouse.set_visible(0)
                    if x >= 600 and x <= 800:
                        if y >= 300 and y <= 320:
                            choose = 1
                            listen = True
                            pygame.mouse.set_visible(0)
                    if x >= 900 and x <= 1050:
                        if y >= 650 and y <= 680:
                            if detail[1] == "":
                                detail[1] = "0"
                            if len(detail[0]) > 0 and int(detail[1]) >= 20 and int(detail[1]) <= 10000: 
                                num = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]
                                lc = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]
                                uc = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
                                s = [33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,58,59,60,61,62,63,64,91,92,93,94,95,96,123,124,125,126,451,247]
                                numl = 0
                                lcl = 0
                                ucl = 0
                                sl = 0
                                size = 0
                                draft = 0
                                word = []
                                count = 0
                                password = ""
                                better = []

                                while True:
                                    size = int(detail[1])
                                    if size >= 5 :
                                        draft = int(size * 0.2)
                                        break

                                while True:
                                    better = []
                                    while True:
                                        ran = int(random.SystemRandom().randint(1, 4))
                                        if ran >= 1 and ran <= 4:
                                            if ran not in better:
                                                better.append(ran)
                                        if len(better) == 4:
                                            break

                                    for i in range(0,4):
                                        if better[i] == 1:
                                            word.append(num[numl])
                                        elif better[i] == 2:
                                            word.append(lc[lcl])
                                        elif better[i] == 3:
                                            word.append(uc[ucl])
                                        elif better[i] == 4:
                                            word.append(s[sl])
                                            
                                    numl += 1
                                    lcl += 1
                                    ucl += 1
                                    sl += 1
                                    count += 1
                                    random.shuffle(word)
                                    if numl >= 9:
                                        numl = 0
                                    if lcl >= 25:
                                        lcl = 0
                                    if ucl >= 25:
                                        ucl = 0
                                    if sl >= 33:
                                        sl = 0
                                    if count == draft:
                                        break
                                    
                                count = count * 4


                                while True:
                                    ran = int(random.SystemRandom().randint(0, 1000))
                                    if (ran >= 33 and ran <= 94) or (ran >= 97 and ran <= 126) or (ran == 451) or (ran == 247):
                                        word.append(ran)
                                        count += 1
                                        random.shuffle(word)
                                    if count >= size:
                                        break


                                sl = 0
                                lcl = 0
                                ucl = 0
                                numl = 0

                                random.shuffle(word)

                                for i in range(0,(size)):
                                    if (word[i] >= 33 and word[i] <= 47) or (word[i] >= 58 and word[i] <= 64) or (word[i] >= 91 and word[i] <= 96) or (word[i] >= 123 and word[i] <= 126) or (word[i] == 451) or (word[i] == 247):
                                        sl += 1
                                    if word[i] >= 97 and word[i] <= 122:
                                        lcl += 1
                                    if word[i] >= 65 and word[i] <= 90:
                                        ucl += 1
                                    if word[i] >= 48 and word[i] <= 57:
                                        numl += 1
                                    password = password+(chr(word[i]))
                                    
                                saved = ""
                                for i in range(1,len(detail[0])):
                                    saved += chr(ord(detail[0][i-1:i])+133)

                                info = open(os.getcwd()+"\data\Ü¥¦"+search,"rb")#start
                                key = info.readline()
                                real = info.readline()
                                dob = info.readline()
                                fav = info.readline()
                                store = info.readline()
                                info.close()#gfadsgsdhgsdhdh
                                f = Fernet(key)
                                real = real = f.decrypt(real)
                                real = real.decode()

                                dob = dob = f.decrypt(dob)
                                dob = dob.decode()

                                fav = fav = f.decrypt(fav)
                                fav = fav.decode()

                                store = store = f.decrypt(store)
                                store = store.decode()

                                if len(store) > 6:
                                    store += ","
                                    store += detail[0]
                                else:
                                    store += detail[0]
                                
                                key = key = Fernet.generate_key()
                                f = Fernet(key)

                                real = real.encode()
                                real = f.encrypt(real)

                                dob = dob.encode()
                                dob = f.encrypt(dob)

                                fav = fav.encode()
                                fav = f.encrypt(fav)

                                store = store.encode()
                                store = f.encrypt(store)
                                
                                info = open(os.getcwd()+"\data\Ü¥¦"+search,"wb")
                                
                                info.write(key)
                                info.write(b'\n')
                                info.write(real)
                                info.write(b'\n')
                                info.write(dob)
                                info.write(b'\n')
                                info.write(fav)
                                info.write(b'\n')
                                info.write(store)

                                info.close()
                                saved = saved + ".txt"
                                key = key = Fernet.generate_key()
                                f = Fernet(key)

                                password = password.encode()
                                password = f.encrypt(password)

                                info = open(os.getcwd()+"\data\Ü¥¦"+saved,"ab")
                                info.write(key)
                                info.write(b'\n')
                                info.write(password)
                                info.close()
                                
                                pygame.quit()
                                quit
                            else:
                                music = pygame.mixer.music.load(os.getcwd()+"\data\size.mp3")
                                pygame.mixer.music.play(1)
                                detail[1] = ""
                    
            if op == 0 and select == 61:
                win.blit(add,(1250,0))
                #pygame.draw.rect(win,(255,255,255),(1250,20,40,40),1)
                x = 50
                y = 100
                for i in range(0,len(storage_show)):
                    win.blit(storage_show[i],(x+10,y+2))
                    pygame.draw.rect(win,(255,255,255),(x,y,200,20),1)
                    click1,click2,click3 = pygame.mouse.get_pressed() 
                    if click1 == True:
                        pos = pygame.mouse.get_pos()
                        line = str(pos)
                        coma = int(line.find(","))
                        fbracket = int(line.find("("))
                        lbracket = int(line.find(")"))
                        X = int(line[fbracket + 1:coma])
                        Y = int(line[coma+2:lbracket])
                        if X >= x and X <= x+200:
                            if Y >= y and Y <= y+20:
                                select = i
                    x += 250
                    if x >= 1550:
                        y += 50
                        x = 50

                click1,click2,click3 = pygame.mouse.get_pressed() 
                if click1 == True:
                    pos = pygame.mouse.get_pos()
                    line = str(pos)
                    coma = int(line.find(","))
                    fbracket = int(line.find("("))
                    lbracket = int(line.find(")"))
                    X = int(line[fbracket + 1:coma])
                    Y = int(line[coma+2:lbracket])
                    if X >= 1250 and X <= 1290:
                        if Y >= 20 and Y <= 60:
                            op = 1
                if select != 61:
                    search = ""
                    for i in range(1,len(storage[select])):
                        search += chr(ord(storage[select][i-1:i])+133)
                    search = search + ".txt"
                    info = open(os.getcwd()+"\data\Ü¥¦"+search,"rb")
                    key = info.readline()
                    real = info.readline()
                    info.close()
                    f = Fernet(key)
                    real = real = f.decrypt(real)
                    real = real.decode()
                    win.fill((100,150,165))
                    pyperclip.copy(real)

                    if len(real) <= 2300:
                        img = qrcode.make(real)
                        img.save("del.png")
                        img = pygame.image.load("del.png")
                        os.remove("del.png")
                        img = pygame.transform.scale(img, (500,500))
                        win.blit(img,(500,250))
                    else:
                        music = pygame.mixer.music.load(os.getcwd()+"\data\qr.mp3")
                        pygame.mixer.music.play(1)
                    win.blit(free.render("The text has been copied and a qrcode has been created",True,(255,255,255)),(100,100))
                    pygame.display.update()
                    count = 0
                    while run:
                        clock.tick(10)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                music = pygame.mixer.music.load(os.getcwd()+"\data\warn.mp3")
                                pygame.mixer.music.play(1)
                        count += 1
                        if count == 300:
                            run = False
                    pyperclip.copy("too late -\_/-")
                    pygame.quit()
                    quit
                
                
                
                
                
        
    else:
        music = pygame.mixer.music.load(os.getcwd()+"\data\wrong.mp3")
        pygame.mixer.music.play(1)
        win.fill((50,54,133))
        win.blit((free.render("The username or password password is incorrect",True,(205,201,122))),(200,450))
        pygame.display.update()
        pygame.time.delay(5000)
        pygame.quit()
        quit
else:
    music = pygame.mixer.music.load(os.getcwd()+"\data\inform.mp3")
    pygame.mixer.music.play(1)
    while True:
        ans = str(input("Please enter the new 12 digit key "))
        if len(ans) == 12:
            break
    test = "\data\Ü¥¦äæáÖãÜÒÝÚ×ãÒØÚÝÚäåÚÜÖéáÚÒÝÚØÖåÚäÔÙ.txt"

    file = open(os.getcwd()+test,"wb")

    key = key = Fernet.generate_key()
    f = Fernet(key)
    
    ans = ans.encode()
    ans = f.encrypt(ans)
    
    file.write(key)
    file.write(b'\n')
    file.write(ans)
    file.close()
