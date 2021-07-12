from pages.python_selenium_test_page import AeromexicoCheckinDesktopPagae
import unittest
from selenium import webdriver
from screenshotscode import Screenshots
from logfilecode import Logfile
import HtmlTestRunner
from os.path import dirname, realpath


class Aeromexico(unittest.TestCase):
    """A sample test class to show how page object works"""

    filepath = realpath(__file__)
    basepath = dirname(filepath)
    print(basepath)

    def setUp(self):

        self.driver = webdriver.Chrome()

        driver = self.driver

        driver.maximize_window()

        desktop_url = "https://docs.google.com/forms/d/e/1FAIpQLSfSGh4qzssK1gnZ6JEUe1D4E3lmGCelVD0VZgdHs_y7K_U7rA/viewform"

        driver.get(desktop_url)

    def test_Selenium_form(self):
        """
        Runs the tests. this is what will be getting called by run.py
        """

        driver = self.driver
        #  files Ojects
        Logfile.create_log_file(self)

        AeromexicoDesktopPagaeObj = AeromexicoCheckinDesktopPagae(driver)

        AeromexicoDesktopPagaeObj.google_sign_in_test_cases()

        AeromexicoDesktopPagaeObj.page_title_test_case()

        AeromexicoDesktopPagaeObj.check_Validation_With_negative_test_screen_one()

        AeromexicoDesktopPagaeObj.positive_test_cases()

        AeromexicoDesktopPagaeObj.check_required_field_test_screen_two()

        AeromexicoDesktopPagaeObj.check_required_field_test_screen_third()

        AeromexicoDesktopPagaeObj.check_required_field_test_screen_fourth()

        AeromexicoDesktopPagaeObj.check_required_field_test_screen_fith()

        # AeromexicoDesktopPagaeObj.check_Cnic_validation()

        # Screenshots method
        Screenshots.take_screenshot(self, 'aeromexico')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/asif/PycharmProjects/webautomation/reports'))

