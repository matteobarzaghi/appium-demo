# Calculator Test Automation with Appium

## Overview
This project demonstrates a simple automated test for an Android Calculator app using Appium and Python's `unittest` framework. The script tests a basic addition operation (`2 + 3 = 5`) to verify the correct functionality of the calculator.

## Prerequisites
Before running this script, ensure you have the following installed and configured:

- **Python 3.x** (Ensure it's added to the system path)
- **Appium Server** (Download and install from [Appium](https://appium.io/))
- **Android SDK & Emulator** (or a physical Android device with debugging enabled)
- **Appium-Python-Client** (Install using `pip install Appium-Python-Client`)
- **Device Setup**: Ensure the emulator or device is running and accessible via `adb`.

## Installation
1. Clone this repository or copy the script to your local machine.
2. Install the required dependencies using:
   ```sh
   pip install -r requirements.txt  # If a requirements file exists
   ```
   Otherwise, install Appium client manually:
   ```sh
   pip install Appium-Python-Client
   ```

## Running the Test
1. Start the Appium server:
   ```sh
   appium
   ```
2. Connect your Android device or start an emulator.
3. Execute the test script:
   ```sh
   python calculator_test.py
   ```

## Test Details
- The script initializes an Appium session targeting an Android Calculator app.
- It interacts with UI elements to perform an addition (`2 + 3`), then asserts that the displayed result is `5`.
- Finally, the test session is terminated.

## Configuration
Modify the `desired_caps` dictionary in `setUp()` to test on different devices or applications:
```python
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "10",
        "deviceName": "emulator-5554",
        "appPackage": "com.android.calculator2",
        "appActivity": ".Calculator",
        "automationName": "UiAutomator2"
    }
```

## Troubleshooting
- **Ensure Appium Server is running** before executing the script.
- **Verify device connectivity** using:
  ```sh
  adb devices
  ```
- If the test fails due to UI element issues, confirm the element IDs using **Appium Inspector**.
- Adjust **timeouts** if necessary, especially for slow devices.

## License
This project is open-source and available under the MIT License.

