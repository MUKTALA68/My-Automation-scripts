#import self

__author__ = 'srikantm'

import sys

sys.path.append('C:\clientapp_test\webapps\printme')
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
#import nose.tools
#import org.openqa.selenium.edge.EdgeDriver
#import openqa.Selenium.Edge
#import system
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

global filenames, docid

class UploadFiles(unittest2.TestCase):
    # noinspection PyStatementEffect

    #def test_fn(self):
        #for i in range(1,2):
            #yield nose.tools.assert_equals, output[i], fn[i]

    def fileList(self):
        path = os.getcwd()
        path += str("\\files")
        list = os.listdir(path)
        return list, path

    def setUp(self):
        #self.driver = webdriver.Firefox()
        #self.driver=webdriver.Ie()
        #self.driver=webdriver.Edge()
        #System.setProperty("webdriver.edge.driver",
        #"C:\clientapp_test\webapps\printme\geckodriver-v0.21.0-win64\MicrosoftWebDriver.exe")
        #WebDriver driver= new EdgeDriver()
        #driver.get("www.qa2.printme.com")
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        #printme_common.LaunchWebsite(self.driver)  # self.db_Con = Database.Database(self.driver)
        #self.driver.close()

    #def test_output(self):
        #ps = printme_settings.printme ( self.driver )
        #abc, path = self.fileList()
        #for j in range(1, 3):
            #self.test_Upload_files(j,ps)
        #self.driver.close()

    #def test_case001_Verify_GetStarted(self):
        #ps = printme_settings.printme(self.driver)
        #self.assertTrue(ps.getStarted.is_displayed(), "Get Started button is not available")

    @pytest.allure.testcase('test_case003')
    def test_output(self, ps, i):
        ps.getStarted.click()
        self.driver.find_element_by_xpath("//*[contains(@src,'assets/img/PM-efi-Logo2.svg')]")
        #self.assertTrue(ps.upload_files_btn.is_displayed(), "Upload Files button is not available")
        #ps.upload_files_btn.click()
        abc, path = self.fileList()
        for i in range(1, 20):
            print(i)
        printme_settings.file_upload(self.driver, locators.upload_files, path, abc[i])
        sleep(10)
        ps.email_releasecode.send_keys("srikantm@efi.com")
        sleep(15)
        ps.send_btn.click()
        sleep(10)
        global docid
        sleep(8)
        docid = ps.doc_id.text
        print(abc[i])
        print(docid)
        self.write_to_csv(filenames=abc[i], docid=docid)
        ps.printme_logo.click()
        ps.getStarted.click()
        sleep(8)

    @staticmethod
    def write_to_csv(filenames, docid):
        print("filename", filenames)
        print("docid", docid)
        try:
            # if not os.path.isfile("C:\\clientapp_test\\webapps\\printme\\Scripts\\website.csv"):
            #     with open('C:\\clientapp_test\\webapps\\printme\\Scripts\\website.csv', 'w+', newline='') as f:
            #         a = csv.writer(f)
            #         a.writerow(["Filename", "DocID"])
            #         #a.writerow([filenames, docid])
            # else:
            with open('C:\\clientapp_test\\webapps\\printme\\Scripts\\website.csv', 'a+', newline='') as f:
                a = csv.writer(f)
                a.writerow([filenames, docid])
        except:
            print("Got exception while writing csv file")
            exit(-1)

    if __name__ == "__main__":
        obj = UploadFiles()
        obj.test_output()
        write_to_csv()



