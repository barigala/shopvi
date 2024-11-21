import random
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from base.BasePage import BasePage
import utils.CustomLogger as cl


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _searchicon1 = '//android.view.ViewGroup[@content-desc="DS_SHOP_https://vishop.myvi.in/documents/35161/38258/search.png"]'  # xpath
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
    _MyntraSearchloc1 = "//android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup"
    _MyntraSearchloc3 = "//android.widget.FrameLayout[@resource-id='android:id/content']//android.widget.ScrollView//android.widget.ImageView"

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
    _SearchIcon2 = 'new UiSelector().className("android.widget.ImageView").instance(1)'
    _MyntraSearchloc2 = 'new UiSelector().className("android.view.ViewGroup").instance(34)'


    def NavtoSearch(self):
        self.click_element_by_uiautomator(self._SearchIcon2)
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
        cl.allureLogs(f"Entered Product ID for search: {searchText}")
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


    def click_on_search_results(self):
        self.click_element_by_uiautomator(self._MyntraSearchloc2)
        time.sleep(5)
        self.takeScreenshot("Clicked on search results")
        print("Successfully clicked on the search results element.")
        cl.allureLogs("Successfully clicked on the search results element.")

    def touch_click_element(self, x, y):
        """Simulates a touch click at specific coordinates."""
        try:
            actions = ActionChains(self.driver)
            touch_input = PointerInput("touch", "finger")  # Directly specify 'touch' and a unique pointer name
            actions.w3c_actions = ActionBuilder(self.driver, mouse=touch_input)

            # Move to location, press down, pause, and release for touch action
            actions.w3c_actions.pointer_action.move_to_location(x, y)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()

            # Perform the actions
            actions.perform()

            cl.allureLogs(f"Touched at location ({x}, {y}) successfully.")
            self.log.info(f"Touched at location ({x}, {y}) successfully.")
        except Exception as e:
            self.log.error(f"Failed to touch at location ({x}, {y}). Error: {str(e)}")
            cl.allureLogs(f"Failed to touch at location ({x}, {y}). Error: {str(e)}")
            self.takeScreenshot(f"TouchClickError_{x}_{y}")
            assert False, f"Failed to perform touch click at ({x}, {y})"

    def click_on_first_search_result(self):
        elements = self.driver.find_elements(AppiumBy.XPATH, self._MyntraSearchloc3)
        if elements:
            elements[0].click()
            print("Clicked on the first search result.")
        else:
            print("Element not found in DOM.")
        time.sleep(5)
        self.takeScreenshot("taking screenshot after navigation")

    def tap_above_middle(self):
        """Tap dynamically at the top and slightly above the middle of the screen."""
        try:
            # Get screen dimensions
            screen_width = self.driver.get_window_size()["width"]
            screen_height = self.driver.get_window_size()["height"]

            # Coordinates for top and slightly above middle taps
            top_y = int(screen_height * 0.1)  # 10% from the top of the screen
            middle_y = int(screen_height * 0.4)  # 40% from the top of the screen
            x = int(screen_width / 2)  # Center of the screen horizontally

            actions = ActionChains(self.driver)

            # Tap at top
            actions.tap(None, x, top_y).perform()
            cl.allureLogs(f"Tapped at top of screen at ({x}, {top_y}).")
            self.log.info(f"Tapped at top of screen at ({x}, {top_y}).")

            # Tap slightly above the middle of the screen
            actions.tap(None, x, middle_y).perform()
            cl.allureLogs(f"Tapped above middle of screen at ({x}, {middle_y}).")
            self.log.info(f"Tapped above middle of screen at ({x}, {middle_y}).")

        except Exception as e:
            self.log.error(f"Failed to perform tap action. Error: {str(e)}")
            cl.allureLogs(f"Failed to perform tap action. Error: {str(e)}")
            self.takeScreenshot("TapAboveMiddleError")
            assert False, f"Failed to perform tap action"

    def tap_middle_above_screen(self):

        screen_size = self.driver.get_window_size()
        screen_width = screen_size['width']
        screen_height = screen_size['height']

        x = screen_width / 2
        y = screen_height * 0.4

        action = ActionChains(self)
        action.move_by_offset(x, y).click().perform()