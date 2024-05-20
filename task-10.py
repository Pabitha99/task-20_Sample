import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
paths = r"C:\Users\Ranga\OneDrive\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.instagram.com/guviofficial/")
# following count
following_count_element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"//ul[@class='x78zum5 x1q0g3np xieb3on']//li[3]//button//span/span")))
following_count = following_count_element.text
print("The number of following:", following_count)
# follower's count
followers_count=WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,"//ul[@class='x78zum5 x1q0g3np xieb3on']//li[2]//button//span/span")))
followers_count = followers_count.text
print("The number of followers:", followers_count)