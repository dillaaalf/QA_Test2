import pytest
from appium import webdriver

@pytest.fixture(scope="function")
def appium_driver(request):
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "YOUR_ANDROID_VERSION",
        "deviceName": "YOUR_DEVICE_NAME",
        "appPackage": "com.eureka.eureka_kt",
        "appActivity": "com.eureka.eureka_kt.MainActivity",
        "automationName": "UiAutomator2",
    }
    
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    request.cls.driver = driver
    yield driver
    driver.quit()
