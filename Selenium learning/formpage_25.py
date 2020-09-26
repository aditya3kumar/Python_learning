from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\aditya kumar\\PycharmProjects\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element_by_css_selector("[name='name']").send_keys("test")
driver.find_element_by_css_selector("[name='email']").send_keys("test@gmail.com")
driver.find_element_by_id("exampleCheck1").click()
sel=Select(driver.find_element_by_id("exampleFormControlSelect1"))
sel.select_by_visible_text("Male")
driver.find_element_by_xpath("//input[@class='btn btn-success']").click()
alert_msg= driver.find_element_by_css_selector("div[class='alert alert-success alert-dismissible']").text
print(alert_msg)
assert "success" in alert_msg