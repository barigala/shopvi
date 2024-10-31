import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import TimeoutException

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
    _searchEdit = 'android.widget.EditText'  # class

    # Categories
    _CC = '//android.widget.TextView[@text="credit cards"]'
    _Entertainment = '//android.widget.TextView[@text="entertainment"]'
    _Food = '//android.widget.TextView[@text="food"]'
    _Shopping = '//android.widget.TextView[@text="shopping"]'
    _Travel = '//android.widget.TextView[@text="travel"]'

    # Categories locators with UI Automator elements
    _CCicon = 'new UiSelector().className("android.widget.ImageView").instance(1)'
    _EntertainmentIcon = 'new UiSelector().className("android.widget.ImageView").instance(2)'
    _FoodIcon = 'new UiSelector().className("android.widget.ImageView").instance(3)'
    _ShoppingIcon = 'new UiSelector().className("android.widget.ImageView").instance(4)'
    _TravelIcon = 'new UiSelector().className("android.widget.ImageView").instance(5)'
    _SearchCloseIcon = 'new UiSelector().className("android.widget.ImageView").instance(1)'

    def NavtoSearch(self):
        self.clickElement(self._searchicon, "xpath")
        time.sleep(1)
        cl.allureLogs("Navigated to Search Page")
        self.takeScreenshot("Navigated to Search Page")

    def VerifyandPrint_allitems_onSearchPage1(self):
        cl.allureLogs("Starting verification of all items on Search Page - Part 1")
        self.takeScreenshot("Verify all items on Search Page - Part 1")

        elements = {
            'Popular Categories': self._popularcategories,
            'Search Box': self._searchBox,
            'Recently Viewed': self._recentlyviewed,
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
        cl.allureLogs("Verified all items on Search Page - Part 1")

    def VerifyandPrint_allitems_onSearchPage2(self):
        cl.allureLogs("Starting verification of all category icons on Search Page")
        self.takeScreenshot("Verify category icons on Search Page")

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
        cl.allureLogs("Verified that all categories are displayed")
        self.takeScreenshot("Categories Icons")

    def SearchProduct(self, searchText):
        self.sendText(searchText, self._searchBox, "xpath")
        cl.allureLogs("Entered Product ID for search")
        self.takeScreenshot("Search Product")

    def verifySearchDisplayedText(self, expected_text):
        """Verify if the expected text is displayed in the specified field."""
        if self.verifyTextInField(expected_text, self._searchEdit, locatorType="class"):
            self.log.info(f"Verified that the field displays the expected text: '{expected_text}'")
            cl.allureLogs("Verified that the field displays the expected text")
            self.takeScreenshot("Search Results Page - Text Verified")
            return True
        else:
            self.log.error(f"Expected text '{expected_text}' not displayed in the field.")
            cl.allureLogs("Expected text not displayed in the field")
            self.takeScreenshot("Search Results Page - Text Not Found")
            return False

    def SearchResultsPagewhenNOresults(self):
        cl.allureLogs("Verifying elements on No Results Found page")
        self.takeScreenshot("No Results Found Page")

        elements = {
            'No Results Found Back Button': self._noresultsfoundbackCTA,
            'No Results Found Text': self._noresultsfoundtext,
            'No Results Found Icon': self._noresultsfoundicon,
        }
        for name, locator in elements.items():
            element_text = self.check_element(locator)
            print(f"{name}: {element_text}")
        cl.allureLogs("Verified No Results Found page elements")

    def ClearSearchBox(self):
        self.click_element_by_uiautomator(self._SearchCloseIcon)
        cl.allureLogs("Verified clicking on Search Box X Icon")
        self.takeScreenshot("Click Search Box X Icon")

    def print_searchresults(self):
        cl.allureLogs("Printing search results in specified index range")
        self.takeScreenshot("Print Search Results")

        start_index = 35
        end_index = 45
        displayed_elements = []

        for index in range(start_index, end_index + 1):
            try:
                element = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().className("android.view.ViewGroup").instance({index})')
                if element.is_displayed():
                    displayed_elements.append(f'Element at index {index} is displayed with text: "{element.text}"')
                    print(f'Element at index {index} is displayed with text: "{element.text}"')
            except Exception as e:
                print(f'Element at index {index} is not found: {str(e)}')

        if not displayed_elements:
            print("No elements are displayed in the specified index range.")
        else:
            print("Displayed elements:")
            for item in displayed_elements:
                print(item)
        cl.allureLogs("Completed printing search results")
        self.takeScreenshot("Search Results Printed")
