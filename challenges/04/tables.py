import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NavigationTest(unittest.TestCase):

  def setUp(self):
    driver = self.driver = webdriver.Chrome(executable_path= r'./chromedriver.exe')
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get('https://the-internet.herokuapp.com/')
    driver.find_element_by_link_text('Sortable Data Tables').click()

  def test_account_link(self):
    driver = self.driver

    data = [[]]*5
    
    for i in range(5):
      header = driver.find_element_by_xpath(f'//*[@id="table1"]/thead/tr/th[{i + 1}]/span')
      data[i].append(header.text)

      for j in range(4):
        cell = driver.find_element_by_xpath(f'//*[@id="table1"]/tbody/tr[{j+1}]/td[{i+1}]')
        data[i].append(cell.text)

    print(data)


  def tearDown(self):
    self.driver.close()

if __name__ == '__main__':
  unittest.main(verbosity=2)