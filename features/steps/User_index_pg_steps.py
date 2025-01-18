from behave import given, when, then


@when('Click on “market” at the left side menu')
def click_on_market_menu(context):
    context.app.User_index_page.click_market_btn()
