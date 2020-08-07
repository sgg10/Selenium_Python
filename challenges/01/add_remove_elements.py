import unittest
from selenium import webdriver
from time import sleep

class AddRemoveElements(unittest.TestCase):

  def setUp(self):
    driver = self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
    driver.maximize_window()
    driver.get('https://the-internet.herokuapp.com/')
    driver.find_element_by_link_text('Add/Remove Elements').click()

  def test_add_remove(self):
    add = int(input('< Cuantos elementos deseas agregar? '))
    remove = int(input('< Cuantos elementos deseas remover? '))
    total = add - remove

    try:
      while total < 0:
        print('> Intentas borrar mas elementos de los que crearas, intenta de nuevo')
        add = int(input('< Cuantos elementos deseas agregar? '))
        remove = int(input('< Cuantos elementos deseas remover? '))
        total = add - remove

      add_button = self.driver.find_element_by_xpath('//*[@id="content"]/div/button')

      for _ in range (add):
        add_button.click()
        sleep(0.5)

      element_list = self.driver.find_elements_by_class_name('added-manually')
      for _ in range(remove):
        element = element_list.pop(0)
        element.click()
        sleep(0.5)
    except:
      print('> Ha ocurrido un error...')

  def tearDown(self):
    self.driver.close()

if __name__ == '__main__':
  unittest.main(verbosity=2)