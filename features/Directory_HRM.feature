Feature: OrangeHRM Enter Directory

  Background: common steps
    Given I launch the chrome browser
    When I open the OrangeHRM homepage
    And Enter username Admin and password admin123
    And Click login button

  Scenario: Search and verify admin user
    When navigate to Admin tab
    Then Enter user admin
    And  Click Search and verify

