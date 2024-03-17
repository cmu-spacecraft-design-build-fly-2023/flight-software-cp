from board_config import BoardConfig
from components import bq25883
from .component_test import ComponentTest

class BQ25883_Test(ComponentTest):
    def __init__(self) -> None:
        self.initialized = False
        self._device = None

        try:
            self._initialize()
        except Exception as e:
            print("Could not initialize BQ25883. Error: " + str(e))
    
    def _initialize(self) -> None:
        self._device = bq25883.BQ25883(BoardConfig.I2C, addr=BoardConfig.BQ25883_I2C_ADDR)
        self.initialized = True

    def _check_for_faults(self) -> bool:
        """__check_for_faults: Check for faults in the BQ25883.
        Returns:
            bool: True if there is a fault, False if there is not a fault.
        """
        fault = False
        status = self._device.fault_status

        if (status & (0xF << 4)) != 0:
            fault = True
        if (status & (0x1 << 4)) != 0:
            print("BQ25883: Input overvoltage")
        if (status & (0x1 << 5)) != 0:
            print("BQ25883: Thermal shutdown")
        if (status & (0x1 << 6)) != 0:
            print("BQ25883: Battery overvoltage")
        if (status & (0x1 << 7)) != 0:
            print("BQ25883: Charge safety timer expired")

        return fault
       
    def run_diagnostic_test(self) -> None:
        """run_diagnostic_test: Run the diagnostic test for the BQ25883.
        """
        if not self.initialized:
            print("BQ25883 not initialized")
            return

        self._device.charge_en = True
        if not self._check_for_faults():
            print("All tests passed")
        else:
            print("BQ25883: Fault detected")
    