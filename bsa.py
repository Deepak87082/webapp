from selenium import webdriver
from time import sleep
from passs import usr,password
from selenium.webdriver.chrome.options import Options

class BsaBot():
    def __init__(self):
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)
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
        present = self.driver.find_element_by_xpath('//*[local-name() = "svg"]/*/*/*/*[name()="tspan"][2]').text.split(' ')
        abst=self.driver.find_element_by_xpath('//*[local-name() = "svg"]/*/*[name()="g"][2]/*/*[name()="tspan"][2]').text.split(' ')   
        print('present: '+present[1]+' %')
        print('Absent: '+abst[1]+' %') 
        self.driver.close()

bot = BsaBot()
bot.login()
