import time
from base.BasePage import BasePage
import utils.CustomLogger as cl

class ShopDashboard(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in Vi Shop dashboard
    _viAppHomeButton = '//android.widget.TextView[@text="home"]'  # xpath
    _dealsButton = '//android.widget.TextView[@text="deals"]'  # xpath
    _exploreButton = '//android.widget.TextView[@text="explore"]'  # xpath
    _myOrdersButton = '//android.widget.TextView[@text="my orders"]'  # xpath
    _viShopButton = '//android.widget.TextView[@text="shop"]'  # xpath

    _deals_Pagetitle = '//android.widget.TextView[@text="offers"]'  # xpath

    _myorders_pagetitle = '//android.widget.TextView[@text="your orders"]'  # xpath
    _myorders_SearchBox = '//android.widget.EditText[@text="search for orders..."]'  # xpath

    _accountsButton = '//android.view.ViewGroup[@content-desc="DS_SHOPshop-account-icon.webp"]'  # xpath
    _searchicon = '//android.view.ViewGroup[@content-desc="DS_SHOP_https://vishop.myvi.in/documents/35161/38258/search.png"]'  # xpath
    _cartIcon = '//android.view.ViewGroup[@content-desc="DS_SHOP_https://vishop.myvi.in/documents/35161/38258/Cart.webp"]'  # xpath

    _accountsButton1 = 'new UiSelector().className("android.widget.ImageView").instance(0)'
    _db_myorders_searchicon = 'new UiSelector().className("android.widget.ImageView").instance(1)'
    _cartIcon1 = 'new UiSelector().className("android.widget.ImageView").instance(2)'

    _backButton = '//android.view.ViewGroup[@content-desc="DS_SHOP_https://vishop.myvi.in/documents/35161/38258/back-arrow.webp"]'  # xpath
    _deals_myorders_backButton = 'new UiSelector().className("android.widget.ImageView").instance(1)'

    #explore page
    _explore_pagetitle = '//android.widget.TextView[@text="our store"]'  # xpath
    _explore_CartIcon = 'new UiSelector().className("android.widget.ImageView").instance(1)'
    _explore_SearchIcon = 'new UiSelector().className("android.widget.ImageView").instance(0)'

    _sdb_shopbycategory = '//android.widget.TextView[@text="shop by category"]'  # xpath
    _sdb_sellingfast = '//android.widget.TextView[@text="selling fast"]'  # xpath
    _sdb_sellingfast_seeallBTN = '(//android.widget.TextView[@text="see all"])[1]'  # xpath
    _sdb_CC = '//android.widget.TextView[@text="credit cards"]'  # xpath
    _sdb_CC_seeallBTN = '(//android.widget.TextView[@text="see all"])[2]'


    _accountpage_recentlyviewed = '//android.widget.TextView[@text="recently viewed"]'
    _accountpage_recentlyviewed_seeallBTN = '//android.widget.TextView[@text="see all"]'
    _accountpage_bigsavings_section = '//android.widget.TextView[@text="big savings"]'
    _accountpage_popular_section = '//android.widget.TextView[@text="super brands, super discounts"]'
    _accountpage_newinstory = '//android.widget.TextView[@text="new in store"]'
    _accountpage_newinstory_seeallBTN = '(//android.widget.TextView[@text="see all"])[1]'
    _accountpage_moviesandOTT = '//android.widget.TextView[@text="movies & OTT"]'
    _accountpage_moviesandOTT_seeallBTN = '(//android.widget.TextView[@text="see all"])[2]'
    _accountpage_moreinstore = '//android.widget.TextView[@text="more in store"]'
    _accountpage_moreinstore_seeallBTN = '//android.widget.TextView[@text="see all"]'
    _accountpage_restcategories1 = '//android.widget.TextView[@text="all"]'
    _accountpage_restcategories2 = '//android.widget.TextView[@text="credit cards"]'
    _accountpage_restcategories3 = '//android.widget.TextView[@text="entertainment"]'
    _accountpage_restcategories4 = '//android.widget.TextView[@text="food"]'
    _accountpage_restcategories5 = '//android.widget.TextView[@text="shopping"]'

    def NavtoShopDashBoard(self):
        # Navigation to Shop Dashboard
        self.clickElement(self._viShopButton, "xpath")
        time.sleep(2)
        cl.allureLogs("Navigated to Shop Dashboard")
        self.takeScreenshot("Navigated to Shop Dashboard")

    def print_allitems_onDashBoard1(self):
            # print the list of all items present on the Vi Shop Dashboard
            cl.allureLogs("Checking all icons on the Vi Shop Dashboard")
            elements = {
                'Vi App Home Button': self._viShopButton,
                'Deals': self._dealsButton,
                'Explore': self._exploreButton,
                'My Orders': self._myOrdersButton,
                'Vi Home': self._viShopButton,
            }
            for name, locator in elements.items():
                element_text = self.check_element(locator)
                cl.allureLogs(f"{name}: {element_text}")
            self.takeScreenshot("Print all elements on Shop Dashboard")

    def print_allitems_onDashBoard2(self):
            # print the list of all items present on the Vi Shop Dashboard
            cl.allureLogs("Checking all icons on the Vi Shop Dashboard")
            elements = {
                'Accounts': self._accountsButton,
                'Search Icon': self._searchicon,
                'Cart Icon': self._cartIcon,
            }
            for name, locator in elements.items():
                element_text = self.check_element(locator)
                cl.allureLogs(f"{name}: {element_text}")
            self.takeScreenshot("Print all Elements on Shop Dashboard")

    def print_allitems_onDashBoard2Prod(self):
            # Verify and print all items under My Orders Page (Ui automator locators used here)
            cl.allureLogs("Verifying and printing all elements under My Orders Page (Part 2 Prod)")
            elements = {
                'Accounts': self._accountsButton1,
                'Search Icon': self._db_myorders_searchicon,
                'Cart Icon': self._cartIcon1,
            }
            for name, locator in elements.items():
                element = self.findelement_by_uiautomator(locator)
                element_text = element.text if element else "Element not found"
                cl.allureLogs(f"{name}: {element_text}")
            self.takeScreenshot("Print all Elements on Shop Dashboard")

    def ShopDashboard_elements(self):
        # print the options present on VI Shop Dashboard
        cl.allureLogs("Checking all elements on the Vi Shop Dashboard")
        elements = {
            'Shop by Category': self._sdb_shopbycategory,
            'Selling Fast': self._sdb_sellingfast,
            'Selling Fast see all button': self._sdb_sellingfast_seeallBTN,
            'Credit cards section': self._sdb_CC,
            'Credit cards section see all button': self._sdb_CC_seeallBTN,
        }
        for name, locator in elements.items():
            element_text = self.check_element(locator)
            cl.allureLogs(f"{name}: {element_text}")
        self.takeScreenshot("Print all elements on Shop Dashboard")

    def NavtoDeals(self):
        # Navigation to Deals page
        cl.allureLogs("Navigating to Deals page")
        self.clickElement(self._dealsButton, "xpath")
        time.sleep(2)
        cl.allureLogs("Navigated to Deals Page")
        self.takeScreenshot("Navigated to Deals Page")

    def print_allitems_onDealsPage(self):
        # print "All items on Deals Page"
        cl.allureLogs("Checking All items on Deals Page")
        elements = {
            'Deals Back Button': self._backButton,
            'Deals Page Title': self._deals_Pagetitle,
            'Deals Cart Icon': self._cartIcon
        }
        for name, locator in elements.items():
            element_text = self.check_element(locator)
            cl.allureLogs(f"{name}: {element_text}")
        self.takeScreenshot("Print all elements on Deals Page")

    def NavtoExplore(self):
        # Navigation to Explore page
        cl.allureLogs("Navigating to Explore Page")
        self.clickElement(self._exploreButton, "xpath")
        time.sleep(2)
        cl.allureLogs("Navigated to Explore Page")
        self.takeScreenshot("Navigated to Explore Page")

    def print_allitems_onExplorePage(self):
        # print "All items on Explore Page"
        cl.allureLogs("Checking All items on Explore Page")

        elements = {
            'Explore Page Title': self._explore_pagetitle,
            'Explore Search Icon': self._searchicon,
            'Explore Cart Icon': self._cartIcon
        }
        for name, locator in elements.items():
            element_text = self.check_element(locator)
            cl.allureLogs(f"{name}: {element_text}")
        self.takeScreenshot("Print all elements on Explore Page")

    def NavtoMyOrders(self):
        # Navigation to My Orders page
        cl.allureLogs("Navigating to My Orders Page")
        self.clickElement(self._myOrdersButton, "xpath")
        time.sleep(2)
        cl.allureLogs("Navigated to My Orders Page")
        self.takeScreenshot("Navigated to My Orders Page")

    def print_allitems_onMyOrders(self):
        # print "All items on My Orders Page"
        cl.allureLogs("Checking All items on My Orders Page")
        elements = {
            'My Orders Back Button': self._backButton,
            'My Orders Page Title': self._myorders_pagetitle,
            'My Orders Cart Icon': self._cartIcon,
            'My Orders Search Box': self._myorders_SearchBox
        }
        for name, locator in elements.items():
            element_text = self.check_element(locator)
            cl.allureLogs(f"{name}: {element_text}")
        self.takeScreenshot("Print all elements on My Orders Page")