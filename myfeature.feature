Feature: add new Collection
    Scenario Outline: User successfully creates a new collection
      Given I launch chrome browser
      And  open metabase website
      And I am logged in my metabase account
      When I click on personal account option
      Then personal collection page opens
      When I click on create new button
      Then a menu is displayed
      When I click on collection
      Then a collection box is opened
     When I enter collection name "<name>"
      And enter description "<description>"
     Then create button is "<enable>" enabled
     And select a location
      And click on create button
      Then it creates a new collection page with entered name

      Examples:
      | name       | description                            | enable |
      | "Demo1"    | "this is description for demo1 "       | yes    |
      | "Demo2"    | " "                                    | yes    |
      | ""         | "collection with no name "             | No     |
      | ""         | " "                                    | No     |