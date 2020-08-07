import unittest
from selenium import webdriver
from time import sleep

class DynamicElements(unittest.TestCase):

  def setUp(self):
    driver = self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
    driver.maximize_window()
    driver.get('https://the-internet.herokuapp.com/')
    driver.find_element_by_link_text('Disappearing Elements').click()

  def test_name_elements(self):
    driver = self.driver

    tries = 1
    menu = driver.find_elements_by_xpath('//*[@id="content"]/div/ul/li')
    sleep(2)

    while len(menu) < 5:
      tries += 1
      driver.refresh()
      sleep(2)
      menu = driver.find_elements_by_xpath('//*[@id="content"]/div/ul/li')

    print(f'Number of tries: {tries}')


  def tearDown(self):
    self.driver.close()

if __name__ == '__main__':
  unittest.main(verbosity=2)