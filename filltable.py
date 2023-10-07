import sqlite3

bicep_workouts = [
  {
    "name": "Barbell Curls",
    "calorie_count": 75 
  },
  {  
    "name": "Hammer Curls", 
    "calorie_count": 65
  },
  {
    "name": "Cable Curls",
    "calorie_count": 85
  },
  {
    "name": "Concentration Curls", 
    "calorie_count": 65
  },
  {
    "name": "Zottman Curls",
    "calorie_count": 85
  },
  {
    "name": "Overhead Zottman Curls",
    "calorie_count": 70
  },
  {
    "name": "Preacher Curls",
    "calorie_count": 65
  },
  {
    "name": "Incline Dumbbell Curls",
    "calorie_count": 65
  }
]
chest_workouts = [
  {
    "name": "Barbell Bench Press", 
    "calorie_count": 110
  },
  {
    "name": "Incline Dumbbell Press",
    "calorie_count": 100
  },
  {
    "name": "Push Ups",
    "calorie_count": 80
  },
  {
    "name": "Decline Push Ups",
    "calorie_count": 90
  },
  {
    "name": "Chest Flys",
    "calorie_count": 80
  },
  {
    "name": "Cable Crossovers",
    "calorie_count": 90
  }
]
leg_workouts = [
  {
    "name": "Barbell Squats",
    "calorie_count": 155
  },
  {
    "name": "Leg Press",
    "calorie_count": 145
  },
  {
    "name": "Leg Extensions",
    "calorie_count": 100
  },
  {
    "name": "Leg Curls",
    "calorie_count": 90
  },
  {
    "name": "Calf Raises",
    "calorie_count": 65
  },
  {
    "name": "Lunges",
    "calorie_count": 140
  } 
]
shoulder_workouts = [
  {
    "name": "Overhead Press",
    "calorie_count": 110
  },
  {
    "name": "Lateral Raises",
    "calorie_count": 70
  },
  {
    "name": "Front Raises",
    "calorie_count": 60
  },
  {
    "name": "Rear Delt Fly", 
    "calorie_count": 80
  },
  {
    "name": "Arnold Press",
    "calorie_count": 90
  },
  {
    "name": "Face Pulls",
    "calorie_count": 70
  }
]
triceps_workouts = [
  {
    "name": "Close Grip Bench Press",
    "calorie_count": 130
  },
  {
    "name": "Triceps Pushdowns",
    "calorie_count": 90
  },
  {
    "name": "Lying Triceps Extensions",
    "calorie_count": 80
  },
  {
    "name": "Overhead Triceps Extensions",
    "calorie_count": 100
  },
  {
    "name": "Dips",
    "calorie_count": 90
  }
]
conn = sqlite3.connect('workouts.db')

cursor = conn.cursor()
cursor.execute('DELETE FROM WorkOuts')
# cursor.execute('CREATE TABLE WorkOuts (Type VARCHAR(255), WorkoutName VARCHAR(255), CalorieCount INTEGER)')

for workout in bicep_workouts:
    cursor.execute(f'INSERT INTO WorkOuts (Type, WorkoutName, CalorieCount) VALUES ("Bicep", "{workout["name"]}", "{workout["calorie_count"]}" )')

for workout in triceps_workouts:
    cursor.execute(f'INSERT INTO WorkOuts (Type, WorkoutName, CalorieCount) VALUES ("Tricept", "{workout["name"]}", "{workout["calorie_count"]}" )')

for workout in chest_workouts:
    cursor.execute(f'INSERT INTO WorkOuts (Type, WorkoutName, CalorieCount) VALUES ("Chest", "{workout["name"]}", "{workout["calorie_count"]}" )')
    
for workout in leg_workouts:
    cursor.execute(f'INSERT INTO WorkOuts (Type, WorkoutName, CalorieCount) VALUES ("Legs", "{workout["name"]}", "{workout["calorie_count"]}" )')
    
for workout in shoulder_workouts:
    cursor.execute(f'INSERT INTO WorkOuts (Type, WorkoutName, CalorieCount) VALUES ("Shoulder", "{workout["name"]}", "{workout["calorie_count"]}" )')
    
conn.commit()

# Fetch and print the inserted data
# cursor.execute('SELECT * FROM WorkOuts')
# for row in cursor.fetchall():
#     print(row)
    
cursor.execute("SELECT * FROM WorkOuts WHERE Type = 'Bicep'")
for row in cursor.fetchall():
    print(row)

conn = sqlite3.connect('workouts.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE WorkOuts (Type VARCHAR(255), WorkoutName VARCHAR(255), CalorieCount INTEGER)')

conn.close()
