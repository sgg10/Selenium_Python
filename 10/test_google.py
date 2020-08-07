import unittest
from selenium import webdriver
from google_page import GooglePage

class CompareProducts(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    cls.driver = webdriver.Chrome(executable_path = r'./chromedriver.exe')

  def test_google(self):
    google = GooglePage(self.driver)
    google.open()
    google.search('platzi')

    self.assertEqual('platzi', google.keyword)

  @classmethod
  def tearDownClass(cls):
    cls.driver.close()

if __name__ == "__main__":
  unittest.main(verbosity=2)