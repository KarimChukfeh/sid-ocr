import time
import math
import subprocess
import json
from neopixel import *


def prepare_flash():    
    # LED strip configuration:
    LED_COUNT = 12      
    LED_PIN = 18      
    LED_FREQ_HZ = 800000  
    LED_DMA = 5       
    LED_BRIGHTNESS = 100 
    LED_INVERT = False
    strip = Adafruit_NeoPixel(
        LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
    strip.begin()

def flash_on():
    for i in range(0, strip.numPixels(), 1):
        strip.setPixelColor(i, Color(255, 255, 255))
    strip.show()

def raspistill():
    subprocess.call("raspistill -o raw.jpg --timeout 2", shell=True)

def flash_off():
    for i in range(0, strip.numPixels(), 1):
        strip.setPixelColor(i, Color(0, 0, 0))
    strip.show()

def trim_img():
    subprocess.call("convert raw.jpg -crop 650x260+1250+800 stuff.jpg", shell=True)

def ocr_sid():
    subprocess.call("tesseract stuff.jpg text", shell=True)
    f = open('text.txt', 'r')
    return f.read(7)

def good_id(sid):
    try:
        for n in sid:
            int(n)
        return True
    except:
        return False

def tell_ruby(sid):
    file = open("/erfid/sid.txt","w")
    file.write("Go")
    file.write(sid)
    file.close

def wait_for_ruby():
    time.sleep(1.5)
    print("done")
    

if __name__ == '__main__':
    perepare_flash()
    flash_on()
    raspistill()
    flash_off()
    trim_img()
    sid = ocr_sid()
    if good_id(sid):
        tell_ruby(sid)
        wait_for_ruby()
    else:
        print("try again or pair manually")
        


        
                
        
        
        
