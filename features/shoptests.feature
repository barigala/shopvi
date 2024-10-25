Feature: Vi Shop Testing

  Scenario Outline: User logs in and navigates through the shop
    Given I open the app and navigate to the mobile number input screen
    When I close the mobile number dialog box
    When I input a valid 10-digit mobile number "<mobile_number>"
    When I click on the send OTP CTA button
    When I input a valid 4-digit OTP "<otp>"
    When I log into the app using login with OTP CTA button
    Then I click on VI Shop from Bottom Navigation and should navigate to the shop Dashboard

  Examples:
    | mobile_number | otp  |
    | 7507233095    | 1234 |


