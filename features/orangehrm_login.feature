Feature: OrangeHRM Login

  Scenario: Login to OrangeHRM with given parameters
    Given I launch the chrome browser
    When I open the OrangeHRM homepage
    And Enter username Admin and password admin123
    And Click login button
    Then User must successfully login to the Dashboard page


  Scenario Outline: Login to OrangeHRM with given parameters
    Given I launch the chrome browser
    When I open the OrangeHRM homepage
    And Enter username <username> and password <password>
    And Click login button
    Then User must successfully login to the Dashboard page

    Examples:
      | username | password |
      | admin    | admin123 |
      | admin123 | admin    |
      | Admin    | admin234 |