import unittest

from selenium import webdriver


class TestExample(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_title(self):
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()