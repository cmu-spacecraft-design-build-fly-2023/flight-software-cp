import board
import busio
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
    I2C2 = busio.I2C(board.SCL2, board.SDA2)
    SPI = busio.SPI(board.SCK, board.MOSI, board.MISO)
    UART = busio.UART(board.TX, board.RX, baudrate=9600)
    
    # Argus1 Hardware
    RFM9X_SPI               = board.SPI
    RFM9X_CS                = board.RF1_CS
    RFM9X_RST               = board.RF1_RST
    RFM9X_EN                = board.EN_RF
    RFM9X_DIO0              = board.RF1_IO0

    BMX160_I2C              = I2C
    BMX160_I2C_ADDR         = const(0x68)
    BMX160_EN               = board.EN_IMU

    ADM1176_I2C             = I2C
    ADM1176_BAT_I2C_ADDR    = const(0x4A)
    ADM1176_JET_I2C_ADDR    = const(0xCA)

    BQ25883_I2C             = I2C
    BQ25883_I2C_ADDR        = const(0x6B)

    PCF8523_I2C             = I2C
    PCF8523_I2C_ADDR        = const(0x4A)

    GPS_UART                = UART
    GPS_EN                  = board.EN_GPS

    # XY Hardware
    DRV8830_I2C             = I2C2
    DRV8830_XP_I2C_ADDR     = const(0xC0)
    DRV8830_XM_I2C_ADDR     = const(0xC2)
    DRV8830_YP_I2C_ADDR     = const(0xC4)
    DRV8830_YM_I2C_ADDR     = const(0xC6)
    DRV8830_CAM_I2C_ADDR    = const(0xC8)

    OPT4001_I2C             = I2C2
    OPT4001_XP_I2C_ADDR     = const(0x42)
    OPT4001_XM_I2C_ADDR     = const(0x43)
    OPT4001_YP_I2C_ADDR     = const(0x44)
    OPT4001_YM_I2C_ADDR     = const(0x45)
    OPT4001_ZP_I2C_ADDR     = const(0x46)
    OPT4001_ZM_I2C_ADDR     = const(0x47)

    # Jetson Hardware

    # Powerboard Hardware