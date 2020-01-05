S# import self

__author__ = 'srikantm'

import sys

sys.path.append('C:\clientapp_test\webapps\printme')
from time import sleep
import printme_common
import printme_settings
import locators
# import Database
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


class UploadFiles(unittest2.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        # self.driver = webdriver.chrome()
        self.driver.maximize_window()
        printme_common.LaunchWebsite(self.driver)  # self.db_Con = Database.Database(self.driver)

    def test_case001_Verify_GetStarted(self):
        ps = printme_settings.printme(self.driver)
        self.assertTrue(ps.getStarted.is_displayed(), "Get Started button is not available")

    @pytest.allure.testcase('test_case002')
    def test_case002_Upload_PNG_file(self):
        ps = printme_settings.printme(self.driver)
        ps.getStarted.click()
        sleep(5)
        self.driver.find_element_by_xpath("//*[contains(@src,'assets/img/PM-efi-Logo2.svg')]")
        # self.assertTrue(ps.upload_files_btn.is_displayed(), "Upload Files button is not available")
        # ps.upload_files_btn.click()
        path = os.getcwd()
        path += str("\\files")
        # path += str("\\files\\png.png")
        print(path)
        global filenames
        filenames = "png.png"
        printme_settings.file_upload(self.driver, locators.upload_files, path, filenames)
        sleep(10)
        ps.email_releasecode.send_keys("srikantm@efi.com")
        sleep(5)
        ps.send_btn.click()
        sleep(5)
        global docid
        sleep(5)
        docid = ps.doc_id.text
        print(docid)
        # ps.printme_logo.click()
        sleep(5)
        # self.driver.close()

    @pytest.allure.testcase('test_case003')
    def test_case003_Upload_PDF_file(self):
        printme_common.LaunchWebsite(self.driver)
        ps = printme_settings.printme(self.driver)
        ps.getStarted.click()
        sleep(5)
        self.driver.find_element_by_xpath("//*[contains(@src,'assets/img/PM-efi-Logo2.svg')]")
        # self.assertTrue(ps.upload_files_btn.is_displayed(), "Upload Files button is not available")
        # ps.upload_files_btn.click()
        path = os.getcwd()
        path += str("\\files")
        # path += str("\\files\\png.png")
        print(path)
        global filenames
        filenames = "pdf.pdf"
        printme_settings.file_upload(self.driver, locators.upload_files, path, filenames)
        sleep(10)
        ps.email_releasecode.send_keys("srikantm@efi.com")
        sleep(5)
        ps.send_btn.click()
        sleep(5)
        global docid
        docid = ps.doc_id.text
        print(docid)
        # ps.printme_logo.click()
        sleep(5)

        # self.driver.close()

        @pytest.allure.testcase('test_case004')
        def write_to_csv():
            global filenames, docid
            print("filename", filenames)
            print("docid", docid)
            try:
                if not os.path.isfile("C:\\clientapp_test\\webapps\\printme\\Scripts\\website.csv"):
                    with open('C:\\clientapp_test\\webapps\\printme\\Scripts\\website.csv', 'w+') as f:
                        a = csv.writer(f)
                        a.writerow(["Filename", "DocID"])
                        a.writerow([filenames, docid])
                else:
                    with open('C:\\clientapp_test\\webapps\\printme\\Scripts\\website.csv', 'a') as f:
                        a = csv.writer(f)
                        a.writerow([filenames, docid])
            except:
                print("Got exception while writing csv file")
                exit(-1)

        if __name__ == "__main__":
            obj = UploadFiles()
            obj.test_case001_Verify_Getstarted()
            obj.test_case002_Upload_PNG_file()
            write_to_csv()
            obj.test_case003_Upload_PDF_file()
            write_to_csv()

        if __name__ == 'main':
            print("Starting the execution")
            unittest2.main()
            print("starting execution")

        def tearDown(self):
            self.driver.quit()
