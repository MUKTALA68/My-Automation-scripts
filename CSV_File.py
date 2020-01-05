 """
    #@pytest.allure.testcase('test_case003')
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
        sleep(10)
        ps.send_btn.click()
        sleep(5)
        global docid
        docid = ps.doc_id.text
        print(docid)
        # ps.printme_logo.click()
        sleep(5)
        self.driver.close()

    #@pytest.allure.testcase('test_case004')
    #def test_case004_Upload_RTF_file(self):
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

    #@pytest.allure.testcase('test_case005')
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

    #@pytest.allure.testcase('test_case006')
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

    #@pytest.allure.testcase('test_case007')
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

    #@pytest.allure.testcase('test_case008')
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

    #@pytest.allure.testcase('test_case009')
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

    #@pytest.allure.testcase('test_case010')
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
        #self.driver.close()

    #@pytest.allure.testcase('test_case011')
    def test_case011_Upload_JPEG_file(self):
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
        filenames = "second.jpeg"
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
        #self.driver.close()

    #@pytest.allure.testcase('test_case012')
    def test_case012_Upload_JPE_file(self):
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
        filenames = "flower - Copy.jpe"
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
        #self.driver.close()

    #@pytest.allure.testcase('test_case013')
    def test_case013_Upload_BMP_file(self):
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
        filenames = "RC Sport.bmp"
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
        #self.driver.close()

    #@pytest.allure.testcase('test_case014')
    def test_case014_Upload_gif_file(self):
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
        filenames = "Ipex_header.gif"
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

    #@pytest.allure.testcase('test_case015')
    def test_case015_Upload_PPTX_file(self):
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
        filenames = "testfile14.pptx"
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
        #self.driver.close()

    #@pytest.allure.testcase('test_case016')
    def test_case016_Upload_PUB_file(self):
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
        filenames = "testpublisher.pub"
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
        #self.driver.close()

    #@pytest.allure.testcase('test_case017')
    def test_case017_Upload_TIFF_file(self):
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
        filenames = "finger.TIF"
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
        #self.driver.close()

    #@pytest.allure.testcase('test_case018')
    def test_case018_Upload_ODP_file(self):
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
        filenames = "file2.ODP"
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
        #self.driver.close()

    #@pytest.allure.testcase('test_case019')
    def test_case019_Upload_ODT_file(self):
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
        filenames = "file2.odt"
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
        #self.driver.close()

    #@pytest.allure.testcase('test_case020')
    def test_case020_Upload_ODS_file(self):
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
        filenames = "file2.ods"
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
        #self.driver.close()

    #@pytest.allure.testcase('test_case021')
    def test_case021_Upload_PAGES_file(self):
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
        filenames = "example.pages"
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
        #self.driver.close()

    #@pytest.allure.testcase('test_case022')
    def test_case022_Upload_ALL_file(self):
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
        filenames = '"file2.ods"' '"file2.odt"' '"finger.TIF"' '"flower - Copy.jpe"' '"Heaven on earth.doc"'
        printme_settings.file_upload(self.driver, locators.upload_files, path, filenames)
        sleep(60)
        ps.email_releasecode.send_keys("srikantm@efi.com")
        sleep(30)
        ps.send_btn.click()
        sleep(20)
        global docid
        docid = ps.doc_id.text
        print(docid)
        # ps.printme_logo.click()
        sleep(10)
        self.driver.close()

    #@pytest.allure.testcase('test_case003C:\clientapp_test\webapps\printme\Scripts\files')

    def tearDown(self):
        self.driver.quit()
        
    '''obj.test_case003_Upload_PDF_file ()
        write_to_csv ()
        obj.test_case004_Upload_RTF_file ()
        write_to_csv ()
        obj.test_case005_Upload_HTML_file ()
        write_to_csv ()
        obj.test_case006_Upload_EXCEL_file ()
        write_to_csv ()
        obj.test_case007_Upload_DOC_file ()
        write_to_csv ()
        obj.test_case008_Upload_TEXT_file ()
        write_to_csv ()
        obj.test_case009_Upload_JPG_file ()
        write_to_csv ()
        obj.test_case010_Upload_JFIF_file ()
        write_to_csv ()


    if __name__ == 'main':
    print("Starting the execution")
    unittest2.main()
    print("starting execution")'''
"""