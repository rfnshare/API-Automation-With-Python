# Created by rfnsh at 2/3/2023
Feature: GitHub API Validation
  # Enter feature description here

  Scenario: Session Management Check
    Given I Have Github Auth Credentials
    When I Hit GitRepo API of Github
    Then Status Code of response should be 200