from selenium import webdriver
from POM.My_Food import Swiggy

class Test_001:
    url="https://www.swiggy.com/"
    fone="9028782326"
    dosa="Dosa"

    def test_login(self,setup):
        self.driver=setup
        self.mp=Swiggy(self.driver)
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.mp.set_01()
        self.mp.set_02(self.fone)
        self.driver.implicitly_wait(10)
        self.mp.set_04(self.dosa)
        self.mp.set_05()


