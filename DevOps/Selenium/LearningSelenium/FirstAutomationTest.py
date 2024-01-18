from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

options = Options()
# options.add_extension('C:/browserdrivers/chromedriver-win64/chromedriver.exe')
driver = webdriver.ChromeOptions('C:/browserdrivers/chromedriver-win64/chromedriver.exe')

driver.get('http://www.google.com/')

time.sleep(5) # Let the user actually see something!

search_box = driver.find_element_by_name('q')

search_box.send_keys('ChromeDriver')

search_box.submit()

time.sleep(5) # Let the user actually see something!

driver.quit()