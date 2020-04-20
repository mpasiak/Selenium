Feature: Task 1

    Scenario Outline: delete item from basket
    Given I added random product to basket
    When I delete it
    Then Nothing is in basket