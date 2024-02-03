# Behave_BDD_Framework

# Run the Features

To run all features

`behave ./features`

In order to run the features after creation, with Allure - use on of the below commands:

`behave -f allure_behave.formatter:AllureFormatter -o reports/ features`

`allure serve reports/`

To run specific tags:

`behave features --tags=regression`

