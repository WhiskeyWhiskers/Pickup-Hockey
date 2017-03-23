from selenium import webdriver
import ipdb

URL = 'http://oaklandice.maxgalaxy.net/BrowseDayCamps.aspx'
driver = webdriver.Chrome()
driver.get(URL)

drop_in_with_gretzky_caret = driver.find_element_by_css_selector("#ContentPlaceHolder1_sideMenuTreeViewn0 > img")
drop_in_with_gretzky_caret.click()

drop_in_link = driver.find_element_by_css_selector("#ContentPlaceHolder1_sideMenuTreeViewt1")
drop_in_link.click()

ipdb.set_trace()
