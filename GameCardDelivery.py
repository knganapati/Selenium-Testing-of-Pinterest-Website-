from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service

# Initialize Chrome WebDriver (replace with Firefox WebDriver if needed)
chromedriver_path =  r"\chromedriver.exe" # Adjust for your path
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

def highlight_element(element):
    driver.execute_script("arguments[0].setAttribute('style', 'border: 6px solid red;');", element)
    time.sleep(2)
    driver.execute_script("arguments[0].setAttribute('style', 'border: 0px;');", element)

# Open Amazon.in
driver.get("https://www.gamecarddelivery.com/login/")
time.sleep(2)

login = driver.find_element(By.XPATH, '//*[@id="__next"]/div/nav/div[1]/div[2]/div/div/div/a[1]/button')
highlight_element(login)
login.click()

time.sleep(2)
email = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[1]/section[1]/form/div[1]/input')
highlight_element(email)
email.send_keys("gowdadeepak680@gmail.com")
time.sleep(1)
pwd = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[1]/section[1]/form/div[2]/input')
highlight_element(pwd)
pwd.send_keys("deep2002")
time.sleep(2)
proceed = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[1]/section[1]/form/button')
highlight_element(proceed)
proceed.click()
time.sleep(2)
gcard = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/nav/div[1]/div[3]/div/div[1]/ul/li[1]/div[1]/a')
highlight_element(gcard)
gcard.click()
time.sleep(5)
gf = driver.find_element(By.XPATH, '//*[@id="__next"]/div/nav/div[1]/div[3]/div/div[1]/ul/li[2]/div[1]/a')
highlight_element(gf)
gf.click()
time.sleep(5)
ag = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div[1]/div[2]/div/div[2]/ul[2]/li/div')
highlight_element(ag)
ag.click()
time.sleep(4)
am = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div[1]/div[2]/div/div[2]/ul[2]/li/ul/div/li[1]/a/span')
highlight_element(am)
am.click()
time.sleep(2)
p1 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div/div[2]/div[1]/div/div[1]/div[2]/button[1]/p')
highlight_element(p1)
p1.click()
time.sleep(2)


cart = driver.find_element(By.XPATH,'//*[@id="__next"]/div/nav/div[1]/div[1]/div[3]/div/a/div/svg/path')
highlight_element(cart)
cart.click()
time.sleep(2)

p2 = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div[2]/div[1]/section/div[5]/div/div[3]/button/svg')
highlight_element(p2)
p2.click()
time.sleep(2)


cart1 = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div[2]/div[1]/section/div[5]/div/div[1]/button/svg')
highlight_element(cart1)
cart1.click()
time.sleep(2)

# cart2 = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div[2]/div[1]/section/div[5]/div/div[1]/button/svg')
# highlight_element(cart2)
# cart2.click()
# time.sleep(2)

driver.back()
time.sleep(2)
time.sleep(3)
# dropdown = driver.find_element(By.XPATH, "//*[@id='Details-2-template--16317651189922__product-grid']")
# highlight_element(dropdown)
# dropdown.click()
# dropdown.click()
# time.sleep(2)
# lowend = driver.find_element(By.XPATH, "//*[@id='Filter-Price-GTE']")
# highlight_element(lowend)
# lowend.send_keys("100")
# highend = driver.find_element(By.XPATH, "//*[@id='Filter-Price-LTE']")
# highlight_element(highend)
# highend.send_keys("5000")
# time.sleep(2)
# dropdown = driver.find_element(By.XPATH, "//*[@id='Details-2-template--16317651189922__product-grid']")
# dropdown.click()
time.sleep(5)
# Example verification (replace with actual verification logic)
assert "Gameodev.in" in driver.title

# Close the browser
driver.quit()
