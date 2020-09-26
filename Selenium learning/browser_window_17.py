from selenium import webdriver
# We are doing how to handle browser new windows and tabs
driver = webdriver.Chrome(executable_path="C:\\Users\\aditya kumar\\PycharmProjects\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element_by_link_text("Click Here").click()
child_window1=driver.window_handles[1]  #It basically create list index 0 is parent window which is default driver in script and other are child window
parent_window=driver.window_handles[0]
driver.switch_to.window(child_window1) # switching control to child window
print(driver.find_element_by_css_selector("div[class='example'] h3").text)
driver.switch_to.window(parent_window) # switch control to parent window
print(driver.find_element_by_css_selector("div[class='example'] h3").text)

