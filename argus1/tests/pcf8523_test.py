import board, microcontroller
import busio, time, sys
from analogio import AnalogIn
import digitalio, sdcardio, pwmio, tasko

from board_config import BoardConfig
from component_test import ComponentTest
import pcf8523

class PCF2583_Test(ComponentTest):
    def __init__(self) -> None:
        self.initialized = False
        self._device = None
        
        try:
            self._initialize()
            self.initialized = True
        except Exception as e:
            print("Could not initialize OPT4001. Error: " + str(e))
    

    def _initialize(self) -> None:
        self._device = pcf2583.PCF8523(BoardConfig.PCF8523_I2C, BoardConfig.PCF8523_I2C_ADDR)

    def _check_lost_power(self) -> bool:
        """_check_lost_power: Check if power was lost since the time was set.
        
        :return: True if power was lost, otherwise true
        """
        if self._device.lost_power:
            return False
        return True
            

    def _check_battery_status(self) -> bool:
        """_check_battery_status: Checks if the battery status is low.
        
        :return: False if the battery is low, otherwise true
        """
        if self._device.battery_low:
            return False
        return True

    def run_diagnostic_test(self) -> None:
        if not self.initialized:
            print("PCF2583 not initialized. Exiting test.")
            return

        success = True
        if not self._check_alarm_status():
            print("PCF2583: Alarm status test failed")
            success = False
        if not self._check_lost_power():
            print("PCF2583: Alarm status test failed")
            success = False

        if success:
            print("All tests passed")
            
