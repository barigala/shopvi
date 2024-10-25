import time
from behave import given, when, then
from pages.NavtoShop import NavtoShop

@given('I open the app and navigate to the mobile number input screen')
def step_open_app_and_navigate(context):
    context.navtoshop = NavtoShop(context.driver)
    context.navtoshop.ClickNumberInputField()

@when('I close the mobile number dialog box')
def step_confirm_number_in_dialog(context):
    context.navtoshop.ClickDialogBox()

@when('I input a valid 10-digit mobile number "{mobile_number}"')
def step_input_mobile_number(context, mobile_number):
    context.navtoshop.inputValidMobileNumber(mobile_number)

@when('I click on the send OTP CTA button')
def step_click_otp_button(context):
    context.navtoshop.ClickOTPButton()

@when('I input a valid 4-digit OTP "{otp}"')
def step_input_otp(context, otp):
    context.navtoshop.inputOTP(otp)

@when('I log into the app using login with OTP CTA button')
def step_log_in_with_otp(context):
    context.navtoshop.LoginWOTPButton()

@then('I click on VI Shop from Bottom Navigation and should navigate to the shop Dashboard')
def step_navigate_to_shop(context):
    context.navtoshop.NavtoShop()
