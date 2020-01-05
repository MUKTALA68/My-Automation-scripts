import locators
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException,StaleElementReferenceException
from selenium.webdriver.common.by import By
import time
import pyrobot
import csv
from selenium.common.exceptions import WebDriverException


class printme:
    def __init__(self, driver):
        try:
            self.driver = driver
            self.get_started = self.driver.find_element_by_class_name ( locators.get_started )
        except:
            pass

    @property
    def getStarted(self):
        return self.driver.find_element_by_class_name ( locators.get_started )

    @property
    def upload_files_btn(self):
        return self.driver.find_element_by_id ( locators.upload_files )

    @property
    def email_releasecode(self):
        return self.driver.find_element_by_xpath ( locators.email_releasecode )

    @property
    def send_btn(self):
        return self.driver.find_element_by_class_name ( locators.send_btn )

    @property
    def doc_id(self):
        return self.driver.find_element_by_xpath ( locators.docid )

    @property
    def printme_logo(self):
        return self.driver.find_element_by_xpath ( locators.printme_logo )

    @property
    def explore_drpdwn(self):
        return self.driver.find_element_by_xpath ( locators.explore_drpdwn )

    @property
    def Apps_and_drivers(self):
        return self.driver.find_element_by_xpath ( locators.Apps_and_drivers )

    @property
    def PrintMe_for_business(self):
        return self.driver.find_element_by_xpath ( locators.PrintMe_for_business )

    @property
    def Locate_a_printer(self):
        return self.driver.find_element_by_xpath ( locators.Locate_a_printer )

    @property
    def support_drpdwn(self):
        return self.driver.find_element_by_xpath ( locators.support_drpdwn )

    @property
    def FAQs(self):
        return self.driver.find_element_by_xpath ( locators.FAQs )

    @property
    def Service_status(self):
        return self.driver.find_element_by_xpath ( locators.Service_status )

    @property
    def Support_center(self):
        return self.driver.find_element_by_xpath ( locators.Support_center )

    @property
    def Global_drpdwn(self):
        return self.driver.find_element_by_xpath ( locators.Global_drpdwn )

    @property
    def English(self):
        return self.driver.find_element_by_xpath ( locators.English )

    @property
    def English_International(self):
        return self.driver.find_element_by_xpath ( locators.English_International )

    @property
    def Francis(self):
        return self.driver.find_element_by_xpath ( locators.Francis )

    @property
    def Italiano(self):
        return self.driver.find_element_by_xpath ( locators.Italiano )

    @property
    def Deutsch(self):
        return self.driver.find_element_by_xpath ( locators.Deutsch )

    @property
    def Espanol(self):
        return self.driver.find_element_by_xpath ( locators.Espanol )

    @property
    def Nederlands(self):
        return self.driver.find_element_by_xpath ( locators.Nederlands )

    @property
    def Portuguese_brasil(self):
        return self.driver.find_element_by_xpath ( locators.Portuguese_brasil )

    @property
    def Learn_more(self):
        return self.driver.find_element_by_xpath ( locators.Learn_more )

    @property
    def Download_apps_and_drivers(self):
        return self.driver.find_element_by_xpath ( locators.Download_apps_and_drivers )

    @property
    def Web_release(self):
        return self.driver.find_element_by_xpath ( locators.Web_release )

    @property
    def Terms_of_use(self):
        return self.driver.find_element_by_xpath ( locators.Terms_of_use )

    @property
    def Privacy_policy(self):
        return self.driver.find_element_by_xpath ( locators.Privacy_policy )

    @property
    def Contact_us(self):
        return self.driver.find_element_by_xpath ( locators.Contact_us )

    @property
    def Copyright(self):
        return self.driver.find_element_by_xpath ( locators.Copyright )

    @property
    def Download_the_iOS_app(self):
        return self.driver.find_element_by_xpath ( locators.Download_the_iOS_app )

    @property
    def Download_the_Android_app(self):
        return self.driver.find_element_by_xpath ( locators.Download_the_Android_app )

    @property
    def Supports_OSX_and_above(self):
        return self.driver.find_element_by_xpath ( locators.Supports_OSX_and_above )

    @property
    def Supports_Windows_and_10(self):
        return self.driver.find_element_by_xpath ( locators.Supports_Windows_and_10 )

    @property
    def PrintMe_Service_Works(self):
        return self.driver.find_element_by_xpath ( locators.PrintMe_Service_Works )

    @property
    def this_site(self):
        return self.driver.find_element_by_xpath ( locators.this_site )

    @property
    def Install_PrintMe(self):
        return self.driver.find_element_by_xpath ( locators.Install_PrintMe )

    @property
    def Cost_PrintMe(self):
        return self.driver.find_element_by_xpath ( locators.Cost_PrintMe )

    @property
    def File_types_and_sizes(self):
        return self.driver.find_element_by_xpath ( locators.File_types_and_sizes )

    @property
    def Print_Documents(self):
        return self.driver.find_element_by_xpath ( locators.Print_Documents )

    @property
    def Interactive_Map(self):
        return self.driver.find_element_by_xpath ( locators.Interactive_Map )

    @property
    def Locate_PrintMe_enabled(self):
        return self.driver.find_element_by_xpath ( locators.Locate_PrintMe_enabled )

    @property
    def Interactive_Map1(self):
        return self.driver.find_element_by_xpath ( locators.Interactive_Map1 )

    @property
    def Long_Print_Documents(self):
        return self.driver.find_element_by_xpath ( locators.Long_Print_Documents )

    @property
    def PrintMe_account(self):
        return self.driver.find_element_by_xpath ( locators.PrintMe_account )

    @property
    def PrintMe_app(self):
        return self.driver.find_element_by_xpath ( locators.PrintMe_app )

    @property
    def Print_boarding_pass(self):
        return self.driver.find_element_by_xpath ( locators.Print_boarding_pass )

    @property
    def this_website(self):
        return self.driver.find_element_by_xpath ( locators.this_website )

    @property
    def PrintMe_mobile_apps(self):
        return self.driver.find_element_by_xpath ( locators.PrintMe_mobile_apps )

    @property
    def PrintMe_benefits(self):
        return self.driver.find_element_by_xpath ( locators.PrintMe_benefits )

    @property
    def Mobile_boarding_pass(self):
        return self.driver.find_element_by_xpath ( locators.Mobile_boarding_pass )

    @property
    def Share_menu(self):
        return self.driver.find_element_by_xpath ( locators.Share_menu )

    @property
    def PrintMe_drs(self):
        return self.driver.find_element_by_xpath ( locators.PrintMe_drs )

    @property
    def PrintMe_drs_benefits(self):
        return self.driver.find_element_by_xpath ( locators.PrintMe_drs_benefits )

    @property
    def PrintMe_drs_upload(self):
        return self.driver.find_element_by_xpath ( locators.PrintMe_drs_upload )

    @property
    def PrintMe_drs_boarding(self):
        return self.driver.find_element_by_xpath ( locators.PrintMe_drs_boarding )

    @property
    def PrintMe_drs_install(self):
        return self.driver.find_element_by_xpath ( locators.PrintMe_drs_install )

    @property
    def PrintMe_Embedded(self):
        return self.driver.find_element_by_xpath ( locators.PrintMe_Embedded )

    @property
    def PrintMe_Canon(self):
        return self.driver.find_element_by_xpath ( locators.PrintMe_Canon )

    @property
    def Canon_website(self):
        return self.driver.find_element_by_xpath ( locators.Canon_website )

    @property
    def PrintMe_Security(self):
        return self.driver.find_element_by_xpath ( locators.PrintMe_Security )

    @property
    def PrintMe_secure(self):
        return self.driver.find_element_by_xpath ( locators.PrintMe_secure )

    @property
    def PrintMe_Support(self):
        return self.driver.find_element_by_xpath ( locators.PrintMe_Support )

    @property
    def Status_page(self):
        return self.driver.find_element_by_xpath ( locators.Status_page )

    @property
    def EFI_Smart_Support(self):
        return self.driver.find_element_by_xpath ( locators.EFI_Smart_Support )

    @property
    def PrintMe_experience(self):
        return self.driver.find_element_by_xpath ( locators.PrintMe_experience )

    @property
    def Map_Search(self):
        return self.driver.find_element_by_xpath ( locators.Map_Search )

    @property
    def Map_button(self):
        return self.driver.find_element_by_xpath ( locators.Map_button )


def file_upload(driver, locator, path, filenames):
    ele = driver.find_element_by_id ( locator )
    ele.click ( )
    r = pyrobot.Robot ( )
    if driver.name == 'internet explorer':
        r.wait_for_window ( "Choose File to Upload", 5 )
    elif driver.name == 'firefox':
        r.wait_for_window ( "File Upload", 5 )
    elif driver.name == 'chrome':
        r.wait_for_window ( "Open", 5 )
    time.sleep ( 5 )
    r.type_string ( path )
    r.key_press ( pyrobot.Keys.enter )
    time.sleep ( 2 )
    r.key_release ( pyrobot.Keys.enter )
    time.sleep ( 5 )
    r.type_string ( filenames )
    r.key_press ( pyrobot.Keys.enter )
    r.key_release ( pyrobot.Keys.enter )
    del r


def sendbtn_click(self):
    wait = WebDriverWait ( self.driver, 5, poll_frequency=4,
                           ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException] )
    ele = wait.until ( EC.element_to_be_clickable ( (By.XPATH, locators.send_btn) )
                       )
    try:
        ele.click ( )
    except WebDriverException:
        print ( "element is not clickable after 20 sec" )


def csvwrite(self):
    wait = WebDriverWait ( self.driver, 5, poll_frequency=4,
                           ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException] )
    ele = wait.until ( EC.element_to_be_clickable ( (By.XPATH, locators.send_btn) )
                       )
    try:
        ele.click ( )
    except WebDriverException:
        print ( "element is not clickable after 20 sec" )


#def csvread(self)
    # csv file name
    #filename = r"C:\Users\srikantm\Music\Printme.csv"

    # initializing the titles and rows list
    fields = []
    #rows = []

    # reading csv file
    #with open ( filename, 'r' ) as csvfile:
        # creating a csv reader object
        #csvreader = csv.reader ( csvfile )

        # extracting field names through first row
        #fields = next ( csvreader )

        # extracting each data row one by one
        #for row in csvreader:
            #rows.append ( row )

        # get total number of rows
        #print ( "Total no. of rows: %d" % (csvreader.line_num) )

    # printing the field names
    #print ( 'Field names are:' + ', '.join ( field for field in fields ) )

    # printing first 5 rows
    #print ( '\nFirst 5 rows are:\n' )
    #for row in rows[:5]:
        #print ( row[0] )
