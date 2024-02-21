import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.scientologycourses.org/fr/tools-for-life/conflicts/start.html")

# Répondre Email
text_area = driver.find_element(By.XPATH, '//*[@id="outer_shell"]/div[2]/div[3]/div/div[2]/div/div/div/div/article/main/div/div[1]/div/form/div[1]/input')
text_area.clear()
random_number = random.randint(10000000, 99999999)
text_area.send_keys(str(random_number)+"@prout.prout")

# Répondre Prénom
text_area = driver.find_element(By.XPATH, '//*[@id="outer_shell"]/div[2]/div[3]/div/div[2]/div/div/div/div/article/main/div/div[1]/div/form/div[2]/div[1]/input')
text_area.clear()
text_area.send_keys("michel")

# Répondre Nom
text_area = driver.find_element(By.XPATH, '//*[@id="outer_shell"]/div[2]/div[3]/div/div[2]/div/div/div/div/article/main/div/div[1]/div/form/div[2]/div[2]/input')
text_area.clear()
text_area.send_keys("crédule")

# Répondre Mot de passe
text_area = driver.find_element(By.XPATH, '//*[@id="outer_shell"]/div[2]/div[3]/div/div[2]/div/div/div/div/article/main/div/div[1]/div/form/div[3]/div[1]/input')
text_area.clear()
text_area.send_keys("menfou123!")

# Répondre Mot de passe bis
text_area = driver.find_element(By.XPATH, '//*[@id="outer_shell"]/div[2]/div[3]/div/div[2]/div/div/div/div/article/main/div/div[1]/div/form/div[3]/div[2]/input')
text_area.clear()
text_area.send_keys("menfou123!")

# Répondre Code Postal
text_area = driver.find_element(By.XPATH, '//*[@id="outer_shell"]/div[2]/div[3]/div/div[2]/div/div/div/div/article/main/div/div[1]/div/form/div[4]/div[1]/input')
text_area.clear()
text_area.send_keys("93000")

time.sleep(1)

submit = driver.find_element(By.XPATH, '//*[@id="outer_shell"]/div[2]/div[3]/div/div[2]/div/div/div/div/article/main/div/div[1]/div/form/div[6]/div/button/span')
submit.click()

time.sleep(10)
