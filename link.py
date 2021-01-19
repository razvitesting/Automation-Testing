import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Link():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(executable_path="D:\\IT materials\\Homework\\Drivere\\chromedriver.exe")
        driver.get(baseUrl)

        elementLogin = None
        try:
            elementLogin = driver.find_element_by_link_text("Login")
        except:
            print("We found exception.")

        if elementLogin is not None:
            print("we found element Login")

        elementPractice = None
        try:
            elementPractice = driver.find_element_by_partial_link_text("Pract")
        except:
            print("We found exception.")

        if elementPractice is not None:
            print("we found element Practice")
        
test = Link()
test.test()