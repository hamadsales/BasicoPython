#Tocando música MP3
import pygame

pygame.init()
pygame.mixer.music.load('arq.mp3')
pygame.mixer.music.play()
pygame.event.wait()

