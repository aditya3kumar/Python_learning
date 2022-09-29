from selenium import webdriver
# We are doing how to handle mouse hovering in one element which show 2 option and by moving we have to click that option
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Users\\aditya kumar\\PycharmProjects\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
mouse_hover=driver.find_element_by_id("mousehover")
action.move_to_element(mouse_hover).perform() # mouse hover on button to get 2 child option
action.move_to_element(driver.find_element_by_link_text("Top")).click().perform()  #click on top after mouse hover on mouse hover button

# to check textfield disappear after click on hide
print(driver.find_element_by_id("displayed-text").is_displayed())
assert driver.find_element_by_id("displayed-text").is_displayed() ==True
driver.find_element_by_id("hide-textbox").click()
assert driver.find_element_by_id("displayed-text").is_displayed()==True
