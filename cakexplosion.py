import random
import sys
import requests
import pygame
from bs4 import BeautifulSoup

pygame.init()

# konstandid
ekraani_laius, ekraan_korgus = 1280, 720
valge = (255, 255, 255)
must = (0, 0, 0)
roosa = (255,192,203)
font = "Arial"
sõna_suurus = 36
sõna_suurus_start = 50
sõna_suurus_leaderboard = 40
sõnu = 1
sprinkles_start_time = None
sprinkles_position = None

kookide_ikoonid_pruunid1 = pygame.transform.scale(pygame.image.load("hyperpruun.png"), (150, 150))
kookide_ikoonid_pruunid2 = pygame.transform.scale(pygame.image.load("hyperpruun1.png"), (150, 150))
kookide_ikoonid_pruunid3 = pygame.transform.scale(pygame.image.load("hyperpruun2.png"), (150, 150))
kookide_ikoonid_pruunid4 = pygame.transform.scale(pygame.image.load("hyperpruun3.png"), (150, 150))
kookide_ikoonid_pruunid5 = pygame.transform.scale(pygame.image.load("hyperpruun4.png"), (150, 150))
kookide_ikoonid_pruunid6 = pygame.transform.scale(pygame.image.load("hyperpruun5.png"), (150, 150))
kookide_ikoonid_pruunid7 = pygame.transform.scale(pygame.image.load("hyperpruun6.png"), (150, 150))
kookide_ikoonid_pruunid8 = pygame.transform.scale(pygame.image.load("hyperpruun7.png"), (150, 150))
kookide_ikoonid_pruunid9 = pygame.transform.scale(pygame.image.load("hyperpruun8.png"), (150, 150))

kookide_ikoonid_valged1 = pygame.transform.scale(pygame.image.load("hypervalge.png"), (150, 150))
kookide_ikoonid_valged2 = pygame.transform.scale(pygame.image.load("hypervalge1.png"), (150, 150))
kookide_ikoonid_valged3 = pygame.transform.scale(pygame.image.load("hypervalge2.png"), (150, 150))
kookide_ikoonid_valged4 = pygame.transform.scale(pygame.image.load("hypervalge3.png"), (150, 150))
sprinkles_ikoon = pygame.transform.scale(pygame.image.load("sprinkles.png"), (150, 150))

kookide_ikoonide_list = [kookide_ikoonid_pruunid1, kookide_ikoonid_pruunid2, kookide_ikoonid_pruunid3, kookide_ikoonid_pruunid4,
                                 kookide_ikoonid_pruunid5, kookide_ikoonid_pruunid6, kookide_ikoonid_pruunid7, kookide_ikoonid_pruunid8,
                                 kookide_ikoonid_pruunid9, kookide_ikoonid_valged1, kookide_ikoonid_valged2, kookide_ikoonid_valged3,
                                 kookide_ikoonid_valged4]

backgrounds_tumedad1 = pygame.image.load("pruunback.png")
backgrounds_tumedad1 = pygame.transform.smoothscale(backgrounds_tumedad1, (ekraani_laius, ekraan_korgus))

backgrounds_tumedad2 = pygame.image.load("pruunback1.png")
backgrounds_tumedad2 = pygame.transform.smoothscale(backgrounds_tumedad2, (ekraani_laius, ekraan_korgus))

backgrounds_tumedad3 = pygame.image.load("pruunback2.png")
backgrounds_tumedad3 = pygame.transform.smoothscale(backgrounds_tumedad3, (ekraani_laius, ekraan_korgus))

backgrounds_tumedad4 = pygame.image.load("pruunback3.png")
backgrounds_tumedad4 = pygame.transform.smoothscale(backgrounds_tumedad4, (ekraani_laius, ekraan_korgus))

backgrounds_tumedad5 = pygame.image.load("pruunback4.png")
backgrounds_tumedad5 = pygame.transform.smoothscale(backgrounds_tumedad5, (ekraani_laius, ekraan_korgus))

backgrounds_tumedad6 = pygame.image.load("pruunback5.png")
backgrounds_tumedad6 = pygame.transform.smoothscale(backgrounds_tumedad6, (ekraani_laius, ekraan_korgus))

backgrounds_tumedad7 = pygame.image.load("pruunback6.png")
backgrounds_tumedad7 = pygame.transform.smoothscale(backgrounds_tumedad7, (ekraani_laius, ekraan_korgus))

backgrounds_tumedad8 = pygame.image.load("pruunback7.png")
backgrounds_tumedad8 = pygame.transform.smoothscale(backgrounds_tumedad8, (ekraani_laius, ekraan_korgus))

backgrounds_heledad1 = pygame.image.load("valgeback.png")
backgrounds_heledad1 = pygame.transform.smoothscale(backgrounds_heledad1, (ekraani_laius, ekraan_korgus))

backgrounds_heledad2 = pygame.image.load("valgeback1.png")
backgrounds_heledad2 = pygame.transform.smoothscale(backgrounds_heledad2, (ekraani_laius, ekraan_korgus))

backgrounds_heledad3 = pygame.image.load("valgeback2.png")
backgrounds_heledad3 = pygame.transform.smoothscale(backgrounds_heledad3, (ekraani_laius, ekraan_korgus))

backgrounds_heledad4 = pygame.image.load("valgeback3.png")
backgrounds_heledad4 = pygame.transform.smoothscale(backgrounds_heledad4, (ekraani_laius, ekraan_korgus))

backgrounds_heledad5 = pygame.image.load("valgeback4.png")
backgrounds_heledad5 = pygame.transform.smoothscale(backgrounds_heledad5, (ekraani_laius, ekraan_korgus))

backgrounds_heledad6 = pygame.image.load("valgeback5.png")
backgrounds_heledad6 = pygame.transform.smoothscale(backgrounds_heledad6, (ekraani_laius, ekraan_korgus))

backgrounds_heledad7 = pygame.image.load("valgeback6.png")
backgrounds_heledad7 = pygame.transform.smoothscale(backgrounds_heledad7, (ekraani_laius, ekraan_korgus))


# ekraani seadistamine
ekraan = pygame.display.set_mode((ekraani_laius, ekraan_korgus))
pygame.display.set_caption("CakeXplosion")
icon = pygame.image.load("birthday-cake.png")
pygame.display.set_icon(icon)

# seadistan fondi
font = pygame.font.Font(None, sõna_suurus)
font_main_start = pygame.font.Font(None, sõna_suurus_start)
font_main_leaderboard = pygame.font.Font(None, sõna_suurus_leaderboard)

# suvaline sõna veebist
def suvaline_sõna_veebist(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    sõnad = []
    for p in soup.select('p'):
        sõnad.append(p.text.split())
    return random.choice(sõnad)

# uue sõna genereerimine
def uus_sõna():
    url = "https://kodu.ut.ee/~tristanl/sõnad.html"
    sõna = random.choice(suvaline_sõna_veebist(url))
    kook = random.choice(kookide_ikoonide_list)
    return {
        "sõna": sõna,
        "x": random.randint(0, ekraani_laius - sõna_suurus * len(sõna)),
        "y": 0,
        "ikoon": kook
    }

# ekraanil olevate sõnade list
sõnad_ekraanil = [uus_sõna() for _ in range(sõnu)]

# muutujad
clock = pygame.time.Clock()

# main menu
def main_menu():
    menu = True
    # nupud
    start_button = pygame.Rect(ekraani_laius//2 - 200//2, ekraan_korgus//2 - 100//2 - 50, 200, 100)
    leaderboard_button = pygame.Rect(ekraani_laius//2 - 200//2, ekraan_korgus//2 + 10, 200, 100)
    start_tekst = font_main_start.render("Alusta", True, must)
    leaderboard_tekst = font_main_leaderboard.render("Edetabel", True, must)
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if start_button.collidepoint(mouse_pos):
                    menu = False
                    game_loop()
                elif leaderboard_button.collidepoint(mouse_pos):
                    display_leaderboard()

        # main menu pilt jms
        ekraan.blit(backgrounds_tumedad8, (0, 0))
        pygame.draw.rect(ekraan, roosa, start_button)
        pygame.draw.rect(ekraan, roosa, leaderboard_button)

        # nuppude teksti joonistamine
        ekraan.blit(start_tekst, (start_button.x + start_button.width // 2 - start_tekst.get_width() // 2,
                                 start_button.y + start_button.height // 2 - start_tekst.get_height() // 2))
        ekraan.blit(leaderboard_tekst, (
        leaderboard_button.x + leaderboard_button.width // 2 - leaderboard_tekst.get_width() // 2,
        leaderboard_button.y + leaderboard_button.height // 2 - leaderboard_tekst.get_height() // 2))
        pygame.display.update()

# leaderboardi kirjutamine
def save_score(score):
    with open('leaderboard.txt', 'r') as f:
        scores = f.readlines()
    scores = [int(s.strip()) for s in scores]
    if score not in scores:
        with open('leaderboard.txt', 'a') as f:
            f.write(str(score) + '\n')

# leaderboard
def display_leaderboard():
    with open('leaderboard.txt', 'r') as f:
        scores = f.readlines()
    scores = sorted([int(score.strip()) for score in scores], reverse=True)
    leaderboard_screen = pygame.display.set_mode((ekraani_laius, ekraan_korgus))
    pygame.display.set_caption("Leaderboard")

    # Leaderboardi runnimine
    running = True
    while running:
        leaderboard_screen.fill(must)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # Kuvab skoorid(parim esimene jn)
        for i, score in enumerate(scores):
            score_text = font.render(f"{i + 1}. {score}", True, valge)
            leaderboard_screen.blit(score_text, (ekraani_laius // 2 - score_text.get_width() // 2, 50 + i * 40))

        pygame.display.flip()

    main_menu()

def loo_sprinkild(x, y):
    ekraan.blit(sprinkles_ikoon, (x, y))

def game_loop():
    # muutujad
    elud = 3
    skoor = 0
    level = 1
    kiirus = 1
    sõna_ilmumise_aeg = pygame.time.get_ticks()
    sisend = ""
    sprinkles_start_time = None
    sõnad_ekraanil = [uus_sõna() for _ in range(sõnu)]
    programm_töötab = True
    while programm_töötab:

        ekraan.fill(must)
        if level == 1: ekraan.blit(backgrounds_tumedad1, (0,0))
        if level == 2: ekraan.blit(backgrounds_heledad1, (0, 0))
        if level == 3: ekraan.blit(backgrounds_tumedad2, (0, 0))
        if level == 4: ekraan.blit(backgrounds_heledad2, (0, 0))
        if level == 5: ekraan.blit(backgrounds_tumedad3, (0, 0))
        if level == 6: ekraan.blit(backgrounds_heledad3, (0, 0))
        if level == 7: ekraan.blit(backgrounds_tumedad4, (0, 0))
        if level == 8: ekraan.blit(backgrounds_heledad4, (0, 0))
        if level == 9: ekraan.blit(backgrounds_tumedad5, (0, 0))
        if level == 10: ekraan.blit(backgrounds_heledad5, (0, 0))
        if level == 11: ekraan.blit(backgrounds_tumedad6, (0, 0))
        if level == 12: ekraan.blit(backgrounds_heledad6, (0, 0))
        if level == 13: ekraan.blit(backgrounds_tumedad7, (0, 0))
        if level == 14: ekraan.blit(backgrounds_heledad7, (0, 0))
        if level == 15: ekraan.blit(backgrounds_tumedad8, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                programm_töötab = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    programm_töötab = False
                elif event.key == pygame.K_BACKSPACE:
                    sisend = sisend[:-1]
                else:
                    sisend += event.unicode

        # kontrollib kas on vaja uus sõna panna
        hetke_aeg = pygame.time.get_ticks()
        sõna_ilmumise_intervall = 3000 - (
                    level - 1) * 200  # iga level läheb 0.2 sekundi võrra lühemaks sõnade ilmumise vahel olev aeg
        if hetke_aeg - sõna_ilmumise_aeg > sõna_ilmumise_intervall:
            sõnad_ekraanil.append(uus_sõna())
            sõna_ilmumise_aeg = hetke_aeg

        # vaatab kas sisend ja sõnad ekraanil samad
        for sõna in sõnad_ekraanil:
            sõna["y"] += kiirus
            ekraan.blit(sõna["ikoon"], (sõna["x"] - 50, sõna["y"] - 75))
            text_surface = font.render(sõna["sõna"], True, valge)
            border_surface = font.render(sõna["sõna"], True, must)

            # Draw the border
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ekraan.blit(border_surface, (sõna["x"] + dx, sõna["y"] + dy))
            ekraan.blit(text_surface, (sõna["x"], sõna["y"]))

            # kui kirjutad sõna mis ekraanil siis automaatselt võtab selle ära ei pea enterit vajutama
            if sisend == sõna["sõna"]:
                skoor += 1
                sprinkles_position = (sõna["x"], sõna["y"])
                sõnad_ekraanil.remove(sõna)
                sisend = ""  # teeb sisendi akna vms tühjaks
                sprinkles_start_time = pygame.time.get_ticks()
            elif sõna["y"] > ekraan_korgus:
                elud -= 1
                sõnad_ekraanil.remove(sõna)

        if sprinkles_start_time is not None and pygame.time.get_ticks() - sprinkles_start_time < 200:
            ekraan.blit(sprinkles_ikoon, (sprinkles_position[0] - 50, sprinkles_position[1] - 75))

        roosa_kast = pygame.Rect(0, 670, 200, 50)
        pygame.draw.rect(ekraan, roosa, roosa_kast)
        input_surface = font.render(sisend, True, must)
        ekraan.blit(input_surface, (10, ekraan_korgus - sõna_suurus))

        if level == 1 or level == 3 or level == 5 or level == 7 or level == 9 or level == 11 or level == 13 or level == 15:
            skoor_surface = font.render("Skoor: {}".format(skoor), True, valge)
            ekraan.blit(skoor_surface, (10, 10))
        else:
            skoor_surface = font.render("Skoor: {}".format(skoor), True, must)
            ekraan.blit(skoor_surface, (10, 10))

        elud_surface = font.render("Elud: {}".format(elud), True, valge)
        ekraan.blit(elud_surface, (1190, 690))

        # kontrolli kas on jõutud uuele levelile. praegu iga 10 punkti tagant level suureneb
        if skoor >= level * 10:
            level += 1
            kiirus += 0.5  # iga leveliga suureneb kukkumise kiirus
        if level == 1 or level == 3 or level == 5 or level == 7 or level == 9 or level == 11 or level == 13 or level == 15:
            mitmes_level = font.render("Level: {}".format(level), True, valge)
            ekraan.blit(mitmes_level, (ekraani_laius - 100, 10))
        else:
            mitmes_level = font.render("Level: {}".format(level), True, must)
            ekraan.blit(mitmes_level, (ekraani_laius - 100, 10))

        # kontrolli kas mäng läbi. Kui -1 punkti ehk alla 0 punkti siis mäng labi
        if elud <= 0:
            font_kaotus = pygame.font.Font(None, 72)
            if level == 1 or level == 3 or level == 5 or level == 7 or level == 9 or level == 11 or level == 13 or level == 15:
                kaotus = font_kaotus.render("Kaotasid mängu!", True, valge)
                ekraan.blit(kaotus, (ekraani_laius // 2 - 200, ekraan_korgus // 2))
            else:
                kaotus = font_kaotus.render("Kaotasid mängu!", True, must)
                ekraan.blit(kaotus, (ekraani_laius // 2 - 200, ekraan_korgus // 2))
            pygame.display.flip()
            pygame.time.wait(3000)  # näitab kaotuse ekraani 3 sekundit
            programm_töötab = False
            save_score(skoor)
            main_menu()

        pygame.display.flip()
        clock.tick(60)

main_menu()
pygame.quit()
sys.exit()
