from board_config import BoardConfig
from components import bmx160
from .component_test import ComponentTest

class BMX160_Test(ComponentTest):
    def __init__(self) -> None:
        self.initialized = False
        self._device = None

        try:
            self._initialize()
            self.initialized = True
        except Exception as e:
            print("Could not initialize BMX160. Error: " + str(e))
    
    def _initialize(self) -> None:
        self._device = bmx160.BMX160_I2C(BoardConfig.I2C)

    def _check_for_errors(self) -> bool:
        """_check_for_errors: Checks for any device errors on BMX160

        :return: true if test passes, false if fails
        """
        success = True

        error_reg = self._device.query_error
        if (error_reg > 0):
            print("BMX160: Error detected. Error register: ", error_reg)
            success = False

        if self._device.fatal_err != 0:
            print("Error: Fatal error as occured")
            success = False 
        
        if(self._device.error_code in bmx160.BMX160_ERROR_CODES):
            print("Non-fatal error", self._device.error_code, " (Refer to datasheet to see type of error)")
            success = False

        if (self._device.drop_cmd_err != 0):
            print("Drop command error received")
            success = False

        return success
       

    def run_diagonstic_test(self) -> None:
        if not self.initialized:
            print("BMX160 not initialized. Exiting test.")
            success = False
            return

        success = True
        if not self._check_for_errors():
            print("BMX160: Error code check test failed")
            success = False

        if success:
            print("All tests passed")
    