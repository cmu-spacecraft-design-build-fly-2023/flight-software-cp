import board, microcontroller
import busio, time, sys
from storage import mount,umount,VfsFat
from analogio import AnalogIn
import digitalio, sdcardio, pwmio, tasko
from micropython import const

class BoardConfig:
    """
    Class: StartupTestConfig

    Contains the configuration for the startup tests.
    """
    # Enables
    RFM9X = True    # Radio
    BMX160 = True   # IMU
    ADM1176 = True  # Power Monitor
    DRV8830 = True  # Torque Coil

    # Interfaces
    I2C = busio.I2C(board.SCL, board.SDA)
    SPI = busio.SPI(board.SCK, board.MOSI, board.MISO)
    UART = busio.UART(board.TX, board.RX, baudrate=9600)
    
    # Argus1 Hardware
    RFM9X_SPI = board.SPI
    RFM9X_CS = board.RF1_CS
    RFM9X_RST = board.RF1_RST
    RFM9X_EN = board.EN_RF
    RFM9X_DIO0 = board.RF1_IO0

    BMX160_I2C = I2C

    ADM1176_I2C = I2C
    ADM1176_I2C_ADDR = const(0x94)

    DRV8830_I2C = I2C
    DRV8830_I2C_ADDR = const(0xC8)

    # XY Hardware

    # Jetson Hardware

    # Powerboard Hardware