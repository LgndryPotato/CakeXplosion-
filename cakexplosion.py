import pygame
import random
import sys

pygame.init()

# konstandid
ekraani_laius, ekraan_korgus = 1280, 720
valge = (255, 255, 255)
must = (0, 0, 0)
font = "Arial"
sõna_suurus = 36
sõnu = 1
sõnade_list = ["üks", "kaks", "kolm", "neli", "viis", "kuus", "seitse", "kaheksa", "üheksa", "kümme"]
kookide_ikoonid_pruunid1 = pygame.image.load("hyperpruun.png")
kookide_ikoonid_pruunid2 = pygame.image.load("hyperpruun1.png")
kookide_ikoonid_pruunid3 = pygame.image.load("hyperpruun2.png")
kookide_ikoonid_pruunid4 = pygame.image.load("hyperpruun3.png")
kookide_ikoonid_pruunid5 = pygame.image.load("hyperpruun4.png")
kookide_ikoonid_pruunid6 = pygame.image.load("hyperpruun5.png")
kookide_ikoonid_pruunid7 = pygame.image.load("hyperpruun6.png")
kookide_ikoonid_pruunid8 = pygame.image.load("hyperpruun7.png")
kookide_ikoonid_pruunid9 = pygame.image.load("hyperpruun8.png")

kookide_ikoonid_valged1 = pygame.image.load("hypervalge.png")
kookide_ikoonid_valged2 = pygame.image.load("hypervalge1.png")
kookide_ikoonid_valged3 = pygame.image.load("hypervalge2.png")
kookide_ikoonid_valged4 = pygame.image.load("hypervalge3.png")

backgrounds_tumedad1 = pygame.image.load("pruunback.png")
backgrounds_tumedad2 = pygame.image.load("pruunback1.png")
backgrounds_tumedad3 = pygame.image.load("pruunback2.png")
backgrounds_tumedad4 = pygame.image.load("pruunback3.png")
backgrounds_tumedad5 = pygame.image.load("pruunback4.png")
backgrounds_tumedad6 = pygame.image.load("pruunback5.png")
backgrounds_tumedad7 = pygame.image.load("pruunback6.png")
backgrounds_tumedad8 = pygame.image.load("pruunback7.png")
backgrounds_tumedad9 = pygame.image.load("pruunback8.png")
backgrounds_tumedad10 = pygame.image.load("pruunback9.png")
backgrounds_tumedad11 = pygame.image.load("pruunback11.png")
backgrounds_tumedad12 = pygame.image.load("pruunback12.png")

backgrounds_heledad1 = pygame.image.load("valgeback.png")
backgrounds_heledad2 = pygame.image.load("valgeback1.png")
backgrounds_heledad3 = pygame.image.load("valgeback2.png")
backgrounds_heledad4 = pygame.image.load("valgeback3.png")
backgrounds_heledad5 = pygame.image.load("valgeback4.png")
backgrounds_heledad6 = pygame.image.load("valgeback5.png")
backgrounds_heledad7 = pygame.image.load("valgeback6.png")
backgrounds_heledad8 = pygame.image.load("valgeback7.png")
backgrounds_heledad9 = pygame.image.load("valgeback8.png")
backgrounds_heledad10 = pygame.image.load("valgeback9.png")
backgrounds_heledad11 = pygame.image.load("valgeback10.png")
backgrounds_heledad12 = pygame.image.load("valgeback11.png")
backgrounds_heledad13 = pygame.image.load("valgeback12.png")
backgrounds_heledad14 = pygame.image.load("valgeback13.png")
backgrounds_heledad15 = pygame.image.load("valgeback14.png")


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
    if level == 1: ekraan.blit(backgrounds_tumedad1, (0,0))
    if level == 2: ekraan.blit(backgrounds_heledad5, (0, 0))
    if level == 3: ekraan.blit(backgrounds_tumedad3, (0, 0))
    if level == 4: ekraan.blit(backgrounds_heledad4, (0, 0))
    if level == 5: ekraan.blit(backgrounds_tumedad5, (0, 0))
    if level == 6: ekraan.blit(backgrounds_heledad6, (0, 0))
    if level == 7: ekraan.blit(backgrounds_tumedad7, (0, 0))
    if level == 8: ekraan.blit(backgrounds_heledad10, (0, 0))
    if level == 9: ekraan.blit(backgrounds_tumedad9, (0, 0))
    if level == 10: ekraan.blit(backgrounds_heledad11, (0, 0))
    if level == 11: ekraan.blit(backgrounds_tumedad11, (0, 0))
    if level == 12: ekraan.blit(backgrounds_heledad12, (0, 0))
    if level == 13: ekraan.blit(backgrounds_tumedad8, (0, 0))
    if level == 14: ekraan.blit(backgrounds_heledad2, (0, 0))
    if level == 15: ekraan.blit(backgrounds_tumedad4, (0, 0))

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
    ekraan.blit(elud_surface, (1190, 690))

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
