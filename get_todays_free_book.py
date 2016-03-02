from time import sleep
from selenium import webdriver

# driver = webdriver.PhantomJS()
driver = webdriver.Firefox()


def click_claim():
    claim_book = driver.find_element_by_xpath(
        '//*[@id="deal-of-the-day"]/div/div/div[2]/div[4]/div[2]/a/div/input'
    )
    claim_book.click()


def go_to_free_learning_page():
    driver.get('https://www.packtpub.com/packt/offers/free-learning')
    driver.find_element_by_xpath('//*[@id="account-bar-login-register"]/a[1]/div').click()
    driver.find_element_by_xpath("id('email')").send_keys("austinhuminski@gmail.com")
    driver.find_element_by_id('password').send_keys('Blue611')

go_to_free_learning_page()
click_claim()
sleep(2)

# Enter in username and password. Submit
# driver.find_element_by_xpath('//*[@id="email"]').click()

driver.find_element_by_id('edit-submit-1').click()

claim_book = driver.find_element_by_xpath(
    '//*[@id="deal-of-the-day"]/div/div/div[2]/div[4]/div[2]/a/div/input'
)
claim_book.click()
