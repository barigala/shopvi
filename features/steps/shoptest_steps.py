from behave import given, when, then
from pages.NavtoShop import NavtoShop
from pages.accountPage import AccountPage
from pages.ShopDashboard import ShopDashboard

"""class ShopSteps:
    def __init__(self, context):
        self.context = context
        self.navtoshop = NavtoShop(context)
        self.accountpage = AccountPage(context)
        self.shopdashboard = ShopDashboard(context)"""

@given('I open the app and navigate to the mobile number input screen')
def step_open_app(context):
    context.NavtoShop = NavtoShop(context)
    context.NavtoShop.ClickNumberInputField()


@when('I close the mobile number dialog box')
def step_close_dialog(context):
    context.NavtoShop.ClickDialogBox()

@when('I input a valid {mobile_number} mobile number')
def step_input_mobile_number(context, mobile_number):
    context.NavtoShop.inputValidMobileNumber(mobile_number)

@when('I click on the send OTP CTA button')
def step_click_otp_button(context):
    context.NavtoShop.ClickOTPButton()

@when('I input a valid {otp} OTP')
def step_input_otp(context, otp):
    context.NavtoShop.inputOTP(otp)

@when('I log into the app using login with OTP CTA button')
def step_login_with_otp(context):
    context.NavtoShop.LoginWOTPButton()

@then('I click on VI Shop from Bottom Navigation and should navigate to the shop Dashboard')
def step_navigate_to_shop(context):
    context.NavtoShop.NavtoShop()

@then('I print all items on the Shop Dashboard')
def step_print_shop_items(context):
    context.ShopDashboard = ShopDashboard(context)
    ShopDBitems = context.ShopDashboard.print_allitems_onDashBoard()
    context.log_items = ShopDBitems  # Store printed items in context for later use

@then('I navigate to the Deals page')
def step_navigate_deals(context):
    context.ShopDashboard.NavtoDeals()

@then('I print all items on the Deals page')
def step_print_deals_items(context):
    DealsPageitems = context.ShopDashboard.print_allitems_onDealsPage()
    context.log_deals_items = DealsPageitems  # Store printed items in context for later use

@then('I navigate to the Explore page')
def step_navigate_explore(context):
    context.ShopDashboard.NavtoExplore()

@then('I print all items on the Explore page')
def step_print_explore_items(context):
    ExplorePageitems = context.ShopDashboard.print_allitems_onExplorePage()
    context.log_explore_items = ExplorePageitems  # Store printed items in context for later use

@then('I navigate to the My Orders page')
def step_navigate_orders(context):
    context.ShopDashboard.NavtoMyOrders()

@then('I print all items on the My Orders page')
def step_print_orders_items(context):
    MyOrdersitems = context.ShopDashboard.print_allitems_onMyOrders()
    context.log_orders_items = MyOrdersitems  # Store printed items in context for later use
