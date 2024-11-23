import time
import pytest
import unittest
from pages.NavtoShop import NavtoShop
from pages.accountPage import AccountPage
from pages.ShopDashboard import ShopDashboard
from pages.Search import SearchPage
from base.DriverClass import Driver
import utils.CustomLogger as cl
import allure
from config.test_data import MOBILE_NUMBER, OTP_CODE, SEARCH_KEYWORDS

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class ShopTest(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.nav_to_shop = NavtoShop(self.driver)
        self.account_page = AccountPage(self.driver)
        self.shop_dashboard = ShopDashboard(self.driver)
        self.search_page = SearchPage(self.driver)


    @pytest.mark.sanity
    @pytest.mark.prod
    @pytest.mark.order(1)
    def test_click_number_input_field(self):
        print("Now Running test_click_number_input_field")
        cl.allureLogs("Navigation to Mobile number input field")
        self.nav_to_shop.ClickNumberInputField()
        cl.allureLogs("Navigation to Mobile number input field successfully completed")


    @pytest.mark.sanity
    @pytest.mark.prod
    @pytest.mark.order(2)
    def test_click_dialog_box(self):
        print("Now Running test_click_dialog_box")
        cl.allureLogs("Dialog box clicked")
        self.nav_to_shop.ClickDialogBox()
        cl.allureLogs("Dialog box clicked successfully")


    @pytest.mark.sanity
    @pytest.mark.prod
    @pytest.mark.order(3)
    def test_input_valid_mobile_number(self):
        #mobile_number = "7507233095"
        print("Now Running test_input_valid_mobile_")
        cl.allureLogs("Inputting valid mobile number: {}".format(MOBILE_NUMBER))
        self.nav_to_shop.inputValidMobileNumber(MOBILE_NUMBER)
        cl.allureLogs("Inputting valid mobile number successfully completed")


    @pytest.mark.sanity
    @pytest.mark.prod
    @pytest.mark.order(4)
    def test_click_otp_button(self):
        print("Now running test_click_otp_button")
        cl.allureLogs("Clicking OTP button")
        self.nav_to_shop.ClickOTPButton()
        cl.allureLogs("Clicking OTP button successfully completed")


    @pytest.mark.sanity
    @pytest.mark.prod
    @pytest.mark.order(5)
    def test_input_otp(self):
        #otp = "1234"
        print("Now Running test_input_otp")
        cl.allureLogs("Inputting OTP: {}".format(OTP_CODE))
        self.nav_to_shop.inputOTP(OTP_CODE)
        cl.allureLogs("Inputting OTP successfully completed")


    @pytest.mark.sanity
    @pytest.mark.prod
    @pytest.mark.order(6)
    def test_click_login_w_otp_button(self):
        print("Now Running test_click_login_w_otp_button")
        cl.allureLogs("Clicking Login with OTP button")
        self.nav_to_shop.LoginWOTPButton()
        cl.allureLogs("Clicking Login with OTP button successfully completed")

    @pytest.mark.sanity
    @pytest.mark.prod
    @pytest.mark.order(7)
    def test_nav_to_shop(self):
        print("TC1: Navigate to Vi Shop")
        cl.allureLogs("Navigating to shop page")
        self.nav_to_shop.NavtoShop()
        cl.allureLogs(" Succesfully navigated to Vi Shop Dashboard")


    @pytest.mark.sanity
    @pytest.mark.order(8)
    def test_shopDashboard(self):
        cl.allureLogs("Checking available elements in shop dashboard")
        print("TC2: All available elements on shop dashboard")
        self.shop_dashboard.print_allitems_onDashBoard1()
        self.shop_dashboard.print_allitems_onDashBoard2()
        cl.allureLogs("Found all available elements")

    @pytest.mark.prod
    @pytest.mark.order(9)
    def test_shopDashboard(self):
        cl.allureLogs("Checking available elements in shop dashboard")
        print("TC2: All available elements on shop dashboard")
        self.shop_dashboard.print_allitems_onDashBoard1()
        self.shop_dashboard.print_allitems_onDashBoard2Prod()
        cl.allureLogs("Found all available elements")


    @pytest.mark.sanity
    @pytest.mark.prod
    @pytest.mark.order(10)
    def test_DealsPage(self):
        cl.allureLogs("Navigation & Checking all available elements in Deals Page")
        print("TC3: Verify the navigation and all the elements present in Deals Page")
        self.shop_dashboard.NavtoDeals()
        self.shop_dashboard.print_allitems_onDealsPage()
        cl.allureLogs("Found all available elements in Deals Page")


    @pytest.mark.sanity
    @pytest.mark.prod
    @pytest.mark.order(11)
    def test_ExplorePage(self):
        cl.allureLogs("Navigation & Checking all available elements in Explore Page")
        print("TC4: Verify the navigation and all the elements present in Explore Page")
        self.shop_dashboard.NavtoExplore()
        self.shop_dashboard.print_allitems_onExplorePage()
        cl.allureLogs("Found all available elements in Explore Page")


    @pytest.mark.sanity
    @pytest.mark.prod
    @pytest.mark.order(12)
    def test_MenuUnder_ShopDashboard(self):
        cl.allureLogs("Navigating to menus under Shop Dashboard")
        print("TC6: Verify all the options available in Shop Dashboard")
        self.shop_dashboard.NavtoShopDashBoard()
        self.shop_dashboard.ShopDashboard_elements()
        cl.allureLogs("Found all available elements under Shop Dashboard")


    @pytest.mark.sanity
    @pytest.mark.prod
    @pytest.mark.order(13)
    def test_AccountsPage(self):
        cl.allureLogs("Finding all Sections in Accounts Page")
        print("TC7: Verify all the sections available in Accounts Page")
        self.account_page.ClickaccountButton()
        self.account_page.VerifyandPrint_allitems_onAccountPage()
        cl.allureLogs("Found all available sections in Accounts Page")


    @pytest.mark.sanity
    @pytest.mark.prod
    @pytest.mark.order(14)
    def test_SavPaymentsPage(self):
        print("TC9: Validate Saved Payments page")
        cl.allureLogs("Validating Saved Payments page")
        self.account_page.NavSavdPay()
        expected_title = "manage payment options"
        expected_text = "nothing saved yet"
        cta_button_locator = "//android.widget.TextView[@text='go back']"
        # Navigate to the page and validate elements
        self.account_page.Savdpay_page(expected_title, expected_text, cta_button_locator)
        cl.allureLogs("Succesfully Validated Saved Payments Page")


    @pytest.mark.sanity
    @pytest.mark.prod
    @pytest.mark.order(15)
    def test_savingsBanner(self):
        print("TC10: Verify the Savings Banner")
        cl.allureLogs("Verifying Savings Banner")
        self.account_page.VerifyTotalSavings_Banner()
        cl.allureLogs("Savings Banner verified successfully")


    @pytest.mark.sanity
    @pytest.mark.prod
    @pytest.mark.order(16)
    def test_FAQPage(self):
        print("TC11: Verify FAQ page")
        cl.allureLogs("Verifying FAQ page")
        self.account_page.NavFAQ()
        self.account_page.VerifyandPrint_allElements_under_FAQpage()
        self.driver.press_keycode(4)
        cl.allureLogs("Succesfully Validated FAQ Page")


    @pytest.mark.sanity
    @pytest.mark.prod
    @pytest.mark.order(17)
    def test_myOrdersPage(self):
        print("TC12: Verify My Orders page")
        cl.allureLogs("Verifying My Orders page")
        self.account_page.NavOrders()
        self.account_page.VerifyandPrint_allElements_under_myOrderspage1()
        self.account_page.VerifyandPrint_allElements_under_myOrderspage2()
        self.driver.press_keycode(4)
        cl.allureLogs("Succesfully Validated My Orders Page")


    @pytest.mark.sanity
    @pytest.mark.prod
    @pytest.mark.order(18)
    def test_CCPage(self):
        print("TC13: Verify Credit Card page")
        cl.allureLogs("Verifying Credit Card page")
        self.account_page.NavCC()
        self.account_page.VerifyandPrint_allElements_under_CCspage()
        self.driver.press_keycode(4)
        cl.allureLogs("Succesfully Validated Credit Card Page")


    @pytest.mark.sanity
    @pytest.mark.prod
    @pytest.mark.order(19)
    def test_CouponsPage(self):
        print("TC14: Verify Coupons page")
        cl.allureLogs("Verifying Coupons page")
        self.account_page.NavCoupons()
        self.account_page.VerifyandPrint_allElements_under_CouponsPage()
        self.driver.press_keycode(4)
        cl.allureLogs("Succesfully Validated Coupons Page")


    @pytest.mark.sanity
    @pytest.mark.prod
    @pytest.mark.order(20)
    def test_ProfilePage(self):
        print("TC15: Verify Profile page")
        cl.allureLogs("Verifying Profile page")
        self.account_page.NavProfilePage()
        self.account_page.VerifyandPrintallElements_underProfilePage1()
        self.account_page.VerifyandPrintallElements_underProfilePage2()
        self.driver.press_keycode(4)
        self.driver.press_keycode(4)
        cl.allureLogs("Succesfully Validated Profile Page")


    @pytest.mark.sanity
    @pytest.mark.prod
    @pytest.mark.order(21)
    def test_searchPage(self):
        print("Now Running test_searchPage")
        cl.allureLogs("Verifying Search Page")
        self.search_page.NavtoSearch()
        self.search_page.VerifyandPrint_allitems_onSearchPage1()
        self.search_page.VerifyandPrint_allitems_onSearchPage2()
        cl.allureLogs("Verified all items on Search Page")


    @pytest.mark.sanity
    @pytest.mark.prod
    @pytest.mark.order(22)
    def test_Inputsearch(self):
        print("Now Running test_Inputsearch")
        cl.allureLogs("Verifying Search Page")
        self.search_page.SearchProduct(SEARCH_KEYWORDS[1])
        cl.allureLogs("Inputting valid Product ID successfully completed")
        print("Validating Input Search Text")
        cl.allureLogs("Verify the input text")
        assert self.search_page.verifySearchDisplayedText(SEARCH_KEYWORDS[1])
        cl.allureLogs("Input Search Text validated successfully")

    @pytest.mark.sanity
    @pytest.mark.prod
    @pytest.mark.order(23)
    def test_ClickonASearchResult(self):
        #self.search_page.click_on_first_search_result()
        #cl.allureLogs("Clicked on Search Result")
        #print("Navigating to Product Details Page")

        x_coordinate = 470
        y_coordinate = 805

        print("Now Running test_TouchClickOnSearchResult")
        cl.allureLogs("Testing Touch Click on Search Result Element")
        time.sleep(5)

        # Perform the touch click using the method defined in SearchPage
        #self.search_page.touch_click_element(x_coordinate, y_coordinate)
        self.search_page.tap_middle_above_screen()
        self.search_page.tap_middle_above_screen()
        self.search_page.tap_middle_above_screen()
        self.search_page.tap_middle_above_screen()

        time.sleep(5)
        # Add assertions as needed for post-click validation
        # Example: Verifying if expected element appears after touch click
        #assert self.search_page.verifySearchDisplayedText("Expected Text"), "Expected text not displayed after touch click."
        cl.allureLogs("Touch click action completed successfully")







if __name__ == "__main__":
    unittest.main()
