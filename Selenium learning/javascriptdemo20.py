from selenium import webdriver
# We are doing how to do execution by using javascript execution because sometime selenium doesn't have access to dom objects
driver = webdriver.Chrome(executable_path="C:\\Users\\aditya kumar\\PycharmProjects\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("TEST")
# #below 'it cannot fetch what we enetered on this text field because selenium fetch through html tags .
driver.find_element_by_name("name").text
#selenium call dom object method to fetch text through dom
print(driver.find_element_by_name("name").get_attribute("value"))

# we can also use js execute script by java script method by calling through selenium driver
print(driver.execute_script('return document.getElementsByName("name")[0].value'))

# How we handle if element not visible on page ex. submenu button shows after click to menu ,without clicking menu directly clicking through js dom object,selenuim cannot do this 
shop_btn=driver.find_element_by_css_selector("a[href*='shop']")

#we used java script to click this element ,the argument we pass 0 if you write other element also after shop_btn then you need pass argument[1] to click that element
driver.execute_script("arguments[0].click();",shop_btn)

#How to scroll the web by using java script executor ,selenium doesn't have feature to scroll up or down

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")