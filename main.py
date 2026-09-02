import asyncio
import pygame
import keyboard

from constant import *

def main():
    print("Welcome to Keyboard Gun!")
    while keyboard.is_pressed('esc') == False:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            print(f"You pressed: {event.name}")
    print("Exiting the game. Goodbye!")

main()