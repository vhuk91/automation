from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
# Path to your Chrome profile
profile_path = r"C:\Users\Vivobook\AppData\Local\Google\Chrome\User Data"

chrome_options = Options()
chrome_options.add_argument(f"user-data-dir={profile_path}")
chrome_options.add_argument('--profile-directory=Profile 4') #Actual profile name

# Initialize the WebDriver with the Chrome options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Open a webpage to test
driver.get("https://www.youtube.com")
driver.wait = WebDriverWait(driver, 10)
# Your automation code here...

# Close the browser
time.sleep(15)
user_input=input("Enter YouTube: ")
if user_input == "y":
    driver.quit()



"""driver = webdriver.Chrome()

# Load the website you want to add cookies to
driver.get("https://www.facebook.com/")

# Read cookies from CSV file
with open('abc.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        cookie = {'name': row[0], 'value': row[1]}
        driver.add_cookie(cookie)

# Refresh the page to apply the cookies
driver.refresh()
time.sleep(5)
# Close the WebDriver
driver.quit()"""
1323