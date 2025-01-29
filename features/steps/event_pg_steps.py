from behave import given, when, then


@when('Click on “Companies” from header menu')
def select_companies(context):
    context.app.events_page.click_company_btn()