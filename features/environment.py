from behave import fixture
from base.DriverClass import Driver
from pages.NavtoShop import NavtoShop
from pages.accountPage import AccountPage

def before_scenario(context, scenario):
    # Initialize driver
    context.driver = Driver.getDriverMethod()  # Now calls static method without argument
    context.nav_to_shop = NavtoShop(context.driver)  # Initialize with driver instance
    context.account_page = AccountPage(context.driver)  # Initialize with driver instance

def after_scenario(context, scenario):
    # Quit driver after each scenario
    if context.driver:
        context.driver.quit()
