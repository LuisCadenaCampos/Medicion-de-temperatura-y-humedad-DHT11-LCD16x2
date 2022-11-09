"""
Autor original de la biblioteca I2C LCD 16x2
Usuario de Github: T-622
Version: 1.0.0
Fuente: https://github.com/T-622/RPI-PICO-I2C-LCD.git

Autor del codifo: Cadena Campos Luis
Fecha de creacion: 01/11/2022
Version de codigo: 1.0.0
Correo:luis14oriente@gmail.com

""" 
#importamos las bibliotecas necesarias
from machine import Pin,I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
import dht,utime

#Indicamos la direccion del i2c
I2C_ADDR   = 0x27
#Declaramos el numero de renglones y columnas
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
i2c = I2C(0,sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c,I2C_ADDR,I2C_NUM_ROWS,I2C_NUM_COLS)

#Declaramos el obejto
dht11 = dht.DHT11(Pin(2))

while True:
    #Actualizamos la temperatura y humedad
    dht11.measure()
    #Obtenemos temperatura y humedad
    T=dht11.temperature() 
    H=dht11.humidity()
    #Mandamos las lecturas al LCD
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr("Temp:"+str(T)+" c") 
    lcd.move_to(0,1)
    lcd.putstr("Humedad:"+str(H)+" g")
    utime.sleep_ms(400)
    #Obtienen nuevos valores cada 400 ms
    
    