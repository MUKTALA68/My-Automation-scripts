# import self

__author__='srikantm'

import sys

sys.path.append('C:\clientapp_test\webapps\printme')
from time import sleep
import printme_common
import printme_settings
import locators
import unittest2
import allure
import pytest
import os
from selenium import webdriver
import csv
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

global filenames, docid

class UploadFiles (unittest2.TestCase):
#class Static_Pages:
    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        #self.driver = webdriver.Opera()
        self.driver.maximize_window()
        printme_common.LaunchWebsite(self.driver)

    @pytest.allure.testcase('test_case0057')
    def test_case057_Map_Search_City(self):
        ps=printme_settings.printme(self.driver)
        ps.explore_drpdwn.click()
        sleep(5)
        self.driver.find_element_by_xpath("//*[contains(@src,'assets/img/PM-efi-Logo2.svg')]")
        self.assertTrue(ps.Locate_a_printer.is_displayed(), "Locate a printer is not available")
        ps.Locate_a_printer.click()
        sleep(5)
        self.assertTrue(ps.Map_Search.is_displayed(), "Map search is not available")
        sleep(5)
        ps.Map_Search.send_keys("Bangalore")
        sleep(5)
        ps.Map_button.click()
        sleep(8)

    @pytest.allure.testcase('test_case0058')
    def test_case058_Map_Search_State(self):
        ps=printme_settings.printme(self.driver)
        ps.explore_drpdwn.click()
        sleep(5)
        self.driver.find_element_by_xpath("//*[contains(@src,'assets/img/PM-efi-Logo2.svg')]")
        self.assertTrue(ps.Locate_a_printer.is_displayed(), "Locate a printer is not available")
        ps.Locate_a_printer.click()
        sleep(5)
        self.assertTrue(ps.Map_Search.is_displayed(), "Map search is not available")
        sleep(5)
        ps.Map_Search.send_keys("Karnataka, India")
        sleep(5)
        ps.Map_button.click()
        sleep(8)

    @pytest.allure.testcase('test_case0059')
    def test_case059_Map_Search_Zip_code(self):
        ps=printme_settings.printme(self.driver)
        ps.explore_drpdwn.click()
        sleep(5)
        self.driver.find_element_by_xpath("//*[contains(@src,'assets/img/PM-efi-Logo2.svg')]")
        self.assertTrue(ps.Locate_a_printer.is_displayed(), "Locate a printer is not available")
        ps.Locate_a_printer.click()
        sleep(5)
        self.assertTrue(ps.Map_Search.is_displayed(), "Map search is not available")
        sleep(5)
        ps.Map_Search.send_keys("560066")
        sleep(5)
        ps.Map_button.click()
        sleep(8)

    def tearDown(self):
        self.driver.quit()

