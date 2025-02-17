from appium import webdriver
import unittest
import time

class CalculatorTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "YOUR_DEVICE_VERSION",  # e.g., "10"
            "deviceName": "Android Emulator",            # or the actual device name
            "appPackage": "com.android.calculator2",       # change if testing a different app
            "appActivity": ".Calculator",                # change if testing a different app
            "automationName": "UiAutomator2"
        }
        # Use one of the URLs provided, usually 127.0.0.1 if running locally
        self.driver = webdriver.Remote("http://127.0.0.1:4723", desired_caps)

    def test_addition(self):
        # Example: Test 2 + 3 = 5 in Calculator
        self.driver.find_element("id", "digit_2").click()
        self.driver.find_element("id", "op_add").click()
        self.driver.find_element("id", "digit_3").click()
        self.driver.find_element("id", "eq").click()

        time.sleep(1)  # Wait for the result to appear

        result = self.driver.find_element("id", "result").text
        self.assertEqual(result, "5", "Expected result of 2 + 3 is 5")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
