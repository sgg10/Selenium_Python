import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DynamicControls(unittest.TestCase):

  def setUp(self):
    driver = self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
    driver.maximize_window()
    driver.get('https://the-internet.herokuapp.com/')
    driver.find_element_by_link_text('Dynamic Controls').click()

  def test_name_elements(self):
    driver = self.driver

    checkbox = driver.find_element_by_css_selector('#checkbox > input[type=checkbox]')
    checkbox.click()

    remove_add_button = driver.find_element_by_css_selector('#checkbox-example > button')
    remove_add_button.click()

    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkbox-example > button')))
    remove_add_button.click()

    enable_disable_button = driver.find_element_by_xpath('//*[@id="input-example"]/button')
    enable_disable_button.click()

    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input-example"]/input')))
    text_box = driver.find_element_by_xpath('//*[@id="input-example"]/input')
    text_box.send_keys('Hello World')
    enable_disable_button.click()



  def tearDown(self):
    self.driver.close()

if __name__ == '__main__':
  unittest.main(verbosity=2)