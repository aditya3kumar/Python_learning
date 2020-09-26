import time

from selenium import webdriver


def main():
    validate_text = "test"
    driver = webdriver.Chrome(executable_path="C:\\Users\\aditya kumar\\PycharmProjects\\chromedriver.exe")
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.find_element_by_css_selector("input[id='name']").send_keys("test")
    driver.find_element_by_id("alertbtn").click()
    # Switch the control to the Alert window
    alert=driver.switch_to.alert # we switch to alert from webdriver because its not in html
    alert_Text = alert.text
    print(alert_Text)
    assert validate_text in alert_Text
    alert.accept()   # For pressing OK we use this accept()

    #Click on confirm button and then alert popup with 2 option ok and cancel ,this time we press cancel
    driver.find_element_by_css_selector("input[id='name']").send_keys("test")
    time.sleep(5)
    driver.find_element_by_id("confirmbtn")


if __name__ == "__main__":
    main()

