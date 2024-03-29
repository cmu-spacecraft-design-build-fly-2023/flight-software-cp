from board_config import BoardConfig
from components import adafruit_gps
from .component_test import ComponentTest

import digitalio
from time import sleep

class GPS_Test(ComponentTest):
    def __init__(self) -> None:
        self.initialized = False
        self._device = None

        try:
            self._initialize()
            self.initialized = True
        except Exception as e:
            print("Could not initialize Adafruit_GPS. Error: " + str(e))
    
    def _initialize(self) -> None:
        self._device = adafruit_gps.GPS(BoardConfig.GPS_UART)
        self._enable = digitalio.DigitalInOut(BoardConfig.GPS_EN)
        self._enable.switch_to_output()

    def _check_for_updates(self) -> bool:
        """_check_for_errors: Checks for an update on the GPS

        :return: true if test passes, false if fails
        """
        success = False
        num_tries = 20

        for i in range(num_tries):
            success = self._device.update()
            if success:
                break
            sleep(1)

        return success
       

    def run_diagnostic_test(self) -> None:
        if not self.initialized:
            print("Adafruit GPS not initialized. Exiting test.")

        success = True
        if not self._check_for_updates():
            print("Adafruit GPS: Update check test failed")
            success = False

        if success:
            print("All tests passed")
    