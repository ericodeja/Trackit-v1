from habit_tracker import add_habit, update_status, view_progress, clear_program, edit_habit, view_database, exit_program


def add():
    name = input("Enter habit name(s)\nSeparate with commas: ").title()
    habit = add_habit(name)
    print(f"'{habit}' has been added.")


def completed():
    name = input("Enter habit name: ").title()
    status = update_status(name)
    print(f"'{name}' marked as completed for {str(status)}")


def habit_progress():
    name = input("Enter habit name: ").title()
    view_progress(name)


def edit():
    option = input("What do you want to edit?\n[Habit / Frequency]: ").title()
    name = input("Enter habit name: ").title()
    value = input("Enter the new value: ").title()
    edit_habit(option, name, value)
    


actions = [add, completed,
           habit_progress, view_database, edit, clear_program, exit_program]


while True:
    print("\n=== Welcome to your habit tracker ===\n")
    print("1. Add Habit")
    print("2. Update Progress")
    print("3. View Streak")
    print("4. View All Habits")
    print("5. Edit")
    print("6. Clear")
    print("7. Exit")

    try:
        option = int(input("\nChoose an option 1 - 7: "))
        actions[option - 1]()
        if 1 < option > 7:
            print("Input a valid number 1 - 7")
    except ValueError:
        print("Input a  number 1 - 7")


