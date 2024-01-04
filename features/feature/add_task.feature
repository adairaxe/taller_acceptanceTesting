Feature: Add a task to the to-do list

  Scenario: User adds a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"

  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks:
      | Task          |
      | Buy groceries |
      | Pay bills     |
    When the user lists all tasks
    Then the output should contain:
      """
      Tasks:
      - Buy groceries
      - Pay bills
      """

  Scenario: Mark a task as completed
    Given the to-do list contains tasks:
    | Task | Status |
    | Buy groceries | Incomplete |
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed

  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks:
      | Task |
      | Buy groceries |
      | Pay bills |
    When the user clears the to-do list
    Then the to-do list should be empty

  Scenario: User changes the description of a task
    Given the to-do list contains tasks:
      | Task          | Description  |
      | Buy groceries | Grocery list |
    When the user changes the description of task "Buy groceries" to "Shopping for food"
    Then the to-do list should show task "Buy groceries" with description "Shopping for food"

  Scenario: User performs a special action on a task
    Given the to-do list contains tasks:
      | Task      |
      | Pay bills |
    When the user performs a special action on task "Pay bills"
    Then the special action should have the desired effect on task "Pay bills"


