import pygame
import sys
import random
import time
running = True
screen = pygame.display.set_mode([1280, 720])
backgroundcolor = pygame.image.load('tlo.jpg')
backgroundcolor = pygame.transform.scale(backgroundcolor, (1280, 720))
whitecolor = 25, 37, 75
clock = pygame.time.Clock()
white = 255, 255, 255
blackcolor = 0, 0, 0
pytania = []
hajs = [1000000, 500000, 250000, 125000, 75000,
        40000, 20000, 10000, 5000, 2000, 1000, 500, 0]
suma_gwarantowana = [1000, 40000]
wygrana = 0
suma = 0
itr = 12
literyodp = ["A.", "B.", "C.", "D."]
kola = {"polowa": True, "publicznosc": True, "zmiana": True}


def pytanka(source):
    with open(source, 'r') as file:
        read = file.read().splitlines()
        for i in read:
            pytania.append(i.split(";"))


q = 0


def checkAns(pop2, lista, pop):
    hasChosen = False
    global q
    font2 = pygame.font.SysFont('Arial', 19, True)
    odpuser = None
    global running
    while running:
        mx, my = pygame.mouse.get_pos()
        if not hasChosen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    running = False
                if 180 < mx < 480 and 380 < my < 510:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        odpuser = "A"
                        hasChosen = not hasChosen
                        break
                elif 180 < mx < 480 and 550 < my < 680:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        odpuser = "B"
                        hasChosen = not hasChosen
                        break
                elif 800 < mx < 1100 and 380 < my < 510:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        odpuser = "C"
                        hasChosen = not hasChosen
                        break
                elif 800 < mx < 1100 and 550 < my < 680:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        odpuser = "D"
                        hasChosen = not hasChosen
                        break
                elif 590 < mx < 690 and 380 < my < 455:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        odpuser = "PUBLICZNOSC"
                        hasChosen = not hasChosen
                        break
                elif 590 < mx < 690 and 485 < my < 560:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        odpuser = "POLOWA"
                        hasChosen = not hasChosen
                        break
                elif 590 < mx < 690 and 590 < my < 665:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        odpuser = "ZMIANA"
                        hasChosen = not hasChosen
                        break
        else:
            break

    if odpuser != pop2:

        if odpuser == "PUBLICZNOSC":
            if kola["publicznosc"]:
                kola["publicznosc"] = False
                pop2zkr = pop2 + "."
                indexpop = literyodp.index(pop2zkr)
                pula = 100
                poprawna = random.randint(50, 70)
                pula -= poprawna
                odp1 = random.randint(0, pula)
                pula -= odp1
                odp2 = random.randint(0, pula)
                pula -= odp2
                odp3 = pula
                pub1 = font2.render(str(poprawna)+"%", 1, (255, 255, 255))
                pub2 = font2.render(str(odp1)+"%", 1, (255, 255, 255))
                pub3 = font2.render(str(odp2)+"%", 1, (255, 255, 255))
                pub4 = font2.render(str(odp3)+"%", 1, (255, 255, 255))
                if (indexpop == 0):
                    screen.blit(pub1, (185, 385))
                    screen.blit(pub2, (185, 555))
                    screen.blit(pub3, (805, 385))
                    screen.blit(pub4, (805, 555))
                    pygame.display.update()
                elif (indexpop == 1):
                    screen.blit(pub2, (185, 385))
                    screen.blit(pub1, (185, 555))
                    screen.blit(pub3, (805, 385))
                    screen.blit(pub4, (805, 555))
                    pygame.display.update()
                elif (indexpop == 2):
                    screen.blit(pub3, (185, 385))
                    screen.blit(pub2, (185, 555))
                    screen.blit(pub1, (805, 385))
                    screen.blit(pub4, (805, 555))
                    pygame.display.update()
                else:
                    screen.blit(pub4, (185, 385))
                    screen.blit(pub2, (185, 555))
                    screen.blit(pub3, (805, 385))
                    screen.blit(pub1, (805, 555))
                    pygame.display.update()
                return checkAns(pop2, lista, pop)
            else:

                return checkAns(pop2, lista, pop)
        elif odpuser == "POLOWA":
            if kola["polowa"]:
                kola["polowa"] = False
                i = random.randint(0, 2)
                pygame.draw.rect(screen, whitecolor, (180, 380, 300, 130))
                pygame.draw.rect(screen, whitecolor, (800, 380, 300, 130))
                pygame.draw.rect(screen, whitecolor, (180, 550, 300, 130))
                pygame.draw.rect(screen, whitecolor, (800, 550, 300, 130))
                pygame.display.update()
                if i == 0 or i == 1:
                    aa = font2.render("A. "+pop, 1, (255, 255, 255))
                    pop2 = 'A'
                    lista.remove(pop)
                    bb = font2.render("B. "+lista[i], 1, (255, 255, 255))
                    screen.blit(aa, (190, 412.5))
                    screen.blit(bb, (190, 582.5))
                    pygame.display.update()
                    return checkAns(pop2, lista, pop)
                elif i == 2:
                    temppop = pop
                    lista.remove(pop)
                    aa = font2.render("A. "+lista[i], 1, (255, 255, 255))
                    bb = font2.render("B. "+pop, 1, (255, 255, 255))
                    screen.blit(aa, (190, 412.5))
                    screen.blit(bb, (190, 582.5))
                    pop2 = "B"
                    pygame.display.update()
                    return checkAns(pop2, lista, pop)
            else:
                return checkAns(pop2, lista, pop)
        elif odpuser == "ZMIANA":
            if kola["zmiana"]:
                # screen.fill(backgroundcolor)
                screen.blit(backgroundcolor, [0, 0])
                kola["zmiana"] = False
                return losujpyt()
            else:
                return checkAns(pop2, lista, pop)
        else:
            return False
    else:
        # screen.fill(backgroundcolor)
        screen.blit(backgroundcolor, [0, 0])
        return True
    pygame.display.update()


def odpowiedzi(odp, pyt):
    a = random.choice(pytania)
    pytania.remove(a)
    pyt = a[0]
    odp = a[1:5]
    lista = []
    i = random.sample(range(1, 5), 4)
    font3 = pygame.font.SysFont('Arial', 16, True)
    pygame.draw.rect(screen, whitecolor, (180, 380, 300, 130))
    pygame.draw.rect(screen, whitecolor, (800, 380, 300, 130))
    pygame.draw.rect(screen, whitecolor, (180, 550, 300, 130))
    pygame.draw.rect(screen, whitecolor, (800, 550, 300, 130))
    pygame.draw.rect(screen, whitecolor, (180, 40, 920, 300))
    pygame.draw.rect(screen, whitecolor, (590, 380, 100, 75))
    pygame.draw.rect(screen, whitecolor, (590, 485, 100, 75))
    pygame.draw.rect(screen, whitecolor, (590, 590, 100, 75))
    kolo1_tak = font3.render("Publiczność", 1, (255, 255, 255))
    kolo2_tak = font3.render("50/50", 1, (255, 255, 255))
    kolo3_tak = font3.render("Zmiana", 1, (255, 255, 255))
    kolo1_nie = font3.render("Publiczność", 1, (128, 38, 0))
    kolo2_nie = font3.render("50/50", 1, (128, 38, 0))
    kolo3_nie = font3.render("Zmiana", 1, (128, 38, 0))
    if kola["publicznosc"]:
        screen.blit(kolo1_tak, (593, 410))
    else:
        screen.blit(kolo1_nie, (593, 410))
    if kola["polowa"]:
        screen.blit(kolo2_tak, (619, 515))
    else:
        screen.blit(kolo2_nie, (619, 515))
    if kola["zmiana"]:
        screen.blit(kolo3_tak, (612, 620))
    else:
        screen.blit(kolo3_nie, (612, 620))
    pop = odp[3]
    for j in range(len(odp)):
        lista.insert(j, odp[i[j]-1])
    for i in range(len(lista)):
        if pop == lista[i]:
            pop2 = literyodp[i][0]
    font4 = pygame.font.SysFont('Arial', 22, True)
    font2 = pygame.font.SysFont('Arial', 19, True)
    text_render1 = font4.render(pyt, 1, (255, 255, 255))
    text_render2 = font2.render("A. "+lista[0], 1, (255, 255, 255))
    text_render3 = font2.render("B. "+lista[1], 1, (255, 255, 255))
    text_render4 = font2.render("C. "+lista[2], 1, (255, 255, 255))
    text_render5 = font2.render("D. "+lista[3], 1, (255, 255, 255))
    text_numer = font2.render(f'Numer pytania {q}', 1, (255, 255, 255))
    text_wygrananext = font2.render(
        f'Pytanie o {hajs[itr]} zł', 1, (255, 255, 255))
    text_wygrana = font2.render(
        f'Twoja aktualna wygrana {suma} zł', 1, (255, 255, 255))
    screen.blit(text_render1, (190, 170))
    screen.blit(text_render2, (190, 412.5))
    screen.blit(text_render3, (190, 582.5))
    screen.blit(text_render4, (810, 412.5))
    screen.blit(text_render5, (810, 582.5))
    screen.blit(text_numer, (190, 50))
    screen.blit(text_wygrananext, (190, 70))
    screen.blit(text_wygrana, (190, 90))
    pygame.display.update()
    if checkAns(pop2, lista, pop):
        return True
    else:
        return False


def losujpyt():
    a = random.choice(pytania)
    pytania.remove(a)
    pyt = a[0]
    odp = a[1:5]

    return odpowiedzi(odp, pyt)


def close():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            running = False


def gra():
    font = pygame.font.SysFont('Arial', 92, True)
    font2 = pygame.font.SysFont('Arial', 18, True)
    global running
    global itr
    global wygrana
    global suma
    global q
    while itr != 0:
        if len(pytania) != 0:
            q += 1
            itr -= 1
            wygrana = hajs[itr+1]
            if wygrana >= 1000:
                suma = 1000
            if wygrana >= 40000:
                suma = 40000
            # screen.fill(backgroundcolor)
            screen.blit(backgroundcolor, [0, 0])
            pygame.display.update()
            a = losujpyt()
        if a == False:
            # screen.fill(backgroundcolor)
            screen.blit(backgroundcolor, [0, 0])
            wygranaa()
            break
        elif itr == 0:
            wygranamilion()
            break


def wygranaa():
    font2 = pygame.font.SysFont('Arial', 74, True)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                running = False
        # screen.fill(backgroundcolor)
        screen.blit(backgroundcolor, [0, 0])

        text1 = font2.render(f'Wygrana: {suma} zł', 1, (255, 255, 255))
        text_rect = text1.get_rect(center=(1280/2, 720/2))
        screen.blit(text1, text_rect)
        pygame.display.update()


def wygranamilion():
    font2 = pygame.font.SysFont('Arial', 74, True)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                running = False
        # screen.fill(backgroundcolor)
        screen.blit(backgroundcolor, [0, 0])
        text1 = font2.render(f'Wygrana: {hajs[0]} zł', 1, (255, 255, 255))
        text_rect = text1.get_rect(center=(1280/2, 720/2))
        screen.blit(text1, text_rect)
        pygame.display.update()


def start():
    pygame.init()
    font = pygame.font.SysFont('Arial', 92, True)
    font2 = pygame.font.SysFont('Arial', 20, True)
    font3 = pygame.font.SysFont('Arial', 54, True)
    text = 'Milionerzy'
    text_render = font.render(text, 1, (255, 255, 255))
    global running
    global screen
    start = font3.render("Start", 1, (255, 255, 255))
    rect = pygame.draw.rect(screen, whitecolor, (540, 400, 200, 100))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                running = False
        # screen.fill(backgroundcolor)
        screen.blit(backgroundcolor, [0, 0])
        pygame.draw.rect(screen, whitecolor, (540, 400, 200, 100))
        screen.blit(text_render, (412, 200))
        screen.blit(start, (578, 420))
        mx, my = pygame.mouse.get_pos()
        if 740 > mx > 540 and 500 > my > 400:
            pygame.draw.rect(screen, white, (540, 400, 200, 100))
            if event.type == pygame.MOUSEBUTTONDOWN:
                gra()
                break
        pygame.display.update()


pytanka('pytania.txt')
start()
