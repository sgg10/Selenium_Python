import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class AssertionsTest(unittest.TestCase):
  
  def setUp(self):
    self.driver = webdriver.Chrome(executable_path = r'./chromedriver.exe')
    driver = self.driver
    driver.maximize_window()
    driver.get('http://demo-store.seleniumacademy.com/')
    driver.implicitly_wait(15)

  def test_search_field(self):
    self.assertTrue(self.is_element_present(By.NAME, 'q'))

  def test_language_options(self):
    self.assertTrue(self.is_element_present(By.ID, 'select-language'))

  def tearDown(self):
    self.driver.quit()

  def is_element_present(self, how, what):
    try:
      self.driver.find_element(by = how, value = what)
    except NoSuchElementException as variable :
      return False
    return True

if __name__ == '__main__':
  unittest.main(verbosity=2)