import asyncio
import random
import pygame
import keyboard

from reload import reload
from config import *
infinite_ammo = False

pygame.mixer.init()

def gun_shot(gun_type):
    match gun_type:
        case "shotgun":
            short_gun_shot()
        case "sniper":
            sniper_shot()
        case _:
            print(f"Unknown gun type: {gun_type}")


def short_gun_shot():
    global shotgun_ammo
    if keyboard.is_pressed('space'):
        reload("shotgun")
    elif shotgun_ammo > 0:
        sound = pygame.mixer.Sound("assests/SFX/ShortGunShot.wav")
        sound.set_volume(volume)
        sound.play()
        sound = pygame.mixer.Sound("assests/SFX/ShortGunPull.wav")
        sound.set_volume(volume)
        sound.play()
        if not infinite_ammo:
            shotgun_ammo -= 1
        print(f"Shotgun ammo: {shotgun_ammo}")
    else:
        sound = pygame.mixer.Sound("assests/SFX/Empty/EmptyShotgunClick.wav")
        sound.set_volume(volume)
        sound.play()

def sniper_shot():
    global sniper_ammo
    if keyboard.is_pressed('space'):
        reload("sniper")
    elif sniper_ammo > 0:
        sound = pygame.mixer.Sound("assests/SFX/SniperShot.wav")
        sound.set_volume(volume)
        sound.play()
        if not infinite_ammo:
            sniper_ammo -= 1
        print(f"Sniper ammo: {sniper_ammo}")
    else:
        sound = pygame.mixer.Sound("assests/SFX/Empty/EmptySniperClick.wav")
        sound.set_volume(volume)
        sound.play()