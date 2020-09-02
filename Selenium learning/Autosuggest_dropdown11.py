import time

from selenium import webdriver



def main():
    driver = webdriver.Chrome(executable_path="C:\\Users\\aditya kumar\\PycharmProjects\\chromedriver.exe")
    # How to handle autosuggest dropdowns when you type something
    driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
    driver.find_element_by_id("autosuggest").send_keys("Ind")
    # time sleep

    time.sleep(2)

    # finding the search option element with css locator

    countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")

    for country in countries:
        print(country.text)
        if country.text == "India":
            country.click()
            break

    # Checking the entered value india is clicked or not by using 'get attribute' value
    # because if you using .text the entered value not present on dom of page beasue it fetches through html so thats we used get atrribute

    print(driver.find_element_by_id("autosuggest").get_attribute('value'))
    assert driver.find_element_by_id("autosuggest").get_attribute('value') == "India"

if __name__ == "__main__":
    main()
