import board, microcontroller
import busio, time, sys
from analogio import AnalogIn
import digitalio, sdcardio, pwmio, tasko

from argus1.board_config import BoardConfig
from component_test import ComponentTest
import opt4001

class OPT4001Test(ComponentTest):
    def __init__(self) -> None:
        self.initialized = False
        self._device = None
        
        try:
            self.initialize()
            self.initialized = True
        except Exception as e:
            print("Could not initialize OPT4001. Error: " + str(e))
    

    def initialize(self,I2C_ADDR) -> None:
        self._device = opt4001.OPT4001(BoardConfig.OPT4001_I2C, addr=I2C_ADDR)

    def _check_id_test(self) -> bool:
        success = self._device.check_id()
        return success
    
    def _read_counter_crc_test(self) -> bool:
        success = True
        (lsb,counter,crc) = self._device.get_lsb_counter_crc(opt4001.RESULT_L) #looking at register 1
        if not (0 <= counter and counter <= 15):
            success = False
            return success
        
        
        
        
        return success
            
