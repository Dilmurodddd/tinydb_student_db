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
    "id": 2,
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
student3 = {
    "id": 3,
    "name": "Madina Karimova",
    "age": 15,
    "gender": "Female",
    "contact": "998-91-987-65-43",
    "grade_level": "Grade 9",
    "subjects": {
        "math": 78,
        "science": 85,
        "english": 92
    },
    "attendance": 97.5,
    "activities": ["Piyano", "Voleybol"],
    "address": {
        "street": "Shodlik ko'chasi",
        "city": "Samarqand",
        "state": "Samarqand viloyati",
        "zip_code": "140100"
    }
}

student4 = {
    "id": 4,
    "name": "Rustam Saidov",
    "age": 17,
    "gender": "Male",
    "contact": "998-93-222-33-44",
    "grade_level": "Grade 11",
    "subjects": {
        "math": 92,
        "science": 89,
        "english": 90
    },
    "attendance": 94.0,
    "activities": ["Basketbol", "Debat Klubi"],
    "address": {
        "street": "Amir Temur shohko'chasi",
        "city": "Buxoro",
        "state": "Buxoro viloyati",
        "zip_code": "200600"
    }
}
student5 = {
    'id':5,
    'name':"Nodira Zayniddinova",
    "age":23,
    "gender":"Female",
    "contact":"+998-96-524-32-35",
    "grade_level":"Grade 10",
    "subjects":{
        "math":88,
        "science":90,
        "english":85
    },
    "attendance":96.0,
    "activites":["Raqs", "Kitob o'qish"],
    "address":{
        "street":"Gagarin ko'chasi",
        "city":"Farg'ona",
        "state":"Farg'ona vilayati",
        "zip_code":"152200"
    }

}