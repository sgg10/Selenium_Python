import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner

class HomePageTest(unittest.TestCase):
  
  def setUp(self):
    self.driver = webdriver.Chrome(executable_path = r'./chromedriver.exe')
    driver = self.driver
    driver.maximize_window()
    driver.get('http://demo-store.seleniumacademy.com/')
    driver.implicitly_wait(15)

  def test_search_text_fiel(self):
    self.driver.find_element_by_id('search')

  def test_search_text_fiel_by_name(self):
    self.driver.find_element_by_name('q')

  def test_search_text_fiel_by_class_name(self):
    self.driver.find_element_by_class_name('input-text')

  def test_search_button_enabled(self):
    self.driver.find_element_by_class_name('button')

  def test_count_of_promo_banner_images(self):
    banner_list = self.driver.find_element_by_class_name('promos')
    banners = banner_list.find_elements_by_tag_name('img')
    self.assertEqual(3, len(banners))

  def test_vip_promo(self):
    # El xpath se obtiene en el menu copy al dar click derecho sobre un componente en HTML
    self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[4]/a/img')

  def test_shopping_cart(self):
    self.driver.find_element_by_css_selector('div.header-minicart span.icon')

  def tearDown(self):
    self.driver.quit()

if __name__ == '__main__':
  unittest.main(verbosity=2, testRunner= HTMLTestRunner(output='reportes', report_name='searchTest'))