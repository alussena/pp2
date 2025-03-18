# from os import environ
# environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

# import pygame, sys, time

# pygame.mixer.init()
# # pygame.mixer.music.load('Sparks - Coldplay.mp3')
# pygame.mixer.music.load('Chezile - Beanie.mp3')
# pygame.mixer.music.play(0)


import pygame
import keyboard
import time

# Initialize pygame mixer
pygame.mixer.init()

# List of songs
songs = ["Sparks - Coldplay.mp3", "Chezile - Beanie.mp3"]
current_index = 0

def play_song():
    pygame.mixer.music.load(songs[current_index])
    pygame.mixer.music.play()

def stop_song():
    pygame.mixer.music.stop()

def next_song():
    global current_index
    current_index = (current_index + 1) % len(songs)
    play_song()

def previous_song():
    global current_index
    current_index = (current_index - 1) % len(songs)
    play_song()

keyboard.add_hotkey('space', play_song)
keyboard.add_hotkey('s', stop_song)
keyboard.add_hotkey('n', next_song)
keyboard.add_hotkey('p', previous_song)

print("Music Player Controls: \nSPACE - Play \nS - Stop \nN - Next \nP - Previous")

while True:
    time.sleep(0.1)
