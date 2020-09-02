from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\aditya kumar\\PycharmProjects\\chromedriver.exe")

def main():
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    #To get element of all three radio button and save to radiobuttons variable as list
    radiobuttons=driver.find_elements_by_css_selector("div[class='left-align'] label input")
    radiobuttons[2].click()# we direct access this as by using index and clicking third radiobutton or you can use any one only thats why do not use loop
    print(radiobuttons[0].is_selected())
    print(radiobuttons[1].is_selected())
    print(radiobuttons[2].is_selected())
    assert radiobuttons[2].is_selected()== True

if __name__ == "__main__":
    main()