Feature: Test Scenarios for product interaction


  Scenario: User can open market tab and filter by developers option
    Given Open the main page
    When Login to the page
    And Click on “market” at the left side menu
    Then Verify the right page opens
    When Click on Developers filter at the top of the page
    Then Verify all cards has the license tag Developers