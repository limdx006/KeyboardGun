import pygame

from config import volume


pygame.mixer.init()

def short_gun_shot():
    sound = pygame.mixer.Sound("assests/SFX/ShortGunShot.wav")
    sound.set_volume(volume)
    sound.play()
    sound = pygame.mixer.Sound("assests/SFX/ShortGunPull.wav")
    sound.set_volume(volume)
    sound.play()