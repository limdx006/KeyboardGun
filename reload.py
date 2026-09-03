import pygame
import random

from config import *

def reload(gun_type):
    global shotgun_ammo
    match gun_type:
        case "shotgun":
            while shotgun_ammo < 8:
                sound = pygame.mixer.Sound("assests/SFX/Reload/ReloadShotgun1.wav")
                sound.set_volume(volume)
                sound.play()
                # Wait until the sound finishes
                pygame.time.wait(int(sound.get_length() * random.randint(600, 800)))
                shotgun_ammo += 1
                print(f"Shotgun ammo: {shotgun_ammo}")  
            sound = pygame.mixer.Sound("assests/SFX/ShortGunPull.wav")
            sound.set_volume(volume)
            sound.play()
        case _:
            print(f"Unknown gun type: {gun_type}")