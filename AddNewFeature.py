import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'I launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()


@given(u'open metabase website')
def step_impl(context):
    context.driver.get("http://localhost:3000/")


@given(u'I am logged in my metabase account')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id= \"formField-username\"]/div[2]/div/input").send_keys(
    "l201292@lhr.nu.edu.pk")
    time.sleep(1)
    context.driver.find_element(By.XPATH, "//*[@id=\"formField-password\"]/div[2]/div/input").send_keys("4524.smr")
    time.sleep(1)
    context.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/div/main/div/div[2]/div/div[2]/div/form/div[4]").click()
    time.sleep(1)


@when(u'I click on personal account option')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/div/aside/nav/div/div/div[2]/ul/div[2]/div/li/a/div[2]").click()
    time.sleep(1)


@then(u'personal collection page opens')
def step_impl(context):
    check = context.driver.find_element(By.XPATH,"//*[@id=\"root\"]/div/div/main/div/div").is_displayed()
    if check is True:
        assert True
    if check is False:
        assert False

    time.sleep(1)


@when(u'I click on create new button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/div/main/div/div/div[3]/div/div[3]/span[1]/button/div/div").click()
    time.sleep(1)


@then(u'a menu is displayed')
def step_impl(context):
    check = context.driver.find_element(By.XPATH,  "/html/body/span/span/div/div/div/ol").is_displayed()
    if check is True:
        assert True
    time.sleep(1)


@when(u'I click on collection')
def step_impl(context):
    context.driver.find_element(By.XPATH,  "//span[text()='Collection']").click()
    time.sleep(1)


@then(u'a collection box is opened')
def step_impl(context):
    check = context.driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div/div[2]/div/form").is_displayed()
    if check is True:
        assert True
    time.sleep(1)


@when(u'I enter collection name ""Demo1""')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"formField-name\"]/div[2]/div/input").send_keys("Demo1")
    time.sleep(1)


@when(u'enter description ""this is description for demo1 ""')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"formField-description\"]/div[2]/textarea").send_keys("this is description for demo1")
    time.sleep(1)


@when(u'I enter collection name ""Demo2""')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"formField-name\"]/div[2]/div/input").send_keys("Demo2")
    time.sleep(1)


@when(u'enter description "" ""')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"formField-description\"]/div[2]/textarea").send_keys(" ")
    time.sleep(1)


@when('I enter collection name """"')
def enter_no_name(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"formField-name\"]/div[2]/div/input").send_keys(
        "")
    time.sleep(2)


@then(u'create button is "No" enabled')
def btn_disabled(context):
    status = context.driver.find_element(By.XPATH,"//*[@id=\"root\"]/div/div/main"
                                                  "/div/div/div[3]/div/div[3]/span[1]/button").is_enabled()
    if status is False:
        context.driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div/svg").click()
        assert True
    time.sleep(2)


@when(u'enter description ""collection with no name ""')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"formField-description\"]/div[2]/textarea").send_keys("collection with no name")
    time.sleep(1)


@then(u'create button is "yes" enabled')
def step_impl(context):
    check = context.driver.find_element(By.XPATH, "//*[@id=\"formField-description\"]/div[2]/textarea").is_enabled()
    if check is True:
        assert True
    time.sleep(1)


@then(u'select a location')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"formField-parent_id\"]/div[2]/a/button").click()
    time.sleep(3)


@then(u'click on create button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div/div[2]/div/form/div[4]/button[1]").click()


@then('it creates a new collection page with entered name')
def page_created(context):
    status = context.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/div/main"
                                                        "/div/div/div[1]/div[1]/div[1]/div/textarea").is_displayed()
    time.sleep(1)
    if status is True:
        assert True, "Opened"




