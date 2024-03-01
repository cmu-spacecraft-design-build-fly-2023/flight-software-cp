"""
Test each component of the argus1 library as an initial
integration test.
Argus1 Version: 1.0

Authors: Harry Rosmann, Gordonson Yan
"""
import board, microcontroller
import busio, time, sys
from storage import mount,umount,VfsFat
from analogio import AnalogIn
import digitalio, sdcardio, pwmio, tasko

from .board_config import BoardConfig

# Hardware Specific Libs
import pycubed_rfm9x # Radio
import bmx160 # IMU
import neopixel # RGB LED
import bq25883 # USB Charger
import adm1176_test # Power Monitor Tests
import bmx160_test # IMU Tests
import bq25883_test # Charger Tests
import drv8830_test
import adafruit_gps_test

from argus1.board_config import BoardConfig

# Common CircuitPython Libs
from os import listdir,stat,statvfs,mkdir,chdir
from bitflags import bitFlag,multiBitFlag,multiByte
from micropython import const

def run_diagnostics():
    # ADM1176
    adm1176 = adm1176_test.ADM1176_Test()
    adm1176.run_diagnostic_test()

    # BQ25883
    bq25883 = bq25883_test.BQ25883_Test()
    bq25883.run_diagnostic_test()
    
    # DRV8830
    drv8830_xp = drv8830_test.DRV8830_Test(BoardConfig.DRV8830_XP_I2C_ADDR)
    drv8830_xm = drv8830_test.DRV8830_Test(BoardConfig.DRV8830_XM_I2C_ADDR)
    drv8830_yp = drv8830_test.DRV8830_Test(BoardConfig.DRV8830_YP_I2C_ADDR)
    drv8830_ym = drv8830_test.DRV8830_Test(BoardConfig.DRV8830_YM_I2C_ADDR)
    drv8830_cam = drv8830_test.DRV8830_Test(BoardConfig.DRV8830_CAM_I2C_ADDR)

    drv8830_list = [drv8830_xp, drv8830_xm, drv8830_yp, drv8830_ym, drv8830_cam]
    for drv in drv8830_list:
        drv.run_diagnostic_test() 

    # OPT4001
    opt4001_xp = opt4001_test.OPT4001_Test(BoardConfig.OPT4001_XP_I2C_ADDR)
    opt4001_xm = opt4001_test.OPT4001_Test(BoardConfig.OPT4001_XM_I2C_ADDR)
    opt4001_yp = opt4001_test.OPT4001_Test(BoardConfig.OPT4001_YP_I2C_ADDR)
    opt4001_ym = opt4001_test.OPT4001_Test(BoardConfig.OPT4001_YM_I2C_ADDR)
    opt4001_zp = opt4001_test.OPT4001_Test(BoardConfig.OPT4001_ZP_I2C_ADDR)
    opt4001_zm = opt4001_test.OPT4001_Test(BoardConfig.OPT4001_ZM_I2C_ADDR)
    
    opt4001_list = [opt4001_xp, opt4001_xm, opt4001_yp, opt4001_ym, opt4001_zp, opt4001_zm]
    for opt in opt4001_list:
        opt.run_diagnostic_test()

    #BMX160
    bmx160_dev = bmx160_test.BMX160_Test()
    bmx160_dev.run_diagonstic_test()

    #Adafruit_GPS
    adafruit_gps = adafruit_gps_test.Adafruit_GPS_Test()
    adafruit_gps.run_diagnostic_test()

    #PCF8523
    pcf8523 = pcf8523_test.PCF2583_Test()
    pcf8523.run_diagnostic_test()

if __name__ == "__main__":
    run_diagnostics()