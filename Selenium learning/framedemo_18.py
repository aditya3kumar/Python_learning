from selenium import webdriver
# We are doing how to handle frame in selnium
driver = webdriver.Chrome(executable_path="C:\\Users\\aditya kumar\\PycharmProjects\\chromedriver.exe")

driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr") # switch driver to frame so it can find elements written frame.
driver.find_element_by_id("tinymce").clear()
driver.find_element_by_id("tinymce").send_keys("TEsting frame ")
driver.switch_to.default_content()  # Switch driver from iframe to main driver
print(driver.find_element_by_css_selector("div[class='example'] h3").text)
