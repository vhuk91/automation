from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
import time


profile_path = r"C:\Users\Vivobook\AppData\Roaming\Mozilla\Firefox\Profiles\74e3fwgs.default-release"

# Create a Firefox profile instance
options = webdriver.FirefoxOptions()
options.profile = webdriver.FirefoxProfile(profile_path)

# Use webdriver_manager to handle geckodriver installation
service = Service(GeckoDriverManager().install())

# Initialize FirefoxDriver with the service and options
driver = webdriver.Firefox(service=service, options=options)

driver.get("https://orbitxch.com/customer/sport/27454571/market/1.230100169")
time.sleep(7)

#map2
p1=driver.find_element(by="xpath", value='/html/body/div[1]/div/div[2]/main/div/div[2]/div/div/div/div[2]/div[5]/div/div/div[2]/div/div[2]/div[2]/div[1]/button/span/div/span[1]')
p1=p1.text
p1=float(p1)

amount_p1 =driver.find_element(by="xpath", value="/html/body/div[1]/div/div[2]/main/div/div[2]/div/div/div/div[2]/div[5]/div/div/div[2]/div/div[2]/div[2]/div[1]/button/span/div/span[2]")
amount_p1=amount_p1.text
amount_p1=int(p1)

p2=driver.find_element(by="xpath", value="/html/body/div[1]/div/div[2]/main/div/div[2]/div/div/div/div[2]/div[5]/div/div/div[3]/div/div[2]/div[2]/div[1]/button/span/div/span[1]")
p2=p2.text
p2=float(p2)

amount_p2=driver.find_element(by="xpath", value="/html/body/div[1]/div/div[2]/main/div/div[2]/div/div/div/div[2]/div[5]/div/div/div[3]/div/div[2]/div[2]/div[1]/button/span/div/span[2]")
amount_p2=amount_p2.text
amount_p2=int(p2)

print("fuck you")
