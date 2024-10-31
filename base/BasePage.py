import os
import time
import allure
from allure_commons.types import AttachmentType
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException, \
    TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
import utils.CustomLogger as cl


class BasePage:
    log = cl.customLogger()
    screenshot_counter = 0

    def __init__(self, driver):
        self.driver = driver

    def waitForElement(self, locatorValue, locatorType="id", timeout=25):
        """Wait for an element to be present and return it."""
        locatorType = locatorType.lower()
        wait = WebDriverWait(self.driver, timeout, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])

        element = None
        try:
            if locatorType == "id":
                element = wait.until(lambda x: x.find_element(AppiumBy.ID, locatorValue))
            elif locatorType == "class":
                element = wait.until(lambda x: x.find_element(AppiumBy.CLASS_NAME, locatorValue))
            elif locatorType == "des":
                element = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                              f'UiSelector().description("{locatorValue}")'))
            elif locatorType == "index":
                element = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                              f'new UiSelector().index({int(locatorValue)})'))
            elif locatorType == "text":
                element = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'text("{locatorValue}")'))
            elif locatorType == "xpath":
                element = wait.until(lambda x: x.find_element(AppiumBy.XPATH, locatorValue))
            else:
                self.log.info(f"Invalid locator type: {locatorType}")
            return element
        except Exception as e:
            self.log.error(
                f"Failed to wait for element with locatorType '{locatorType}' and locatorValue '{locatorValue}'. Error: {str(e)}")
            self.takeScreenshot(f"WaitForElementError_{locatorType}_{locatorValue}")
            return None

    def getElement(self, locatorValue, locatorType="id"):
        """Retrieve an element after waiting for it."""
        try:
            element = self.waitForElement(locatorValue, locatorType)
            self.log.info(f"Element found with locatorType '{locatorType}' and locatorValue '{locatorValue}'")
            return element
        except Exception as e:
            self.log.error(
                f"Failed to find element with locatorType '{locatorType}' and locatorValue '{locatorValue}'. Error: {str(e)}")
            return None

    def clickElement(self, locatorValue, locatorType="id"):
        """Click an element after waiting for it."""
        try:
            element = self.getElement(locatorValue, locatorType)
            if element:
                element.click()
                self.log.info(f"Clicked element with locatorType '{locatorType}' and locatorValue '{locatorValue}'")
            else:
                raise Exception("Element not found")
        except Exception as e:
            self.log.error(
                f"Failed to click element with locatorType '{locatorType}' and locatorValue '{locatorValue}'. Error: {str(e)}")
            self.takeScreenshot(f"ClickElementError_{locatorType}_{locatorValue}")
            assert False

    def sendText(self, text, locatorValue, locatorType="id"):
        """Send text to an element."""
        try:
            element = self.getElement(locatorValue, locatorType)
            if element:
                element.clear()
                self.log.info(f"cleared the text field for element with locatorType '{locatorType}' and locatorValue '{locatorValue}'")
                element.send_keys(text)
                self.log.info(f"Sent text '{text}' to element with locatorType '{locatorType}' and locatorValue '{locatorValue}'")
            else:
                raise Exception("Element not found")
        except Exception as e:
            self.log.error(
                f"Failed to send text to element with locatorType '{locatorType}' and locatorValue '{locatorValue}'. Error: {str(e)}")
            self.takeScreenshot(f"SendTextError_{locatorType}_{locatorValue}")
            assert False

    def isDisplayed(self, locatorValue, locatorType="id"):
        """Check if an element is displayed."""
        try:
            element = self.getElement(locatorValue, locatorType)
            if element and element.is_displayed():
                self.log.info(
                    f"Element with locatorType '{locatorType}' and locatorValue '{locatorValue}' is displayed")
                return True
            return False
        except Exception as e:
            self.log.error(
                f"Failed to check display status for element with locatorType '{locatorType}' and locatorValue '{locatorValue}'. Error: {str(e)}")
            self.takeScreenshot(f"IsDisplayedError_{locatorType}_{locatorValue}")
            return False

    def clickKeypadButton(self, digit):
        """Click a button on the keypad by its text."""
        try:
            locatorValue = f'//android.widget.TextView[@text="{digit}"]'
            self.clickElement(locatorValue, "xpath")
            time.sleep(1)
            self.log.info(f"Clicked keypad button with digit '{digit}'")
        except Exception as e:
            self.log.error(f"Failed to click keypad button with digit '{digit}'. Error: {str(e)}")

    def sendNumberViaKeypad(self, number):
        """Send a number via keypad, with a delay for consecutive identical digits."""
        try:
            previous_digit = None
            for digit in str(number):
                if previous_digit == digit:
                    time.sleep(1)
                self.clickKeypadButton(digit)
                previous_digit = digit
            self.log.info(f"Successfully sent number '{number}' via keypad")
        except Exception as e:
            self.log.error(f"Failed to send number '{number}' via keypad. Error: {str(e)}")

    def clickOtpButton(self, digit):
        """Click the OTP button identified by the second occurrence of a digit."""
        try:
            locatorValue = f'(//android.widget.TextView[@text="{digit}"])[2]'
            self.clickElement(locatorValue, "xpath")
            self.log.info(f"Clicked OTP button with digit '{digit}'")
        except Exception as e:
            self.log.error(f"Failed to click OTP button with digit '{digit}'. Error: {str(e)}")

    def sendOtpViaKeypad(self, otp):
        """Send an OTP via keypad, handling repeated digits with a delay."""
        try:
            previous_digit = None
            for digit in str(otp):
                if previous_digit == digit:
                    time.sleep(0.5)
                self.clickOtpButton(digit)
                previous_digit = digit
            self.log.info(f"Successfully sent OTP '{otp}' via keypad")
        except Exception as e:
            self.log.error(f"Failed to send OTP '{otp}' via keypad. Error: {str(e)}")

    def pressBackButton(self):
        """Press the Android back button."""
        try:
            self.driver.press_keycode(4)  # Keycode for the BACK button
            self.log.info("Pressed BACK button")
        except Exception as e:
            self.log.error(f"Failed to press BACK button. Error: {str(e)}")

    def takeScreenshot(self, description):
        """Take a screenshot, save it locally, and attach it to Allure report with numbered filenames."""
        BasePage.screenshot_counter += 1  # Increment the screenshot counter
        filename = f"{BasePage.screenshot_counter:03d}_{description}_{time.strftime('%d_%m_%Y_%H_%M_%S')}.png"  # Add the counter prefix with leading zeros
        screenshotDirectory = "./screenshot"
        screenshotPath = os.path.join(screenshotDirectory, filename)

        try:
            # Ensure the screenshot directory exists
            if not os.path.exists(screenshotDirectory):
                os.makedirs(screenshotDirectory)

            # Save the screenshot and attach it to the Allure report
            self.driver.save_screenshot(screenshotPath)
            allure.attach(self.driver.get_screenshot_as_png(), name=description, attachment_type=AttachmentType.PNG)
            self.log.info(f"Screenshot taken and saved at '{screenshotPath}'")
        except Exception as e:
            self.log.error(f"Failed to take screenshot. Error: {str(e)}")


    def get_page_title(self, locator):
        element = self.driver.find_element(AppiumBy.XPATH, locator)
        title = element.text
        print(f"Page title is: {title}")
        return title

    def check_element(self, locator):
        elements = self.driver.find_elements(AppiumBy.XPATH, locator)
        return len(elements) > 0

    def click_element(self, locator):
        element = self.driver.find_element(AppiumBy.XPATH, locator)
        element.click()
        print("CTA button clicked.")

    def check_text_present(self, locator, expected_text):
        element = self.driver.find_element(AppiumBy.XPATH, locator)
        actual_text = element.text
        return expected_text in actual_text

    def validate_text_displayed(self, locator, expected_text):
        element = self.driver.find_element(AppiumBy.XPATH, locator)
        actual_text = element.text
        assert actual_text == expected_text, f"Expected text '{expected_text}' but got '{actual_text}'"
        print(f"Text '{expected_text}' is displayed correctly.")

    # Method to validate if image is displayed
    def validate_image_displayed(self, locator):
        element = self.driver.find_element(AppiumBy.XPATH, locator)
        is_displayed = element.is_displayed()
        assert is_displayed, "Image is not displayed"
        print("Image is displayed correctly.")

    def verifyTextInField(self, expectedText, locatorValue, locatorType="id"):
        """Verify the displayed text in an input field matches the expected text."""
        try:
            element = WebDriverWait(self.driver, 10).until(
                lambda driver: self.getElement(locatorValue, locatorType)
            )
            actualText = element.get_attribute("text")
            self.log.info(f"Expected text '{expectedText}', found '{actualText}'")
            return actualText == expectedText
        except TimeoutException:
            self.log.error(f"Element not found with locatorType '{locatorType}' and locatorValue '{locatorValue}'")
            self.takeScreenshot(f"VerifyTextError_{locatorType}_{locatorValue}")
            return False
        except Exception as e:
            self.log.error(
                f"Error verifying text in element with locatorType '{locatorType}' and locatorValue '{locatorValue}'. Error: {str(e)}")
            self.takeScreenshot(f"VerifyTextError_{locatorType}_{locatorValue}")
            return False

    def get_scroll_coordinates(self):
        #Returns the start and end coordinates for a scroll gesture based on screen size.
        screen_size = self.driver.get_window_size()  # Get screen size
        width = screen_size['width']
        height = screen_size['height']
        # Define start and end points for the scroll gesture
        start_x = width / 2  # Middle of the screen horizontally
        start_y = height * 0.8  # Near the bottom of the screen vertically
        end_x = width / 2  # Same X coordinate for vertical swipe
        end_y = height * 0.2  # Near the top of the screen vertically

        return start_x, start_y, end_x, end_y

    def scroll(self, max_swipes=10):
        """
        Scrolls down the screen a specified number of times.

        :param max_swipes: Number of swipe attempts (default is 10).
        """
        start_x, start_y, end_x, end_y = self.get_scroll_coordinates()

        for i in range(max_swipes):
            print(f"Scrolling down, swipe attempt {i + 1}")
            self.driver.swipe(start_x, start_y, end_x, end_y, 1000)

    def print_allElements_withScroll(self, element_locators, max_swipes=10):
        """
        Prints all elements on the page, scrolling down if necessary to capture elements
        across a long page.
        :param element_locators: A list of locators for the elements to retrieve.
        :param max_swipes: Number of swipe attempts (default is 10).
        """
        elements_found = set()  # Use a set to store unique elements

        # Iterate through scroll attempts
        for i in range(max_swipes):
            print(f"Scroll attempt {i + 1}")
            for locator in element_locators:
                try:
                    elements = self.driver.find_elements(AppiumBy.XPATH, locator)  # Adjust by locator type
                    for element in elements:
                        text = element.text
                        if text not in elements_found:
                            elements_found.add(text)
                            print(f"Element found: {text}")
                except Exception as e:
                    print(f"Error finding element with locator {locator}: {e}")

            # Scroll down to load more elements
            self.scroll(1)
            time.sleep(0.5)

        if not elements_found:
            print("No elements found on the page.")
        else:
            print(f"Total elements found: {len(elements_found)}")

    def findelement_by_uiautomator(self, uiautomator_string, timeout=10):
        try:
            cl.allureLogs(f"Trying to find element by UIAutomator: {uiautomator_string}")
            element = WebDriverWait(self.driver, timeout).until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, uiautomator_string)
            )
            cl.allureLogs(f"Element found by UIAutomator: {uiautomator_string}")
            return element
        except Exception as e:
            cl.allureLogs(f"Error finding element by UIAutomator: {uiautomator_string} - {str(e)}")
            return None

    def iselement_present_by_uiautomator(self, uiautomator_string, timeout=10):
        try:
            cl.allureLogs(f"Checking if element is present by UIAutomator: {uiautomator_string}")
            WebDriverWait(self.driver, timeout).until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, uiautomator_string)
            )
            cl.allureLogs(f"Element is present by UIAutomator: {uiautomator_string}")
            return True
        except Exception as e:
            cl.allureLogs(f"Element not present by UIAutomator: {uiautomator_string} - {str(e)}")
            return False

    def click_element_by_uiautomator(self, uiautomator_string, timeout=10):
        try:
            cl.allureLogs(f"Trying to click element by UIAutomator: {uiautomator_string}")
            element = WebDriverWait(self.driver, timeout).until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, uiautomator_string)
            )
            element.click()
            cl.allureLogs(f"Element clicked by UIAutomator: {uiautomator_string}")
            return True
        except Exception as e:
            cl.allureLogs(f"Error clicking element by UIAutomator: {uiautomator_string} - {str(e)}")
            return False

    def check_elements_by_uiautomator(self, elements_dict, timeout=10):
        """
        Check the presence of multiple elements provided as a dictionary where
        keys are descriptive names and values are UIAutomator strings.
        Logs the status of each element found or not found.
        """
        for element_name, uiautomator_string in elements_dict.items():
            try:
                element = WebDriverWait(self.driver, timeout).until(
                    lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, uiautomator_string)
                )
                cl.allureLogs(f"Element found: {element_name}")
                print(f"Element found: {element_name}")
            except Exception as e:
                cl.allureLogs(f"Error finding element '{element_name}' with UIAutomator selector: {uiautomator_string}. Error: {str(e)}")
                print(f"Error finding element '{element_name}' with UIAutomator selector: {uiautomator_string}. Error: {str(e)}")
