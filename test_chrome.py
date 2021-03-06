import os
import unittest
import time
from selenium import webdriver


class ChromeTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # get the path of ChromeDriver
        dir = os.getenv('ChromeWebDriver')
        driver = os.path.join(dir, 'chromedriver.exe')
        cls.browser = webdriver.Chrome(executable_path=driver)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    def testGoogle(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)
        time.sleep(2)

    def testBing(self):
        self.browser.get('http://www.bing.com')
        self.assertIn('Bing', self.browser.title)
        time.sleep(2)

    def testYahoo(self):
        self.browser.get('http://www.yahoo.com')
        self.assertIn('Yahoo', self.browser.title)

    def testOutlook(self):
        self.browser.get('http://www.outlook.com')
        self.assertIn('Sign in to your Microsoft account', self.browser.title)
        time.sleep(2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
