from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
import time


pin = 1.77
bet = 3000

profile_path = r"C:\Users\Vivobook\AppData\Roaming\Mozilla\Firefox\Profiles\74e3fwgs.default-release"

# Create a Firefox profile instance
options = webdriver.FirefoxOptions()
options.profile = webdriver.FirefoxProfile(profile_path)

# Use webdriver_manager to handle geckodriver installation
service = Service(GeckoDriverManager().install())

# Initialize FirefoxDriver with the service and options
driver = webdriver.Firefox(service=service, options=options)

driver.get("https://csgopositive.com/")
time.sleep(88)

specific_element = driver.find_element(by="id", value="bet_sum_input")
specific_element.clear()
specific_element.send_keys(bet)

while True:
    odds_element = driver.find_element(by="xpath", value="/html/body/div[9]/div[2]/div/form/div[1]/span[1]/i")
    odds = odds_element.text
    odds = float(odds)
    print(odds)
    if odds >= pin:
        specific_element = driver.find_element(by="id", value="place_bet_btn")
        specific_element.click()
        print("bet placed successfully")
        answer=input("continue? y/n")
        if answer == "y":
            continue
    else:
        continue

time.sleep(7)
driver.quit()




