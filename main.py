from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.safari.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=Service(executable_path="/Users/chetan/Desktop/Projects/Instagram Automation/chromedriver"))
driver.maximize_window()


driver.get("https://www.instagram.com")

username_xpath_selector = "//input[@name='username']"
password_xpath_selector = "//input[@name='password']"
username = ""
password = ""

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, username_xpath_selector))
)

# send the keys "username" to the element with class username_class
username = driver.find_element(By.XPATH, username_xpath_selector)
username.send_keys(username)
time.sleep(2)

# # send the keys "password to the element with class password_class"
password = driver.find_element(By.XPATH, password_xpath_selector)
password.send_keys(password + Keys.ENTER)

not_now_xpath_selector = "//div[@class='_ac8f']//div"

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, not_now_xpath_selector))
)

not_now = driver.find_element(By.XPATH, not_now_xpath_selector)
not_now.click()

malla_not_now_xpath_selector = "//div[@class='_a9-z']//button"

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, malla_not_now_xpath_selector))
)

malla_not_now = driver.find_elements(By.XPATH, malla_not_now_xpath_selector)[1]
malla_not_now.click()
print("logged in")
time.sleep(5)

# # wait until the element with class name "x1e56ztr x1gslohp" appears
# WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "_aarf x1e56ztr x1gslohp"))
# )

# driver.find_element(By.CLASS_NAME, "_aarf x1e56ztr x1gslohp")
# driver.click()

# while True:
#     time.sleep(10)
#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CLASS_NAME, "_ac0d"))
#     )
#     driver.find_element(By.CLASS_NAME, "_ac0d")
#     driver.click()