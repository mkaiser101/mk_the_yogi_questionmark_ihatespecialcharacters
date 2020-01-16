from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys

user_name = "fatALBERT"
password = "yoyoMAisTHEmove"

binary = FirefoxBinary(r'C:\\Program Files\\Mozilla Firefox\\firefox.exe')
path = r'C:\\geckodriver-path\\geckodriver.exe'
driver = webdriver.Firefox(executable_path=path, firefox_binary=binary)

driver.get('https://www.earthtreksclimbing.com/crystal-city/yoga/')
#element = driver.find_element_by_id("REGISTER FOR A CLASS")
#element.send_keys(user_name)
#element = driver.find_element_by_id("pass")
#element.send_keys(password)
#element.send_keys(Keys.RETURN)
#element.close()


ids = driver.find_elements_by_xpath('//*[@id]')
for ii in ids:
    print (ii.tag_name)
    print(ii.get_attribute('id'))    # id name as string