import pygame
pygame.init()
pygame.mixer.init()

# Load music
pygame.mixer.music.load("CanYouHearTheMusic.mp3")

# Play music
pygame.mixer.music.play()

# Keep the program running
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)  # Adjust the playback speed
