import sys
from time import sleep
import platform
sys.path.append("C:\clientapp_test\webapps\printme")
import os
import time
import csv
import locators
import Waits as wr
#from printme import locators
from  selenium import webdriver
#import sqlite3
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class Session:
    '''
    Session is for all Exprespay  session.
    It will be used by all test cases
    '''
    def CreateSession(self):
        ####### converting unicode characters  to string in evn variables
        copyenv  = os.environ.copy()
        for k in copyenv:
            if ((type(k) != str) or (type(copyenv[k]) != str)):
                os.environ[k] = str(os.environ[k])
        ################################################################
        cmdDict={}
                
        self.ParseCommandLine(cmdDict)

        try:
            
            if 'browser' in cmdDict:
                self.browser = cmdDict['browser']
                print("browser value",cmdDict['browser'])
                print("browser",self.browser)

                if 'firefox' in cmdDict['browser'].lower():
                    self.driver=webdriver.Firefox()
                if 'ie' in cmdDict['browser'].lower():
                    self.driver=webdriver.Ie()
                if 'chrome' in cmdDict['browser'].lower():
                    self.driver=webdriver.Chrome()
            else:
                self.driver=webdriver.Firefox()
        except:
            self.driver=webdriver.Firefox()
            
        return self.driver
        
        
  
    def ParseCommandLine(self, cmdDict):
        i=1
        count=len(sys.argv)
        temp = list(sys.argv)
        while ( i < count ):
            arg=temp[i]
            if '=' in arg:
                key,value = arg.split("=")
                cmdDict[key] = value
                del temp[i]
                count-=1
                i-=1
            i+=1

    

class LaunchWebsite:
    def __init__(self, driver: object) -> object:
        self.driver =driver
        self.driver.implicitly_wait(10)
        #self.driver.get(locators.xpresspay_qa_url)
        #self.driver.get(locators.xpresspay_staples_url)
        self.driver.get(locators.printme_qa_url)
        self.driver.maximize_window()

def Cloud(driver):
    if driver.current_url[8:18]=='qa-staples':
        return "https://qa-staples-selfserve.efi.com"
    elif driver.current_url[8:15]=='qa-self':
        return "https://qa-selfserve.efi.com"
    elif driver.current_url[8:16]=='dev-self':
        return "https://dev-selfserve.efi.com"
    elif driver.current_url[8:16]=='epcdev10':
        return "https://epcdev10.qaefi.com"
    elif driver.current_url[8:19]=='pre-staples':
         return "https://pre-staples-selfserve.efi.com"
    elif driver.current_url[8:19]=='dev-staples':
         return "https://dev-staples-selfserve.efi.com"

class Login():
    def __init__(self, driver):
        try:
            self.driver =driver
            self.loginbutton=self.driver.find_element_by_id(locators.hlogin)
        except:
            pass
    @property
    def email(self):
        return self.driver.find_element_by_id(locators.email)

    @property
    def password(self):
        return self.driver.find_element_by_id(locators.password)

    @property
    def login(self):
        return self.driver.find_element_by_id(locators.login)
    
           

        
    def Login(self,email,password):
        sleep(5)
        eid=self.driver.find_element_by_id(locators.email)
        eid.send_keys(email)
        pwd=self.driver.find_element_by_id(locators.password)
        pwd.send_keys(password)
        login=self.driver.find_element_by_id(locators.login)
        login.click()
        #sleep(10)
        if Wait(self.driver,'errorMessage',3)==True:
            print (" error while Login ")
            error=self.driver.find_element_by_id('errorMessage')
            return error.text        
        
        if Wait(self.driver,locators.configuration_tab,20)==True:
            print("Login operation successful")
            return True
        else:
            print("Login operation unsuccessful")
            return False

# class Location:
#     def __init__(self, driver):
#         try:
#             self.driver =driver
#             self.location_tab = self.driver.find_element_by_id(locators.location_tab)
#             self.add_location_button=self.driver.find_element_by_id(locators.add_location_button)
#             self.select_location = self.driver.find_element_by_id(locators.select_location)
#             self.location_name=self.driver.find_element_by_id(locators.location_name)
#             self.branch_code=self.driver.find_element_by_id(locators.branch_code)
#             self.streetname=self.driver.find_element_by_id(locators.street)
#             self.cityname=self.driver.find_element_by_id(locators.city)
#             self.statename=self.driver.find_element_by_id(locators.state)
#             self.zipcode=self.driver.find_element_by_id(locators.zipcode)
#             self.phone = self.driver.find_element_by_id(locators.phone)
#             self.timezone = self.driver.find_element_by_id(locators.timezone)
#             self.import_location = self.driver.find_element_by_id(locators.import_location)
#             self.phone=self.driver.find_element_by_id(locators.phone)
#             self.timezone=self.driver.find_element_by_id(locators.timezone)
#             self.add_Button=self.driver.find_element_by_id(locators.add_Button)
#             #self.add_device_profile=self.driver.find_element_by_id(locators.add_device_profile)
#             self.cancel_Button=self.driver.find_element_by_id(locators.cancel_Button)
#             self.edit_button = self.driver.find_element_by_id(locators.edit_button)
#             self.editlocation_cancel_btn = self.driver.find_element_by_id(locators.editlocation_cancel_btn)
#             self.editlocation_save_btn = self.driver.find_element_by_id(locators.editlocation_save_btn)
#             self.editlocation_name = self.driver.find_element_by_id(locators.editlocation_name)
#             self.import_pricing_taxes=self.driver.find_element_by_id(locators.import_pricing_taxes)
#         except:
#             pass
#
#     @property
#     def error_msg(self):
#         form =  self.driver.find_element_by_id(locators.Add_location_form)
#         return form.find_element_by_xpath("//form[@id='newLocationForm']/descendant::label[@class='errormsg']").text
#     @property
#     def Location_err(self):
#         form =  self.driver.find_element_by_id(locators.Add_location_form)
#         return form.find_element_by_xpath("//form[@id='newLocationForm']/descendant::label[@for='addLocationName'][@class='errormsg']").text
#     @property
#     def Street_err(self):
#         form =  self.driver.find_element_by_id(locators.Add_location_form)
#         return form.find_element_by_xpath("//form[@id='newLocationForm']/descendant::label[@for='addLocationAddress1'][@class='errormsg']").text
#     @property
#     def City_err(self):
#         form =  self.driver.find_element_by_id(locators.Add_location_form)
#         return form.find_element_by_xpath("//form[@id='newLocationForm']/descendant::label[@for='addLocationCity'][@class='errormsg']").text
#     @property
#     def State_err(self):
#         form =  self.driver.find_element_by_id(locators.Add_location_form)
#         return form.find_element_by_xpath("//form[@id='newLocationForm']/descendant::label[@for='addLocationState'][@class='errormsg']").text
#     @property
#     def Zip_err(self):
#         form =  self.driver.find_element_by_id(locators.Add_location_form)
#         return form.find_element_by_xpath("//form[@id='newLocationForm']/descendant::label[@for='addLocationZip'][@class='errormsg']").text
#
#     @property
#     def close_form(self):
#         form =  self.driver.find_element_by_id(locators.Add_location_form)
#         return form.find_element_by_xpath("//div[@id='addlocation']/descendant::input[@type='image'][@class='close']")
#
#     @property
#     def Add_location_from_dropdown(self):
#         Select(self.select_location).select_by_visible_text("Add Location...")
#
#     @property
#     def add_device_profile(self):
#         return self.driver.find_element_by_id(locators.add_device_profile)
#
#     def Navigate_LocationForm(self):
#         self.location_tab.click()
#         self.add_location_button.click()
#
#
#     def AddLocation(self,data):
#         if Wait(self.driver,locators.location_tab,5)==True:
#             time.sleep(5)
#             self.location_tab.click()
#             time.sleep(5)
#             self.add_location_button.click()
#         if Wait(self.driver,"newLocationForm",2)==True:
#             self.branch_code.send_keys(data[1])
#             self.location_name.send_keys(data[0])
#             self.streetname.send_keys(data[2])
#             self.cityname.send_keys(data[3])
#             Select(self.statename).select_by_visible_text(data[4])
#             self.zipcode.send_keys(data[5])
#             self.phone.send_keys(data[6])
#             Select(self.timezone).select_by_value(data[7])
#             if data[8]==0:
#                 self.location_dst.check()
#             if data[11]==1:
#                 self.import_location.check()
#             form = self.driver.find_element_by_id("newLocationForm")
#             table = form.find_element_by_tag_name("table")
#             rnum = Table_Search(table,data[10])
#             if rnum!=None:
#                 pass
#                 #table.find_element_by_xpath("//tbody/tr["+str(rnum)+"]/td[2]/label").click()
#             else:
#                 return False
#             self.add_Button.click()
#             time.sleep(1)
#             if Wait(self.driver,"newLocationForm",10)==True:
#                 return False
#             try:
#                Select(self.select_location).select_by_visible_text(data[0])
#                return True
#             except NoSuchElementException:
#                print("The combo value do not exist")
#                return False
#
#     @property
#     def import_button(self):
#         return self.driver.find_element_by_id(locators.import_location)
#
#     @property
#     def yes(self):
#         return self.driver.find_element_by_id(locators.yes_import)
#
#     @property
#     def no(self):
#         return self.driver.find_element_by_id(locators.no_import)
#
#
#
#
#
#
#
#
#
#
#
#     def DeleteLocation(self,locname):
#         try:
#            Select(self.select_location).select_by_visible_text(locname)
#         except:
#             print ("Error in selecting location:"+locname)
#             return False
#         #if combobox(select_location,locname)==True:
#             ##location selected , delete it now
#         try:
#             time.sleep(5)
#             delete_location = self.driver.find_element_by_id(locators.delete_location)
#             delete_location.click()
#             time.sleep(1)
#             yes_button=self.driver.find_element_by_id(locators.delete_location_yes)
#             time.sleep(1)
#             yes_button.click()
#             print("Location %s sucessfully deleted"%(locname))
#             return True
#         except:
#             print ("Error in deleting location"+locname)
#             return False
#
#         # else:
#         #     print("error while Deleting location name")
#
#     def DeleteAllLocations(self):
#         self.driver.find_element_by_partial_link_text('Location').click()
#         time.sleep(5)
#         if self.driver.find_element_by_id(locators.New_location_form).is_displayed()==True:
#             self.driver.find_element_by_id(locators.cancel_Button).click()
#             return
#         a=self.driver.find_element_by_id(locators.select_location)
#         select = Select(a)
#         while(len(select.options)>1):
#             wr.Clickable(self.driver).Wait_click_id(locators.delete_location)
#             delete_location=self.driver.find_element_by_id(locators.delete_location)
#             delete_location.click()
#             yes_button=self.driver.find_element_by_id(locators.delete_location_yes)
#             yes_button.click()
#             sleep(5)
#         try:
#                 cancel=self.driver.find_element_by_id(locators.cancel_Button)
#                 cancel.click()
#         except:
#             pass
#
#
# class Device:
#     def __init__(self, driver):
#
#         try:
#
#             self.driver =driver
#             self.device_name=self.driver.find_element_by_id(locators.device_name)
#             self.device_type=self.driver.find_element_by_id(locators.device_type)
#             self.cancel_device_button=self.driver.find_element_by_id(locators.cancel_device_button)
#             if self.cancel_device_button.text=='':
#                 new_device=self.driver.find_element_by_id('newdeviceform')
#                 self.cancel_device_button=new_device.find_element_by_id(locators.cancel_device_button)
#
#             self.add_device_button=self.driver.find_element_by_id(locators.add_device_button)
#             if self.add_device_button.text=='':
#                 new_device=self.driver.find_element_by_id('newdeviceform')
#                 self.add_device_button=new_device.find_element_by_id(locators.add_device_button)
#
#         except:
#             pass
#
#     @property
#     def manufacturer(self):
#         return self.driver.find_element_by_id(locators.manufacturer)
#
#     @property
#     def device_name(self):
#         return self.driver.find_element_by_id(locators.device_name)
#
#     @property
#     def device_type(self):
#         return self.driver.find_element_by_id(locators.device_type)
#
#     @property
#     def cancel_device_button(self):
#         new_device=self.driver.find_element_by_id('newdeviceform')
#         return new_device.find_element_by_id(locators.cancel_device_button)
#
#     @property
#     def add_device_button(self):
#         new_device=self.driver.find_element_by_id('newdeviceform')
#         return new_device.find_element_by_id(locators.add_device_button)
#
#     @property
#     def modelname(self):
#         return self.driver.find_element_by_id(locators.model)
#
#     @property
#     def allow_copying(self):
#         return self.driver.find_element_by_id(locators.allow_copying)
#
#     @property
#     def allow_printing(self):
#         return self.driver.find_element_by_id(locators.allow_printing)
#
#     @property
#     def chare_all_output_as_color(self):
#         return self.driver.find_element_by_id(locators.chare_all_output_as_color)
#
#     @property
#     def print_via_network_radio_button(self):
#         return self.driver.find_element_by_id(locators.print_via_network_radio_button)
#
#     @property
#     def print_via_network_ip(self):
#         return self.driver.find_element_by_id(locators.print_via_network_ip)
#
#     @property
#     def print_via_direct_connect(self):
#         return self.driver.find_element_by_id(locators.print_via_direct_connect)
#
#     @property
#     def allow_receipt_printing(self):
#         return self.driver.find_element_by_id(locators.allow_receipt_printing)
#
#     @property
#     def allow_printing_from_USB(self):
#         return self.driver.find_element_by_id(locators.allow_printing_from_USB)
#
#     @property
#     def allow_printing_from_Printme(self):
#         return self.driver.find_element_by_id(locators.allow_printing_from_Printme)
#
#     @property
#     def allow_printing_from_dropbox(self):
#         return self.driver.find_element_by_id(locators.allow_printing_from_dropbox)
#
#     @property
#     def allow_printing_from_Googledrive(self):
#         return self.driver.find_element_by_id(locators.allow_printing_from_Googledrive)
#
#     @property
#     def allow_printing_from_OneDrive(self):
#         return self.driver.find_element_by_id(locators.allow_printing_from_OneDrive)
#
#     @property
#     def show_advanced_settings(self):
#         return self.driver.find_element_by_id(locators.show_advanced_settings)
#
#     @property
#     def protocol(self):
#         return self.driver.find_element_by_id(locators.protocol)
#
#     @property
#     def queue(self):
#         return self.driver.find_element_by_id(locators.queue)
#
#     @property
#     def port_number(self):
#         return self.driver.find_element_by_id(locators.port_number)
#
#     @property
#     def ping_printer_status(self):
#         return self.driver.find_element_by_id(locators.ping_printer_status)
#
#     @property
#     def enable_snmp_status(self):
#         return self.driver.find_element_by_id(locators.enable_snmp_status)
#
#     @property
#     def community_name(self):
#         return self.driver.find_element_by_id(locators.community_name)
#
#     @property
#     def device_index(self):
#         return self.driver.find_element_by_id(locators.device_index)
#
#     @property
#     def hide_advanced_settings(self):
#         return self.driver.find_element_by_id(locators.hide_advanced_settings)
#
#     @property
#     def device_already_exist(self):
#         return self.driver.find_element_by_xpath(locators.device_already_exist)
#
#     @property
#     def form(self):
#         return self.driver.find_element_by_id("newdeviceform")
#
#     def AddDevice(self,type,data):
#         GotoLocationTab(self.driver)
#         L = Location(self.driver)
#         #L.location_tab.click()
#         if type=='M500':
#             try:
#                #Select(L.select_location).select_by_value('2104')
#                Select(L.select_location).select_by_visible_text(data[5])
#             except NoSuchElementException:
#                print("The combo value do not exist")
#
#             time.sleep(3)
#             L.add_device_profile.click()
#             self.device_name.send_keys(data[0])
#
#             try:
#                Select(self.device_type).select_by_value(data[3])
#             except NoSuchElementException:
#                print("The combo value do not exist")
#
#             try:
#                Select(self.manufacturer).select_by_visible_text(data[1])
#                Select(self.modelname).select_by_visible_text(data[2])
#             except NoSuchElementException:
#                print("The combo value do not exist")
#
#             time.sleep(3)
#             if self.allow_copying.is_selected()==False:
#                 self.allow_copying.click()
#             if self.allow_printing.is_selected()==False:
#                 self.allow_printing.click()
#             self.print_via_direct_connect.click()
#             self.add_device_button.click()
#             time.sleep(2)
#             if Wait(self.driver,"newdeviceform",2)==True:
#                 return False
#             elif Wait(self.driver,"newdeviceform",2)==False:
#                 return True
#
#
#         elif type=='Kiosk':
#             try:
#                #Select(L.select_location).select_by_value('2104')
#                Select(L.select_location).select_by_visible_text(data[5])
#             except NoSuchElementException:
#                print("The combo value do not exist")
#
#             time.sleep(3)
#             L.add_device_profile.click()
#             self.device_name.send_keys(data[0])
#
#             try:
#                Select(self.device_type).select_by_value(data[3])
#             except NoSuchElementException:
#                print("The combo value do not exist")
#             self.add_device_button.click()
#             time.sleep(2)
#
#             if Wait(self.driver,"newdeviceform",2)==True:
#                 return False
#             elif Wait(self.driver,"newdeviceform",2)==False:
#                 return True
#
#     def DeleteDevice(self,name,location):
#         L = Location(self.driver)
#         L.location_tab.click()
#         try:
#                #Select(L.select_location).select_by_value('2104')
#                Select(L.select_location).select_by_visible_text(location)
#         except NoSuchElementException:
#                print("The combo value do not exist")
#         table = self.driver.find_element_by_id(locators.device_table_list)
#         rnum = Device_Table_Search(table,name)
#         action = table.find_element_by_xpath("//tbody/tr["+str(rnum)+"]/td[5]")
#         action.find_element_by_partial_link_text("Actions").click()
#         time.sleep(1)
#         action.find_element_by_id(locators.delete_device_btn).click()
#         time.sleep(1)
#         if Wait(self.driver,locators.device_delete_btn,5)==True:
#             self.driver.find_element_by_id(locators.device_delete_btn).click()
#             time.sleep(2)
#             if Table_Search(table,name)==None:
#                return True
#             else:
#                 return False
#         else:
#             return False

          



def combobox(element, value):
        select = Select(element)
        options = select.options
        for i in options:
            if type(i) != str and type(i) == str:
                if value.lower().replace(" ", "") == i.text.lower().replace(" ", ""):
                    value = i.text
        try:
            select.select_by_visible_text(value)
        except:
            if value.isdigit():
                value = int(value)
                if value < len(options):
                    value = options[value].text
                    select.select_by_visible_text(value)
                else:
                    print("Failed to select value %s for combobox "%(str(value)))
                    return False                    
            else:
                print("Failed to select value %s for combobox "%(value))
                return False                  
     
        return True 

def Wait(driver,locator,time):
        try:
            wait = WebDriverWait(driver ,time)
            element = wait.until(EC.element_to_be_clickable((By.ID,locator)))
            return True
        except:
##            print(("Control with id %s does not load"%locator))
            return False

def Table_Search(tablewebelement,value):
    """ This Function can be used to search some value in a HTML Table
         it takes webelement of the table and value to be serached as argument
    """
    rnum = -1
    for i in (tablewebelement.find_elements_by_tag_name("tr")):
            rnum+=1
            for j in (i.find_elements_by_tag_name("td")):
                    if value in j.text:
##				if value.lower().replace(" ","") == j.find_element_by_tag_name("span").text.lower().replace(" ",""):
                                    return rnum

def Table_Search_Row(tablewebelement,value):
    """ This Function can be used to search some value in a HTML Table
         it takes webelement of the table and value to be serached as argument
    """
    for i in (tablewebelement.find_elements_by_tag_name("tr")):
            for j in (i.find_elements_by_tag_name("td")):
                    if value in j.text:
                        return i

def Device_Table_Search(tablewebelement,txt):
    tbody = tablewebelement.find_element_by_xpath("tbody")
    sz = len(tbody.find_elements_by_tag_name("tr"))
    for i in range(1,sz+1):
        if txt == tbody.find_element_by_xpath("//tr["+str(i)+"]/td[2]/span").text:
           return i


def rows(tablewebelement):
    """ This functions returns the Rows of a HTML table """

    if tablewebelement is None:
        return []
    try:
        return [row.text for row in tablewebelement.find_elements_by_tag_name("tr")]
    except:
        return []

def RowCount(tablewebelement):
    """ This functions returns the number of  Rows in a HTML table """

    RowCnt = []
    if tablewebelement is None:
        return 0
    try:
        for i in (tablewebelement.find_elements_by_tag_name("tr")):
            if i .is_displayed():
                RowCnt.append(i)
        return len(RowCnt)
    except:
        return []

def ColumnCount(tablewebelement):
    """ This functions returns the number of  Column  in a HTML table """

    if tablewebelement is None:
        return 0
    try:
        ColCnt = []
        row  = tablewebelement.find_element_by_tag_name("tr")
        if len (row.find_elements_by_tag_name("td")) == 0:
            for i in row.find_elements_by_tag_name("th"):
                if i.is_displayed():
                    ColCnt.append(i)
            return len(ColCnt)
        else:
            for i in row.find_elements_by_tag_name("td"):
                if i.is_displayed():
                    ColCnt.append(i)
            return len(ColCnt)
    except:
        return []


def close_webPage(driver):
    driver.close()
        
  
    
def GotoLocationTab(driver):
    Configuration_tab = driver.find_element_by_id(locators.configuration_tab)
    Configuration_tab.click()
    sleep(10)
    Location_tab=driver.find_element_by_id(locators.location_tab)
    Location_tab.click()

def GotoGlobalTab(driver):
    Configuration_tab=driver.find_element_by_id(locators.configuration_tab)
    Configuration_tab.click()
    sleep(5)
    Global_tab=driver.find_element_by_id(locators.global_tab)
    Global_tab.click()

def GotoGeneralTab(driver):
    Configuration_tab=driver.find_element_by_id(locators.configuration_tab)
    Configuration_tab.click()
    sleep(5)
    Global_tab=driver.find_element_by_id(locators.global_tab)
    Global_tab.click()
    general_tab=driver.find_element_by_id(locators.general_tab)
    general_tab.click()
    

def GotoRegionsTab(driver):
    Configuration_tab=driver.find_element_by_id(locators.configuration_tab)
    Configuration_tab.click()
    sleep(5)
    Global_tab=driver.find_element_by_id(locators.global_tab)
    Global_tab.click()
    regions_tab=driver.find_element_by_id(locators.regions_tab)
    regions_tab.click()

def GotoDeviceSettingsTab(driver):
    Configuration_tab=driver.find_element_by_id(locators.configuration_tab)
    Configuration_tab.click()
    sleep(5)
    Global_tab=driver.find_element_by_id(locators.global_tab)
    Global_tab.click()
    devicesettings_tab=driver.find_element_by_id(locators.devicesettings_tab)
    devicesettings_tab.click()

def GotoPaymentTab(driver):
    Configuration_tab=driver.find_element_by_id(locators.configuration_tab)
    sleep(5)
    Configuration_tab.click()    
    #Global_tab=driver.find_element_by_id(locators.global_tab)
    #Global_tab.click()
    payment_tab=driver.find_element_by_id(locators.payment_tab)
    payment_tab.click()
    sleep(5)

def GotoTaxesTab(driver):
    Configuration_tab=driver.find_element_by_id(locators.configuration_tab)
    Configuration_tab.click()
    sleep(5)
    Global_tab=driver.find_element_by_id(locators.global_tab)
    Global_tab.click()
    sleep(5)
    taxes_tab=driver.find_element_by_id(locators.taxes_tab)
    taxes_tab.click()

def GotoProductsTab(driver):
    Configuration_tab=driver.find_element_by_id(locators.configuration_tab)
    sleep(2)
    Configuration_tab.click()
    sleep(5)
    Global_tab=driver.find_element_by_id(locators.global_tab)
    Global_tab.click()
    products_tab=driver.find_element_by_id(locators.products_tab)
    products_tab.click()

def GotoLiablityagreementTab(driver):
    Configuration_tab=driver.find_element_by_id(locators.configuration_tab)
    Configuration_tab.click()
    sleep(5)
    Global_tab=driver.find_element_by_id(locators.global_tab)
    Global_tab.click()
    liablityagreement_tab=driver.find_element_by_id(locators.liablityagreement_tab)
    liablityagreement_tab.click()

def GotoDeviceProfileTab(driver):
    Configuration_tab=driver.find_element_by_id(locators.configuration_tab)
    Configuration_tab.click()
    sleep(5)
    Location_tab=driver.find_element_by_id(locators.location_tab)
    Location_tab.click()
    deviceprofile_tab=driver.find_element_by_id(locators.deviceprofile_tab)
    deviceprofile_tab.click()

def GotoTaxRateTab(driver):
    Configuration_tab=driver.find_element_by_id(locators.configuration_tab)
    Configuration_tab.click()
    sleep(5)
    Location_tab=driver.find_element_by_id(locators.location_tab)
    Location_tab.click()
    sleep(5)
    taxrate_tab=driver.find_element_by_id(locators.taxrate_tab)
    taxrate_tab.click()

def GotoPriceListTab(driver):
    sleep(5)
    Configuration_tab=driver.find_element_by_id(locators.configuration_tab)
    Configuration_tab.click()
    sleep(5)
    Location_tab=driver.find_element_by_id(locators.location_tab)
    Location_tab.click()
    pricelist_tab=driver.find_element_by_id(locators.pricelist_tab)
    pricelist_tab.click()

def GotoReceiptsTab(driver):
    Configuration_tab=driver.find_element_by_id(locators.configuration_tab)
    Configuration_tab.click()
    sleep(5)
    Location_tab=driver.find_element_by_id(locators.location_tab)
    Location_tab.click()
    sleep(5)
    receipt_tab=driver.find_element_by_id(locators.general_receipt_tab)
    receipt_tab.click()

def GotoStaffAccountTab(driver):
    Configuration_tab=driver.find_element_by_id(locators.configuration_tab)
    Configuration_tab.click()
    time.sleep(5)
    Staff_account=driver.find_element_by_id(locators.staff_account_tab)
    Staff_account.click()


def GotoConfigurationTab(driver):
    Configuration_tab=driver.find_element_by_id(locators.configuration_tab)
    Configuration_tab.click()
    sleep(5)

def GotoReportsTab(driver):
    reports_tab=driver.find_element_by_id(locators.reports_tab)
    reports_tab.click()

def GotoTransactionsTab(driver):
    transactions_tab=driver.find_element_by_id(locators.transactions_tab)
    transactions_tab.click()

def GotoDashboardTab(driver):
    dashboard_tab=driver.find_element_by_id(locators.dashboard_tab)
    dashboard_tab.click()

def File_Upload(driver,value):
        from time import sleep
        from autl import autl 
        app=autl.Application()
        sleep(1)       
        
        if driver.name == 'chrome':
            app.Connect("chrome")
            win = app.Window_()
            browse_win = app.WaitForWindow('Open',10)
        if driver.name == 'firefox':
            app.Connect("Firefox")
            win = app.Window_()
            win.Click();win.Activate()
            browse_win = app.WaitForWindow('File Upload',10)

########### will handle for IE ############

        if len(app.Windows_()) >= 2:
            print(("Windows on screen are : ", app.Windows_()))
            
            filename = win["*/l=File*"].Next()
            if os.path.exists(value):
                filename.Click()
                filename.SetText(value)
            else:
                print(("File %s can't be found on Desktop or StorageLoc"%value))
                exit(-1)

            
            from time import sleep
            openbutton = win["*/l=Open"]
            if not isinstance(openbutton, autl.Button):
                openbutton = win["*/c=Button"]
        
            try:
                openbutton.Click()

            except:
                win['*/l=File name'].Next().Click()
                win.TypeKeys('{Enter}')            

            if openbutton.IsShown():
                openbutton.Click()          
                          
           
        else:
            print("Window file Upload does not appear")
            exit(-1)


def select_from_date(driver,value):
	values = value.split("/")
	day = values[0]
	month = values[1]
	year = values[2]
	select_year_from(driver,year)
	select_month_from(driver,month)
	select_day_from(driver,day)


def select_year_from(driver,year):
    if (not str(year).isdigit()) or (2050 < int(year) or  int(year) < 1980):
        print(("Invalid year given accepted 4 digits given : %s"%year))
        exit( -1 )
    a= driver.find_element_by_xpath('//div[@class="calendar left"]/table/thead/tr/th[2]').text
    b=a.split(" ")
    temp_year=b[1]
    while int(temp_year) != int(year):

        sleep(0.5)

        if int(temp_year) == int(year):
            break
        if int(temp_year) > int(year):
            driver.find_element_by_xpath('//div[@class="calendar left"]/table/thead/tr/th[1]').click() #Prev

        else:
            driver.find_element_by_xpath('//div[@class="calendar left"]/table/thead/tr/th[3]').click() # Next

        a= driver.find_element_by_xpath('//div[@class="calendar left"]/table/thead/tr/th[2]').text
        b=a.split(" ")
        temp_year=b[1]

def select_day_from(driver,day):
    table = driver.find_element_by_xpath('//div[@class="calendar left"]/table')
    flag = False
    day=int(day)
    if day > 0 and day < 32:
        for d in table.find_elements_by_tag_name("td"):
            if d.text == str(day):
                d.click()
                flag = True
                break
        if not flag:
            print(("Invalid day [%s] given to select in the calender"%day))
            exit ( -1 )
    else:
        print(("Invalid day [%s] given to select in the calender"%day))
        exit ( -1 )

def select_month_from(driver,month):
    if (not str(month).isdigit()) or (12 < int(month) or  int(month) < 1):
        print(("Invalid month given accepted [1-12], given :%s"%month))
        exit ( -1 )
    month_dict = {"January":1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}
    a = driver.find_element_by_xpath('//div[@class="calendar left"]/table/thead/tr/th[2]').text;
    b=a.split(" ")
    month_name=b[0]
    month_index = month_dict.get(month_name)
    if not month_index:
        print ("Error finding Month name")
        exit ( -1 )

    while month_index != int(month):
	    a = driver.find_element_by_xpath('//div[@class="calendar left"]/table/thead/tr/th[2]').text
	    b=a.split(" ")
	    month_name=b[0]
	    month_index = month_dict.get(month_name)
	    sleep(0.5)
	    Next = driver.find_element_by_xpath('//div[@class="calendar left"]/table/thead/tr/th[3]')
	    Prev = driver.find_element_by_xpath('//div[@class="calendar left"]/table/thead/tr/th[1]')
	    if month_index == int(month):
		    break
	    if month_index > int(month):
		    Prev.click()
	    else:
		    Next.click()



def select_to_date(driver,value):
	values = value.split("/")
	day = values[0]
	month = values[1]
	year = values[2]
	select_year_to(driver,year)
	select_month_to(driver,month)
	select_day_to(driver,day)
	driver.find_element_by_css_selector("button.btn.btn-small.btn-success.applyBtn").click()


def select_year_to(driver,year):
    if (not str(year).isdigit()) or (2050 < int(year) or  int(year) < 1980):
        print(("Invalid year given accepted 4 digits given : %s"%year))
        exit( -1 )
    a= driver.find_element_by_xpath('//div[@class="calendar right"]/table/thead/tr/th[2]').text
    b=a.split(" ")
    temp_year=b[1]
    while int(temp_year) != int(year):

        sleep(0.5)

        if int(temp_year) == int(year):
            break
        if int(temp_year) > int(year):
            driver.find_element_by_xpath('//div[@class="calendar right"]/table/thead/tr/th[1]').click() #Prev

        else:
            driver.find_element_by_xpath('//div[@class="calendar right"]/table/thead/tr/th[3]').click() # Next

        a= driver.find_element_by_xpath('//div[@class="calendar right"]/table/thead/tr/th[2]').text
        b=a.split(" ")
        temp_year=b[1]

def select_day_to(driver,day):
    table = driver.find_element_by_xpath('//div[@class="calendar right"]/table')
    flag = False
    day=int(day)
    if day > 0 and day < 32:
        for d in table.find_elements_by_tag_name("td"):
            if d.text == str(day):
                d.click()
                flag = True
                break
        if not flag:
            print(("Invalid day [%s] given to select in the calender"%day))
            exit ( -1 )
    else:
        print(("Invalid day [%s] given to select in the calender"%day))
        exit ( -1 )

def select_month_to(driver,month):
    if (not str(month).isdigit()) or (12 < int(month) or  int(month) < 1):
        print(("Invalid month given accepted [1-12], given :%s"%month))
        exit ( -1 )
    month_dict = {"January":1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}
    a = driver.find_element_by_xpath('//div[@class="calendar left"]/table/thead/tr/th[2]').text;
    b=a.split(" ")
    month_name=b[0]
    month_index = month_dict.get(month_name)
    if not month_index:
        print ("Error finding Month name")
        exit ( -1 )

    while month_index != int(month):
	    a = driver.find_element_by_xpath('//div[@class="calendar right"]/table/thead/tr/th[2]').text
	    b=a.split(" ")
	    month_name=b[0]
	    month_index = month_dict.get(month_name)
	    sleep(0.5)
	    Next = driver.find_element_by_xpath('//div[@class="calendar right"]/table/thead/tr/th[3]')
	    Prev = driver.find_element_by_xpath('//div[@class="calendar right"]/table/thead/tr/th[1]')
	    if month_index == int(month):
		    break
	    if month_index > int(month):
		    Prev.click()
	    else:
		    Next.click()

def GotoTransactionTab(driver):
    trans_tab = driver.find_element_by_id(locators.transaction_tab)
    trans_tab.click()


def GotoFaxAreaTab(driver):
    Configuration_tab=driver.find_element_by_id(locators.configuration_tab)
    Configuration_tab.click()
    time.sleep(15)
    Location_tab=driver.find_element_by_id(locators.location_tab)
    Location_tab.click()
    time.sleep(15)
    faxareacode_tab=driver.find_element_by_id(locators.faxareacode_tab)
    faxareacode_tab.click()
    time.sleep(15)


def write_to_csv(filenames,docid):
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
