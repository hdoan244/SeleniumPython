'''
Created on 1 Jul. 2018

@author: Danny
'''
import os
import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class LoginPage(unittest.TestCase):
    @classmethod
    def setUp(inst):
        # get the path of ChromeDriverServer
        dir = os.path.dirname(__file__)
        chrome_driver_path = dir + "\chromedriver.exe"
        inst.driver = webdriver.Chrome(chrome_driver_path)
        inst.driver.implicitly_wait(20)
        inst.driver.maximize_window()

        # navigate to Hudl login page
        inst.driver.get("https://www.hudl.com/login")
        
    def test_credential(self):
        # check field exists in Hudl login page
        self.assertTrue(self.is_element_present(By.ID,"email"))
        self.assertTrue(self.is_element_present(By.ID,"password"))
        self.assertTrue(self.is_element_present(By.ID,"logIn"))
        
        # enter Hudl coach credentials
        username = self.driver.find_element_by_id("email")
        password = self.driver.find_element_by_id("password")
        submit   = self.driver.find_element_by_id("logIn")
  
        username.send_keys("hdoan244@yahoo.com")
        password.send_keys("huudoan85")
        submit.click()
  
        # check if the login is successful
        correct_page = "https://www.hudl.com/home"
        wait = WebDriverWait( self, 5 )
  
        try:
            page_loaded = wait.until_not(
                lambda driver: self.driver.current_url == "https://www.hudl.com/login"
            )
        except TimeoutException:
            self.fail( "Loading timeout expired" )
        
        self.assertEqual(self.driver.current_url, correct_page, msg = "Successful Login")
    
    @classmethod
    def tearDown(inst):
        # close the browser window
        inst.driver.quit()
        
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException: return False
        return True

if __name__ == '__main__':
    unittest.main(verbosity=2)