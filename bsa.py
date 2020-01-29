from selenium import webdriver
from time import sleep
from passs import usr,password
class BsaBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    def login(self):
        self.driver.get('http://ais.univnext.com/Index')
        email = self.driver.find_element_by_xpath('//*[@id="username"]')
        email.send_keys(usr)
        pwd = self.driver.find_element_by_xpath('//*[@id="password"]')
        pwd.send_keys(password)
        login_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/button[1]')
        login_btn.click()
        sleep(2)
        pop_up = self.driver.find_element_by_xpath('/html/body/div[7]/div[1]/a/span')
        pop_up.click()
        #sleep(5)
        present = self.driver.find_element_by_xpath('//*[local-name() = "svg"]/*/*/*/*[name()="tspan"][2]').text.split(' ')
        #//*[@id="highcharts-0"]/svg/g[2]/g[1]/text/tspan[1]')
        self.driver.close()
        abs=100-float(present[1])
        print('present: '+present[1]+' %')
        print('Absent: '+str(round(abs,2))+' %')


bot = BsaBot()
bot.login()
