"""
Test each component of the argus1 library as an initial
integration test.
Argus1 Version: 1.0

Authors: Harry Rosmann, Gordonson Yan
"""

from board_config import BoardConfig

from tests import adm1176_test, bmx160_test, bq25883_test, drv8830_test, opt4001_test, pcf8523_test, rfm9x_test, gps_test

def run_diagnostics():
    # PCF8523
    # print("Running PCF8523 Tests")
    # pcf8523 = pcf8523_test.PCF8523_Test()
    # pcf8523.run_diagnostic_test()
    # print()

    # # ADM1176 Battery
    # print("Running ADM1176 Battery Tests")
    # adm1176_b = adm1176_test.ADM1176_Test(BoardConfig.ADM1176_BAT_I2C_ADDR)
    # adm1176_b.run_diagnostic_test()
    # print()

    # print("Running ADM1176 Jetson Tests")
    # adm1176_j = adm1176_test.ADM1176_Test(BoardConfig.ADM1176_JET_I2C_ADDR)
    # adm1176_j.run_diagnostic_test()
    # print()

    #BMX160
    # print("Running BMX160 Tests")
    # bmx160_dev = bmx160_test.BMX160_Test()
    # bmx160_dev.run_diagonstic_test()
    # print()

    # BQ25883
    # print("Running BQ25883 Tests")
    # bq25883 = bq25883_test.BQ25883_Test()
    # bq25883.run_diagnostic_test()
    # print()

    # # RMF9x
    # print("Running RFM9X Test")
    # rfm9x = rfm9x_test.RFM9X_Test()
    # rfm9x.run_diagnostic_test()
    # print()
    
    # DRV8830
    print("Running DRV8830 Tests")
    drv8830_xp = drv8830_test.DRV8830_Test(BoardConfig.DRV8830_XP_I2C_ADDR)
    drv8830_xp.run_diagnostic_test()
    # print()
    # drv8830_xm = drv8830_test.DRV8830_Test(BoardConfig.DRV8830_XM_I2C_ADDR)
    # drv8830_xm.run_diagnostic_test()
    # print()
    # drv8830_yp = drv8830_test.DRV8830_Test(BoardConfig.DRV8830_YP_I2C_ADDR)
    # drv8830_yp.run_diagnostic_test()
    # print()
    # drv8830_ym = drv8830_test.DRV8830_Test(BoardConfig.DRV8830_YM_I2C_ADDR)
    # drv8830_ym.run_diagnostic_test()
    # print()
    # drv8830_cam = drv8830_test.DRV8830_Test(BoardConfig.DRV8830_CAM_I2C_ADDR)
    # drv8830_cam.run_diagnostic_test()
    # print()

    # OPT4001
    # print("Running OPT4001 Tests")
    # opt4001_xp = opt4001_test.OPT4001_Test(BoardConfig.OPT4001_XP_I2C_ADDR)
    # opt4001_xp.run_diagnostic_test()
    # print()
    # opt4001_xm = opt4001_test.OPT4001_Test(BoardConfig.OPT4001_XM_I2C_ADDR)
    # opt4001_xm.run_diagnostic_test()
    # print()
    # opt4001_yp = opt4001_test.OPT4001_Test(BoardConfig.OPT4001_YP_I2C_ADDR)
    # opt4001_yp.run_diagnostic_test()
    # print()
    # opt4001_ym = opt4001_test.OPT4001_Test(BoardConfig.OPT4001_YM_I2C_ADDR)
    # opt4001_ym.run_diagnostic_test()
    # print()
    # opt4001_zp = opt4001_test.OPT4001_Test(BoardConfig.OPT4001_ZP_I2C_ADDR)
    # opt4001_zp.run_diagnostic_test()
    # print()
    # opt4001_zm = opt4001_test.OPT4001_Test(BoardConfig.OPT4001_ZM_I2C_ADDR)
    # opt4001_zm.run_diagnostic_test()
    # print()

    # GPS
    # print("Running GPS Test")
    # gps = gps_test.GPS_Test()
    # gps.run_diagnostic_test()
    # print()


print("Running diagnostics...\n")
run_diagnostics()