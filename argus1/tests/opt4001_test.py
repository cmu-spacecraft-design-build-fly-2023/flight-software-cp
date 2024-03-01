import board, microcontroller
import busio, time, sys
from analogio import AnalogIn
import digitalio, sdcardio, pwmio, tasko

from argus1.board_config import BoardConfig
from component_test import ComponentTest
import opt4001

class OPT4001_Test(ComponentTest):
    def __init__(self, i2c_address: int) -> None:
        self.initialized = False
        self._device = None

        self.i2c_address = i2c_address
        
        try:
            self._initialize()
            self.initialized = True
        except Exception as e:
            print("Could not initialize OPT4001. Error: " + str(e))
    

    def _initialize(self) -> None:
        self._device = opt4001.OPT4001(BoardConfig.OPT4001_I2C, self.i2c_address)

    def _check_id_test(self) -> bool:
        """Checks the opt4001 id to ensure that we can interface with the devices
        
        :return: True if read successful, otherwise false
        """
        success = self._device.check_id()
        return success
    
    def _read_counter_crc_test(self) -> bool:
        """_read_counter_crc_test: Checks if the crc counter functions properly

        :return: True if pass, otherwise false
        """
        success = True
        lsb, counter,crc = self._device.get_lsb_counter_crc(opt4001.RESULT_L) #looking at register 1
        if not (0 <= counter) and (counter <= 15):
            success = False
        
        return success
    
    def run_diagnostic_test(self):
        if not self.initialized():
            print("OPT4001 not initialized. Exiting test.")
            return

        success = True

        if not self._read_counter_crc_test():
            print("OPT4001: CRC counter test failed")
            success = False
        
        if not self._check_id_test():
            print("OPT4001: ID check failed")
            success = False

        if success:
            print("All tests passed")
