import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):

  @classmethod # Permite que se cargue todo en una sola ventana, hay que cambiar self por cls
  def setUpClass(cls):
    #return super().setUp()
    cls.driver = webdriver.Chrome(executable_path= r'./chromedriver')
    driver = cls.driver
    driver.implicitly_wait(10)

  def test_hello_world(self):
    driver = self.driver
    driver.get('https://www.platzi.com')

  def test_visit_google(self):
    driver = self.driver
    driver.get('https://www.google.com')

  @classmethod
  def tearDownClass(cls):
    #return super().tearDown()
    cls.driver.quit()

if __name__ == '__main__':
  unittest.main(verbosity=2, testRunner= HTMLTestRunner(output='reportes', report_name='hello-world-report'))