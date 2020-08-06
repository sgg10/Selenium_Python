import unittest
from selenium import webdriver

class RegisterNewUser(unittest.TestCase):

  def setUp(self):
    driver = self.driver = webdriver.Chrome(executable_path = r'../chromedriver.exe')
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get('http://demo-store.seleniumacademy.com')

  def test_new_user(self):
    driver = self.driver
    driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/a/span[2]').click()
    driver.find_element_by_link_text('Log In').click()
    create_account_button = driver.find_element_by_xpath('//*[@id="login-form"]/div/div[1]/div[2]/a/span/span')
    self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
    create_account_button.click()

    #Form
    self.assertTrue('Create New Customer Account' == driver.title)
    first_name = driver.find_element_by_id('firstname')
    middle_name = driver.find_element_by_id('middlename')
    last_name = driver.find_element_by_id('lastname')
    email = driver.find_element_by_id('email_address')
    news_letter_suscription = driver.find_element_by_id('is_subscribed')
    password = driver.find_element_by_id('password')
    confirm_password = driver.find_element_by_id('confirmation')
    submit_button = driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button')
    self.assertTrue(
      first_name.is_enabled() and
      middle_name.is_enabled() and
      last_name.is_enabled() and
      email.is_enabled(),
      news_letter_suscription.is_enabled() and
      password.is_enabled() and
      confirm_password.is_enabled() and
      submit_button.is_enabled()
    )

    # Write data
    first_name.send_keys('Test')
    middle_name.send_keys('Selenium')
    last_name.send_keys('Python')
    email.send_keys('sample@sgg10.com')
    password.send_keys('Test123456')
    confirm_password.send_keys('Test123456')
    submit_button.click()

  def tearDown(self):
    self.driver.implicitly_wait(3)
    self.driver.close()

if __name__ == "__main__":
  unittest.main(verbosity=2)
