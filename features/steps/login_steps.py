from behave import given, when, then
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@given("the user is on the Eureka Edutech login page")
def open_login_page(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.get("https://www.eurekaedutech.com/")

@when("the user enters valid credentials")
def enter_valid_credentials(context):
    # Your automation code to enter valid credentials goes here

@then("the user should be logged in successfully")
def verify_successful_login(context):
    # Your automation code to verify successful login goes here
    context.driver.quit()
