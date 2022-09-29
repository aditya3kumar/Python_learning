
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\Users\\aditya kumar\\PycharmProjects\\chromedriver.exe")
#driver.implicitly_wait(5) # globally wait untill 5 sec for every element in script
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ca")
driver.find_element_by_css_selector("button.search-button").click()
add_cart=driver.find_elements_by_css_selector("div[class='product'] button")
for item in add_cart:
    item.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

# below element gets no such exception becasue while loading driver unable to find promocode element for this we use implicit wait or explicit wait
wait= WebDriverWait(driver, 10) # we use only for promo applying condition only
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"input.promocode")))
driver.find_element_by_css_selector("input.promocode").send_keys("rahulshettyacademy")

wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"button.promoBtn")))# we use for promocode applying only
driver.find_element_by_css_selector("button.promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"span.promoInfo")))
promo_code=driver.find_element_by_css_selector("span.promoInfo").text
assert "Code applied ..!"== promo_code
print("Passed")

# Now we used explicit code for same scenario above
