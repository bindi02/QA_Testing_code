from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
driver = webdriver.Firefox()
driver.get("http://chartsandchords.grantjbutler.com")

element = driver.find_element_by_link_text("HOME")
print element
element.click()

x = driver.find_element_by_link_text("SHOP")
print x
x.click()

y = driver.find_element_by_link_text("SEARCH")
print y
y.click()

z = driver.find_element_by_link_text("ADD TO CART")
print z
z.click()



