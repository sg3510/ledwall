# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
#___Import ADC stuff___
import busio
i2c = busio.I2C(board.SCL, board.SDA)
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

ads = ADS.ADS1115(i2c)

chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
chan2 = AnalogIn(ads, ADS.P2)
chan3 = AnalogIn(ads, ADS.P3)

#____Configure Pixels____



# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18
 
# The number of NeoPixels
num_pixels = 60
 
# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB
 
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False,
                           pixel_order=ORDER)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos*3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos*3)
        g = 0
        b = int(pos*3)
    else:
        pos -= 170
        r = 0
        g = int(pos*3)
        b = int(255 - pos*3)
    return (r, g, b) if ORDER == neopixel.RGB or ORDER == neopixel.GRB else (r, g, b, 0)
 

 
def assign_quad0(brightness):
  for i in range(0,5):
    for j in range(0,3):
      pixels[i+10*j] = [int(k * brightness/255.0) for k in pixels[i+10*j]]

def assign_quad1(brightness):
  for i in range(5,10):
    for j in range(0,3):
      pixels[i+10*j] = [int(k * brightness/255.0) for k in pixels[i+10*j]]

def assign_quad2(brightness):
  for i in range(0,5):
    for j in range(3,6):
      pixels[i+10*j] = [int(k * brightness/255.0) for k in pixels[i+10*j]]

def assign_quad3(brightness):
  for i in range(5,10):
    for j in range(3,6):
      pixels[i+10*j] = [int(k * brightness/255.0) for k in pixels[i+10*j]]

def rainbow_cycle(wait):
  a = chan0.voltage
  b = chan1.voltage
  c = chan2.voltage
  d = chan3.voltage
  for j in range(255):
      for i in range(num_pixels):
          pixel_index = (i * 256 // num_pixels) + j
          pixels[i] = wheel(pixel_index & 255)
      a = a*0.9 + 0.1*chan0.voltage
      b = b*0.9 + 0.1*chan2.voltage
      c = c*0.9 + 0.1*chan1.voltage
      d = d*0.9 + 0.1*chan3.voltage
      assign_quad0(min(int(a/3.0*255),255))
      assign_quad1(min(int(b/3.0*255),255))
      assign_quad2(min(int(c/3.0*255),255))
      assign_quad3(min(int(d/3.0*255),255))
      pixels.show()
      time.sleep(wait)
 
while True:
    # # Comment this line out if you have RGBW/GRBW NeoPixels
    # pixels.fill((255, 0, 0))
    # # Uncomment this line if you have RGBW/GRBW NeoPixels
    # # pixels.fill((255, 0, 0, 0))
    # pixels.show()
    # time.sleep(1)
 
    # # Comment this line out if you have RGBW/GRBW NeoPixels
    # pixels.fill((0, 255, 0))
    # # Uncomment this line if you have RGBW/GRBW NeoPixels
    # # pixels.fill((0, 255, 0, 0))
    # pixels.show()
    # time.sleep(1)
 
    # # Comment this line out if you have RGBW/GRBW NeoPixels
    # pixels.fill((0, 0, 255))
    # # Uncomment this line if you have RGBW/GRBW NeoPixels
    # # pixels.fill((0, 0, 255, 0))
    # pixels.show()
    # time.sleep(1)
 
    rainbow_cycle(0.01)    # rainbow cycle with 1ms delay per step