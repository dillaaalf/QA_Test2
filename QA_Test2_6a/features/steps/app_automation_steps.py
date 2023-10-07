from behave import given, when, then
from appium import webdriver

@given("the Eureka app is installed on a mobile device")
def setup_mobile_app(context):
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "YOUR_ANDROID_VERSION",
        "deviceName": "YOUR_DEVICE_NAME",
        "appPackage": "com.eureka.eureka_kt",
        "appActivity": "com.eureka.eureka_kt.MainActivity",
        "automationName": "UiAutomator2",
    }
    
    context.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

@when("the user enters valid credentials and logs in")
def enter_valid_credentials(context):
    # Your automation code to interact with the mobile app goes here

@then("the user should be successfully logged in")
def verify_successful_login(context):
    # Your automation code to verify successful login goes here
    context.driver.quit()
