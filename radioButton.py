import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class radioButton():

    def testradioButton(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(executable_path="D:\\IT materials\\Homework\\Drivere\\chromedriver.exe")
        driver.get(baseUrl)

        bmwRadioBtn = driver.find_element_by_id("bmwradio")
        bmwRadioBtn.click()
        time.sleep(5)

        benzRadioBtn = driver.find_element_by_id("benzradio")
        benzRadioBtn.click()
        time.sleep(5)

        hondaRadioBtn = driver.find_element_by_id("hondaradio")
        hondaRadioBtn.click()
        time.sleep(5)

    def testRadioButtonList(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(executable_path="D:\\IT materials\\Homework\\Drivere\\chromedriver.exe")
        driver.get(baseUrl)

        radioBtnList = driver.find_elements(By.XPATH , "//input[contains(@type, 'radio') and contains (@name, 'cars')]" )
        size = len(radioBtnList)

        print("Size of the list: %d " % size) 

        for radioButton in radioBtnList:
            isSelected = radioButton.is_selected()
            if not isSelected:
                radioButton.click()
                time.sleep(5)


    
test = radioButton()
test.testRadioButtonList()



#name cars
#type radio
#// input[@name='cars']
#// input[@type='radio']