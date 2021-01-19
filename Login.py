import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\\IT materials\\Homework\\Drivere\\chromedriver.exe")
baseUrl = "http://www.demo.guru99.com/V4/"
username = "mngr304119"
password = "AgYduhu"


class Login():

    def tc01_login_success(self):
       
        driver.get(baseUrl)

        username = driver.find_elements(By.NAME, "uid")
        username.send_keys(username)

        password = driver.find_elements(By.NAME, "password")
        password.send_keys(password)

        button = driver.find_elements(By.NAME, "btnLogin")
        button.click()

        time.sleep(5)


        actualTitle = driver.title
        if (actualTitle == "Guru99 Bank Manager HomePage"):
            print("Test Case T01 Login success PASSED")
        else:
            print("Test Case T01 Login success FAILED")

        

    def login_username_maxim_char(self):

        driver.get(baseUrl)

        username = driver.find_element(By.NAME, "uid")
        username.send_keys(username + "asdfgjhliupq")

        password = driver.find_element(By.NAME, "password")
        password.send_keys(password)

        button = driver.find_element(By.NAME, "btnLogin")
        button.click()

        time.sleep(5)

        actualTitle = driver.title
        if (actualTitle == "Guru99 Bank Manager HomePage"):
            print("T10 Login with a username that has characters >10 PASS")
        else:
            print("T10 Login with a username that has characters >10 FAILED")



    def login_NOK(self, usernameString, passwordString, testCase):

        driver.get(baseUrl)

        if usernameString != "":
            username = driver.find_element(By.NAME, "uid")
            username.send_keys(usernameString)


        if passwordString != "":
            password = driver.find_element(By.NAME, "password")
            password.send_keys(passwordString)

        button = driver.find_element(By.NAME, "btnLogin")
        button.click()

        time.sleep(5)

        actualTitle = None
        try:
            actualTitle = driver.title
        except:
            print("Test Case  " + testCase +  " PASSED")
            
        if actualTitle is not None:
            print("Test Case  " + testCase +  " FAILED")



test = Login()

test.tc01_login_success()
test.login_NOK("usernameNOK" , "AgYduhu" , "T02 Login wrong username and correct password -")
test.login_NOK("mngr304119" , "asdfkeys" , "T03 Login correct username and wrong password -")
test.login_NOK("usernameNOK" , "asdfkeys" , "T04 Login wrong username and wrong password -")
test.login_NOK("" , "AgYduhu" , "T05 Login empty username and correct password -")
test.login_NOK("" , "asdfkeys" , "T06 Login empty username and wrong password -")
test.login_NOK("mngr304119" , "" , "T07 Login correct username and empty password -")
test.login_NOK("usernameNOK" , "" , "T08 Login wrong username and empty password -")
test.login_NOK("","", "T09 Login empty user and empty password -")
test.login_username_maxim_char()



driver.quit()