import time

from appium.webdriver.common.appiumby import AppiumBy

from base.BasePage import BasePage
import utils.CustomLogger as cl


class AccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in Contact us form
    _accountButton = '//android.view.ViewGroup[@content-desc="DS_SHOPshop-account-icon.webp"]'
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


    #Common locators across all accounts pages sections
    _backarrow = '//android.view.ViewGroup[@content-desc="DS_SHOP_https://vishop.myvi.in/documents/35161/38258/back-arrow.webp"]'
    _bellIcon = '//android.view.ViewGroup[@content-desc="DS_SHOP_https://vishop.myvi.in/documents/35161/38258/notification-icon.webp"]'
    _searchIcon = '//android.view.ViewGroup[@content-desc="DS_SHOP_https://vishop.myvi.in/documents/35161/38258/search.png"]'

    #Locators under profile page
    _saveButton = '//android.widget.TextView[@text="save"]'
    _textdesc = '//android.widget.TextView[@text="Order details will be sent to this email address"]'
    _mydetailsPage = '//android.widget.TextView[@text="my details"]'
    #Locators under profile page with ui automator selector
    _profilePic = 'new UiSelector().className("android.widget.ImageView").instance(1)' #uiAutomator
    _mobileNumberField = 'new UiSelector().className("android.view.ViewGroup").instance(31)'
    _emailIDField = 'new UiSelector().className("android.view.ViewGroup").instance(32)'

    #Locators under saved payments page
    _sppagetitle = '//android.view.View[@text="manage payment options"]'
    _pagetext = '//android.widget.TextView[@text="nothing saved yet"]'

    #Locators under FAQs page
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
        self.waitForElement(self._accountButton, "xpath")
        self.clickElement(self._accountButton, "xpath")
        cl.allureLogs("Clicked on Account Button")
        self.takeScreenshot("Clicked on Account Button")


    def VerifyTotalSavings_Banner(self):
        elements = {
            'Is Savings banner Displayed': self._SavingsBanner,
        }
        for name, locator in elements.items():
            element_text = self.iselement_present_by_uiautomator(locator)
            print(f"{name}: {element_text}")

    def VerifyandPrint_allitems_onAccountPage(self):
        elements = {
            'Page Title' : self._pagetitle,
            'Your Orders' : self._yourorders,
            'Credit Cards' : self._cc,
            'Coupons' : self._coupons,
            'Saved Payments' : self._savedpay,
            'Help & Support' : self._HelpandSupport,
            'FAQs' : self._FAQ,
            'Terms & Conditions' : self._TandC,
            'Privacy Policy' : self._privacypolicy,
            'About Us' : self._aboutUS,
            'Powered By' : self._poweredBy,
            'Back Arrow' : self._backarrow,
            'Bell Icon' : self._bellIcon,
            'Search Icon' : self._searchIcon,
            'Mobile Number in Profile' : self._profileNumber,
            'Edit Icon' : self._editIcon,
        }
        for name, locator in elements.items():
            element_text = self.check_element(locator)
            print(f"{name}: {element_text}")



    def NavOrders(self):
        self.clickElement(self._yourorders,"xpath")
        time.sleep(2)
        cl.allureLogs("Clicked on My Orders")
        self.takeScreenshot("Navigataed to My Orders")

    def NavCC(self):
        self.clickElement(self._cc,"xpath")
        time.sleep(2)
        cl.allureLogs("Clicked on Credit Cards")
        self.takeScreenshot("Navigated to Credit Cards")

    def NavCoupons(self):
        self.clickElement(self._coupons,"xpath")
        time.sleep(2)
        cl.allureLogs("Clicked on Coupons")
        self.takeScreenshot("Navigated to Coupons")

    def NavSavdPay(self):
        self.clickElement(self._savedpay,"xpath")
        time.sleep(2)
        cl.allureLogs("Clicked on Saved Payments")
        self.takeScreenshot("Navigated to Saved Payments")

    def NavHelpandSupport(self):
        self.clickElement(self._HelpandSupport,"xpath")
        time.sleep(2)
        cl.allureLogs("Clicked on Help & Support")
        self.takeScreenshot("Navigated to Help & Support")

    def NavFAQ(self):
        self.clickElement(self._FAQ,"xpath")
        time.sleep(2)
        cl.allureLogs("Clicked on FAQ")
        self.takeScreenshot("Navigated to FAQ")


    def VerifyandPrint_allElements_under_FAQpage(self):
        elements = {
            'FAQ Page Title': self._faqPageTitle,
            'FAQ Page Search Box': self._faqsearchbox,
            'FAQ Page All Filter Option' : self._faqAllFilter,
            'FAQ Page Account Filter Option' : self._faqAccountFilter,
            'FAQ Page Cancellation Filter Option' : self._faqCancellationFilter,
            'FAQ Page Refund Filter Option' : self._faqRefundFilter,
            'FAQ Q1' : self._faqQ1,
            'FAQ Q2' : self._faqQ2,
            'FAQ Q3' : self._faqQ3,
            'FAQ Q4' : self._faqQ4,
            'FAQ Q5' : self._faqQ5,
            'FAQ Q6' : self._faqQ6,
            'FAQ Q7' : self._faqQ7,
            'FAQ Q8' : self._faqQ8,
            'FAQ Q9' : self._faqQ9,
            'FAQ Q10' : self._faqQ10
        }
        for name, locator in elements.items():
            element_text = self.check_element(locator)
            print(f"{name}: {element_text}")

    def NavTandC(self):
        self.clickElement(self._TandC,"xpath")
        time.sleep(2)
        cl.allureLogs("Clicked on Terms & Conditions")
        self.takeScreenshot("Navigated to Terms & Conditions")

    def NavPrivacyPolicy(self):
        self.clickElement(self._privacypolicy,"xpath")
        time.sleep(2)
        cl.allureLogs("Clicked on Privacy Policy")
        self.takeScreenshot("Navigated to Privacy Policy")

    def NavAboutUS(self):
        self.clickElement(self._aboutUS,"xpath")
        time.sleep(2)
        cl.allureLogs("Clicked on About Us")
        self.takeScreenshot("Navigated to About Us")


    def Savdpay_page(self, expected_title, expected_text, ctabutton):
        ctabutton = '//android.widget.TextView[@text="go back"]'

        page_title = self.get_page_title(self._sppagetitle)
        if page_title == expected_title:
            print(f"Page title '{page_title}' matches the expected title.")
        else:
            print(f"Page title '{page_title}' does not match the expected title. Clicking back button.")
            self.driver.press_keycode(4)
            return

        if self.check_text_present(self._pagetext, expected_text):
            print(f"Expected text '{expected_text}' found on the page.")
        else:
            print(f"Expected text '{expected_text}' not found. Clicking back button.")
            self.driver.press_keycode(4)
            return

        if self.check_element(ctabutton):
            print("CTA button found. Clicking CTA button.")
            self.click_element(ctabutton)
        else:
            print("CTA button not found. Clicking back button.")
            self.driver.press_keycode(4)

    def VerifyandPrint_allElements_under_myOrderspage(self):
        elements = {
            'my Orders Page Title' : self._yourorders,
            'my Orders Page Back Arrow' : self._backarrow,
            'my Orders Page Search Box' : self._ordersSearchBox,
            'my Orders Page Search Icon' :self._searchIcon
        }
        for name, locator in elements.items():
            element_text = self.check_element(locator)
            print(f"{name}: {element_text}")

    def VerifyandPrint_allElements_under_CCspage(self):
        elements = {
            'CC Page Title' : self._CCpagetitle,
            'CC Page Back Arrow' : self._backarrow,
            'CC Page Search Icon' :self._searchIcon,
            'CC Page Resume Application' : self._CCresumeapplication
        }
        for name, locator in elements.items():
            element_text = self.check_element(locator)
            print(f"{name}: {element_text}")

    def VerifyandPrint_allElements_under_CouponsPage(self):
        elements = {
            'Coupons Page Title' : self._CouponsPageTitle,
            'Coupons Page Back Arrow' : self._backarrow,
            'Coupons Page Coupons not available Text' : self._CouponsnotavailableText,
            'Coupons Page Coupons Not Available Texts Description' : self._CouponsnotavailableTextDesc,
            'Coupons Page Explore our Stores Text' : self._CouponsXploreStores,
            'Coupons Page Explore our Stores Filter 1' : self._CouponsXploreStoresFilter1,
            'Coupons Page Explore our Stores Filter 2' : self._CouponsXploreStoresFilter2,
            'Coupons Page Explore our Stores Filter 3' : self._CouponsXploreStoresFilter3,
            'Coupons Page Explore our Stores Filter 4' : self._CouponsXploreStoresFilter4,
            'Coupons Page Explore our Stores Filter 5' : self._CouponsXploreStoresFilter5,
            }
        for name, locator in elements.items():
            element_text = self.check_element(locator)
            print(f"{name}: {element_text}")

    def VerifyandPrint_allElements_under_ProfilePage(self):
        elements = {
            'Profile Picture': self._profilePic,
            'Profile Page Mobile Number Field': self._mobileNumberField,
            'Profile Page Email ID Field': self._emailIDField,
            }
        for name, locator in elements.items():
            element_text = self.iselement_present_by_uiautomator(locator)
            print(f"{name}: {element_text}")

    def VerifyandPrintallElements_underProfilePage(self):
        elements = {
                'Profile Page Title': self._mydetailsPage,
                'Profile Page Back Button': self._backarrow,
                'Profile Page Text': self._textdesc,
                'Profile Page Save Button': self._saveButton,
            }
        for name, locator in elements.items():
                element_text = self.check_element(locator)
                print(f"{name}: {element_text}")

    def NavProfilePage(self):
        self.clickElement(self._editIcon, "xpath")
        time.sleep(2)
        cl.allureLogs("Clicked on Profile Page Edit Icon")
        self.takeScreenshot("Navigated to Profile Edit Page")