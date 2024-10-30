import time
from base.BasePage import BasePage
import utils.CustomLogger as cl

class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _searchicon = '//android.view.ViewGroup[@content-desc="DS_SHOP_https://vishop.myvi.in/documents/35161/38258/search.png"]'  # xpath
    _popularcategories = '//android.widget.TextView[@text="popular categories"]'
    _recentlyviewed = '//android.widget.TextView[@text="recently viewed"]'
    _recentlyviewedseeall = '//android.widget.TextView[@text="see all"]'
    _noresultsfoundbackCTA = '//android.widget.TextView[@text="back"]'
    _noresultsfoundtext = '//android.widget.TextView[@text="Looks like there is no relevant products to your search."]'
    _noresultsfoundicon = '//android.widget.ScrollView/android.view.ViewGroup/android.widget.ImageView'
    _sort = '//android.widget.TextView[@text="sort"]'
    _filter = '//android.widget.TextView[@text="filter"]'
    _recentsearches = '//android.widget.TextView[@text="recent searches"]'
    _searchBox = '//android.widget.EditText[@text="Search for products,brands etc"]'
    _searchEdit = 'android.widget.EditText' #class

    # Categories
    _CC = '//android.widget.TextView[@text="credit cards"]'
    _Entertainment = '//android.widget.TextView[@text="entertainment"]'
    _Food = '//android.widget.TextView[@text="food"]'
    _Shopping = '//android.widget.TextView[@text="shopping"]'
    _Travel = '//android.widget.TextView[@text="travel"]'

    #categories locators with UI Automator elements
    _CCicon = 'new UiSelector().className("android.widget.ImageView").instance(1)'
    _EntertainmentIcon = 'new UiSelector().className("android.widget.ImageView").instance(2)'
    _FoodIcon = 'new UiSelector().className("android.widget.ImageView").instance(3)'
    _ShoppingIcon = 'new UiSelector().className("android.widget.ImageView").instance(4)'
    _TravelIcon = 'new UiSelector().className("android.widget.ImageView").instance(5)'



    def NavtoSearch(self):
        self.clickElement(self._searchicon, "xpath")
        time.sleep(1)
        cl.allureLogs("Navigated to Search Page")
        self.takeScreenshot("Navigated to Search Page")

    def VerifyandPrint_allitems_onSearchPage1(self):
        elements = {
            'Popular Categories' : self._popularcategories,
            'Search Box' : self._searchBox,
            'Recently Viewed' : self._recentlyviewed,
            'Credit Card Category': self._CC,
            'Entertainment Category': self._Entertainment,
            'Food Category': self._Food,
            'Shopping Category': self._Shopping,
            'Travel Category': self._Travel,
            'Recent Searches': self._recentsearches,
            'Recently Viewed see all': self._recentlyviewedseeall,
        }
        for name, locator in elements.items():
            element_text = self.check_element(locator)
            print(f"{name}: {element_text}")

    def VerifyandPrint_allitems_onSearchPage2(self):
        elements = {
            'Credit Card Category Icon': self._CCicon,
            'Entertainment Category Icon': self._EntertainmentIcon,
            'Food Category Icon': self._FoodIcon,
            'Shopping Category Icon': self._ShoppingIcon,
            'Travel Category Icon': self._TravelIcon,

        }
        for name, locator in elements.items():
            element_text = self.iselement_present_by_uiautomator(locator)
            print(f"{name}: {element_text}")


    def SearchProduct(self, searchText):
        self.sendText(searchText, self._searchBox, "xpath")
        cl.allureLogs("Input Product ID for search")
        self.takeScreenshot("Search Product")

    def verifySearchDisplayedText(self, expected_text):
        """Verify if the expected text is displayed in the specified field."""
        if self.verifyTextInField(expected_text, self._searchEdit, locatorType="class"):
            self.log.info(f"Verified that the field displays the expected text: '{expected_text}'")
            return True
        else:
            self.log.error(f"Expected text '{expected_text}' not displayed in the field.")
            return False

    def SearchResultsPagewhenNOresults(self):
        elements = {
            'No Results Found Back Button' : self._noresultsfoundbackCTA,
            'No Results Found Text' : self._noresultsfoundtext,
            'No Results Found Icon': self._noresultsfoundicon,
        }
        for name, locator in elements.items():
            element_text = self.check_element(locator)
            print(f"{name}: {element_text}")


    def ClearSearchBox(self):
        search_box = self.driver.find_element(self._searchBox)
        search_box.clear()



