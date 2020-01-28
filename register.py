from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

user_name = "fatALBERT"
password = "yoyoMAisTHEmove"

first_name = 'Matthew'
middle_name = 'P'
last_name = 'Kaiser'
binary = FirefoxBinary(r'C:\\Program Files\\Mozilla Firefox\\firefox.exe')
path = r'C:\\geckodriver-path\\geckodriver.exe'
driver = webdriver.Firefox(executable_path=path, firefox_binary=binary)

driver.get('https://app.rockgympro.com/b/widget/?a=list&&widget_guid=866f9c3341cc4bc6888c922779411230&random=5e2236f3ed592&iframeid=&mode=p')
element = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/fieldset[12]/div/a')
element.click()
element = driver.find_element_by_xpath('/html/body/div[1]/div/form/div[6]/div/fieldset/table/tbody/tr[2]/td[1]/a[2]')
element.click()
element = driver.find_element_by_xpath('/html/body/div[1]/div/form/fieldset/div[1]/table/tbody/tr/td[4]/a')
element.click()

element = driver.find_element_by_id("pfirstname-pindex-1-1")
element.send_keys(first_name)
element = driver.find_element_by_id("plastname-pindex-1-1")
element.send_keys(last_name)
# element = driver.find_element_by_id("pmiddle-pindex-1-1")
# element.send_keys(middle_name)

select = Select(driver.find_element_by_id("participant-birth-pindex-1month"))
select.select_by_visible_text("May")
select = Select(driver.find_element_by_id("participant-birth-pindex-1day"))
select.select_by_visible_text("6")
select = Select(driver.find_element_by_id("participant-birth-pindex-1year"))
select.select_by_visible_text("1996")

element = driver.find_element_by_xpath('/html/body/div[1]/div/form/a[2]')
element.click()

select = Select(driver.find_element_by_id("copy-pinfo-select"))
select.select_by_visible_text("Matthew Kaiser")

element = driver.find_element_by_id("customer-email")
element.send_keys("mkaiser101@gmail.com")

element = driver.find_element_by_id("customer-phone")
element.send_keys("mkaiser101@gmail.com")

element = driver.find_element_by_id("customer-address-line1")
element.send_keys("3000 Spout Run Pwky Apt B503")

element = driver.find_element_by_id("customer-city")
element.send_keys("Arlington")

element = driver.find_element_by_id("customer-state")
element.send_keys("VA")

element = driver.find_element_by_id("customer-zip")
element.send_keys("22201")

element = driver.find_element_by_id("confirm_booking_button")
element.click()









# ids = driver.find_elements_by_xpath('//*[@id]')
# for ii in ids:
#     #print (ii.tag_name)
#     print(ii.get_attribute('id'))    # id name as string





# #element.close()

    


# element = driver.find_element_by_xpath('//*[@id="pcount-pid-1-316074"]').click()
# element.send_keys('1')
# element.send_keys(Keys.RETURN)
# element.close()



# element = driver.find_element_by_id("fl-post-7284").click()
#element.send_keys(user_name)
#element = driver.find_element_by_id("pass")
#element.send_keys(password)
#element.send_keys(Keys.RETURN)
#element.close()
# buttons = ['menu-main-nav', 'menu-item-35', 'menu-item-28', 'menu-item-29', 'menu-item-14233', 'menu-item-33', 'menu-item-8834', 'menu-item-32', 'menu-main-nav-1', 'content', 'primary', 'main', 'fl-post-7284', 'headerSpacer', 'fl-accordion-5a8b5ea406d09-tab-0', 'fl-accordion-5a8b5ea406d09-label-0', 'fl-accordion-5a8b5ea406d09-icon-0', 'fl-accordion-5a8b5ea406d09-panel-0', 'fl-accordion-5a8b5ea406d09-tab-1', 'fl-accordion-5a8b5ea406d09-label-1', 'fl-accordion-5a8b5ea406d09-icon-1', 'fl-accordion-5a8b5ea406d09-panel-1', 'fl-accordion-5a8b5ea406d09-tab-2', 'fl-accordion-5a8b5ea406d09-label-2', 'fl-accordion-5a8b5ea406d09-icon-2', 'fl-accordion-5a8b5ea406d09-panel-2', 'fl-accordion-5a8b5ea406d09-tab-3', 'fl-accordion-5a8b5ea406d09-label-3', 'fl-accordion-5a8b5ea406d09-icon-3', 'fl-accordion-5a8b5ea406d09-panel-3', 'fl-accordion-5a8b5ea406d09-tab-4', 'fl-accordion-5a8b5ea406d09-label-4', 'fl-accordion-5a8b5ea406d09-icon-4', 'fl-accordion-5a8b5ea406d09-panel-4', 'fl-accordion-5a8b5ea406d09-tab-5', 'fl-accordion-5a8b5ea406d09-label-5', 'fl-accordion-5a8b5ea406d09-icon-5', 'fl-accordion-5a8b5ea406d09-panel-5', 'fl-accordion-5a8b5ea406d09-tab-6', 'fl-accordion-5a8b5ea406d09-label-6', 'fl-accordion-5a8b5ea406d09-icon-6', 'fl-accordion-5a8b5ea406d09-panel-6', 'fl-accordion-5a8b5ea406d09-tab-7', 'fl-accordion-5a8b5ea406d09-label-7', 'fl-accordion-5a8b5ea406d09-icon-7', 'fl-accordion-5a8b5ea406d09-panel-7', 'fl-accordion-5a8b5ea406d09-tab-8', 'fl-accordion-5a8b5ea406d09-label-8', 'fl-accordion-5a8b5ea406d09-icon-8', 'fl-accordion-5a8b5ea406d09-panel-8', 'fl-accordion-5a8b5ea406d09-tab-9', 'fl-accordion-5a8b5ea406d09-label-9', 'fl-accordion-5a8b5ea406d09-icon-9', 'fl-accordion-5a8b5ea406d09-panel-9', 'fl-accordion-5a8b5ea406d09-tab-10', 'fl-accordion-5a8b5ea406d09-label-10', 'fl-accordion-5a8b5ea406d09-icon-10', 'fl-accordion-5a8b5ea406d09-panel-10', 'fl-accordion-5a8b5ea406d09-tab-11', 'fl-accordion-5a8b5ea406d09-label-11', 'fl-accordion-5a8b5ea406d09-icon-11', 'fl-accordion-5a8b5ea406d09-panel-11', 'fl-accordion-5a8b5ea406d09-tab-12', 'fl-accordion-5a8b5ea406d09-label-12', 'fl-accordion-5a8b5ea406d09-icon-12', 'fl-accordion-5a8b5ea406d09-panel-12', 'fl-accordion-5a8b5ea406d09-tab-13', 'fl-accordion-5a8b5ea406d09-label-13', 'fl-accordion-5a8b5ea406d09-icon-13', 'fl-accordion-5a8b5ea406d09-panel-13', 'fl-accordion-5a8b5ea406d09-tab-14', 'fl-accordion-5a8b5ea406d09-label-14', 'fl-accordion-5a8b5ea406d09-icon-14', 'fl-accordion-5a8b5ea406d09-panel-14', 'fl-accordion-5a8b5ea406d09-tab-15', 'fl-accordion-5a8b5ea406d09-label-15', 'fl-accordion-5a8b5ea406d09-icon-15', 'fl-accordion-5a8b5ea406d09-panel-15', 'fl-accordion-5a8b5ea406d09-tab-16', 'fl-accordion-5a8b5ea406d09-label-16', 'fl-accordion-5a8b5ea406d09-icon-16', 'fl-accordion-5a8b5ea406d09-panel-16', 'fl-accordion-5a8b5ea406d09-tab-17', 'fl-accordion-5a8b5ea406d09-label-17', 'fl-accordion-5a8b5ea406d09-icon-17', 'fl-accordion-5a8b5ea406d09-panel-17', 'rgp_never_redirect_script_id', 'rgp-iframe-spinner', 'rgpiframe5e22353dbaa1f', 'mobile-nav', 'menu-main-nav-2', 'menu-footer-quicklinks', 'menu-item-18', 'menu-item-15', 'menu-item-17', 'menu-item-19', 'menu-item-26', 'menu-item-27', 'menu-item-20', 'menu-item-24', 'menu-item-25', 'menu-item-21', 'menu-item-22', 'menu-item-14004', 'hs-script-loader', 'hs-script-loader', 'wpstats', '', '', '_hjRemoteVarsFrame', '']
# for button in buttons:
#     try:
#         element = driver.find_element_by_id(button).click()
#         print(button)
#     except: 
#         pass
# buttons = []  
# ids = driver.find_elements_by_xpath('//*[@id]')
# for ii in ids:
#     #print (ii.tag_name)
#     yellow = (ii.get_attribute('id'))    # id name as string
#     buttons.append(yellow)