Feature: OrangeHRM Logo
  Scenario: Logo presence on HRM homepage
    Given launch chrome browser
    When open orange hrm homepage
    Then verify logo is present on homepage
    And close browser

