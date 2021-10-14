from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker
import time

faker = Faker()
fake_email = faker.email()
print(fake_email)

xpath_value_21kg = '//a[@data-link="https://demo1.netcoresmartech.com/prdev_ramya_s/product/21kg-mega-capacity-with-3-5kg/"]'
##driver = webdriver.Chrome('/Users/mukeshtiwari/Documents/selsetup/chromedriver')
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://demo1.netcoresmartech.com/prdev_ramya_s/")
print(driver.title)
driver.maximize_window()
driver.execute_script("smartech('identify', '" + fake_email + "');")

driver.get("https://demo1.netcoresmartech.com/prdev_ramya_s/?id=1")

time.sleep(10)

read_more_21_kg = driver.find_element_by_xpath(xpath_value_21kg)
read_more_21_kg.click()

time.sleep(10)

print(driver.current_url)
driver.close()