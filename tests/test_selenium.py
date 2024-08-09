import os
import unittest

from selenium import webdriver


class TestExample(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Remote(
            command_executor=os.getenv('SELENIUM_REMOTE_URL', 'http://localhost:4444/wd/hub'),
            options=options
        )


    def test_title(self):
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/"),
        driver.save_screenshot("screenshot/test.png")

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()