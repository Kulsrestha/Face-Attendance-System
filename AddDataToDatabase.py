import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-attendance-system-cd7d4-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "128745":
        {
            "name": "Kulsrestha Joshi",
            "major": "Computer Science",
            "starting_year": 2020,
            "total_attendance": 5,
            "grade": "G",
            "year": 4,
            "last_attendance_time": "2023-08-20 00:54:34"
        },
    "236789":
        {
            "name": "Narendra Modi",
            "major": "Politics",
            "starting_year": 2014,
            "total_attendance": 8,
            "grade": "G",
            "year": 8,
            "last_attendance_time": "2023-08-20 00:54:34"
        },
    "346789":
        {
            "name": "Elon Musk",
            "major": "Artificial Intelligence",
            "starting_year": 2016,
            "total_attendance": 4,
            "grade": "G",
            "year": 4,
            "last_attendance_time": "2023-08-20 00:54:34"
        },
    "563634":
        {
            "name": "Hrithik Roshan",
            "major": "Acting",
            "starting_year": 2000,
            "total_attendance": 5,
            "grade": "G",
            "year": 4,
            "last_attendance_time": "2023-08-20 00:54:34"
        }
}

for key,value in data.items():
    ref.child(key).set(value)