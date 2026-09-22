def build_task_summary(tasks):
    """Return a summary of tasks grouped by status."""
    pass


def organize_files(files):
    """Group a list of filenames by extension."""
    pass


def calculate_expenses(expenses):
    """Return totals per category and overall total."""
    pass


if __name__ == "__main__":
    sample_tasks = [
        {"name": "Estudar Python", "priority": "high", "done": True},
        {"name": "Lavar louça", "priority": "low", "done": False},
        {"name": "Fazer exercícios", "priority": "high", "done": True},
        {"name": "Organizar mochila", "priority": "medium", "done": False},
    ]

    sample_files = ["notes.txt", "main.py", "data.csv", "image.png", "README"]

    sample_expenses = [
        {"category": "food", "amount": 25.50},
        {"category": "transport", "amount": 12.00},
        {"category": "food", "amount": 10.75},
        {"category": "books", "amount": 30.00},
    ]

    print(build_task_summary(sample_tasks))
    print(organize_files(sample_files))
    print(calculate_expenses(sample_expenses))
