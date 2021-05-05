from behave import *

@given('I prefer DuckDuckGo to Google')
def step_impl(context):
    context.duckduckgo.open()
    assert context.duckduckgo.get_title.__contains__('DuckDuckGo')

@given('want to read {title} quickly')
def step_impl(context, title):
    context.duckduckgo.search(title + ' сокращённо')

@when('I open Briefly website')
def step_impl(context):
    context.duckduckgo.open_briefly()

@then('author is {author}')
def step_impl(context, author):
    assert context.briefly.get_author() == author

@then('it was written in {year}')
def step_impl(context, year):
    assert context.briefly.get_year() == year
    