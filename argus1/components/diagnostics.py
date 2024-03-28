"""
diagnostics.py

This file contains the base class for alll components which need diagnostic tests run

Author: Harry Rosmann
Date: 03/26/2024
"""

from micropython import const
import math

class Diagnostics:
    """
    Interface for all component diagnostic tests
    """

    ############### ERROR CODES ###############
    NOERROR = const(0)

    # ADM1176 errors
    ADM1176_NOT_INITIALIZED                         = const(1)
    ADM1176_NOT_CONNECTED_TO_POWER                  = const(2)
    ADM1176_VOLTAGE_OUT_OF_RANGE                    = const(3)
    ADM1176_COULD_NOT_TURN_ON                       = const(4)
    ADM1176_COULD_NOT_TURN_OFF                      = const(5)
    ADM1176_ADC_OC_OVERCURRENT_MAX                  = const(6)
    ADM1176_ADC_ALERT_OVERCURRENT_MAX               = const(7)
    ADM1176_ADC_OC_OVERCURRENT_MIN_THRESHOLD        = const(8)
    ADM1176_ADC_ALERT_OVERCURRENT_MIN_THRESHOLD     = const(9)
    
    # BQ25883 errors
    BQ25883_NOT_INITIALIZED                         = const(10)
    BQ25883_INPUT_OVERVOLTAGE                       = const(11)
    BQ25883_THERMAL_SHUTDOWN                        = const(12)
    BQ25883_BATTERY_OVERVOLTAGE                     = const(13)
    BQ25883_CHARGE_SAFETY_TIMER_EXPIRED             = const(14)
    
    # OPT4001 errors
    OPT4001_NOT_INITIALIZED                         = const(15)
    OPT4001_CRC_COUNTER_TEST_FAILED                 = const(16)
    OPT4001_ID_CHECK_FAILED                         = const(17)
    
    # Adafruit GPS errors
    ADAFRUIT_GPS_NOT_INITIALIZED                    = const(18)
    ADAFRUIT_GPS_UPDATE_CHECK_FAILED                = const(19)
    
    # PCF8523 errors
    PCF8523_NOT_INITIALIZED                         = const(20)
    PCF8523_BATTERY_LOW                             = const(21)
    PCF8523_LOST_POWER                              = const(22)
    
    # BMX160 errors
    BMX160_NOT_INITIALIZED                          = const(23)
    BMX160_FATAL_ERROR                              = const(24)
    BMX160_NON_FATAL_ERROR                          = const(25)
    BMX160_DROP_COMMAND_ERROR                       = const(26)
    BMX160_UNSPECIFIED_ERROR                        = const(27)
    
    # DRV8830 errors
    DRV8830_NOT_INITIALIZED                         = const(28)
    DRV8830_OVERCURRENT_EVENT                       = const(29)
    DRV8830_UNDERVOLTAGE_LOCKOUT                    = const(30)
    DRV8830_OVERTEMPERATURE_CONDITION               = const(31)
    DRV8830_EXTENDED_CURRENT_LIMIT_EVENT            = const(32)
    DRV8830_THROTTLE_OUTSIDE_RANGE                  = const(33)
    DRV8830_THROTTLE_VOLTS_OUTSIDE_RANGE            = const(34)
    DRV8830_THROTTLE_RAW_OUTSIDE_RANGE              = const(35)
    
    # RFM9X errors
    RFM9X_NOT_INITIALIZED                           = const(36)

    __ERROR_MIN = const(0)
    __ERROR_MAX = const(36)

    def __init__(self):
        self.__errors_present = False

    def error_present(self) -> bool:
        return self.__errors_present

    def run_diagnostics(self) -> list[int] | None:
        """run_diagnostic_test: Run all tests for the component
        """
        raise NotImplementedError("Subclasses must implement run_diagnostic_test method")

    @staticmethod
    def convert_errors_to_byte_array(errors: list[int]) -> bytes:
        """convert_errors_to_byte_array: Convert a list of errors to a packed set of bytes.
        Each bit represents a corresponding error. 

        :param errors: The list of errors. Must be a valid diagnostic error
        :returns: The byte array of toggled error bits
        """
        BITS_IN_BYTE = const(8)

        num_bytes = Diagnostics.__ERROR_MAX / BITS_IN_BYTE
        error_bytes = bytearray([0x00] * num_bytes)

        unique_errors = list(set(errors))
        
        for error in unique_errors:
            # Ensure it is a valid error number
            if error < Diagnostics.__ERROR_MIN or error > Diagnostics.__ERROR_MAX:
                raise RuntimeError(f"Unrecognized error number ({error})")
            
            # NOTE: We do want to track if there is no error

            byte_num = error / BITS_IN_BYTE

            error_bytes[byte_num] |= (0x1 << error)

        return error_bytes
            


            

