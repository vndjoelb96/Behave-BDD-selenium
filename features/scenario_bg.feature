Feature: OrangeHRM Login

  Background: common steps
    Given I launch the chrome browser
    When I open the OrangeHRM homepage
    And Enter username Admin and password admin123
    And Click login button

  @regression
  Scenario: Login to OrangeHRM with given parameters
    Then User must successfully login to the Dashboard page

  @search @smoke
  Scenario: Search User
    When Navigate to search page
    Then search page should display

  @search @regression
  Scenario: Advanced Search User
    When Navigate to advanced search page
    Then advanced search page should display