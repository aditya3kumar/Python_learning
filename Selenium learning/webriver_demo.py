from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#browser exposes an execuatble file
# Through selenium we invoke this executable file which invokes the real browsers

#open chrome browser
driver = webdriver.Chrome(executable_path="C:\\Users\\aditya kumar\\PycharmProjects\\chromedriver.exe")

#open firefox browser

# driver = webdriver.Firefox(executable_path="C:\\Users\\aditya kumar\\PycharmProjects\\geckodriver.exe")

#  open the url
driver.get("https://www.globalsqa.com/samplepagetest/")

# to maximize browser
driver.maximize_window()


driver.find_element_by_xpath("//input[id='g2599-name']").send_keys('TEST')

print('page title',driver.title)
print('page url',driver.current_url)  # xpath //tagname[@attribute='value']
driver.refresh()
