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

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class ShopTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.nav_to_shop = NavtoShop(self.driver)
        self.account_page = AccountPage(self.driver)
        self.shop_dashboard = ShopDashboard(self.driver)
        self.search_page = SearchPage(self.driver)

    @pytest.mark.order(1)
    def test_click_number_input_field(self):
        print("Now Running test_click_number_input_field")
        cl.allureLogs("Navigation to Mobile number input field")
        self.nav_to_shop.ClickNumberInputField()
        cl.allureLogs("Navigation to Mobile number input field successfully completed")

    @pytest.mark.order(2)
    def test_click_dialog_box(self):
        print("Now Running test_click_dialog_box")
        cl.allureLogs("Dialog box clicked")
        self.nav_to_shop.ClickDialogBox()
        cl.allureLogs("Dialog box clicked successfully")

    @pytest.mark.order(3)
    def test_input_valid_mobile_number(self):
        mobile_number = "7507233095"
        print("Now Running test_input_valid_mobile_")
        cl.allureLogs("Inputting valid mobile number: {}".format(mobile_number))
        self.nav_to_shop.inputValidMobileNumber(mobile_number)
        cl.allureLogs("Inputting valid mobile number successfully completed")

    @pytest.mark.order(4)
    def test_click_otp_button(self):
        print("Now running test_click_otp_button")
        cl.allureLogs("Clicking OTP button")
        self.nav_to_shop.ClickOTPButton()
        cl.allureLogs("Clicking OTP button successfully completed")

    @pytest.mark.order(5)
    def test_input_otp(self):
        otp = "1234"
        print("Now Running test_input_otp")
        cl.allureLogs("Inputting OTP: {}".format(otp))
        self.nav_to_shop.inputOTP(otp)
        cl.allureLogs("Inputting OTP successfully completed")

    @pytest.mark.order(6)
    def test_click_login_w_otp_button(self):
        print("Now Running test_click_login_w_otp_button")
        cl.allureLogs("Clicking Login with OTP button")
        self.nav_to_shop.LoginWOTPButton()
        cl.allureLogs("Clicking Login with OTP button successfully completed")

    @pytest.mark.order(7)
    def test_nav_to_shop(self):
        print("TC1: Navigate to Vi Shop")
        cl.allureLogs("Navigating to shop page")
        self.nav_to_shop.NavtoShop()
        cl.allureLogs(" Succesfully navigated to Vi Shop Dashboard")

    @pytest.mark.order(8)
    def test_shopDashboard(self):
        cl.allureLogs("Checking available elements in shop dashboard")
        print("TC2: All available elements on shop dashboard")
        self.shop_dashboard.print_allitems_onDashBoard()
        cl.allureLogs("Found all available elements")

    @pytest.mark.order(9)
    def test_DealsPage(self):
        cl.allureLogs("Navigation & Checking all available elements in Deals Page")
        print("TC3: Verify the navigation and all the elements present in Deals Page")
        self.shop_dashboard.NavtoDeals()
        self.shop_dashboard.print_allitems_onDealsPage()
        cl.allureLogs("Found all available elements in Deals Page")

    @pytest.mark.order(10)
    def test_ExplorePage(self):
        cl.allureLogs("Navigation & Checking all available elements in Explore Page")
        print("TC4: Verify the navigation and all the elements present in Explore Page")
        self.shop_dashboard.NavtoExplore()
        self.shop_dashboard.print_allitems_onExplorePage()
        cl.allureLogs("Found all available elements in Explore Page")

    @pytest.mark.order(11)
    def test_myOrdersPage(self):
        cl.allureLogs("Navigation & Checking all available elements in My Orders Page")
        print("TC5: Verify the navigation and all the elements present in My Orders Page")
        self.shop_dashboard.NavtoMyOrders()
        self.shop_dashboard.print_allitems_onMyOrders()
        cl.allureLogs("Found all available elements in My Orders Page")

    @pytest.mark.order(12)
    def test_MenuUnder_ShopDashboard(self):
        cl.allureLogs("Navigating to menus under Shop Dashboard")
        print("TC6: Verify all the options available in Shop Dashboard")
        self.shop_dashboard.NavtoShopDashBoard()
        self.shop_dashboard.ShopDashboard_elements()
        cl.allureLogs("Found all available elements under Shop Dashboard")

    @pytest.mark.order(13)
    def test_AccountsPage(self):
        cl.allureLogs("Finding all Sections in Accounts Page")
        print("TC7: Verify all the sections available in Accounts Page")
        self.account_page.ClickaccountButton()
        self.account_page.VerifyandPrint_allitems_onAccountPage()
        cl.allureLogs("Found all available sections in Accounts Page")


    @pytest.mark.order(14)
    def test_NavPagesinAccountPage(self):
        cl.allureLogs("Navigation across sections inside Accounts Page")
        print("TC8: Verify the navigation to credit cards page")
        self.account_page.NavCC()
        time.sleep(1)
        self.driver.press_keycode(4)  # Keycode for the BACK button
        self.account_page.NavCoupons()
        time.sleep(1)
        self.driver.press_keycode(4)
        self.account_page.NavOrders()
        time.sleep(1)
        self.driver.press_keycode(4)
        self.account_page.NavSavdPay()
        time.sleep(1)
        self.driver.press_keycode(4)
        self.account_page.NavHelpandSupport()
        time.sleep(1)
        self.driver.press_keycode(4)
        self.account_page.NavFAQ()
        time.sleep(1)
        self.driver.press_keycode(4)
        self.account_page.NavTandC()
        time.sleep(1)
        self.driver.press_keycode(4)
        self.account_page.NavPrivacyPolicy()
        time.sleep(1)
        self.driver.press_keycode(4)
        self.account_page.NavAboutUS()
        time.sleep(1)
        self.driver.press_keycode(4)


    @pytest.mark.order(15)
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

    @pytest.mark.order(16)
    def test_savingsBanner(self):
        print("TC10: Verify the Savings Banner")
        cl.allureLogs("Verifying Savings Banner")
        self.account_page.VerifyTotalSavings_Banner()
        cl.allureLogs("Savings Banner verified successfully")

    @pytest.mark.order(17)
    def test_FAQPage(self):
        print("TC11: Verify FAQ page")
        cl.allureLogs("Verifying FAQ page")
        self.account_page.NavFAQ()
        self.account_page.VerifyandPrint_allElements_under_FAQpage()
        self.driver.press_keycode(4)
        cl.allureLogs("Succesfully Validated FAQ Page")

    @pytest.mark.order(18)
    def test_myOrdersPage(self):
        print("TC12: Verify My Orders page")
        cl.allureLogs("Verifying My Orders page")
        self.account_page.NavOrders()
        self.account_page.VerifyandPrint_allElements_under_myOrderspage()
        self.driver.press_keycode(4)
        cl.allureLogs("Succesfully Validated My Orders Page")

    @pytest.mark.order(19)
    def test_CCPage(self):
        print("TC13: Verify Credit Card page")
        cl.allureLogs("Verifying Credit Card page")
        self.account_page.NavCC()
        self.account_page.VerifyandPrint_allElements_under_CCspage()
        self.driver.press_keycode(4)
        cl.allureLogs("Succesfully Validated Credit Card Page")

    @pytest.mark.order(20)
    def test_CouponsPage(self):
        print("TC14: Verify Coupons page")
        cl.allureLogs("Verifying Coupons page")
        self.account_page.NavCoupons()
        self.account_page.VerifyandPrint_allElements_under_CouponsPage()
        self.driver.press_keycode(4)
        cl.allureLogs("Succesfully Validated Coupons Page")

    @pytest.mark.order(21)
    def test_ProfilePage(self):
        print("TC15: Verify Profile page")
        cl.allureLogs("Verifying Profile page")
        self.account_page.NavProfilePage()
        self.account_page.VerifyandPrintallElements_underProfilePage()
        self.account_page.VerifyandPrint_allElements_under_ProfilePage()
        self.driver.press_keycode(4)
        self.driver.press_keycode(4)
        cl.allureLogs("Succesfully Validated Profile Page")

    @pytest.mark.order(22)
    def test_searchPage(self):
        print("Now Running test_searchPage")
        cl.allureLogs("Verifying Search Page")
        self.search_page.NavtoSearch()
        self.search_page.VerifyandPrint_allitems_onSearchPage1()
        self.search_page.VerifyandPrint_allitems_onSearchPage2()
        cl.allureLogs("Verified all items on Search Page")

    @pytest.mark.order(23)
    def test_Inputsearch(self):
        searchText = "Zzz"
        print("Now Running test_Inputsearch")
        cl.allureLogs("Verifying Search Page")
        self.search_page.SearchProduct(searchText)
        cl.allureLogs("Inputting valid Product ID successfully completed")

    @pytest.mark.order(24)
    def test_ValidateInputSearchText(self):
        print("Validating Input Search Text")
        cl.allureLogs("Verify the input text")
        assert self.search_page.verifySearchDisplayedText("Zzz")
        cl.allureLogs("Input Search Text validated successfully")


    @pytest.mark.order(25)
    def test_Verifytheelementsaftersearch(self):
            print("Now Running test_Verifytheelementsaftersearch")
            cl.allureLogs("Verifying elements after searching")
            self.search_page.SearchResultsPagewhenNOresults()
            cl.allureLogs("Verified all items after searching")

    @pytest.mark.order(25)
    def test_ValidateInputSearchText(self):
        searchtext = "apple"
        print("Validating Valid Input Search Text")
        cl.allureLogs("Verify the input text with Valid Input Search Text")
        self.search_page.ClearSearchBox()
        self.search_page.SearchProduct(searchtext)
        cl.allureLogs("Input Search Text validated successfully")

if __name__ == "__main__":
    unittest.main()
