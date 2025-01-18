from behave import given, when, then


@given('Open the main page')
def open_home_page(context):
    context.app.home_page.open_home_page()


@when ('Login to the page')
def login_credentials(context):
    context.app.home_page.login_credentials()





