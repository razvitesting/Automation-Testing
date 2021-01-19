# open google.com
# perform a search

import time
from selenium import webdriver


class ChromeDriverWindows():
    def test(self):
        baseUrl = "https://google.com"
        driver = webdriver.Chrome(executable_path="D:\\IT materials\\Exercises&Homework\\Drivere\\chromedriver.exe")
        driver.get(baseUrl)
        time.sleep(10)

        element = None
        element = driver.find_element_by_name("q")
        if element is not None:
            print("We found element by name")
        
        element.send_keys("selenium")
        element.submit()
        


incercare = ChromeDriverWindows()
incercare.test()
