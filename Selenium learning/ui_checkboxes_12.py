from selenium import webdriver


def main():
    driver = webdriver.Chrome(executable_path="C:\\Users\\aditya kumar\\PycharmProjects\\chromedriver.exe")
    # How to handle multiple checkboxes
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#Finding the all checkbox option and saved to var
    checkboxes=driver.find_elements_by_xpath("//div[@class='right-align']/fieldset/label/input")
# by looping and clicking one by one all checkbox
    for checkbox in checkboxes:
        checkbox.click()
        assert checkbox.is_selected()
    driver.close()

### Now again we check only for one checkbox out of 3 checkbox

    driver = webdriver.Chrome(executable_path="C:\\Users\\aditya kumar\\PycharmProjects\\chromedriver.exe")
    # How to handle multiple checkboxes
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    # Finding the all checkbox option and saved to var
    checkboxes = driver.find_elements_by_xpath("//div[@class='right-align']/fieldset/label/input")
    # by looping and clicking only one from all checkbox
    for checkbox in checkboxes:
        if checkbox.get_attribute('id') == "checkBoxOption2": #using get_trribute to find out exact locator where u want to click
            checkbox.click()
            assert checkbox.is_selected()


if __name__ == "__main__":
    main()

