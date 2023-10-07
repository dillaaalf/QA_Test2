Feature: Eureka Mobile App Automation

  Scenario: Verify login functionality
    Given the Eureka app is installed on a mobile device
    When the user enters valid credentials and logs in
    Then the user should be successfully logged in
