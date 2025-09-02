# 📈 Trackit

Trackit is a simple yet powerful CLI-based habit tracker that helps you build consistency and stay accountable to your daily routines.
Whether you're tracking your meditation, workouts, or reading, Trackit makes habit tracking effortless right from your terminal.

---

## 🚀 Features

- ✅ Add and remove habits
- 📅 Daily check-ins with streak tracking
- 📊 View current status and streaks
- 🧠 Monthly reset logic
- 💾 Data stored in a JSON file (local storage)

---

## 📂 Project Structure

```
trackit/
├── data/
│   └── habits.json        # Stores user habits and streaks
├── trackit.py             # Main script to run the CLI
├── utils.py               # Helper functions
└── README.md              # You're reading this!
```

---

## 🛠️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ericodeja/trackit.git
cd trackit
```

### 2. Run the App

```bash
python trackit.py
```

---

## 💡 How to Use

- Add a habit: Add a new habit you want to track.
- Mark as done: Each day, check in and mark your progress.
- View stats: See your current streaks and habits list.

---

## 🧪 Example Habit JSON

```json
{
  "Workout": {
        "streak": 1,
        "log": [
            "2025-07-07"
        ],
        "frequency": {
            "type": "daily",
            "time_left": [
                10,
                "hour(s)"
            ]
        }
    },
    "Read": {
        "streak": 0,
        "log": [],
        "frequency": {
            "type": "hourly",
            "time_left": null
        }
    },
```

---

## 📦 Dependencies

- Python 3.7+
- datetime (built-in)
- json (built-in)

No external libraries needed!

---

## 🔒 Data Privacy

All your data is stored locally on your machine. No internet connection or account required. Your habits, your rules.

---

## 📌 Future Upgrades

- [ ] PostgreSQL support for persistent storage  
- [ ] Web or API interface  
- [ ] Reminders/notifications  
- [ ] Statistics dashboard

---

## 👨‍💻 Author

Built with consistency and clarity by https://github.com/ericodeja
"This was my first version of TrackIt using JSON files as storage. The upgraded version with a real database and production-ready backend is https://github.com/ericodeja/Trackit-v2.git."

---

## 🧘‍♂️ Stay Disciplined

> “You do not rise to the level of your goals. You fall to the level of your systems.”  
> — James Clear
