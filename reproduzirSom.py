import pygame


def reproduzirmusica():
    pygame.mixer.init()
    sound = pygame.mixer.Sound('F:\\Yuri\\Programacao\\Projetos\\Automatizacoes\\SPFC_Ticket\\canto_angelical.mp3')
    sound.play()
    pygame.time.wait(int(sound.get_length() * 1000))
    return
