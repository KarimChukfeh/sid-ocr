import time
import math
import subprocess
import json
from neopixel import *

def neoring():
    LED_COUNT = 12      
    LED_PIN = 18      
    LED_FREQ_HZ = 800000  
    LED_DMA = 5       
    LED_BRIGHTNESS = 100 
    LED_INVERT = False
    neoring = Adafruit_NeoPixel(
        LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
    neoring.begin()
    return strip

def flash_on(neoring):
    for i in range(0, strip.numPixels(), 1):
        neoring.setPixelColor(i, Color(255, 255, 255))
    neoring.show()

def raspistill():
    subprocess.call("raspistill -o raw.jpg --timeout 2", shell=True)

def flash_off(neoring):
    for i in range(0, strip.numPixels(), 1):
        neoring.setPixelColor(i, Color(0, 0, 0))
    neoring.show()

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
    flash_on(neoring())
    raspistill()
    flash_off(neoring())
    trim_img()
    sid = ocr_sid()
    if good_id(sid):
        tell_ruby(sid)
        wait_for_ruby()
    else:
        print("try again or pair manually")
        


        
                
        
        
        
