import board, microcontroller
import busio, time, sys
from analogio import AnalogIn
import digitalio, sdcardio, pwmio, tasko

from component_test import ComponentTest
from board_config import BoardConfig
import drv8830

class DRV8830_Test(ComponentTest):
    def __init__(self) -> None:
        self.initialized = False
        self._device = None

        try:
            self.initialize()
            self.initialized = True
        except Exception as e:
            print("Could not initialize DRV8830. Error: " + str(e))
    
    def initialize(self, I2C_ADDR) -> None:
        self._device = drv8830.DRV8830(BoardConfig.DRV8830_I2C, addr=I2C_ADDR)

    def _check_for_faults(self) -> bool:
        """_check_for_faults: Checks for any device faluts returned by fault function in DRV8830

        :return: true if test passes, false if fails
        """
        success = True
        faults_flag, faults = self._device.fault()
        
        if not faults_flag:
            return success
        
        success = False
        
        if ("OCP" in faults):
            print("ERROR: Overcurrent event - device disabled, clear fault to reactivate")
        if ("UVLO" in faults):
            print("ERROR: Undervoltage lockout - device disabled, resumes with voltage restoration")
        if ("OTS" in faults):
            print("ERROR: Overtemperature condition - device disabled, resumes with lower temperature")
        if ("ILIMIT" in faults):
            print("ERROR: Extended current limit event - device disabled, clear fault to reactivate")

        return success
    
    def _throttle_tests(self) -> bool:
        """_throttle_tests: Checks for any throttle errors in DRV8830, whether the returned reading is
        outside of the set range indicated in the driver file

        :return: true if test passes, false if fails
        """
        success = True
        throttle_val = self._device.throttle()
        if throttle_val is not None:
            if (throttle_val < -1.0) or (throttle_val > 1.0):
                print("ERROR: Throttle value outside of settled range")
                success = False
                return success
            
        throttle_volts_val = self._device.throttle_volts()
        if throttle_volts_val is not None:
            if (throttle_volts_val < -5.06) or (throttle_volts_val > 5.06):
                print("ERROR: Throttle Volts value outside of settled range")
                success = False
                return success
            
        throttle_raw_val = self._device.throttle_volts()
        if throttle_raw_val is not None:
            if (throttle_raw_val < -63) or (throttle_raw_val > 63):
                print("ERROR: Throttle raw value outside of settled range")
                success = False
                return success
        
        return success

    def run_diagnostic_test(self, I2C_ADDR) -> None:
        if not self.initialized(I2C_ADDR):
            print("DRV8830 not initialized. Exiting test.")

        success = True
        if not self._check_for_faults():
            print("DRV8830: Fault Register Flag check test failed")
            success = False
        
        if not self._throttle_tests():
            print("DRV8830: Throttle test failed")
            success = False

        if success:
            print("All tests passed")
    