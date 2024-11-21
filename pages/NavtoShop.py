import time
from base.BasePage import BasePage
import utils.CustomLogger as cl


class NavtoShop(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values
    _numberInputField = 'enter mobile number'  # text
    _numberDialogBox = "NONE OF THE ABOVE"  # text
    _sendOTP = "send OTP"  # text
    _inputOTP = "login with OTP"  # text
    _shopButton = "shop"  # text


    def ClickNumberInputField(self):
        #This method clicks on the mobile number input field.
        cl.allureLogs("Waiting to click on Mobile Number Input Field")
        self.waitForElement(self._numberInputField, "text")
        self.clickElement(self._numberInputField, "text")
        cl.allureLogs("Clicked on Mobile Number Input Field")
        self.takeScreenshot("Clicked on Mobile Number Input Field")

    def ClickDialogBox(self):
        #This method clicks on the dialog box.
        self.clickElement(self._numberDialogBox, "text")
        cl.allureLogs("Clicked on Dialog Box")
        self.takeScreenshot("Clicked on Dialog Box")

    def inputValidMobileNumber(self, mobile_number):
        #This method validates the mobile number length and inputs the 10-digit mobile number using the sendNumberViaKeypad method.

        if len(mobile_number) == 10 and mobile_number.isdigit():
            cl.allureLogs(f"Entering 10-digit mobile number: {mobile_number}")

            for digit in mobile_number:
                self.sendNumberViaKeypad(digit)
                cl.allureLogs(f"Entered digit: {digit}")
                time.sleep(0.5)  # Optional: Delay to ensure stability between digit inputs

            cl.allureLogs("Mobile number input completed")
            self.takeScreenshot("Entered Mobile Number")
        else:
            cl.allureLogs(f"Invalid mobile number: {mobile_number}. Please enter a valid 10-digit number.")
            raise ValueError("Mobile number must be exactly 10 digits and numeric.")

    def ClickOTPButton(self):
        #This method clicks on the OTP button.
        self.clickElement(self._sendOTP, "text")
        cl.allureLogs("Clicked on OTP button")
        self.takeScreenshot("Clicked on OTP button")

    def inputOTP(self, OTP_number):
        #This method validates the mobile number length and inputs the 4-digit OTP number using the sendNumberViaKeypad method.

        if len(OTP_number) == 4 and OTP_number.isdigit():
            cl.allureLogs(f"Entering 4-digit OTP number: {OTP_number}")

            for digit in OTP_number:
                self.sendOtpViaKeypad(digit)
                cl.allureLogs(f"Entered digit: {digit}")
                time.sleep(0.5)  # Optional: Delay to ensure stability between digit inputs

            cl.allureLogs("OTP number input completed")
            self.takeScreenshot("Entered OTP Number")
        else:
            cl.allureLogs(f"Invalid OTP number: {OTP_number}. Please enter a valid 4-digit number.")
            raise ValueError("OTP number must be exactly 4 digits and numeric.")

    def LoginWOTPButton(self):
        #This method clicks on the Login with OTP button.
        self.clickElement(self._inputOTP, "text")
        cl.allureLogs("Clicked on Login with OTP button")
        self.takeScreenshot("Clicked on Login with OTP button")

    def NavtoShop(self):
        #This method clicks on the Vi Shop button present on Vi App Dashboard
        self.waitForElement(self._shopButton, "text")
        time.sleep(0.5)
        self.clickElement(self._shopButton, "text")
        cl.allureLogs("Clicked on Shop button")
        self.takeScreenshot("Clicked on Shop button")
