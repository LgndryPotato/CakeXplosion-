import pygame
import random
import sys

pygame.init()

# konstandid
ekraani_laius, ekraan_korgus = 800, 600
valge = (255, 255, 255)
must = (0, 0, 0)
font = "Arial"
sõna_suurus = 36
sõnu = 1
sõnade_list = ["üks", "kaks", "kolm", "neli", "viis", "kuus", "seitse", "kaheksa", "üheksa", "kümme"]

# ekraani seadistamine
ekraan = pygame.display.set_mode((ekraani_laius, ekraan_korgus))
pygame.display.set_caption("CakeXplosion")
icon = pygame.image.load("birthday-cake.png")
pygame.display.set_icon(icon)

# seadistan fondi
font = pygame.font.Font(None, sõna_suurus)


# uue sõna genereerimine
def uus_sõna():
    sõna = random.choice(sõnade_list)
    return {
        "sõna": sõna,
        "x": random.randint(0, ekraani_laius - sõna_suurus * len(sõna)),
        "y": 0,
        "värv": (255, 255, 255),
    }


# ekraanil olevate sõnade list
sõnad_ekraanil = [uus_sõna() for _ in range(sõnu)]

# muutujad
elud = 3
skoor = 0
level = 1
kiirus = 1
sisend = ""
clock = pygame.time.Clock()
sõna_ilmumise_aeg = pygame.time.get_ticks()

programm_töötab = True
while programm_töötab:

    ekraan.fill(must)

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

    # vaatab kas sisend ja sõnad ekraanid samad
    for sõna in sõnad_ekraanil:
        sõna["y"] += kiirus
        text_surface = font.render(sõna["sõna"], True, sõna["värv"])
        ekraan.blit(text_surface, (sõna["x"], sõna["y"]))
        # kui kirjutad sõna mis ekraanil siis automaatselt võtab selle ära ei pea enterit vajutama
        if sisend == sõna["sõna"]:
            skoor += 1
            sõnad_ekraanil.remove(sõna)
            sisend = ""  # teeb sisendi akna vms tühjaks
        elif sõna["y"] > ekraan_korgus:
            elud -= 1
            sõnad_ekraanil.remove(sõna)

    input_surface = font.render(sisend, True, valge)
    ekraan.blit(input_surface, (10, ekraan_korgus - sõna_suurus))

    skoor_surface = font.render("Skoor: {}".format(skoor), True, valge)
    ekraan.blit(skoor_surface, (10, 10))

    elud_surface = font.render("Elud: {}".format(elud), True, valge)
    ekraan.blit(elud_surface, (700, 560))

    # kontrolli kas on jõutud uuele levelile. praegu iga 10 punkti tagant level suureneb
    if skoor >= level * 10:
        level += 1
        kiirus += 0.5  # iga leveliga suureneb kukkumise kiirus

    mitmes_level = font.render("Level: {}".format(level), True, valge)
    ekraan.blit(mitmes_level, (ekraani_laius - 100, 10))

    # kontrolli kas mäng läbi. Kui -1 punkti ehk alla 0 punkti siis mäng labi
    if elud <= 0:
        font_kaotus = pygame.font.Font(None, 72)
        kaotus = font_kaotus.render("Kaotasid mängu!", True, valge)
        ekraan.blit(kaotus, (ekraani_laius // 2 - 200, ekraan_korgus // 2))
        pygame.display.flip()
        pygame.time.wait(3000)  # näitab kaotuse ekraani 3 sekundit
        programm_töötab = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
