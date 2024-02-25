import board, microcontroller
import busio, time, sys
from analogio import AnalogIn
import digitalio, sdcardio, pwmio, tasko

from argus1.board_config import BoardConfig
from component_test import ComponentTest
import pycubed_rfm9x

class RFM9X_Test(ComponentTest):
    """
    Class: RFM9X_Test

    Contains the test functions for the RFM9X module.
    """
    def __init__(self):
        try:
            self.initialize()
        except Exception as e:
            print("Could not initialize RFM9X. Error: " + str(e))

    
    def initialize(self) -> None:
        """initialize: Initialize the RFM9X module for testing
        """
        self.rfm9x = pycubed_rfm9x.RFM9x(self.config.SPI,
                                         self.config.RFM9X_CS, 
                                         self.config.RFM9X_RST, 
                                         self.config.RFM9X_DIO0, 
                                         self.config.RFM9X_I2C)

        
    def run_diagnostic_test(self) -> None:
        """run_diagnostic_test: Run all tests for the RFM9X module
        """
        pass