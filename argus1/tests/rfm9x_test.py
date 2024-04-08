from board_config import BoardConfig
import digitalio
from components import pycubed_rfm9x
from .component_test import ComponentTest
import math

class RFM9X_Test(ComponentTest):
    """
    Class: RFM9X_Test

    Contains the test functions for the RFM9X module.
    """
    def __init__(self):
        try:
            self._initialize()
            self.initialized = True
        except Exception as e:
            print("Could not initialize RFM9X. Error: " + str(e))

    
    def _initialize(self) -> None:
        """initialize: Initialize the RFM9X module for testing
        """
        radio_en = digitalio.DigitalInOut(BoardConfig.RFM9X_EN)
        radio_en.switch_to_output()
        radio_en.value = True
        cs = BoardConfig.RFM9X_CS
        reset = BoardConfig.RFM9X_RST
        frequency = 915.6
        self._device = pycubed_rfm9x.RFM9x(BoardConfig.RFM9X_SPI, cs, reset, frequency)

    def _read_frequency(self) -> bool:
        frequency = self._device.frequency_mhz()
        if math.isclose(frequency, 433, abs_tol = 1) or math.isclose(frequency, 915.6, abs_tol = 1):
            return True
        else:
            return False

    def run_diagnostic_test(self) -> None:
        """run_diagnostic_test: Run all tests for the RFM9X module
        """
        success = True
        if not self.initialized:
            print("RFM9X not initialized. Exiting test.")
            success = False
            return
        
        if not self._read_frequency():
            print("RFM9X: Frequency reading incorrect.")
            success = False

        if success:
            print("RFM9X: All tests pass!")
        

        
