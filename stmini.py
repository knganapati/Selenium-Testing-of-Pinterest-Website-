from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

chromedriver_path = r"C:\Users\k n ganapati\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

def highlight_element(element):
    driver.execute_script("arguments[0].setAttribute('style', 'border: 6px solid red;');", element)
    time.sleep(1)
    driver.execute_script("arguments[0].setAttribute('style', 'border: 0px;');", element)

driver.get("https://in.pinterest.com/")
wait = WebDriverWait(driver, 20)

login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__PWS_ROOT__"]/div/div[1]/div/div[1]/div/div[2]/div[2]/button/div/div')))
highlight_element(login_button)
login_button.click()

email = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]')))
highlight_element(email)
email.send_keys("tangentsub@gmail.com")

pwd = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]')))
highlight_element(pwd)
pwd.send_keys("elastic_collission@24")

proceed = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__PWS_ROOT__"]/div/div[1]/div[2]/div/div/div/div/div/div[4]/form/div[7]/button/div/div/div')))
highlight_element(proceed)
proceed.click()

try:
    error_message = wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Something went wrong")]')))
    highlight_element(error_message)
    print("Invalid login credentials.")
    driver.quit()
except:
    home = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="HeaderContent"]/div/div/div[2]/div/div/div/div[2]/a/div/div/span')))
    highlight_element(home)
    home.click()

time.sleep(2)

def smooth_scroll():
    page_height = driver.execute_script("return document.body.scrollHeight")
    for i in range(0, page_height, 100):
        driver.execute_script(f"window.scrollTo(0, {i});")
        time.sleep(0.1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)

smooth_scroll()

explore_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="HeaderContent"]/div/div/div[2]/div/div/div/div[3]/a/div/div/span')))
highlight_element(explore_button)
explore_button.click()

time.sleep(5)

search_box = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchBoxContainer"]/div/div/div[2]/input')))
highlight_element(search_box)
search_box.click()
search_box.send_keys("cycling")
search_box.send_keys(Keys.ENTER)
time.sleep(7)

for i in range(1, 4):
    pin_xpath = f'//*[@id="__PWS_ROOT__"]/div/div[1]/div/div[2]/div/div/div[{i}]/div/div[1]/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/a/div/div[1]/div/div/div/div/div/img'
    pin = wait.until(EC.element_to_be_clickable((By.XPATH, pin_xpath)))
    highlight_element(pin)
    pin.click()

    time.sleep(2)

    save_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gradient"]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div[1]/div[1]/div/div/div/div[2]/div/div/div/div/div[2]/button/div/div/div/div')))
    highlight_element(save_button)
    save_button.click()

    time.sleep(2)

    download_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pin-action-dropdown-item-0"]/div')))
    highlight_element(download_button)
    download_button.click()

    time.sleep(2)

    driver.back()
    time.sleep(2)

product_page_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="HeaderContent"]/div/div/div[2]/div/div/div/div[2]/a/div/div/span')))
highlight_element(product_page_button)
product_page_button.click()

time.sleep(5)

product_image = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__PWS_ROOT__"]/div/div[1]/div/div[2]/div/div/div[4]/div/div[1]/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/a/div/div[1]/div/div/div/div/div/img')))
highlight_element(product_image)
product_image.click()

time.sleep(2)

save_image_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pin-action-dropdown-item-0"]/div')))
highlight_element(save_image_button)
save_image_button.click()

time.sleep(5)

like_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__PWS_ROOT__"]/div/div[1]/div/div[2]/div/div/div[4]/div/div[1]/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/a/div/div[1]/div/div/div/div/div/img')))
highlight_element(like_button)
like_button.click()

time.sleep(2)

follow_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__PWS_ROOT__"]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div/div/div[2]/div[1]/div/div/div[2]/button')))
highlight_element(follow_button)
follow_button.click()

time.sleep(2)

driver.get("https://in.pinterest.com/")

time.sleep(2)

smooth_scroll()

driver.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# import time

# # Initialize Chrome WebDriver with the correct path
# chromedriver_path = chromedriver_path = r"C:\Users\k n ganapati\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# service = Service(chromedriver_path)
# driver = webdriver.Chrome(service=service)

# def highlight_element(element):
#     driver.execute_script("arguments[0].setAttribute('style', 'border: 6px solid red;');", element)
#     time.sleep(1)
#     driver.execute_script("arguments[0].setAttribute('style', 'border: 0px;');", element)

# # Open Pinterest website
# driver.get("https://in.pinterest.com/")
# wait = WebDriverWait(driver, 20)

# # Interact with elements
# login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__PWS_ROOT__"]/div/div[1]/div/div[1]/div/div[2]/div[2]/button/div/div')))
# highlight_element(login_button)
# login_button.click()

# email = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]')))
# highlight_element(email)
# email.send_keys("tangentsub@gmail.com")

# pwd = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]')))
# highlight_element(pwd)
# pwd.send_keys("elastic_collission@24")

# proceed = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__PWS_ROOT__"]/div/div[1]/div[2]/div/div/div/div/div/div[4]/form/div[7]/button/div/div/div')))
# highlight_element(proceed)
# proceed.click()

# home = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="HeaderContent"]/div/div/div[2]/div/div/div/div[2]/a/div/div/span')))
# highlight_element(home)
# home.click()

# # Wait for the home page to load
# time.sleep(2)

# def smooth_scroll():
#     # Get the height of the entire page
#     page_height = driver.execute_script("return document.body.scrollHeight")
#     for i in range(0, page_height, 100):
#         driver.execute_script(f"window.scrollTo(0, {i});")
#         time.sleep(0.09)  # Adjust the sleep time for smoother or faster scrolling
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(2)  # Allow time to ensure everything loads at the bottom
#     driver.execute_script("window.scrollTo(0, 0);")
#     time.sleep(1)  # Allow time to scroll back to the top

# explore = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="HeaderContent"]/div/div/div[2]/div/div/div/div[3]/a/div/div/span')))
# highlight_element(explore)
# explore.click()
# time.sleep(5)

# search_box = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchBoxContainer"]/div/div/div[2]/input')))
# highlight_element(search_box)
# search_box.click()
# search_box.send_keys("bike")
# search_box.send_keys(Keys.ENTER)
# time.sleep(7)

# image = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__PWS_ROOT__"]/div/div[1]/div/div[2]/div/div/div[4]/div/div[1]/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/a/div/div[1]/div/div/div/div/div/img')))
# highlight_element(image)
# image.click()
# time.sleep(6)

# # actions = ActionChains(driver)
# # for _ in range(3):
# #     actions.send_keys(Keys.PAGE_DOWN).perform()
# #     time.sleep(2)

# view = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@data-test-id="pin"]//img')))
# highlight_element(view)
# view.click()
# time.sleep(6)

# save = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gradient"]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div[1]/div[1]/div/div/div/div[2]/div/div/div/div/div[2]/button/div/div/div/div')))
# highlight_element(save)
# save.click()
# time.sleep(6)

# dot = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gradient"]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div[1]/div[1]/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div/button/div/div')))
# highlight_element(dot)
# dot.click()
# time.sleep(6)


# download = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pin-action-dropdown-item-0"]/div')))
# highlight_element(download)
# download.click()
# time.sleep(6)



# # Example verification (replace with actual verification logic)
# assert "Pinterest" in driver.title

# # Close the browser
# driver.quit()
