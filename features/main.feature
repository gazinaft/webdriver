Feature: lab is done

  Scenario Outline: Brief <title> retell
    Given I prefer DuckDuckGo to Google
    And want to read <title> quickly
      When I open Briefly website
      Then author is <author>
      And it was written in <year>


  Examples: Titles
    | title     | author            | year |
    | Палата №6 | Антон Чехов       | 1892 |
    | Идиот     | Фёдор Достоевский | 1868 |