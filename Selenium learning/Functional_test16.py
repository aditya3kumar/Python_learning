#We verify the scenario of greenkart application
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\aditya kumar\\PycharmProjects\\chromedriver.exe")
#Search the vegetablestarts with 'CA' word which show results of 4 veggies and hit the search button
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(6)
driver.find_element_by_css_selector("input.search-keyword").send_keys("ca")
driver.find_element_by_css_selector("button.search-button").click()

#Case 1 - Verifying  or validating whether products selected in page 1 are same in page 2 at checkout
#Case 2 - Verifying Price decreases after discout applied in total amount
#Case 3 - Verify if sum of products in check out page matches with total amount

# adding all veggies to cart ,click on add cart button of all veggies
add_carts=driver.find_elements_by_xpath("//div[@class='product-action']/button")
list_addcart=[]
for add_cart in add_carts:
    add_cart.click()
# We use to fetch veggie names from add cart element only by using xpath transverse from child to parent technique only otherwise we need to use for loop again to fetch name of veggie.
#//div[@class='product-action']/button/parent::div/parent::div/h4" this total xpath ,till button is for add car button from there we do child to parent tansverse so we start from parent keyword only.
    list_addcart.append(add_cart.find_element_by_xpath("parent::div/parent::div/h4").text)
print(list_addcart)
driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
originalamt=float(driver.find_element_by_css_selector("span.discountAmt").text)
driver.find_element_by_css_selector("input.promocode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector("button.promoBtn").click()
# Fetching veggie name in checkout page
veggie_checkout=[]
veggie_names=driver.find_elements_by_xpath("//p[@class='product-name']")
for veggie_name in veggie_names:
    veggie_checkout.append(veggie_name.text)
print(veggie_checkout)
assert list_addcart==veggie_checkout #case 1 validation
print("Case 1 Passed")

promo=driver.find_element_by_css_selector("span.promoInfo").text
if "Code applied ..!" == promo:
    discount_amt=float(driver.find_element_by_css_selector("span.discountAmt").text)
    assert (originalamt > discount_amt)
    print("Case 2 passed")
else:
    promocode=driver.find_element_by_css_selector("input.promocode").get_property('value')
    print(promocode,'is',promo,',please use valid coupon')
# Case 3 validation
total_amt_checkout=float(driver.find_element_by_css_selector("span.totAmt").text)
sum=0
list_amount=[]

Total_amounts=driver.find_elements_by_xpath("//table[@class='cartTable']/tr/td[5]/p")
for total_amount in Total_amounts:
    list_amount.append(float(total_amount.text))
    sum=sum+float(total_amount.text)
print(sum)
print(list_amount,total_amt_checkout)
assert total_amt_checkout==sum
print('Case 3 Passed')


