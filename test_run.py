__author__ = 'kirshnk'

import unittest2
import HTMLTestRunner
from UploadFiles import UploadFiles
'''
from Add_device import D_profile
from Add_device import D_profile_Staples
from Location import Location
from Location import Location_Staples
from Trans import Trans
from Trans import Trans_X500
from Taxes import Taxes
from Taxes import Taxes_Staples
from Device_Settings_G5 import Logos as G5logos
from Device_Settings_G5 import Home_screen as G5home
from Device_Settings_G5 import Screen_Saver as G5SS
from Device_Settings_G5 import Home_screen_Staples as SG5home
from Device_Settings_G5 import Logos_Staples as SG5Logos
from Device_Settings_G5 import Screen_Saver_Staples as SG5SS
from Device_Settings_M500 import Logos as M5logos
from Device_Settings_M500 import Home_screen as M5home
from Device_Settings_M500 import Screen_Saver as M5SS
from Device_Settings_M500 import Settings as M5settings
from Device_Settings_M500 import Home_screen_Staples as SM5home
from Device_Settings_M500 import Logos_Staples as SM5Logos
from Device_Settings_M500 import Screen_Saver_Staples as SM5SS
from Device_Settings_CS import EmailReceipts as ER
from payment_types import P_Type
from payment_types import P_Types_Staples
from Pricelist import Priclist
from Receipts import Receipts
from Taxrate import Taxrate
from Taxrate import Taxrate_Staples
from LiabilityAgreement import Liability
from LiabilityAgreement import Liability_Staples
from Products import Product
from StaffAccount import StaffAccount
from StaffAccount import StaffAccount_Staples
from Error_test import Error_Payment
from Error_test import Error_Product1
from Error_test import Error_Product2
from Error_test import Error_Price
from Error_test import Error_Config
from Dash import Web_socket
from Dash import Dash_Kiosk
from Dash import Dash_M500
from Dash import Dash_Kiosk_Staples
from Dash import Dash_M500_Staples
from User_Roles_Scripts_admin import User_Roles_Admin
from User_Roles_Scripts_staff import User_Roles_Staff
from DTC_Format import Format_M500
from DTC_Format import Format_Kiosk
from Regions import Region
from Reports import Reports
from Timings import timecount
#from Timings_Incognito_Mode import timecount as incognito_timecount
#from Timings_Dashboard import timecount as dash_time
from Timings1_Config_Nickname import timecount as T1
from Timings2_Regions import timecount as T2
from Timings3_Device_setting_idle_timeout import timecount as T3
from Timings4_Payment import timecount as T4
from Timings5_Tax import timecount as T5
from Timings6_Liability_Agreement import timecount as T6
from Timings7_Location_TaxRate import timecount as T7
from Timings8_local_area_code_edit import timecount as T8
from Timings9_Location_device_edit_add import timecount as T9
from Timings10_Config_Staff_Account import timecount as T10
from Timings11_Screensaver_del_add import timecount as T11
from Timings12_Reports_6_months import timecount as T12
from Timings_13_Reports_3_months import timecount as T13
from Timings_14_Reports_1_month import timecount as T14
from Timings_15_Reports_1_week import timecount as T15
from Land_on_Dashboard_Login import timecount as T16
from Timings_Price_List import timecount as T17
from Fax_Area_Code import Faxareacode
#from Device_Email_receipt_std import Device_Email_receipt_std
from Heartland_payment import Heartland_payment
from ImportCSVAccountAccess import AccountAccess
from SupportFiles import SupportFiles

from Device_Email_receipt_std import Device_Email_receipt
from Office365 import Office
from Device_Settings_CR import Device_Settings_CR_settings

from Surcharge import Surcharge
from ConfigurableAccount import ConfigurableAccount
from FreedomPay_payment import FreedomPay
#from Products import Product_UK as productsUK
'''
import time


def Get_cloud():
    import sys
    sys.path.append("C:\clientapp_test\webapps\printme")
    import printme_common as Com
    from selenium import webdriver
    #d = webdriver.Chrome("chromedriver.exe")
    d = webdriver.Firefox()
    Com.LaunchWebsite(d)
    cloud = Com.Cloud(d)
    d.close()
    return cloud


def test_run():

    suite1 = unittest2.TestLoader().loadTestsFromTestCase(UploadFiles)


    #suite = unittest2.TestSuite([suite2,suite3,suite4,suite5,suite6,suite7,suite8,suite9,suite10,suite11,suite12,suite13,suite14,suite15,suite16,suite17,suite18,suite19,suite20,suite21,suite22,suite23,suite24,suite25,suite26,suite27,suite28,suite29,suite30,suite31,suite32, suite33, suite34, suite35, suite36, suite37, suite38, suite39, suite40, suite41, suite42, suite43, suite44, suite45, suite46, suite47, suite48, suite49, suite32, suite33, suite34, suite35, suite36, suite37, suite38, suite39, suite40, suite41, suite42, suite43, suite44, suite45, suite46, suite47, suite48, suite49])
    #The below suite is used for qa-selfserve
    #suite = unittest2.TestSuite([suite8,suite1,suite2,suite3,suite4,suite5,suite6,suite7,suite9,suite10,suite11,suite12,suite13,suite14,suite15,suite16,suite17,suite18,suite19,suite20,suite21,suite22,suite23,suite24,suite25,suite26,suite27,suite28,suite72,suite73,suite74])
    #suite = unittest2.TestSuite([suite1,suite2,suite3,suite4,suite5,suite7,suite8,suite9,suite10,suite11,suite12,suite13,suite14,suite15,suite16,suite17,suite18,suite19,suite20,suite21,suite22,suite23,suite24,suite25,suite26,suite27,suite28,suite29])
    #suite = unittest2.TestSuite([suite1,suiteC:\clientapp_test\webapps\expresspay\Scripts\files
    # 2,suite3,suite4,suite5,suite7,suite8,suite9,suite10,suite14,suite15,suite16,suite17,suite18,suite19,suite20,suite21,suite22,suite23,suite24,suite25,suite26,suite27,suite28])
    #suite = unittest2.TestSuite([suite1,suite2,suite3,suite4,suite5,suite7,suite8,suite9,suite10,suite11,suite12,suite13,suite14,suite15,suite16,suite17,suite18,suite19,suite20,suite21,suite22,suite23,suite24,suite25,suite26])
    #suite = unittest2.TestSuite([suite43,suite42,suite40,suite41,suite23,suite24,suite34,suite35,suite36,suite39,suite32,suite33,suite37,suite38,suite44,suite45,suite46,suite47,suite71])
    #suite = unittest2.TestSuite([suite54,suite55,suite56,suite57,suite58,suite59,suite60,suite61,suite62,suite63, suite64])
    #suite = unittest2.TestSuite([suite58,suite57,suite56,suite54,suite55,suite59,suite60,suite61,suite62,suite63, suite64, suite69, suite70])
    #suite = unittest2.TestSuite([suite1,suite10, suite23])
    #suite = unittest2.TestSuite([suite11])
    #suite = unittest2.TestSuite([suite76, suite77, suite78])
    #suite = unittest2.TestSuite([suite32, suite33, suite34,suite35, suite36, suite37, suite38, suite39, suite40, suite41, suite42, suite43, suite44, suite45, suite46, suite47, suite48, suite50, suite72, suite75,suite77, suite78])
    #The below suite is used for qa-staples-selfserve
    suite = unittest2.TestSuite([suite1])
    #suite = unittest2.TestSuite([suite101,suite102,suite103])
    outfile = open(str(int(time.time()))+"-report.html", "w",encoding='utf-8',errors='replace')
    runner = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='PRINTME AUTOMATION REPORT',
                description='Result of tests',
                cloud = Get_cloud()
                )
    runner.run(suite)

test_run()

#C:\clientapp_test\webapps\expresspay\Scripts\files
