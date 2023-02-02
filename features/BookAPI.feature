# Created by rfnsh at 2/2/2023
Feature: Verify Books Added & Deleted using library API
  # Enter feature description here

  Scenario: Verify AddBook API Functionality
    Given the book details which needs to be added to library
    When we execute the AddBook PostAPI method
    Then book is successfully added