import time
from appium.webdriver.common.appiumby import AppiumBy
from base.BasePage import BasePage
import utils.CustomLogger as cl

class AccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Common locators across all accounts pages sections
    _backarrow = '//android.view.ViewGroup[@content-desc="DS_SHOP_https://vishop.myvi.in/documents/35161/38258/back-arrow.webp"]'
    _bellIcon = '//android.view.ViewGroup[@content-desc="DS_SHOP_https://vishop.myvi.in/documents/35161/38258/notification-icon.webp"]'
    _searchIcon = '//android.view.ViewGroup[@content-desc="DS_SHOP_https://vishop.myvi.in/documents/35161/38258/search.png"]'

    _accountButton1 = 'new UiSelector().description("DS_SHOPshop-account-icon.webp")'  # uiautomator
    _accountButton2 = 'new UiSelector().className("android.widget.ImageView").instance(0)' #uiautomator selector observeved newly
    _pagetitle = '//android.widget.TextView[@text="account"]'
    _yourorders = '//android.widget.TextView[@text="your orders"]'
    _cc = '//android.widget.TextView[@text="credit cards"]'
    _coupons = '//android.widget.TextView[@text="coupons"]'
    _savedpay = '//android.widget.TextView[@text="saved payments"]'
    _HelpandSupport = '//android.widget.TextView[@text="help & support"]'
    _FAQ = '//android.widget.TextView[@text="FAQs"]'
    _TandC = '//android.widget.TextView[@text="terms & conditions"]'
    _privacypolicy = '//android.widget.TextView[@text="privacy policy"]'
    _aboutUS = '//android.widget.TextView[@text="about us"]'
    _poweredBy = '//android.widget.TextView[@text="powered by Vodafone Idea Business Service Ltd."]'
    _profileNumber = '//android.widget.TextView[@text="7507233095"]'
    _editIcon = '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView'
    _SavingsBanner = 'new UiSelector().className("android.widget.ImageView").instance(5)'

    # Locators under orders page
    _ordersSearchBox = '//android.widget.EditText[@text="search for orders..."]'
    _ordersPageTitle = '//android.widget.TextView[@text="your orders"]'


    _ordersSearchIcon = 'new UiSelector().className("android.widget.ImageView").instance(1)'
    _ordersPageFilterIcon = 'new UiSelector().className("android.widget.ImageView").instance(3)'


    # Locators under credit cards page
    _CCresumeapplication = '//android.widget.TextView[@text="resume applications"]'
    _CCpagetitle = '//android.widget.TextView[@text="my applications"]'

    # Locators under coupons page
    _CouponsPageTitle = '//android.widget.TextView[@text="coupons"]'
    _CouponsnotavailableText = '//android.widget.TextView[@text="no coupons yet!"]'
    _CouponsnotavailableTextDesc = '//android.widget.TextView[@text="I’ll come rushing when I have something for you!"]'

    _CouponsXploreStores = '//android.widget.TextView[@text="explore our stores"]'
    _CouponsXploreStoresFilter1 = '//android.widget.TextView[@text="credit cards"]'
    _CouponsXploreStoresFilter2 = '//android.widget.TextView[@text="entertainment"]'
    _CouponsXploreStoresFilter3 = '//android.widget.TextView[@text="food"]'
    _CouponsXploreStoresFilter4 = '//android.widget.TextView[@text="shopping"]'
    _CouponsXploreStoresFilter5 = '//android.widget.TextView[@text="travel"]'


    # Locators under profile page
    _saveButton = '//android.widget.TextView[@text="save"]'
    _textdesc = '//android.widget.TextView[@text="Order details will be sent to this email address"]'
    _mydetailsPage = '//android.widget.TextView[@text="my details"]'
    # Locators under profile page with ui automator selector
    _profilePic = 'new UiSelector().className("android.widget.ImageView").instance(1)'  # uiAutomator
    _mobileNumberField = 'new UiSelector().className("android.view.ViewGroup").instance(31)'
    _emailIDField = 'new UiSelector().className("android.view.ViewGroup").instance(32)'

    # Locators under saved payments page
    _sppagetitle = '//android.view.View[@text="manage payment options"]'
    _pagetext = '//android.widget.TextView[@text="nothing saved yet"]'

    # Locators under FAQs page
    _faqsearchbox = '//android.widget.EditText[@text="search for questions"]'
    _faqAllFilter = '//android.widget.TextView[@text="ALL"]'
    _faqAccountFilter = '//android.widget.TextView[@text="Account"]'
    _faqCancellationFilter = '//android.widget.TextView[@text="Cancellation"]'
    _faqRefundFilter = '//android.widget.TextView[@text="Refund"]'
    _faqPageTitle = '//android.widget.TextView[@text="FAQs"]'
    _faqQ1 = '//android.widget.TextView[@text="How to make a purchase on Vi Shop?"]'
    _faqQ2 = '//android.widget.TextView[@text="Where can I find the terms & conditions?"]'
    _faqQ3 = '//android.widget.TextView[@text="What products are available on Vi Shop?"]'
    _faqQ4 = '//android.widget.TextView[@text="Can I purchase a product for someone else?"]'
    _faqQ5 = '//android.widget.TextView[@text="How do I view my order details?"]'
    _faqQ6 = '//android.widget.TextView[@text="How do I redeem gift cards or vouchers?"]'
    _faqQ7 = '//android.widget.TextView[@text="How long is the product valid?"]'
    _faqQ8 = '//android.widget.TextView[@text="What all payment methods can I use?"]'
    _faqQ9 = '//android.widget.TextView[@text="How do I claim a refund?"]'
    _faqQ10 = '//android.widget.TextView[@text="How can I cancel or exchange a digital product?"]'




    def ClickaccountButton(self):
        # Clicking on the Account button
        cl.allureLogs("Attempting to click on Account Button")
        self.iselement_present_by_uiautomator(self._accountButton2)
        self.click_element_by_uiautomator(self._accountButton2)
        cl.allureLogs("Clicked on Account Button")
        self.takeScreenshot("Clicked on Account Button")

    def VerifyTotalSavings_Banner(self):
        # Verify the total savings banner is shown or not
        cl.allureLogs("Verifying Total Savings Banner presence")
        elements = {
            'Is Savings banner Displayed': self._SavingsBanner,
        }
        for name, locator in elements.items():
            element_text = self.iselement_present_by_uiautomator(locator)
            cl.allureLogs(f"{name}: {element_text}")
            self.takeScreenshot(f"Checked element presence for {name}")

    def VerifyandPrint_allitems_onAccountPage(self):
        # Verify and print all items under Account Page
        cl.allureLogs("Verifying and printing all items on Account Page")
        elements = {
            'Account Page Title': self._pagetitle,
            'Account Page Back Arrow': self._backarrow,
            'Account Page Bell Icon': self._bellIcon,
            'Account Page Search Icon': self._searchIcon,
            'Account Page My Orders': self._yourorders,
            'Account Page Credit Cards': self._cc,
            'Account Page Coupons': self._coupons,
            'Account Page Saved Payments': self._savedpay,
            'Account Page Help & Support': self._HelpandSupport,
            'Account Page Terms & Conditions': self._TandC,
            'Account Page Privacy Policy': self._privacypolicy,
            'Account Page FAQs': self._FAQ,
            'About US' : self._aboutUS,
            'Powered By' : self._poweredBy,
            'Edit Icon' : self._editIcon,
            'Profile Number' : self._profileNumber,
        }
        for name, locator in elements.items():
            element_text = self.check_element(locator)
            cl.allureLogs(f"{name}: {element_text}")
        self.takeScreenshot("Verifying and printing all items on Account Page")

    def NavOrders(self):
        # Navigation to the My Orders page
        cl.allureLogs("Navigating to My Orders")
        self.clickElement(self._yourorders,"xpath")
        time.sleep(2)
        cl.allureLogs("Clicked on My Orders")
        self.takeScreenshot("Navigated to My Orders")

    def NavCC(self):
        # Navigation to Credit Cards Page
        cl.allureLogs("Navigating to Credit Cards")
        self.clickElement(self._cc,"xpath")
        time.sleep(2)
        cl.allureLogs("Clicked on Credit Cards")
        self.takeScreenshot("Navigated to Credit Cards")

    def NavCoupons(self):
        # Navigation to Coupons Page
        cl.allureLogs("Navigating to Coupons")
        self.clickElement(self._coupons,"xpath")
        time.sleep(2)
        cl.allureLogs("Clicked on Coupons")
        self.takeScreenshot("Navigated to Coupons")

    def NavSavdPay(self):
        # Navigation to Saved Payments Page
        cl.allureLogs("Navigating to Saved Payments")
        self.clickElement(self._savedpay,"xpath")
        time.sleep(2)
        cl.allureLogs("Clicked on Saved Payments")
        self.takeScreenshot("Navigated to Saved Payments")

    def NavHelpandSupport(self):
        # Navigation to Help & Support Page
        cl.allureLogs("Navigating to Help & Support")
        self.clickElement(self._HelpandSupport,"xpath")
        time.sleep(2)
        cl.allureLogs("Clicked on Help & Support")
        self.takeScreenshot("Navigated to Help & Support")

    def NavFAQ(self):
        # Navigation to FAQ Page
        cl.allureLogs("Navigating to FAQ")
        self.clickElement(self._FAQ,"xpath")
        time.sleep(2)
        cl.allureLogs("Clicked on FAQ")
        self.takeScreenshot("Navigated to FAQ")

    def VerifyandPrint_allElements_under_FAQpage(self):
        # Verify and print all items under FAQ Page
        cl.allureLogs("Verifying and printing all elements under FAQ Page")
        elements = {
            'FAQ Search Box': self._faqsearchbox,
            'FAQ All Filter': self._faqAllFilter,
            'FAQ Account Filter': self._faqAccountFilter,
            'FAQ Cancellation Filter': self._faqCancellationFilter,
            'FAQ Refund Filter': self._faqRefundFilter,
            'FAQ Page Title': self._faqPageTitle,
            'FAQ Q1': self._faqQ1,
            'FAQ Q2': self._faqQ2,
            'FAQ Q3': self._faqQ3,
            'FAQ Q4': self._faqQ4,
            'FAQ Q5': self._faqQ5,
            'FAQ Q6': self._faqQ6,
            'FAQ Q7': self._faqQ7,
            'FAQ Q8': self._faqQ8,
            'FAQ Q9': self._faqQ9,
            'FAQ Q10': self._faqQ10,
        }
        for name, locator in elements.items():
            element_text = self.check_element(locator)
            cl.allureLogs(f"{name}: {element_text}")
        self.takeScreenshot("Verifying and printing all elements under FAQ Page")

    def NavTandC(self):
        # Navigation to Terms & Conditions Page
        cl.allureLogs("Navigating to Terms & Conditions")
        self.clickElement(self._TandC,"xpath")
        time.sleep(2)
        cl.allureLogs("Clicked on Terms & Conditions")
        self.takeScreenshot("Navigated to Terms & Conditions")

    def NavPrivacyPolicy(self):
        # Navigation to Privacy Policy Page
        cl.allureLogs("Navigating to Privacy Policy")
        self.clickElement(self._privacypolicy,"xpath")
        time.sleep(2)
        cl.allureLogs("Clicked on Privacy Policy")
        self.takeScreenshot("Navigated to Privacy Policy")

    def NavAboutUS(self):
        # Navigation to About Us Page
        cl.allureLogs("Navigating to About Us")
        self.clickElement(self._aboutUS,"xpath")
        time.sleep(2)
        cl.allureLogs("Clicked on About Us")
        self.takeScreenshot("Navigated to About Us")

    def Savdpay_page(self, expected_title, expected_text, ctabutton):
        # Navigation to Saved Payments Page and verify the elements present in that page
        cl.allureLogs("Verifying Saved Payments Page")
        page_title = self.get_page_title(self._sppagetitle)
        if page_title == expected_title:
            cl.allureLogs(f"Page title '{page_title}' matches the expected title.")
        else:
            cl.allureLogs(f"Page title '{page_title}' does not match the expected title. Clicking back button.")
            self.takeScreenshot("Title Mismatch - Going Back")
            self.driver.press_keycode(4)
            return

        if self.check_text_present(self._pagetext, expected_text):
            cl.allureLogs(f"Expected text '{expected_text}' found on the page.")
        else:
            cl.allureLogs(f"Expected text '{expected_text}' not found. Clicking back button.")
            self.takeScreenshot("Text Mismatch - Going Back")
            self.driver.press_keycode(4)
            return

        if self.check_element(ctabutton):
            cl.allureLogs("CTA button found. Clicking CTA button.")
            self.click_element(ctabutton)
            self.takeScreenshot("CTA Button Clicked")
        else:
            cl.allureLogs("CTA button not found. Clicking back button.")
            self.takeScreenshot("CTA Not Found - Going Back")
            self.driver.press_keycode(4)

    def VerifyandPrint_allElements_under_myOrderspage1(self):
        # Verify and print all items under My Orders Page (Xpath locators used here)
        cl.allureLogs("Verifying and printing all elements under My Orders Page (Part 1)")
        elements = {
            'Orders Page Search Box': self._ordersSearchBox,
            'Orders Page Title': self._ordersPageTitle
        }
        for name, locator in elements.items():
            element = self.findelement_by_uiautomator(locator)
            element_text = element.text if element else "Element not found"
            cl.allureLogs(f"{name}: {element_text}")
        self.takeScreenshot("My Orders Page Part 1")

    def VerifyandPrint_allElements_under_myOrderspage2(self):
        # Verify and print all items under My Orders Page (UIAutomator locators used here)
        cl.allureLogs("Verifying and printing all elements under My Orders Page (Part 2)")
        elements = {
            'Orders Page Search Icon': self._ordersSearchIcon,
            'Orders Page Filter Icon': self._ordersPageFilterIcon
        }
        self.check_elements_by_uiautomator(elements)
        self.takeScreenshot("My Orders Page Part 2")


    def VerifyandPrint_allElements_under_CCspage(self):
        # Verify and print all items under Credit Cards Page
        cl.allureLogs("Verifying and printing all elements under Credit Cards Page")
        elements = {
            'CC Page Title': self._CCpagetitle,
            'CC Resume Application': self._CCresumeapplication,
        }
        for name, locator in elements.items():
            element_text = self.check_element(locator)
            cl.allureLogs(f"{name}: {element_text}")
        self.takeScreenshot("Verifying and printing all elements under Credit Cards Page")

    def NavProfilePage(self):
        # Navigation to Profile Page and verify the elements present in that page
        cl.allureLogs("Navigating to Profile Page")
        self.clickElement(self._editIcon,"xpath")
        time.sleep(2)
        cl.allureLogs("Clicked on Profile")
        self.takeScreenshot("Navigated to Profile Page")

    def VerifyandPrintallElements_underProfilePage1(self):
        # Verify and print all items under My Details Page (UIAutomator locators used here)
        cl.allureLogs("Verifying and printing all elements under Profile Page (Part 1)")
        elements = {
            'My Details Page Text': self._mydetailsPage,
            'Text Description': self._textdesc,
            'Save Button': self._saveButton
        }
        for name, locator in elements.items():
            element = self.findelement_by_uiautomator(locator)
            element_text = element.text if element else "Element not found"
            cl.allureLogs(f"{name}: {element_text}")
        self.takeScreenshot("Profile Page Part 1")

    def VerifyandPrintallElements_underProfilePage2(self):
        # Verify and print all items under My Details Page (UIAutomator locators used here)
        cl.allureLogs("Verifying and printing all elements under Profile Page (Part 2)")
        elements = {
            'Profile Picture': self._profilePic,
            'Mobile Number Field': self._mobileNumberField,
            'Email ID Field': self._emailIDField
        }
        self.check_elements_by_uiautomator(elements)
        self.takeScreenshot("Profile Page Part 2")


    def VerifyandPrint_allElements_under_CouponsPage(self):
        # Verify and print all items under Coupons Page
        cl.allureLogs("Verifying and printing all elements under Coupons Page")
        elements = {
            'Coupon Page Title': self._CouponsPageTitle,
            'Coupon Page Back Arrow': self._backarrow,
            'Coupon Page Search Icon': self._searchIcon,
            'Coupons not available Text': self._CouponsnotavailableText,
            'Coupons not available Text Description': self._CouponsnotavailableTextDesc,
            'Coupons Page Explore' : self._CouponsXploreStores,
            'Coupons Page Filter 1' : self._CouponsXploreStoresFilter1,
            'Coupons Page Filter 2' : self._CouponsXploreStoresFilter2,
            'Coupons Page Filter 3' : self._CouponsXploreStoresFilter3,
            'Coupons Page Filter 4' : self._CouponsXploreStoresFilter4,
            'Coupons Page Filter 5' : self._CouponsXploreStoresFilter5,
        }
        for name, locator in elements.items():
            element_text = self.check_element(locator)
            cl.allureLogs(f"{name}: {element_text}")
        self.takeScreenshot("Verifying and printing all elements under Coupons Page")


