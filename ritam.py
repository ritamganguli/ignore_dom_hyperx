import unittest

from selenium import webdriver
import os


username = "shubhamr"  # Replace the username
access_key = "dl8Y8as59i1YyGZZUeLF897aCFvIDmaKkUU1e6RgBmlgMLIIhh"  # Replace the access key


class FirstSampleTest(unittest.TestCase):
    # Generate capabilities from here: https://www.lambdatest.com/capabilities-generator/
    # setUp runs before each test case and
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        option = {
            "build": 'PyunitTest sample build',  # Change your build name here
            "name": 'Py-unittest',  # Change your test name here
            "browserName": 'Safari',
            "version": 'latest',
            "platform": os.environ.get("TARGET_OS"),
            "network": 'true',  # Enable or disable network logs
            "smartUI.project": "HyperX_racv_1",
             "smartUI.build" : "buildName",
             "selenium_version": "4.0.0"
        }
        chrome_options.set_capability("LT:Options", option)
        self.driver = webdriver.Remote(
            command_executor="https://{}:{}@hub.lambdatest.com/wd/hub".format(
                username, access_key),
            options = chrome_options
        )
    # tearDown runs after each test case

    def tearDown(self):
        self.driver.quit()

    # """ You can write the test cases here """
    def test_unit_user_should_able_to_add_item(self):
        # try:
        driver = self.driver

        # Url
        driver.get("https://lambdatest.com")
        print("Taking screenshot")
        # script = """smartui.takeFullPageScreenshot, {
        #         "screenshotName": "Ritam_12",
        #         "smartScroll": true,
        #         "ignoreDOM": {"xpath": ["/html/body/div[1]/div[1]/section[1]"]}
        #     }"""
        # driver.execute_script(script)

        config = {
            "screenshotName": "Ignore-XPath",
            "fullPage": False,  # Set to True for full-page screenshots in Chrome
            "smartScroll": True,
            "ignoreDOM": {
                "xpath": ["/html/body/div[1]/div[1]/section[1]"],  # Ignoring elements by XPath
            },
        }
        driver.execute_script("smartui.takeScreenshot", config)
        print("screenshot taken successfully")


if __name__ == "__main__":
    unittest.main()