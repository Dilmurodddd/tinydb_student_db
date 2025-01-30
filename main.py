from tinydb import TinyDB, Query

# Create or connect to the database
db = TinyDB('students.json')

# Reference the default table
students1 = {
    "id": 1,
    "name": "John Doe",
    "age": 16,
    "gender": "Male",
    "contact": "123-456-7890",
    "grade_level": "Grade 10",
    "subjects": {
        "math": 85,
        "science": 90,
        "english": 88
    },
    "attendance": 92.5,
    "activities": ["Basketball", "Debate Club"],
    "address": {
        "street": "123 Main St",
        "city": "Springfield",
        "state": "IL",
        "zip_code": "62704"
    }
}
ssdunet2 = {
    "id": 1,
    "name": "Ali Hasanov",
    "age": 16,
    "gender": "Male",
    "contact": "998-90-123-45-67",
    "grade_level": "Grade 10",
    "subjects": {
        "math": 87,
        "science": 91,
        "english": 85
    },
    "attendance": 95.0,
    "activities": ["Football", "Chess Club"],
    "address": {
        "street": "Yangiobod ko'chasi",
        "city": "Toshkent",
        "state": "Toshkent shahri",
        "zip_code": "100011"
    }
}




