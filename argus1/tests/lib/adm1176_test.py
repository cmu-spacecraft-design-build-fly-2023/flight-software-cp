import board, microcontroller
import busio, time, sys
from analogio import AnalogIn
import digitalio, sdcardio, pwmio, tasko
from micropython import const

from component_test import ComponentTest
from board_config import BoardConfig
import adm1176

class ADM1176_Tests(ComponentTest):
    def __init__(self) -> None:
        self.initialized = False
        self._device = None
        
        try:
            self.initialize()
            self.initialized = True
        except Exception as e:
            print("Could not initialize ADM1176. Error: " + str(e))
    
    def initialize(self) -> None:
        self._device = adm1176.ADM1176(BoardConfig.ADM1176_I2C, addr=BoardConfig.ADM1176_I2C_ADDR)
        self._device.ON()
        self._device.clear()
        self._device.overcurrent_level()

    def _simple_vi_read(self) -> bool:
        """_simple_volt_read: Reads the voltage ten times, ensures that it does not fluctuate
        too much.
         
        :return: true if test passes, false if fails
        """
        V_MAX = const(4.5)
        V_MIN = const(3.0)
        
        # prev_c = 0.0
        # prev_v = 0.0
        
        for i in range(10):
            (rVoltage, rCurrent) = self._device.read_voltage_current()
            if (rVoltage == 0 or rCurrent == 0):
                print("Error: Not connected to power!! Voltage: ", rVoltage, " Current: ", rCurrent)
                return False
            elif (rVoltage > V_MAX or rVoltage < V_MIN ):
                print("Error: Voltage out of typical range!! Voltage Reading: ",rVoltage)
                return False
            # elif (prev_c == rCurrent):
            #     print("Error: No change in Current!! Prev Current: ", prev_c, " New Current: ", rCurrent)
            #     return False
            # elif (prev_v == rVoltage):
            #     print("Error: No change in voltage!!")
            #     return False
            
            # prev_v = rVoltage
            # prev_c = rCurrent
        
        return True
    
    def _on_off_test(self) -> bool:
        """_on_off_test: Turns the device on, off, and on 
        again and ensures corresponding register set

        :return: true if test passes, false if fails
        """
        # Turn the device on
        self._device.ON()
        status_reg = self._device.status()
        if ((status_reg & adm1176.STATUS_OFF_STATUS) != adm1176.STATUS_OFF_STATUS):
            print("Error: Could not turn on device")
            return False
         

        # Turn the device off
        self._device.OFF()
        status_reg = self._device.status()
        if ((status_reg & adm1176.STATUS_OFF_STATUS) != 0):
            print("Error: Could not turn off device")
            return False

        # Turn the device on again
        self._device.ON()
        status_reg = self._device.status()
        if ((status_reg & adm1176.STATUS_OFF_STATUS) != adm1176.STATUS_OFF_STATUS):
            print("Error: Could not turn on device")
            return False
        
        return True
    
    def _overcurrent_test(self) -> bool:
        """_overcurrent_test: Tests that the threshold is triggering
        correctly.
        
        :return: true if test passes, false if fails
        """
        success = True

        # Set the overcurrent threshold to max
        self._device.overcurrent_level(0xFF)
        self._device.clear()

        status = self._device.status()
        if ((status & adm1176.STATUS_ADC_OC) == adm1176.STATUS_ADC_OC):
            print("Error: ADC OC was triggered at overcurrent max")
            success = False
        elif ((status & adm1176.STATUS_ADC_ALERT) ==  adm1176.STATUS_ADC_ALERT):
            print("Error: ADC Alert was triggered at overcurrent max")
            success = False

        # Set the overcurrent thresh to min
        self._device.overcurrent_level(0x00)
        self._device.clear()

        status = self._device.status()
        if ((status & adm1176.STATUS_ADC_OC) != adm1176.STATUS_ADC_OC):
            print("Error: ADC OC was triggered at overcurrent min threshold")
            success = False
        elif ((status & adm1176.STATUS_ADC_ALERT) !=  adm1176.STATUS_ADC_ALERT):
            print("Error: ADC Alert was triggered at overcurrent min threshold")
            success = False

        return success

    def run_diagnostic_test(self) -> None:
        if not self.initialized:
            print("ADM1176 not initialized. Exiting test.")
            
        print("Running tests for ADM1176...")
        success = True
        if not self._simple_vi_read():
            print("ADM1176: Simple VI read failed")
            success = False
        if not self._on_off_test():
            print("ADM1176: on/off test failed")
            success = False
        if not self._overcurrent_test():
            print("ADM1176: Overcurrent test failed")
            success = False

        if success:
            print("ADM1176: All tests pass!")
        
        
        