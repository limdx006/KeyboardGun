import asyncio
import keyboard

from SFX import *
from config import *

current_gun = "shotgun"

def main():
    print("Welcome to Keyboard Gun!")
    print(f"Current gun: {current_gun}")
    while keyboard.is_pressed('esc') == False:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            print(f"You pressed: {event.name}")
            if len(event.name) == 1 and event.name.isalnum() or event.name == "space":  # Check if the key is a single character or space
                gun_shot(current_gun)
    print("Exiting the game. Goodbye!")

main()