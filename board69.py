import random
import winsound
import logging
from pynput import keyboard

# Define the list of sound files
SOUNDS = ['hentai1.wav', 'hentai2.wav', 'hentai3.wav', 'hentai4.wav', 'hentai5.wav', 'hentai7.wav', 'how-naughty.wav', 'yes-daddy.wav', 'yamete_kudasai.wav', 'uwu_egirl.wav']

# Create a logger that writes to a file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, format='%(asctime)s - %(message)s')

def on_press(key):
    # Play a random sound and log the key press and sound played
    if key == keyboard.Key.esc:
        logging.info('Program stopped')
        return False  # Stop listener if ESC key is pressed
    else:
        sound = random.choice(SOUNDS)
        winsound.PlaySound(sound, winsound.SND_ASYNC)
        logging.info('Key pressed: %s | Sound played: %s', key, sound)

# Create a listener that triggers the on_press function on key press events
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
