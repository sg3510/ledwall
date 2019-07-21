#Setup
import board
import busio
from time import sleep
i2c = busio.I2C(board.SCL, board.SDA)
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

ads = ADS.ADS1115(i2c)

chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
chan2 = AnalogIn(ads, ADS.P2)
chan3 = AnalogIn(ads, ADS.P3)

while True:
	a = chan0.voltage
	sleep(0.01)
	b = chan1.voltage
	sleep(0.01)
	c = chan2.voltage
	sleep(0.01)
	d = chan3.voltage
	sleep(0.01)
	print("{0:2.2} - {0:2.2} - {0:2.2} - {0:2.2}".format(a,b,c,d))