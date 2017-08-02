import time
import math
import subprocess
from PIL import image

from neopixel import *

# LED strip configuration:
LED_COUNT = 12      # Number of LED pixels.
LED_PIN = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
# True to invert the signal (when using NPN transistor level shift)
LED_INVERT = False

# Main program logic follows:
if __name__ == '__main__':
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(
        LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    for i in range(0, strip.numPixels(), 1):
        strip.setPixelColor(i, Color(255, 255, 255))
    while True:
        strip.show()
        subprocess.call("raspistill -o raw.jpg")
        img = "raw.jpg"
        raw = Image.open(img)
        raw.show()
        result = original.crop((25, 25, 100, 100))
        strip.
        
        
        
        