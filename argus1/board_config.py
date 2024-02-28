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
    BMX160_I2C_ADDR = const(0x68)

    ADM1176_I2C = I2C
    ADM1176_I2C_ADDR = const(0x94)

    BQ25883_I2C = I2C
    BQ25883_I2C_ADDR = const(0x6B)

    DRV8830_I2C = I2C
    DRV8830_XP_I2C_ADDR     = const(0xC0)
    DRV8830_XM_I2C_ADDR     = const(0xC2)
    DRV8830_YP_I2C_ADDR     = const(0xC4)
    DRV8830_YM_I2C_ADDR     = const(0xC6)
    DRV8830_CAM_I2C_ADDR    = const(0xC8)

    OPT4001_I2C = I2C
    OPT4001_EXPANDER1_I2C_ADDR = const(0x42)
    OPT4001_EXPANDER2_I2C_ADDR = const(0x43)
    OPT4001_GND_I2C_ADDR = const(0x44)
    OPT4001_VDD_I2C_ADDR = const(0x45)
    OPT4001_SDA_I2C_ADDR = const(0x46)
    OPT4001_SCL_I2C_ADDR = const(0x47)

    PCF2583_I2C = I2C
    PCF2583_I2C_ADDR = const(0x68)

    GPS_I2C = I2C

    # XY Hardware

    # Jetson Hardware

    # Powerboard Hardware