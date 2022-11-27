from selenium.webdriver.common.by import By

class Swiggy:
    signin="/html/body/div[1]/div[1]/div[1]/div/div[1]/div[1]/div/div[1]/div/a[1]"
    phone_number="/html/body/div[2]/div/div/div[2]/div/div/div/form/div[1]/div/input"
    login="/html/body/div[2]/div/div/div[2]/div/div/div/form/div[2]/a"
    serch="//*[@id='root']/div[1]/header/div/div/ul/li[5]/div/a"
    dosa="//input[@class='_2FkHZ']"
    s_button="icon-magnifier"

    def __init__(self,driver):
        self.driver=driver

    def set_01(self):
        self.driver.find_element(By.XPATH,self.signin).click()

    def set_02(self,fone):
        self.driver.find_element(By.XPATH,self.phone_number).send_keys(fone)

    def set_03(self):
        self.driver.find_element(By.XPATH,self.login).click()

    def set_04(self,dosa):
        self.driver.find_element(By.XPATH,self.serch).click()
        self.driver.find_element(By.XPATH,self.dosa).send_keys(dosa)

    def set_05(self):
        self.driver.find_element(By.XPATH,self.s_button).click()



