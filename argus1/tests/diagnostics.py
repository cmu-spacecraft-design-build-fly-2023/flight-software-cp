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

# Hardware Specific Libs
import pycubed_rfm9x # Radio
import bmx160 # IMU
import neopixel # RGB LED
import bq25883 # USB Charger
import adm1176_tests # Power Monitor Tests
import bmx160_tests # IMU Tests
import bq25883_tests # Charger Tests

# Common CircuitPython Libs
from os import listdir,stat,statvfs,mkdir,chdir
from bitflags import bitFlag,multiBitFlag,multiByte
from micropython import const

def main():
    # ADM1176
    adm1176 = adm1176_tests.ADM1176_Tests()
    adm1176.run_diagnostic_test()

    # BQ25883
    bq25883 = bq25883_tests.bq25883_Tests()
    bq25883.run_diagnostic_test()
    

if __name__ == "__main__":
    main()