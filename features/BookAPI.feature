# Created by rfnsh at 2/2/2023
Feature: Verify Books Added & Deleted using library API
  # Enter feature description here
  @smoke
  Scenario: Verify AddBook API Functionality
    Given the book details which needs to be added to library
    When we execute the AddBook PostAPI method
    Then book is successfully added
    And Status Code of response should be 200

  @regression
  Scenario Outline: Verify AddBook API Functionality
    Given the book details with <isbn> & <aisle>
    When we execute the AddBook PostAPI method
    Then book is successfully added
    And Status Code of response should be 200
      Examples:
        | isbn  | aisle |
        | qwer  | 7894  |
        | zxcv  | 5464  |

# behave features/BookAPI.feature --no-capture --tags=regression