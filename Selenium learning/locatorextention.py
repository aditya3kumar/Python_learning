
from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\\Users\\aditya kumar\\PycharmProjects\\chromedriver.exe")

#open firefox browser

# driver = webdriver.Firefox(executable_path="C:\\Users\\aditya kumar\\PycharmProjects\\geckodriver.exe")

#  open the url
driver.get("https://login.salesforce.com/?locale=in")

# to create or generate css by ID only
  # enter username

driver.find_element_by_css_selector("#username").send_keys('CSS by ID')
   #enter password

driver.find_element_by_css_selector(".password").send_keys('testing123')

# clear the enter password by using clear()

driver.find_element_by_css_selector(".password").clear()


# by using linktext go to forget password

driver.find_element_by_link_text("Forgot Your Password?").click()

# generating xpath on basis of text only
    # //tagname[text()='xxx']
        # after forget password page we need to click cancel

driver.find_element_by_xpath("//a[text()='Cancel']").click()



# same flow we are using for XPATH and CSS parenting child

#enter username
#  user name find through parent child xpath

driver.find_element_by_xpath("//form[@name='login']/div[1]/div[1]/input[1]").send_keys('Parent xpath')

#enter password

# password through css  parenting child

print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(1)").text)

print(driver.find_element_by_xpath("//form[@name='login']/label[1]").text)
#//*[contains(@class,'input r4 wide mb16 mt8 username')]


