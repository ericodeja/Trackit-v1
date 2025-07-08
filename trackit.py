import json
from datetime import date, datetime, timedelta
import calendar
import sys


status = ["Not Started", "Completed"]
database = {}
file_path = "habits.json"
frequency = ["hourly", "daily", "weekly", "monthly", "yearly"]


try:
    with open(file_path, "r") as file:
        data = json.load(file)
    for key, value in data.items():
        database[key] = {"streak": value["streak"],
                         "log": value["log"],
                         "frequency": {
            "type": value["frequency"]["type"],
            "time_left": value["frequency"]["time_left"]
        }
        }
except ValueError:
    pass
except FileNotFoundError:
    pass


def add_habit():
    habit_list = []
    habit = input("Enter habit name(s) (separate with commas): ").title()
    if not habit:
        print("\n--Input a habit")
    else:
        for item in habit.split(","):
            habit_list.append(item)

    # Checking if habit already exists and check if input is empty
    for key in database.keys():
        if key in habit_list:
            habit_list.remove(key)
            print(f"'{key}' already exists.")

    def frequency_conditions(choice):
        found = False
        for item in frequency:
            if choice == item:
                found = True
                return item
        if not found:
            print("Enter a valid frequency")

    # Adding to database
    for item in habit_list:
        choice = input(
            f"\nEnter frequency of habit '{item}' -> {frequency}:")
        database[item] = {"streak": 0,
                          "log": [],
                          "frequency": {"type": frequency_conditions(choice),
                                        "time_left": None

                                        }
                          }
        print(f"Habit '{item}' added.\n")
    save_program()


def time_left(type):
    now = datetime.now()
    today = date.today()
    day = today.day
    year = today.year
    month = today.month
    week_indx = today.weekday()

    if type == "hourly":
        next_hour = (now + timedelta(hours=1)).replace(minute=0,
                                                       second=0, microsecond=0)
        remaining = next_hour - now
        minutes = remaining.seconds // 60
        return minutes, "minutes(s)"

    elif type == "daily":
        next_day = (now + timedelta(days=1)
                    ).replace(hour=0, minute=0, second=0)
        time_left_delta = next_day - now
        hour = time_left_delta.seconds // 3600
        return hour, "hour(s)"

    elif type == "weekly":
        days_left = 6 - week_indx
        message = 6 if week_indx == 6 else days_left
        return message, "day(s)"

    elif type == "monthly":
        month_range = calendar.monthrange(year, month)[1]
        days_left = month_range - day
        return days_left, "day(s)"

    elif type == "yearly":
        last_day = date(year, 12, 31)
        days_left = (last_day - today).days
        return days_left, "day(s)"


def update_status():
    # Check if the database is empty
    if not database:
        print("!You have no saved habit")
        return

    # Find habit
    found = False
    habit = input("Enter habit name: ").title()
    for key, value in database.items():
        if habit == key:
            found = True
            # Habit Found
            remaining_time = value["frequency"]["time_left"]
            try:
                # Update Status
                # Checking if user can update status
                if remaining_time:
                    remaining, root = remaining_time
                    message = f"You have {remaining} {root} left."
                    print(message)
                else:
                    # Updating Status
                    new_status = input(
                        "Update Status ['completed']: ").title()
                    # Updating Log
                    if new_status in status:
                        value["log"].append(str(date.today()))
                        value["streak"] = len(value["log"])

                        # User Feedback
                        print(
                            f"{habit} marked as completed for {date.today()}")

                        # Updating Time Left
                        time_range = time_left(value["frequency"]["type"])
                        value["frequency"]["time_left"] = time_range
                        break

                    else:
                        print("Invalid Input")
            except ValueError:
                print("Invalid input")
    if not found:
        print("Invalid habit ID.")
    save_program()


def view_progress():
    if not database:
        print("!You have no saved habit")
        return

    found = False
    habit = input("Enter habit name: ").title()
    for key, value in database.items():
        if habit == key:
            found = True
            streak = value["streak"]
            month = streak // 30
            week = (streak % 30) // 7
            day = (streak % 30) % 7

            if month:
                print(
                    f"You are on a {month} month(s), {week} week(s) and {day} day(s) streak")
            elif week:
                print(f"You are on {week} week(s) and {day} day(s) streak")
            elif day:
                print(f"You are on a {day} day(s) streak")
            elif streak == 0:
                print("0 days")
    if not found:
        print("Invalid habit ID.")


def exit_program():
    while True:
        option = input("Do you want to exit the program? (y/n): ").lower()
        if option == "y" or option == "yes":
            print("Exiting Program...")
            with open(file_path, "w") as file:
                json.dump(database, file, indent=4)
            sys.exit()
        elif option == "n" or option == "no":
            continue
        else:
            print("Enter a valid response (y/n)")


def clear_program():
    option = input("Do you want to clear the program? (y/n): ").lower()
    if option == "y" or option == "yes":
        print("Clearing database....")
        save_program()
        database.clear()
    elif option == "n" or option == "no":
        return
    else:
        print("Enter a valid response y/n")
    save_program()


def save_program():
    with open(file_path, "w") as file:
        json.dump(database, file, indent=4)


def edit_key():
    if not database:
        print("!You have no saved habit")
        return

    habit_name = ""
    found = False
    habit = input("Input habit: \n").title()
    for key in database.keys():
        if key == habit:
            found = True
            habit_name = key

    if found == True:
        edited_habit = input("Enter the new habit: \n").title()
        database[edited_habit] = database[habit_name]
        del database[habit_name]
        print(f"\n{habit_name} has been renamed\n")

    else:
        print("\nHabit doesn't exist\n")
    save_program()


def view_database():

    if not database:
        print("!You have no saved habits.")
        return

    print(f"{"Habit":<20}{"Type":<10}{"Time Left":<25}{"Streak":<25}{"Log":<25} ")
    print("-" * 70)

    for habits, info in database.items():
        time_left = info["frequency"]["time_left"]
        freq_type = info["frequency"]["type"]

        if time_left:
            time_left = f"{time_left[0]} {time_left[1]}"
        else:
            time_left = "N/A"

        log = ", ".join(info["log"]) if info["log"] else "-"

        print(
            f"{habits:<20}{freq_type:<10}{time_left:<25}{info['streak']:<25}{log:<25}")


actions = [add_habit, update_status,
           view_progress, view_database, edit_key, clear_program, exit_program]


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
