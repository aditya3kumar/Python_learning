from selenium import webdriver
# End to End scenario from selecting only blackberry product to checkout out of all
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\Users\\aditya kumar\\PycharmProjects\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_css_selector("a[href*='shop']").click() # click on shop button
phones=driver.find_elements_by_xpath("//div[@class='card h-100']") ## fetch all product and put in loop
for phone in phones:
    product_name=(phone.find_element_by_xpath("div/h4/a").text)
    if product_name=="Blackberry": # find only blackberry product
        #Add blackbeery phone into cart
        phone.find_element_by_xpath("div[2]/button").click()
driver.find_element_by_css_selector("a[class='nav-link btn btn-primary']").click()

driver.find_element_by_css_selector("button[class='btn btn-success']").click()
driver.find_element_by_id("country").send_keys("ind")

wait= WebDriverWait(driver,7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element_by_link_text("India").click()
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_css_selector("input[class='btn btn-success btn-lg']").click()
success_msg=driver.find_element_by_css_selector("div[class='alert alert-success alert-dismissible']").text
assert "Success! Thank you!" in success_msg

# how to take screenshot and save in file
driver.get_screenshot_as_file("screen.png")






