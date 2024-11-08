import random
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

    def print_searchresults(self, search_text):
        """Finds and prints displayed element groups based on the specified search text."""
        cl.allureLogs(f"Printing search results for the search text: {search_text}")
        self.takeScreenshot("Print Search Results")

        start_index = 0
        end_index = 100
        max_unsuccessful_attempts = 2
        unsuccessful_attempts = 0
        displayed_groups = []

        for index in range(start_index, end_index + 1):
            try:
                # Locate the group container
                group_container = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,f'new UiSelector().className("android.view.ViewGroup").instance({index})')

                # Locate image within the group
                image_element = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,f'new UiSelector().className("android.widget.ImageView").instance({index})'                )

                # Locate text elements within the group (matching any text)
                text_elements = self.driver.find_elements(AppiumBy.XPATH,f'//android.widget.TextView[contains(@text, "{search_text}")]')

                # Ensure all elements are displayed before considering this a valid group
                if group_container.is_displayed() and image_element.is_displayed() and text_elements:
                    displayed_groups.append((group_container, image_element, text_elements))
                    print(f"Displayed element group at index {index} with text: '{text_elements[0].text}'")
                    unsuccessful_attempts = 0  # Reset unsuccessful attempt counter
                else:
                    unsuccessful_attempts += 1
            except Exception as e:
                print(f"Element group at index {index} not found: {str(e)}")
                unsuccessful_attempts += 1

            # Stop searching after reaching the max consecutive unsuccessful attempts
            if unsuccessful_attempts >= max_unsuccessful_attempts:
                print("Stopping search due to consecutive unsuccessful attempts.")
                break

        if not displayed_groups:
            print("No element groups are displayed in the specified index range.")
            cl.allureLogs("No element groups displayed in the specified range.")
        else:
            print("Displayed element groups found:")
            for i, group in enumerate(displayed_groups):
                group_text = group[2][0].text if group[2] else "[No Text]"
                print(f"Element Group {i} with text: '{group_text}'")

        cl.allureLogs("Completed printing search results")
        self.takeScreenshot("Search Results Printed")
        return displayed_groups

    def click_Oneofthe_searchResults(self, search_text):
        """Uses print_searchresults to find element groups and clicks one randomly based on the search text."""
        displayed_groups = self.print_searchresults(search_text)

        if displayed_groups:
            random_group = random.choice(displayed_groups)
            random_group[0].click()  # Click the group container
            group_text = random_group[2][0].text if random_group[2] else "[No Text]"
            print(f"Clicked on a random element group with text: '{group_text}'")
            cl.allureLogs(f"Clicked on a random element group with text: '{group_text}'")
        else:
            print("No element groups found to click.")
            cl.allureLogs("No element groups found to click.")

    def click_element_with_bounds(self, bounds):
        self.click_by_bounds(bounds)