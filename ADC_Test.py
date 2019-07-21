#Setup
import board
import busio
from time import sleep
i2c = busio.I2C(board.SCL, board.SDA)
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

ads = ADS.ADS1115(i2c)
ads.overRideConversionDelay(65);


chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
chan2 = AnalogIn(ads, ADS.P2)
chan3 = AnalogIn(ads, ADS.P3)

while True:
	a = chan0.voltage
	b = chan1.voltage
	c = chan2.voltage
	d = chan3.voltage
	print("{0:2.2f} - {1:2.2f} - {2:2.2f} - {3:2.2f}".format(a,b,c,d))