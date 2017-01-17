import unittest
from urlparse import urljoin

from selenium import webdriver
from selenium.webdriver import ActionChains

from teamcity import is_running_under_teamcity
from teamcity.unittestpy import TeamcityTestRunner

class AcmeAppTest(unittest.TestCase):
    def setUp(self):
        driver = webdriver.PhantomJS()
        self.url = 'http://localhost:56120'
        driver.get(self.url)
        driver.maximize_window()
        self.driver = driver

    def tearDown(self):
        pass

    def test_about_page(self):
        driver = self.driver
        about_link = driver.find_element_by_xpath('//a[text()="About"]')
        ActionChains(driver).move_to_element(about_link).perform()
        about_link.click()
        self.assertEqual(driver.title, 'About - My ASP.NET Application')

    def test_contact_page(self):
        driver = self.driver
        contact_link = driver.find_element_by_xpath('//a[text()="Contact"]')
        ActionChains(driver).move_to_element(contact_link).perform()
        contact_link.click()
        self.assertEqual(driver.title, 'Contact - My ASP.NET Application')
        addresses = driver.find_elements_by_xpath('//address')
        self.assertEqual(len(addresses), 2)
        self.assertEqual(driver.current_url, urljoin(self.url, "Home/Contact"))

    def test_register_page(self):
        driver = self.driver
        driver.get(urljoin(self.url, 'Account/Register'))
        register_button = driver.find_element_by_xpath('//input[@value="Register"]')
        register_button.click()
        errors = driver.find_element_by_class_name('validation-summary-errors')
        expected_errors = ['the email field is required.', 'the password field is required.']
        received_errors = str(errors.text).lower().split('\n')
        self.assertTrue(set(received_errors).issubset(expected_errors))


if __name__ == '__main__':
    if is_running_under_teamcity():
        runner = TeamcityTestRunner()
    else:
        runner = unittest.TextTestRunner()
    unittest.main(testRunner=runner)