from behave import fixture, use_fixture
from selenium import webdriver
from pageObjects.brieflyPO import BrieflyPO
from pageObjects.duckDuckGoPO import DuckDuckGoPO

@fixture
def browser_firefox(context):

    browser = webdriver.Firefox()
    browser.implicitly_wait(2)
    context.duckduckgo = DuckDuckGoPO(browser)
    context.briefly = BrieflyPO(browser)

    yield context
    
    browser.quit()


def before_all(context):
    use_fixture(browser_firefox, context)