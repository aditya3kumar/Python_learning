from selenium import webdriver
# how to set behaviour of chrome browser ref- https://www.guru99.com/chrome-options-desiredcapabilities.html#1
chrome_option=webdriver.ChromeOptions()
chrome_option.add_argument("--start-maximized") # Always start in maximize mode
chrome_option.add_argument("headless") # it will execute without opening chrome browse in behind the screen
driver = webdriver.Chrome(executable_path="C:\\Users\\aditya kumar\\PycharmProjects\\chromedriver.exe",options=chrome_option)
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)