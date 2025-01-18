from behave import given, when, then


@when('Click on {string} filter at the top of the page')
def select_filter(context, string):
    context.app.markets_page.click_filter_btn(string)


@then('Verify the right page opens')
def verify_right_page(context):
    context.app.markets_page.verify_market_pg()


@then('Verify all cards has the license tag {tags}')
def verify_cards_tag(context, tags):
    context.app.markets_page.verify_all_cards_tag(tags)