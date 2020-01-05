# import self

__author__ = 'srikantm'

import sys

sys.path.append ( 'C:\clientapp_test\webapps\printme' )
from time import sleep
import printme_common
import printme_settings
import locators
# import Database
import unittest2
import os
from selenium import webdriver
import csv
import pytest
import allure
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

global filenames, docid


class UploadFiles (unittest2.TestCase):
    # noinspection PyStatementEffect

    def setUp(self):
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Ie()
        # self.driver=webdriver.Edge()
        # System.setProperty("webdriver.edge.driver",
        # "C:\clientapp_test\webapps\printme\geckodriver-v0.21.0-win64\MicrosoftWebDriver.exe")
        # WebDriver driver= new EdgeDriver()
        # driver.get("www.qa2.printme.com")
        #self.driver = webdriver.Chrome ( )
        self.driver.maximize_window()
        printme_common.LaunchWebsite(self.driver)  # self.db_Con = Database.Database(self.driver)
        #self.driver.close()

    def test_case001_Verify_GetStarted(self):
        ps = printme_settings.printme(self.driver)
        self.assertTrue(ps.getStarted.is_displayed(), "Get Started button is not available")

    @pytest.allure.testcase('test_case003')
    def test_case002_Upload_PDF_file(self):
        printme_common.LaunchWebsite(self.driver)
        ps = printme_settings.printme(self.driver)
        ps.getStarted.click()
        sleep(5)
        self.driver.find_element_by_xpath ( "//*[contains(@src,'assets/img/PM-efi-Logo2.svg')]" )
        # self.assertTrue(ps.upload_files_btn.is_displayed(), "Upload Files button is not available")
        # ps.upload_files_btn.click()
        path = os.getcwd ( )
        WaitForElement ( your_element_textbox )
        path += str ( "\\files" )
        # path += str("\\files\\png.png")
        print ( path )
        global filenames
        filenames = "pdf.pdf"
        printme_settings.file_upload ( self.driver, locators.upload_files, path, filenames )
        sleep ( 10 )
        ps.email_releasecode.send_keys ( "srikantm@efi.com" )
        sleep ( 10 )
        ps.send_btn.click ( )
        sleep ( 5)
        global docid
        docid = ps.doc_id.text
        print ( docid )
        # ps.printme_logo.click()
        sleep ( 5 )
        self.driver.close ( )

    @pytest.allure.testcase('test_case004')
    def test_case003_Upload_RTF_file(self):
        printme_common.LaunchWebsite ( self.driver )
        ps = printme_settings.printme ( self.driver )
        ps.getStarted.click ( )
        sleep ( 5 )
        self.driver.find_element_by_xpath ( "//*[contains(@src,'assets/img/PM-efi-Logo2.svg')]" )
        # self.assertTrue(ps.upload_files_btn.is_displayed(), "Upload Files button is not available")
        # ps.upload_files_btn.click()
        path = os.getcwd ( )
        path += str ( "\\files" )
        # path += str("\\files\\png.png")
        print ( path )
        global filenames
        filenames = "bbb - Copy.rtf"
        printme_settings.file_upload ( self.driver, locators.upload_files, path, filenames )
        sleep ( 10 )
        ps.email_releasecode.send_keys ( "srikantm@efi.com" )
        sleep ( 10 )
        ps.send_btn.click ( )
        sleep ( 5 )
        global docid
        docid = ps.doc_id.text
        print ( docid )
        # ps.printme_logo.click()
        sleep ( 5 )
        self.driver.close()

        #def tearDown(self):
            #self.driver.quit ( )

        obj = UploadFiles ( )
        obj.test_case001_Verify_Getstarted ( )
        obj.test_case003_Upload_PDF_file ()
        write_to_csv ()
        obj.test_case004_Upload_RTF_file ()
        write_to_csv ()

        if __name__ == 'main':
            print("Starting the execution")
            unittest2.main()
            print("starting execution")