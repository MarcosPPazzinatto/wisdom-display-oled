from machine import Pin
from machine import PWM
from machine import SoftI2C
import ssd1306
import gfx
from time import sleep
import time

count = None

led_red = PWM(Pin(19))
led_green = PWM(Pin(23))
led_blue = PWM(Pin(18))

led_red.duty_u16(0)
led_green.duty_u16(0)
led_blue.duty_u16(0)

def rgb_color(red_value, green_value, blue_value):
    if red_value < 0:
        red_value = 0
    if red_value > 100:
        red_value = 100

    led_red.duty_u16(red_value * 65535 // 100)

    if green_value < 0:
        green_value = 0
    if green_value > 100:
        green_value = 100

    led_green.duty_u16(green_value * 65535 // 100)

    if blue_value < 0:
        blue_value = 0
    if blue_value > 100:
        blue_value = 100

    led_blue.duty_u16(blue_value * 65535 // 100)

led_25   = Pin(13, Pin.OUT)
led_50   = Pin(4, Pin.OUT)
led_75   = Pin(16, Pin.OUT)
led_100  = Pin(17, Pin.OUT)

led_25.off()
led_50.off()
led_75.off()
led_100.off()

i2c_21_22 = SoftI2C(sda=Pin(21), scl=Pin(22))

#Author: 'Marcos Paulo Pazzinatto'
#Description: 'Show counter in display'

rgb_color(0, 0, 0)
led_25.off()
led_50.off()
led_75.off()
led_100.off()
oled = ssd1306.SSD1306_I2C(128, 64, i2c_21_22)
graphics = gfx.GFX(128, 64, oled.pixel)
while True:
  count = (count if isinstance(count, int) else 0) + 1
  oled.fill(0)
  oled.drawTextBMP(contador, int(0), int(0))
  oled.show()
  time.sleep(1)



