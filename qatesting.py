from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
driver = webdriver.Firefox()
driver.get("http://chartsandchords.grantjbutler.com")

element = driver.find_element_by_link_text("Home")
print element
element.click()

x = driver.find_element_by_link_text("Products")
print x
x.click()

y = driver.find_element_by_link_text("About")
print y
y.click()

z = driver.find_element_by_link_text("Contact")
print z
z.click()

a = driver.find_element_by_link_text("Log in")

print a
a.click()
b = driver.find_element_by_link_text("Create account")
print b
b.click()


