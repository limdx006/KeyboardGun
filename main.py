import asyncio
import keyboard

from SFX import *
from config import *

def main():
    print("Welcome to Keyboard Gun!")
    while keyboard.is_pressed('esc') == False:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            print(f"You pressed: {event.name}")
            short_gun_shot()
            
    print("Exiting the game. Goodbye!")

main() 