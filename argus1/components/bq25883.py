"""
`bq25883`
====================================================

CircuitPython driver for the BQ25883 2-cell USB boost-mode charger.

* Author(s): Max Holliday

Implementation Notes
--------------------

"""

from micropython import const
from adafruit_bus_device.i2c_device import I2CDevice

from adafruit_register.i2c_struct import ROUnaryStruct, UnaryStruct
from adafruit_register.i2c_bits import ROBits, RWBits
from adafruit_register.i2c_bit import ROBit, RWBit

from diagnostics import Diagnostics

# Registers
_BATV_LIM       = const(0x00)
_CHRGI_LIM      = const(0x01) 
_VIN_LIM        = const(0x02) 
_IIN_LIM        = const(0x03) 
_TERM_CTRL      = const(0x04) 
_CHRGR_CRTL1    = const(0x05) 
_CHRGR_CRTL2    = const(0x06) 
_CHRGR_CRTL3    = const(0x07) 
_CHRGR_CRTL4    = const(0x08) 
_OTG_CTRL       = const(0x09) 
_ICO_LIM        = const(0x0A) 
_CHRG_STAT1     = const(0x0B) 
_CHRG_STAT2     = const(0x0C) 
_NTC_STAT       = const(0x0D) 
_FAULT_STAT     = const(0x0E)
_CHRGR_FLAG1    = const(0x0F) 
_CHRGR_FLAG2    = const(0x10) 
_FAULT_FLAG     = const(0x11) 
_CHRGR_MSK1     = const(0x12) 
_CHRGR_MSK2     = const(0x13) 
_FAULT_MSK      = const(0x14) 
_ADC_CTRL       = const(0x15)
_ADC_FN_CTRL    = const(0x16) 
_IBUS_ADC1      = const(0x17) 
_IBUS_ADC0      = const(0x18) 
_ICHG_ADC1      = const(0x19) 
_ICHG_ADC0      = const(0x1A) 
_VBUS_ADC1      = const(0x1B) 
_VBUS_ADC0      = const(0x1C)
_VBAT_ADC1      = const(0x1D) 
_VBAT_ADC0      = const(0x1E) 
_VSYS_ADC1      = const(0x1F) 
_VSYS_ADC0      = const(0x20) 
_TS_ADC1        = const(0x21) 
_TS_ADC0        = const(0x22) 
_TDIE_ADC1      = const(0x23)
_TDIE_ADC0      = const(0x24)
_PART_INFO      = const(0x25)

def _to_signed(num):
    if num > 0x7FFF:
        num -= 0x10000
    return num

class BQ25883(Diagnostics):
    """BQ25883: The 
    
    """
    _pn                  = ROBits(4,_PART_INFO,3,1,False)
    _fault_status        = ROBits(8,_FAULT_STAT,0,1,False)
    _chrgr_status1       = ROBits(8,_CHRG_STAT1,0,1,False)
    _chrgr_status2       = ROBits(8,_CHRG_STAT2,0,1,False)
    _chrg_status         = ROBits(3,_CHRG_STAT1,0,1,False)
    _otg_ctrl            = ROBits(8,_OTG_CTRL,0,1,False)
    _chrg_ctrl2          = ROBits(8,_CHRGR_CRTL2,0,1,False)
    _wdt                 = RWBits(2,_CHRGR_CRTL1,4,1,False)
    _ntc_stat            = RWBits(3,_NTC_STAT,0,1,False)
    _en_chrg             = RWBit(_CHRGR_CRTL2,3,1,False)
    _reg_rst             = RWBit(_PART_INFO, 7, 1, False)
    _stat_dis            = RWBit(_CHRGR_CRTL1, 6, 1, False)
    _inlim               = RWBit(_CHRGI_LIM, 6, 1, False)
    _ichrg               = RWBits(5,_CHRGI_LIM,0,1,False)

    def __init__(self, i2c_bus, addr=0x6B):
        self.i2c_device = I2CDevice(i2c_bus, addr)
        self.i2c_addr = addr
        assert self._pn == 3, "Unable to find BQ25883"

    @property
    def fault_status(self) -> int:
        return self._fault_status
    
    @property
    def charger_status1(self) -> int:
        return self._chrgr_status1
    
    @property
    def charger_status2(self) -> int:
        return self._chrgr_status2
    
    @property
    def charge_status(self) -> int:
        return self._chrg_status
    
    @property
    def ntc_status(self) -> int:
        return self._ntc_stat

    @property
    def charge_en(self) -> bool:
        return self._chrg_ctrl2
    @charge_en.setter
    def charge_en(self, value: bool) -> None:
        self._en_chrg = value

    @property
    def charging_current(self) -> int:
       return self._ichrg
    @charging_current.setter
    def charging_current(self, value: int) -> None:
        # default:0x1e=1500mA, 0x8=400mA
        self._ichrg=value

    @property
    def wdt(self) -> int:
        return self._wdt
    @wdt.setter
    def wdt(self, value: int) -> None:
        if not value:
            self._wdt = 0
        else:
            self._wdt = value

    @property
    def en_led(self) -> bool:
        return not self._stat_dis
    @en_led.setter
    def led(self, value: bool) -> None:
        self._stat_dis = not value

######################### DIAGNOSTICS #########################
    
    def __check_for_faults(self) -> list[int]:
        """__check_for_faults: Check for faults in the BQ25883.
        Returns:
            bool: True if there is a fault, False if there is not a fault.
        """
        errors: list[int] = []

        status = self.fault_status

        if (status & (0xF << 4)) != 0:
            list.append[Diagnostics.BQ25883_INPUT_OVERVOLTAGE]
        if (status & (0x1 << 5)) != 0:
            list.append[Diagnostics.BQ25883_THERMAL_SHUTDOWN]
        if (status & (0x1 << 6)) != 0:
            list.append[Diagnostics.BQ25883_BATTERY_OVERVOLTAGE]
        if (status & (0x1 << 7)) != 0:
            list.append[Diagnostics.BQ25883_CHARGE_SAFETY_TIMER_EXPIRED]

        return errors

    def run_diagnostics(self) -> list[int] | None:
        """run_diagnostic_test: Run all tests for the component

        :return: List of error codes
        """
        error_list = []

        error_list = self.__check_for_faults()

        error_list = list(set(error_list))

        if not Diagnostics.NOERROR in error_list:
            super().__errors_present = True

        return error_list