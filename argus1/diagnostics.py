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

from board_config import BoardConfig

from tests import adm1176_test
import tests

# Hardware Specific Libs
# import pycubed_rfm9x # Radio
# import bmx160 # IMU
# import neopixel # RGB LED
# import bq25883 # USB Charger
# import adm1176_tests # Power Monitor Tests
# import bmx160_tests # IMU Tests
# import bq25883_tests # Charger Tests
# import drv8830_tests

# Common CircuitPython Libs
from os import listdir,stat,statvfs,mkdir,chdir
from micropython import const

def run_diagnostics():
    print("Running ADM1176 Tests")
    # ADM1176
    adm1176 = adm1176_test.ADM1176_Test()
    adm1176.run_diagnostic_test()

    # BQ25883
    bq25883 = BQ25883_Test()
    bq25883.run_diagnostic_test()
    
    # DRV8830
    drv8830_xp = DRV8830_Test()
    drv8830_xp.run_diagnostic_test(BoardConfig.DRV8830_XP_I2C_ADDR)
    drv8830_xp.run_diagnostic_test(BoardConfig.DRV8830_XM_I2C_ADDR)
    drv8830_xp.run_diagnostic_test(BoardConfig.DRV8830_YP_I2C_ADDR)
    drv8830_xp.run_diagnostic_test(BoardConfig.DRV8830_YM_I2C_ADDR)
    drv8830_xp.run_diagnostic_test(BoardConfig.DRV8830_CAM_I2C_ADDR)

    #BMX160
    bmx160_dev = BMX160_Test()
    bmx160_dev.run_diagonstic_test()

print("Running diagnostics...")
run_diagnostics()