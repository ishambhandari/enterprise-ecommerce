from behave import given, then
from selenium import webdriver

@given('I am on the homepage')
def step_impl(context):
    context.browser.get(context.server_url)

@then('I should see "{text}"')
def step_impl(context, text):
    assert text in context.browser.page_source
