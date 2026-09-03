import asyncio
import keyboard

from SFX import *
from config import *

current_gun = "shotgun"
infinite_ammo = False

def main():
    print("Welcome to Keyboard Gun!")
    print(f"Current gun: {current_gun}")
    while keyboard.is_pressed('esc') == False:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            print(f"You pressed: {event.name}")
            gun_shot(current_gun)
    print("Exiting the game. Goodbye!")

main()