from habits import Habit
from storage import write_db
from utils import next_hour, next_day, last_day, month_range, week_days_left, now, today, week_indx, day
import sys


frequency_list = ["Hourly", "Daily", "Weekly", "Monthly", "Yearly"]


def add_habit(name):
    # Check if name is empty
    if not name:
        print("!Habit cannot be empty")
        return

    habits = [part.strip() for part in name.split(",")]

    # Check if habit already exists
    for key in Habit.habit_list.keys():
        if key in habits:
            habits.remove(key)
            message = f"'{key}' already exists"
            print(message)

    # Get frequency of habit and add it to to the JSON file
    for habit in habits:
        frequency = input(
            f"Enter a frequency for '{habit}'\n{frequency_list}").title()

        if frequency == "":
            frequency = "Daily"
        if frequency in frequency_list:
            Habit(habit, frequency)
            write_db(Habit.habit_list)

        else:
            print(f"Invalid input -> {frequency}")
            return False
    return habits


def time_left(type):
    # Countdown
    if type == frequency_list[0]:
        remaining = next_hour - now
        minutes = remaining.seconds // 60
        return minutes, "minutes(s)"

    elif type == frequency_list[1]:
        remaining = next_day - now
        hour = remaining.seconds // 3600
        return hour, "hour(s)"

    elif type == frequency_list[2]:
        message = 6 if week_indx == 6 else week_days_left
        return message, "day(s)"

    elif type == frequency_list[3]:
        remaining = month_range - day
        return remaining, "days(s)"

    elif type == frequency_list[4]:
        remaining = (last_day - today).days
        return remaining, "day(s)"


def get_properties(name):
    if not Habit.habit_list:
        print("!You have no saved habit")
        return

    for key, value in Habit.habit_list.items():
        if name == key:
            return value

    print(f"No habit found with name: {name}")
    return None


def update_status(name):
    properties = get_properties(name)

    if properties:
        # Update Log
        properties["log"].append(str(today))
        properties["streak"] += 1

        # Update Time_Left
        countdown = time_left(properties["frequency"])
        properties["time_left"] = countdown

        write_db(Habit.habit_list)
        return today


def view_progress(name):
    properties = get_properties(name)
    if properties:
        return f"'{name}' has a {properties["streak"]} day(s) streak"

    write_db(Habit.habit_list)


def exit_program():
    option = input("Do you want to exit the program? (y/n): ").lower()
    if option == "y" or option == "yes":
        print("Exiting Program...")
        write_db(Habit.habit_list)
        sys.exit()
    elif option == "n" or option == "no":
        return
    else:
        print("Enter a valid response (y/n)")


def clear_program():
    option = input("Do you want to clear the program? (y/n): ").lower()
    if option == "y" or option == "yes":
        print("Clearing database....")
        Habit.habit_list.clear()
        write_db(Habit.habit_list)
    elif option == "n" or option == "no":
        return
    else:
        print("Enter a valid response y/n")


def edit_habit(option, name, value):
    def edit_name(name, value):
        Habit.habit_list[value] = Habit.habit_list[name]
        del Habit.habit_list[name]
        write_db(Habit.habit_list)
        print("Updated")

    def edit_frequency(name, value):
        if value == "":
            value = "Daily"
        if value in frequency_list:
            Habit.habit_list[name]["frequency"] = value
            print("Updated")

    if not Habit.habit_list:
        print("!You have no saved habit")
        return

    found = False
    for key in Habit.habit_list.keys():
        if name == key:
            found = True
        if value == key:
            print(f"'{value}' already exists.")
            return

    if not found:
        print(f"'{name}' doesn't exist.")

    if found:
        if option == "Habit":
            edit_name(name, value)
        elif option == "Frequency":
            edit_frequency(name, value)
        else:
            print("!Invalid input")

    write_db(Habit.habit_list)


def view_database():

    if not Habit.habit_list:
        print("!You have no saved habits.")
        return

    print(f"{"Habit":<20}{"Type":<10}{"Time Left":<25}{"Streak":<25}{"Log":<25} ")
    print("-" * 70)

    for key, value in Habit.habit_list.items():
        time_left = value["time_left"]
        freq_type = value["frequency"]

        if time_left:
            time_left = f"{time_left[0]} {time_left[1]}"
        else:
            time_left = "N/A"

        log = ", ".join(value["log"]) if value["log"] else "-"

        print(
            f"{key:<20}{freq_type:<10}{time_left:<25}{value['streak']:<25}{log:<25}")
