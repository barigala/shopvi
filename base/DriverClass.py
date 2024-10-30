from appium import webdriver
from appium.options.android import UiAutomator2Options

class Driver:

    @staticmethod
    def getDriverMethod():
        # Desired capabilities for the app
        options = UiAutomator2Options()
        options.platform_name = 'Android'
        options.automation_name = 'UiAutomator2'
        options.platform_version = '14'
        options.device_name = 'POCO X6 5G'
        options.udid = '79003d15'
        options.app = 'D:\\PyProjects\\vishop.apk'
        options.app_package = 'com.mventus.selfcare.activity'
        options.app_activity = 'com.mventus.selfcare.activity.MainActivity'
        options.full_reset = False
        options.auto_grant_permissions = True
        #options.no_reset = True


        # Initialize the Appium driver
        driver = webdriver.Remote('http://localhost:4723', options=options)
        return driver