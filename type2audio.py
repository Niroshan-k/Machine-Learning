import pygame
from gtts import gTTS

def playaudio(audio):
    pygame.mixer.init()  # Initialize the mixer module
    pygame.mixer.music.load(audio)  # Load the audio file
    pygame.mixer.music.play()  # Play the audio file
    
    # Keep the script running until the audio finishes playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # Wait and prevent CPU overuse

def convert_to_audio(text):
    audio = gTTS(text=text, lang='en')
    audio.save("textaudio.mp3")
    playaudio("textaudio.mp3")

convert_to_audio("Hello world, my name is Lakshan.")

