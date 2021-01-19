import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Class():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(executable_path="D:\\IT materials\\Homework\\Drivere\\chromedriver.exe")
        driver.get(baseUrl)

        elementLogin = None
        try:
            elementLogin = driver.find_element_by_class("input")
        except:
            print("We found exception.")

        if elementLogin is not None:
            print("we found Class input")

    
        
test = Class()
test.test()