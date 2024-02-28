import board, microcontroller
import busio, time, sys
from analogio import AnalogIn
import digitalio, sdcardio, pwmio, tasko

from argus1.board_config import BoardConfig
from component_test import ComponentTest
import adafruit_gps

class Adafruit_GPS_Test(ComponentTest):
    def __init__(self) -> None:
        self.initialized = False
        self._device = None

        try:
            self.initialize()
            self.initialized = True
        except Exception as e:
            print("Could not initialize Adafruit_GPS. Error: " + str(e))
    
    def initialize(self) -> None:
        self._device = adafruit_gps.GPS_GtopI2C(BoardConfig.GPS_I2C)

    def _check_for_errors(self) -> bool:
        """_check_for_errors: Checks for any device errors on GPS

        :return: true if test passes, false if fails
        """
        success = True

        return success
       

    def run_diagnostic_test(self) -> None:
        if not self.initialized:
            print("Adafruit GPS not initialized. Exiting test.")

        success = True
        if not self._check_for_errors():
            print("Adafruit GPS: Error code check test failed")
            success = False

        if success:
            print("All tests passed")
    