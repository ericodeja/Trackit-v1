from storage import all_habits


class Habit:
    habit_list = {}
    # habit_list.update(all_habits)
    habit_list.update(all_habits)

    def __init__(self, name, frequency, streak=0, log=[], time_left=(0, "")):

        self.name = name
        self.frequency = frequency
        self.streak = streak
        self.log = log
        self.time_left = time_left

        self.add_item()

    def add_item(self):
        Habit.habit_list[self.name] = {
            "streak": self.streak,
            "frequency": self.frequency,
            "log": self.log,
            "time_left": self.time_left
        }

    def get_properties(self):
        return {
            "name": self.name,
            "streak": self.streak,
            "frequency": self.frequency,
            "log": self.log,
            "time_left": self.time_left
        }

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name}, {self.frequency})"
