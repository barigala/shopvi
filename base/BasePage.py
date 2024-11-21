import os
import time
import allure
from allure_commons.types import AttachmentType
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException, \
    TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
import utils.CustomLogger as cl
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.actions.pointer_input import PointerInput



class BasePage:
    log = cl.customLogger()
    screenshot_counter = 0

    def __init__(self, driver):
        self.driver = driver

    def waitForElement(self, locatorValue, locatorType="id", timeout=25):
        """
        Waits for an element to be present on the screen based on locator type and value.
        Difference: Uses various locator strategies like ID, class, description, etc., to find elements.
        Usage: Use this to ensure an element is present before interacting with it, reducing the chance of errors from elements not loading in time.
        """
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
        """
        Retrieves an element after waiting for it to be present.
        Difference: uses `waitForElement` internally.
        Usage:Use this when you need to retrieve an element for further actions (e.g., clicking, sending text).
        """
        try:
            element = self.waitForElement(locatorValue, locatorType)
            self.log.info(f"Element found with locatorType '{locatorType}' and locatorValue '{locatorValue}'")
            return element
        except Exception as e:
            self.log.error(
                f"Failed to find element with locatorType '{locatorType}' and locatorValue '{locatorValue}'. Error: {str(e)}")
            return None

    def clickElement(self, locatorValue, locatorType="id"):
        """
        Clicks an element after waiting for it to be present.
        Difference: Combines `getElement` and `.click()`.
        Usage: Use this to perform click actions on elements, handling waiting internally.
        """
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
        """
        Sends input text to an element, clearing any existing text.
        Difference: Clears text before sending new input.
        Usage: Use this for input fields where text might need to be cleared first.
        """
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
        """
        Checks if an element is visible on the screen.
        Difference: Uses `getElement` and `.is_displayed()`.
        Usage: Use to verify that an element is visible before interacting with it.
        """
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
        """
        Clicks a specific button on an on-screen keypad by its text value.
        Difference: Focuses on keypad interactions.
        Usage: Use for numeric inputs where buttons appear on a keypad (e.g., entering PINs).
        """
        try:
            locatorValue = f'//android.widget.TextView[@text="{digit}"]'
            self.clickElement(locatorValue, "xpath")
            time.sleep(1)
            self.log.info(f"Clicked keypad button with digit '{digit}'")
        except Exception as e:
            self.log.error(f"Failed to click keypad button with digit '{digit}'. Error: {str(e)}")

    def sendNumberViaKeypad(self, number):
        """
        Sends a number by clicking on individual digits on a keypad with a delay between consecutive identical digits.
        Difference: Uses delays for repeated digits.
        Usage: Use to input multi-digit numbers like phone numbers via keypad, especially when consecutive digits are present.
        """
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
        """
        Clicks an OTP button on the keypad based on a specific digit's position.
        Difference: Clicks second occurrence of a digit.
        Usage: Use when needing to distinguish between repeated digits, often in OTP entry fields where each digit has multiple entries.
        """
        try:
            locatorValue = f'(//android.widget.TextView[@text="{digit}"])[2]'
            self.clickElement(locatorValue, "xpath")
            self.log.info(f"Clicked OTP button with digit '{digit}'")
        except Exception as e:
            self.log.error(f"Failed to click OTP button with digit '{digit}'. Error: {str(e)}")

    def sendOtpViaKeypad(self, otp):
        """
        Sends an OTP via keypad, handling repeated digits with delays.
        Difference:Focuses on OTPs with repeated digits.
        Usage: Use to enter OTP codes, especially if digits might repeat consecutively.
        """
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


    def takeScreenshot(self, description):
        """
        Takes a screenshot, saves it with a unique name, and attaches it to Allure reports.
        Usage: Use to capture the screen for error/debugging purposes, particularly in test reporting.
        """
        BasePage.screenshot_counter += 1  # Increment the screenshot counter
        filename = f"{BasePage.screenshot_counter:03d}_{description}_{time.strftime('%d_%m_%Y_%H_%M_%S')}.png"  # Add the counter prefix with leading zeros
        screenshotDirectory = "./tests/screenshot"
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
        """
        Retrieves and prints the title text from a page element using a locator.
        Usage: Use for validating page titles or headers when navigation or loading new screens.
        """
        element = self.driver.find_element(AppiumBy.XPATH, locator)
        title = element.text
        print(f"Page title is: {title}")
        return title

    def check_element(self, locator):
        """
        Checks if elements exist based on a given locator by counting the number of matching elements.
        Difference: Uses `.find_elements()` instead of waiting for one specific element.
        Usage: Useful for checking if any elements matching the locator exist.
        """
        elements = self.driver.find_elements(AppiumBy.XPATH, locator)
        return len(elements) > 0

    def click_element(self, locator):
        """
        Clicks an element directly based on its locator without waiting.
        Difference: No waiting mechanism.
        Usage: Use when certain the element is already loaded; otherwise, consider `clickElement`.
        """
        element = self.driver.find_element(AppiumBy.XPATH, locator)
        element.click()
        print("CTA button clicked.")

    def check_text_present(self, locator, expected_text):
        """
        Verifies if a specific text is present within an element.
        Usage: Use to validate if an element's text content includes the expected text.
        """
        element = self.driver.find_element(AppiumBy.XPATH, locator)
        actual_text = element.text
        return expected_text in actual_text


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
            self.log.error(f"Error verifying text in element with locatorType '{locatorType}' and locatorValue '{locatorValue}'. Error: {str(e)}")
            self.takeScreenshot(f"VerifyTextError_{locatorType}_{locatorValue}")
            return False

    def findelement_by_uiautomator(self, uiautomator_string, timeout=10):
        """
        Searches for an element using a UIAutomator string within a specified timeout period.
        If the element is found, it returns the element; otherwise, logs an error and returns None.
        """
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
        """
        Check if an element is present using a UIAutomator string within a specified timeout period.
        Returns True if the element is found, False otherwise.
        """
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
        """
        Attempts to click an element located using a UIAutomator string within the specified timeout.
        Returns True if the click action succeeds, and logs the action; otherwise, logs an error and returns False.
        """
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

