import time
from base.BasePage import BasePage
import utils.CustomLogger as cl


class ShopDashboard(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators values in Vi Shop dashboard
    _ShopButton = '//android.widget.TextView[@text="shop"]' #xpath
    _viAppHomeButton = '//android.widget.TextView[@text="home"]' #xpath
    _dealsButton = '//android.widget.TextView[@text="deals"]'   #xpath
    _exploreButton = '//android.widget.TextView[@text="explore"]' #xpath
    _myOrdersButton = '//android.widget.TextView[@text="my orders"]' #xpath
    _vihomeButton = '//android.widget.TextView[@text="home"]' #xpath
    _accountsButton = '//android.view.ViewGroup[@content-desc="DS_SHOPshop-account-icon.webp"]' #xpath
    _searchicon = '//android.view.ViewGroup[@content-desc="DS_SHOP_https://vishop.myvi.in/documents/35161/38258/search.png"]' #xpath
    _cartIcon = '//android.view.ViewGroup[@content-desc="DS_SHOP_https://vishop.myvi.in/documents/35161/38258/Cart.webp"]' #xpath
    _backButton = '//android.view.ViewGroup[@content-desc="DS_SHOP_https://vishop.myvi.in/documents/35161/38258/back-arrow.webp"]' #xpath
    _deals_Pagetitle = '//android.widget.TextView[@text="deals"]' #xpath
    _explore_pagetitle = '//android.widget.TextView[@text="explore"]' #xpath
    _myorders_pagetitle = '//android.widget.TextView[@text="your orders"]' #xpath
    _myorders_SearchBox = '//android.widget.EditText[@text="search for orders..."]' #xpath
    _accountpage_shopbycategory = '//android.widget.TextView[@text="shop by category"]' #xpath
    _accountpage_sellingfast = '//android.widget.TextView[@text="selling fast"]' #xpath
    _accountpage_sellingfast_seeallBTN = '(//android.widget.TextView[@text="see all"])[1]' #xpath
    _accountpage_CC = '//android.widget.TextView[@text="credit cards"]' #xpath
    _accountpage_CC_seeallBTN = '(//android.widget.TextView[@text="see all"])[2]'
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
        self.clickElement(self._ShopButton, "xpath")
        time.sleep(2)
        cl.allureLogs("Navigated to Shop Dashboard")
        self.takeScreenshot("Navigated to Shop Dashboard")

    def print_allitems_onDashBoard(self):
        elements = {
            'Vi Home Button': self._viAppHomeButton,
            'Deals': self._dealsButton,
            'Explore': self._exploreButton,
            'My Orders': self._myOrdersButton,
            'Vi Home': self._vihomeButton,
            'Accounts': self._accountsButton,
            'Search Icon': self._searchicon,
            'Cart Icon': self._cartIcon,
        }
        for name, locator in elements.items():
            element_text = self.check_element(locator)
            print(f"{name}: {element_text}")


    def ShopDashboard_elements(self):
        elements = {
            'Shop by Category': self._accountpage_shopbycategory,
            'Selling Fast': self._accountpage_sellingfast,
            'Selling Fast see all button': self._accountpage_sellingfast_seeallBTN,
            'Credit cards section': self._accountpage_CC,
            'Credit cards section see all button': self._accountpage_CC_seeallBTN,
        }
        for name, locator in elements.items():
            element_text = self.check_element(locator)
            print(f"{name}: {element_text}")
        #self.print_allElements_withScroll(elements)

    def NavtoDeals(self):
        self.clickElement(self._dealsButton, "xpath")
        time.sleep(2)
        cl.allureLogs("Navigated to Deals Page")
        self.takeScreenshot("Navigated to Deals Page")

    def print_allitems_onDealsPage(self):
        elements = {
            'Deals Back Button': self._backButton,
            'Deals Page Title': self._deals_Pagetitle,
            'Deals Cart Icon' : self._cartIcon
        }
        for name, locator in elements.items():
            element_text = self.check_element(locator)
            print(f"{name}: {element_text}")

    def NavtoExplore(self):
        self.clickElement(self._exploreButton, "xpath")
        time.sleep(2)
        cl.allureLogs("Navigated to Explore Page")
        self.takeScreenshot("Navigated to Explore Page")

    def print_allitems_onExplorePage(self):
        elements = {
            'Explore Page Title': self._explore_pagetitle,
            'Explore Search Icon' :self._searchicon,
            'Explore Cart Icon' : self._cartIcon
        }
        for name, locator in elements.items():
            element_text = self.check_element(locator)
            print(f"{name}: {element_text}")


    def NavtoMyOrders(self):
        self.clickElement(self._myOrdersButton, "xpath")
        time.sleep(2)
        cl.allureLogs("Navigated to My Orders Page")
        self.takeScreenshot("Navigated to My Orders Page")

    def print_allitems_onMyOrders(self):
        elements = {
            'My Orders Back Button': self._backButton,
            'My Orders Page Title': self._myorders_pagetitle,
            'My Orders Cart Icon' : self._cartIcon,
            'My Orders Search Box': self._myorders_SearchBox
        }
        for name, locator in elements.items():
            element_text = self.check_element(locator)
            print(f"{name}: {element_text}")