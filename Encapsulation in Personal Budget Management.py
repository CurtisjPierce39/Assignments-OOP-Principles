class BudgetCategory:   #Question 1 Task 1
    # Constructor and private attributes
    # ...
    def __init__(self):
        self._categories = {
            "Food": 0,
            "Entertainment": 0,
            "Utilities": 0,
            "Transportation": 0,
            "Housing": 0,
            "Other": 0
        } 
        self._current_month_budget = {}
    # Getters and setters for category name and budget
    # ...
    def set_budget_for_category(self, category, amount): #Question 1 Task 2

        if category in self._categories:
            self._categories[category] = amount
            self._current_month_budget[category] = 0
        else:
            print("Invalid category")

    def add_expense(self, category, amount): #Question 1 Task 3
        # Method to add an expense to the category
        # ...
        if category in self._categories:
            self._categories[category] += amount
        else:
            print("Invalid category")

    def display_category_summary(self): #Question 1 Task 4
        # Method to display the budget category details
        # ...
        for category, balance in self._categories.items():
            print(f"{category}: ${balance}")

new_category = BudgetCategory()
new_category.add_expense('Utilities', 200)
new_category.add_expense('Housing', 1500)
new_category.add_expense('Food', 500)
new_category.add_expense('Food', 100)
new_category.display_category_summary()