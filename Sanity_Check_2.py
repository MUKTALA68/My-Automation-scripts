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
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

global filenames, docid

class UploadFiles:
    def __init__(self):
        self.driver = webdriver.Firefox()
        #self.driver = webdriver.chrome()
        self.driver.maximize_window()
        printme_common.LaunchWebsite(self.driver)  # self.db_Con = Database.Database(self.driver)

    def test_case001_Verify_Getstarted(self):
        ps = printme_settings.printme(self.driver)  # self.assertTrue(ps.getStarted.is_displayed(), "Get Started button is not available")

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
        #self.driver.close()

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
        ps.send_HTMLtables.html
        btn.click()
        sleep(5)
        global docid
        docid = ps.doc_id.text
        print(docid)
        # ps.printme_logo.click()
        sleep(5)
        #self.driver.close()

    def test_case004_Upload_RTF_file(self):
        printme_common.LaunchWebsite(self.driver)
        ps = printme_settings.printme(self.driver)
        ps.getStarted.click()
        sleep(5)
        self.driver.find_element_by_xpath("//*[contains(@src,'assets/img/PM-efi-Logo2.svg')]")
        #self.assertTrue(ps.upload_files_btn.is_displayed(), "Upload Files button is not available")
        # ps.upload_files_btn.click()
        path = os.getcwd()
        path += str("\\files")
        # path += str("\\files\\png.png")
        print(path)
        global filenames
        filenames = "bbb - Copy.rtf"
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
        #self.driver.close()

    def test_case005_Upload_HTML_file(self):
        printme_common.LaunchWebsite(self.driver)
        ps = printme_settings.printme(self.driver)
        ps.getStarted.click()
        sleep(5)
        self.driver.find_element_by_xpath("//*[contains(@src,'assets/img/PM-efi-Logo2.svg')]")
        #self.assertTrue(ps.upload_files_btn.is_displayed(), "Upload Files button is not available")
        # ps.upload_files_btn.click()
        path = os.getcwd()
        path += str("\\files")
        # path += str("\\files\\png.png")
        print(path)
        global filenames
        filenames = "HTMLtables.html"
        printme_settings.file_upload(self.driver, locators.upload_files, path, filenames)
        sleep(20)
        ps.email_releasecode.send_keys("srikantm@efi.com")
        sleep(15)
        ps.send_btn.click()
        sleep(10)
        global docid
        docid = ps.doc_id.text
        print(docid)
        # ps.printme_logo.click()
        sleep(5)
        #self.driver.close()

    def test_case006_Upload_EXCEL_file(self):
        printme_common.LaunchWebsite(self.driver)
        ps = printme_settings.printme(self.driver)
        ps.getStarted.click()
        sleep(5)
        self.driver.find_element_by_xpath("//*[contains(@src,'assets/img/PM-efi-Logo2.svg')]")
        #self.assertTrue(ps.upload_files_btn.is_displayed(), "Upload Files button is not available")
        # ps.upload_files_btn.click()
        path = os.getcwd()
        path += str("\\files")
        # path += str("\\files\\png.png")
        print(path)
        global filenames
        filenames = "EML File Test cases - Doc 2.xlsx"
        printme_settings.file_upload(self.driver, locators.upload_files, path, filenames)
        sleep(20)
        ps.email_releasecode.send_keys("srikantm@efi.com")
        sleep(15)
        ps.send_btn.click()
        sleep(10)
        global docid
        docid = ps.doc_id.text
        print(docid)
        # ps.printme_logo.click()
        sleep(5)
        #self.driver.close()

    def test_case007_Upload_DOC_file(self):
        printme_common.LaunchWebsite(self.driver)
        ps = printme_settings.printme(self.driver)
        ps.getStarted.click()
        sleep(5)
        self.driver.find_element_by_xpath("//*[contains(@src,'assets/img/PM-efi-Logo2.svg')]")
        #self.assertTrue(ps.upload_files_btn.is_displayed(), "Upload Files button is not available")
        # ps.upload_files_btn.click()
        path = os.getcwd()
        path += str("\\files")
        # path += str("\\files\\png.png")
        print(path)
        global filenames
        filenames = "Heaven on earth.doc"
        printme_settings.file_upload(self.driver, locators.upload_files, path, filenames)
        sleep(20)
        ps.email_releasecode.send_keys("srikantm@efi.com")
        sleep(15)
        ps.send_btn.click()
        sleep(10)
        global docid
        docid = ps.doc_id.text
        print(docid)
        # ps.printme_logo.click()
        sleep(5)
        #self.driver.close()

    def test_case008_Upload_TEXT_file(self):
        printme_common.LaunchWebsite(self.driver)
        ps = printme_settings.printme(self.driver)
        ps.getStarted.click()
        sleep(5)
        self.driver.find_element_by_xpath("//*[contains(@src,'assets/img/PM-efi-Logo2.svg')]")
        #self.assertTrue(ps.upload_files_btn.is_displayed(), "Upload Files button is not available")
        # ps.upload_files_btn.click()
        path = os.getcwd()
        path += str("\\files")
        # path += str("\\files\\png.png")
        print(path)
        global filenames
        filenames = "officeworks_Failure_1.txt"
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
        #self.driver.close()

    def test_case009_Upload_JPG_file(self):
        printme_common.LaunchWebsite(self.driver)
        ps = printme_settings.printme(self.driver)
        ps.getStarted.click()
        sleep(5)
        self.driver.find_element_by_xpath("//*[contains(@src,'assets/img/PM-efi-Logo2.svg')]")
        #self.assertTrue(ps.upload_files_btn.is_displayed(), "Upload Files button is not available")
        # ps.upload_files_btn.click()
        path = os.getcwd()
        path += str("\\files")
        # path += str("\\files\\png.png")
        print(path)
        global filenames
        filenames = "download.jpg"
        printme_settings.file_upload(self.driver, locators.upload_files, path, filenames)
        sleep(20)
        ps.email_releasecode.send_keys("srikantm@efi.com")
        sleep(10)
        ps.send_btn.click()
        sleep(8)
        global docid
        docid = ps.doc_id.text
        print(docid)
        # ps.printme_logo.click()
        sleep(5)
        #self.driver.close()

    def test_case010_Upload_JFIF_file(self):
        printme_common.LaunchWebsite(self.driver)
        ps = printme_settings.printme(self.driver)
        ps.getStarted.click()
        sleep(5)
        self.driver.find_element_by_xpath("//*[contains(@src,'assets/img/PM-efi-Logo2.svg')]")
        #self.assertTrue(ps.upload_files_btn.is_displayed(), "Upload Files button is not available")
        # ps.upload_files_btn.click()
        path = os.getcwd()
        path += str("\\files")
        # path += str("\\files\\png.png")
        print(path)
        global filenames
        filenames = "Testttt.JFIF"
        printme_settings.file_upload(self.driver, locators.upload_files, path, filenames)
        sleep(15)
        ps.email_releasecode.send_keys("srikantm@efi.com")
        sleep(10)
        ps.send_btn.click()
        sleep(5)
        global docid
        docid = ps.doc_id.text
        print(docid)
        # ps.printme_logo.click()
        sleep(5)
        self.driver.close()

    def test_case011_Upload_JPEG_file(self):
        printme_common.LaunchWebsite(self.driver)
        ps = printme_settings.printme(self.driver)
        ps.getStarted.click()
        self.assertTrue(ps.upload_files_btn.is_displayed(), "Upload Files button is not available")
        # ps.upload_files_btn.click()
        path = os.getcwd()
        path += str("\\files")
        # path += str("\\files\\png.png")
        print(path)
        filenames = "second.jpeg"
        printme_settings.file_upload(self.driver, locators.upload_files, path, filenames)
        sleep(15)
        ps.email_releasecode.send_keys("srikantm@efi.com")
        sleep(10)
        ps.send_btn.click()
        sleep(5)
        docid = ps.doc_id.text
        print(docid)
        # ps.printme_logo.click()
        sleep(5)
        self.driver.close()

    def test_case012_Upload_JPE_file(self):
        printme_common.LaunchWebsite(self.driver)
        ps = printme_settings.printme(self.driver)
        ps.getStarted.click()
        self.assertTrue(ps.upload_files_btn.is_displayed(), "Upload Files button is not available")
        # ps.upload_files_btn.click()
        path = os.getcwd()
        path += str("\\files")
        # path += str("\\files\\png.png")
        print(path)
        filenames = "flower - Copy.jpe"
        printme_settings.file_upload(self.driver, locators.upload_files, path, filenames)
        sleep(15)
        ps.email_releasecode.send_keys("srikantm@efi.com")
        sleep(10)
        ps.send_btn.click()
        sleep(5)
        docid = ps.doc_id.text
        print(docid)
        # ps.printme_logo.click()
        sleep(5)
        self.driver.close()

    def test_case013_Upload_BMP_file(self):
        printme_common.LaunchWebsite(self.driver)
        ps = printme_settings.printme(self.driver)
        ps.getStarted.click()
        self.assertTrue(ps.upload_files_btn.is_displayed(), "Upload Files button is not available")
        # ps.upload_files_btn.click()
        path = os.getcwd()
        path += str("\\files")
        # path += str("\\files\\png.png")
        print(path)
        filenames = "RC Sport.bmp"
        printme_settings.file_upload(self.driver, locators.upload_files, path, filenames)
        sleep(15)
        ps.email_releasecode.send_keys("srikantm@efi.com")
        sleep(10)
        ps.send_btn.click()
        sleep(5)
        docid = ps.doc_id.text
        print(docid)
        # ps.printme_logo.click()
        sleep(5)
        self.driver.close()

    def test_case014_Upload_gif_file(self):
        printme_common.LaunchWebsite(self.driver)
        ps = printme_settings.printme(self.driver)
        ps.getStarted.click()
        self.assertTrue(ps.upload_files_btn.is_displayed(), "Upload Files button is not available")
        # ps.upload_files_btn.click()
        path = os.getcwd()
        path += str("\\files")
        # path += str("\\files\\png.png")
        print(path)
        filenames = "Ipex_header.gif"
        printme_settings.file_upload(self.driver, locators.upload_files, path, filenames)
        sleep(20)
        ps.email_releasecode.send_keys("srikantm@efi.com")
        sleep(15)
        ps.send_btn.click()
        sleep(10)
        docid = ps.doc_id.text
        print(docid)
        # ps.printme_logo.click()
        sleep(5)
        self.driver.close()

    def test_case015_Upload_PPTX_file(self):
        printme_common.LaunchWebsite(self.driver)
        ps = printme_settings.printme(self.driver)
        ps.getStarted.click()
        self.assertTrue(ps.upload_files_btn.is_displayed(), "Upload Files button is not available")
        # ps.upload_files_btn.click()
        path = os.getcwd()
        path += str("\\files")
        # path += str("\\files\\png.png")
        print(path)
        filenames = "testfile14.pptx"
        printme_settings.file_upload(self.driver, locators.upload_files, path, filenames)
        sleep(15)
        ps.email_releasecode.send_keys("srikantm@efi.com")
        sleep(10)
        ps.send_btn.click()
        sleep(5)
        docid = ps.doc_id.text
        print(docid)
        # ps.printme_logo.click()
        sleep(5)
        self.driver.close()

    def test_case016_Upload_PUB_file(self):
        printme_common.LaunchWebsite(self.driver)
        ps = printme_settings.printme(self.driver)
        ps.getStarted.click()
        self.assertTrue(ps.upload_files_btn.is_displayed(), "Upload Files button is not available")
        # ps.upload_files_btn.click()
        path = os.getcwd()
        path += str("\\files")
        # path += str("\\files\\png.png")
        print(path)
        filenames = "testpublisher.pub"
        printme_settings.file_upload(self.driver, locators.upload_files, path, filenames)
        sleep(15)
        ps.email_releasecode.send_keys("srikantm@efi.com")
        sleep(10)
        ps.send_btn.click()
        sleep(5)
        docid = ps.doc_id.text
        print(docid)
        # ps.printme_logo.click()
        sleep(5)
        self.driver.close()

    def test_case017_Upload_TIFF_file(self):
        printme_common.LaunchWebsite(self.driver)
        ps = printme_settings.printme(self.driver)
        ps.getStarted.click()
        self.assertTrue(ps.upload_files_btn.is_displayed(), "Upload Files button is not available")
        # ps.upload_files_btn.click()
        path = os.getcwd()
        path += str("\\files")
        # path += str("\\files\\png.png")
        print(path)
        filenames = "finger.TIF"
        printme_settings.file_upload(self.driver, locators.upload_files, path, filenames)
        sleep(15)
        ps.email_releasecode.send_keys("srikantm@efi.com")
        sleep(10)
        ps.send_btn.click()
        sleep(5)
        docid = ps.doc_id.text
        print(docid)
        # ps.printme_logo.click()
        sleep(5)
        self.driver.close()

    def test_case018_Upload_ODP_file(self):
        printme_common.LaunchWebsite(self.driver)
        ps = printme_settings.printme(self.driver)
        ps.getStarted.click()
        self.assertTrue(ps.upload_files_btn.is_displayed(), "Upload Files button is not available")
        # ps.upload_files_btn.click()
        path = os.getcwd()
        path += str("\\files")
        # path += str("\\files\\png.png")
        print(path)
        filenames = "file2.ODP"
        printme_settings.file_upload(self.driver, locators.upload_files, path, filenames)
        sleep(15)
        ps.email_releasecode.send_keys("srikantm@efi.com")
        sleep(10)
        ps.send_btn.click()
        sleep(5)
        docid = ps.doc_id.text
        print(docid)
        # ps.printme_logo.click()
        sleep(5)
        self.driver.close()

    def test_case019_Upload_ODT_file(self):
        printme_common.LaunchWebsite(self.driver)
        ps = printme_settings.printme(self.driver)
        ps.getStarted.click()
        self.assertTrue(ps.upload_files_btn.is_displayed(), "Upload Files button is not available")
        # ps.upload_files_btn.click()
        path = os.getcwd()
        path += str("\\files")
        # path += str("\\files\\png.png")
        print(path)
        filenames = "file2.odt"
        printme_settings.file_upload(self.driver, locators.upload_files, path, filenames)
        sleep(15)
        ps.email_releasecode.send_keys("srikantm@efi.com")
        sleep(10)
        ps.send_btn.click()
        sleep(5)
        docid = ps.doc_id.text
        print(docid)
        # ps.printme_logo.click()
        sleep(5)
        self.driver.close()

    def test_case020_Upload_ODS_file(self):
        printme_common.LaunchWebsite(self.driver)
        ps = printme_settings.printme(self.driver)
        ps.getStarted.click()
        self.assertTrue(ps.upload_files_btn.is_displayed(), "Upload Files button is not available")
        # ps.upload_files_btn.click()
        path = os.getcwd()
        path += str("\\files")
        # path += str("\\files\\png.png")
        print(path)
        filenames = "file2.ods"
        printme_settings.file_upload(self.driver, locators.upload_files, path, filenames)
        sleep(15)
        ps.email_releasecode.send_keys("srikantm@efi.com")
        sleep(10)
        ps.send_btn.click()
        sleep(5)
        docid = ps.doc_id.text
        print(docid)
        # ps.printme_logo.click()
        sleep(5)
        self.driver.close()

    def test_case021_Upload_PAGES_file(self):
        printme_common.LaunchWebsite(self.driver)
        ps = printme_settings.printme(self.driver)
        ps.getStarted.click()
        self.assertTrue(ps.upload_files_btn.is_displayed(), "Upload Files button is not available")
        # ps.upload_files_btn.click()
        path = os.getcwd()
        path += str("\\files")
        # path += str("\\files\\png.png")
        print(path)
        filenames = "example.pages"
        printme_settings.file_upload(self.driver, locators.upload_files, path, filenames)
        sleep(15)
        ps.email_releasecode.send_keys("srikantm@efi.com")
        sleep(10)
        ps.send_btn.click()
        sleep(5)
        docid = ps.doc_id.text
        print(docid)
        # ps.printme_logo.click()
        sleep(5)
        self.driver.close()

    def test_case022_Upload_ALL_file(self):
        printme_common.LaunchWebsite(self.driver)
        ps = printme_settings.printme(self.driver)
        ps.getStarted.click()
        self.assertTrue(ps.upload_files_btn.is_displayed(), "Upload Files button is not available")
        # ps.upload_files_btn.click()
        path = os.getcwd()
        path += str("\\files")
        # path += str("\\files\\png.png")
        print(path)
        filenames = "file2.ods" "file2.odt" "finger.TIF" "flower - Copy.jpe" "Heaven on earth.doc"
        printme_settings.file_upload(self.driver, locators.upload_files, path, filenames)
        sleep(60)
        ps.email_releasecode.send_keys("srikantm@efi.com")
        sleep(30)
        ps.send_btn.click()
        sleep(20)
        docid = ps.doc_id.text
        print(docid)
        # ps.printme_logo.click()
        sleep(10)
        self.driver.close()

    def tearDown(self):
        self.driver.quit()


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
    obj.test_case004_Upload_RTF_file()
    write_to_csv()
    obj.test_case005_Upload_HTML_file()
    write_to_csv()
    obj.test_case006_Upload_EXCEL_file()
    write_to_csv()
    obj.test_case007_Upload_DOC_file()
    write_to_csv()
    obj.test_case008_Upload_TEXT_file()
    write_to_csv()
    obj.test_case009_Upload_JPG_file()
    write_to_csv()
    obj.test_case010_Upload_JFIF_file()
    write_to_csv()



  


