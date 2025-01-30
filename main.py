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

},
student6 ={
    "id": 6,
    "name": "Javlonbek Tashkentov",
    "age": 15,
    "gender": "Male",
    "contact": "998-95-123-45-67",
    "grade_level": "Grade 9",
    "subjects": {
        "math": 80,
        "science": 78,
        "english": 82
    },
    "attendance": 95.5,
    "activities": ["Shaxmat", "Rassomlik"],
    "address": {
        "street": "Ko'kcha ko'chasi",
        "city": "Andijon",
        "state": "Andijon viloyati",
        "zip_code": "170200"
    }
},
student7 = {
    "id": 7,
    "name": "Shahnoza Baxtiyorova",
    "age": 14,
    "gender": "Female",
    "contact": "998-91-456-78-90",
    "grade_level": "Grade 8",
    "subjects": {
        "math": 86,
        "science": 88,
        "english": 87
    },
    "attendance": 98.0,
    "activities": ["Teatr", "Piyano"],
    "address": {
        "street": "Almazar ko'chasi",
        "city": "Toshkent",
        "state": "Toshkent shahri",
        "zip_code": "100500"
    }
},
student8 = {
    "id": 8,
    "name": "Dilorom Raxmonova",
    "age": 16,
    "gender": "Female",
    "contact": "998-93-234-56-78",
    "grade_level": "Grade 10",
    "subjects": {
        "math": 92,
        "science": 89,
        "english": 90
    },
    "attendance": 96.5,
    "activities": ["Fotografiya", "Voleybol"],
    "address": {
        "street": "Toshkent ko'chasi",
        "city": "Navoiy",
        "state": "Navoiy viloyati",
        "zip_code": "210100"
    }
},
student9 = {
    "id": 9,
    "name": "Olimjon Azimov",
    "age": 17,
    "gender": "Male",
    "contact": "998-92-345-67-89",
    "grade_level": "Grade 11",
    "subjects": {
        "math": 93,
        "science": 94,
        "english": 89
    },
    "attendance": 93.0,
    "activities": ["Fotografiya", "Skripka"],
    "address": {
        "street": "Bodomzor ko'chasi",
        "city": "Qarshi",
        "state": "Qashqadaryo viloyati",
        "zip_code": "180100"
    }
},
student10 = {
    "id": 9,
    "name": "Gulnoza Ismoilova",
    "age": 14,
    "gender": "Female",
    "contact": "998-90-654-32-10",
    "grade_level": "Grade 9",
    "subjects": {
        "math": 79,
        "science": 83,
        "english": 86
    },
    "attendance": 92.0,
    "activities": ["Teatr", "Raqs"],
    "address": {
        "street": "Qo'qon ko'chasi",
        "city": "Qo'qon",
        "state": "Farg'ona viloyati",
        "zip_code": "150200"
    }
},
students11 = {
    "id": 10,
    "name": "Bunyodbek Kamilov",
    "age": 16,
    "gender": "Male",
    "contact": "998-91-543-21-09",
    "grade_level": "Grade 10",
    "subjects": {
        "math": 85,
        "science": 91,
        "english": 88
    },
    "attendance": 95.5,
    "activities": ["Basketbol", "Shaxmat"],
    "address": {
        "street": "Shahrisabz ko'chasi",
        "city": "Toshkent",
        "state": "Toshkent shahri",
        "zip_code": "100015"
    }
},
students12 = {
    "id": 11,
    "name": "Zaynab Muxtorova",
    "age": 15,
    "gender": "Female",
    "contact": "998-94-212-34-56",
    "grade_level": "Grade 9",
    "subjects": {
        "math": 82,
        "science": 86,
        "english": 90
    },
    "attendance": 96.0,
    "activities": ["Raqs", "Kitob o'qish"],
    "address": {
        "street": "Bog'ishamol ko'chasi",
        "city": "Namangan",
        "state": "Namangan viloyati",
        "zip_code": "160100"
    }
},
students13 = {
    "id": 12,
    "name": "Bahromjon Sirojov",
    "age": 16,
    "gender": "Male",
    "contact": "998-90-789-01-23",
    "grade_level": "Grade 10",
    "subjects": {
        "math": 90,
        "science": 88,
        "english": 85
    },
    "attendance": 94.5,
    "activities": ["Kanoe", "Shaxmat"],
    "address": {
        "street": "G'azalkent ko'chasi",
        "city": "Jizzax",
        "state": "Jizzax viloyati",
        "zip_code": "170100"
    }
},
students14 = {
    "id": 13,
    "name": "Shavkatbek Yunusov",
    "age": 17,
    "gender": "Male",
    "contact": "998-93-456-78-90",
    "grade_level": "Grade 11",
    "subjects": {
        "math": 95,
        "science": 92,
        "english": 88
    },
    "attendance": 97.0,
    "activities": ["Futbol", "Voleybol"],
    "address": {
        "street": "Bodur ko'chasi",
        "city": "Toshkent",
        "state": "Toshkent shahri",
        "zip_code": "100016"
    }
},
students15 = {
    "id": 15,
    "name": "Samar Rakhmonov",
    "age": 15,
    "gender": "Male",
    "contact": "998-91-123-45-67",
    "grade_level": "Grade 9",
    "subjects": {
        "math": 85,
        "science": 88,
        "english": 80
    },
    "attendance": 95.0,
    "activities": ["Basketbol", "Piyano"],
    "address": {
        "street": "Bahor ko'chasi",
        "city": "Xiva",
        "state": "Xorazm viloyati",
        "zip_code": "220100"
    }
},
students16 = {
    "id": 16,
    "name": "Dilnoza Mirzaeva",
    "age": 22,
    "gender": "Female",
    "contact": "998-94-567-89-01",
    "grade_level": "Grade 10",
    "subjects": {
        "math": 88,
        "science": 84,
        "english": 87
    },
    "attendance": 94.5,
    "activities": ["Fotografiya", "Raqs"],
    "address": {
        "street": "Yusufbek ko'chasi",
        "city": "Toshkent",
        "state": "Toshkent shahri",
        "zip_code": "100021"
    }
},
students17= {
    "id": 17,
    "name": "Jasurbek Umarov",
    "age": 17,
    "gender": "Male",
    "contact": "998-93-123-45-67",
    "grade_level": "Grade 11",
    "subjects": {
        "math": 90,
        "science": 89,
        "english": 84
    },
    "attendance": 96.0,
    "activities": ["Shaxmat", "Basketbol"],
    "address": {
        "street": "O'zbekiston ko'chasi",
        "city": "Sirdaryo",
        "state": "Sirdaryo viloyati",
        "zip_code": "120100"
    }
},
students18 = {
    "id": 18,
    "name": "Maksuda Tohirova",
    "age": 14,
    "gender": "Female",
    "contact": "998-90-987-65-43",
    "grade_level": "Grade 9",
    "subjects": {
        "math": 82,
        "science": 86,
        "english": 88
    },
    "attendance": 97.5,
    "activities": ["Voleybol", "Piyano"],
    "address": {
        "street": "Navro'z ko'chasi",
        "city": "Farg'ona",
        "state": "Farg'ona viloyati",
        "zip_code": "150300"
    }
},
students19 = {
    "id": 19,
    "name": "Bekzod Yusupov",
    "age": 15,
    "gender": "Male",
    "contact": "998-91-789-01-23",
    "grade_level": "Grade 9",
    "subjects": {
        "math": 80,
        "science": 89,
        "english": 83
    },
    "attendance": 95.5,
    "activities": ["Basketbol", "Kompyuter o'yinlari"],
    "address": {
        "street": "Shayxontohur ko'chasi",
        "city": "Toshkent",
        "state": "Toshkent shahri",
        "zip_code": "100014"
    }
},
students20 = {
    "id": 20,
    "name": "Suhrobbek Mamadaliyev",
    "age": 16,
    "gender": "Male",
    "contact": "998-92-345-67-89",
    "grade_level": "Grade 10",
    "subjects": {
        "math": 88,
        "science": 85,
        "english": 90
    },
    "attendance": 96.0,
    "activities": ["Voleybol", "Shaxmat"],
    "address": {
        "street": "Mirobod ko'chasi",
        "city": "Buxoro",
        "state": "Buxoro viloyati",
        "zip_code": "200500"
    }
},
students21 = {
    "id": 21,
    "name": "Muxtorbek Islomov",
    "age": 14,
    "gender": "Male",
    "contact": "998-90-234-56-78",
    "grade_level": "Grade 9",
    "subjects": {
        "math": 86,
        "science": 81,
        "english": 87
    },
    "attendance": 97.0,
    "activities": ["Shaxmat", "Raqs"],
    "address": {
        "street": "Bunyodkor ko'chasi",
        "city": "Toshkent",
        "state": "Toshkent shahri",
        "zip_code": "100017"
    }
},
students22 = {
    "id": 22,
    "name": "Mokhira Kholmatova",
    "age": 16,
    "gender": "Female",
    "contact": "998-91-234-56-78",
    "grade_level": "Grade 10",
    "subjects": {
        "math": 91,
        "science": 85,
        "english": 90
    },
    "attendance": 96.5,
    "activities": ["Futbol", "Kitob o'qish"],
    "address": {
        "street": "Xalqlar do'stligi ko'chasi",
        "city": "Andijon",
        "state": "Andijon viloyati",
        "zip_code": "170300"
    }
}
students23 = {
    "id": 23,
    "name": "Ravshanbek Tolibov",
    "age": 17,
    "gender": "Male",
    "contact": "998-93-456-78-90",
    "grade_level": "Grade 11",
    "subjects": {
        "math": 93,
        "science": 88,
        "english": 92
    },
    "attendance": 94.0,
    "activities": ["Basketbol", "Voleybol"],
    "address": {
        "street": "Hamza ko'chasi",
        "city": "Samarqand",
        "state": "Samarqand viloyati",
        "zip_code": "140200"
    }
}
students24 = {
    "id": 24,
    "name": "Mavluda Karimova",
    "age": 14,
    "gender": "Female",
    "contact": "998-91-567-89-01",
    "grade_level": "Grade 9",
    "subjects": {
        "math": 84,
        "science": 85,
        "english": 86
    },
    "attendance": 97.5,
    "activities": ["Raqs", "Voleybol"],
    "address": {
        "street": "Sayram ko'chasi",
        "city": "Toshkent",
        "state": "Toshkent shahri",
        "zip_code": "100018"
    }
},
students25 = {
    "id": 25,
    "name": "Aziza Hakimova",
    "age": 15,
    "gender": "Female",
    "contact": "998-90-765-43-21",
    "grade_level": "Grade 10",
    "subjects": {
        "math": 87,
        "science": 92,
        "english": 89
    },
    "attendance": 95.0,
    "activities": ["Fotografiya", "Piyano"],
    "address": {
        "street": "Chilonzor ko'chasi",
        "city": "Toshkent",
        "state": "Toshkent shahri",
        "zip_code": "100019"
    }
},
students26 = {
    "id": 26,
    "name": "Abdulloh Begmatov",
    "age": 16,
    "gender": "Male",
    "contact": "998-92-234-56-78",
    "grade_level": "Grade 10",
    "subjects": {
        "math": 90,
        "science": 94,
        "english": 85
    },
    "attendance": 97.0,
    "activities": ["Futbol", "Kompyuter o'yinlari"],
    "address": {
        "street": "Farhod ko'chasi",
        "city": "Navoiy",
        "state": "Navoiy viloyati",
        "zip_code": "210200"
    }
},
students27 = {
    "id": 27,
    "name": "Karimjon Alimov",
    "age": 17,
    "gender": "Male",
    "contact": "998-91-234-56-78",
    "grade_level": "Grade 11",
    "subjects": {
        "math": 94,
        "science": 88,
        "english": 87
    },
    "attendance": 93.5,
    "activities": ["Shaxmat", "Futbol"],
    "address": {
        "street": "Farg'ona ko'chasi",
        "city": "Buxoro",
        "state": "Buxoro viloyati",
        "zip_code": "200700"
    }
},
students28 = {
    "id": 28,
    "name": "Kamronbek Rashidov",
    "age": 16,
    "gender": "Male",
    "contact": "998-93-345-67-89",
    "grade_level": "Grade 10",
    "subjects": {
        "math": 91,
        "science": 85,
        "english": 88
    },
    "attendance": 96.5,
    "activities": ["Basketbol", "Raqs"],
    "address": {
        "street": "Toshkent ko'chasi",
        "city": "Termiz",
        "state": "Surxondaryo viloyati",
        "zip_code": "190100"
    }
},
students29 = {
    "id": 29,
    "name": "Gulbahor Yuldasheva",
    "age": 15,
    "gender": "Female",
    "contact": "998-94-234-56-78",
    "grade_level": "Grade 9",
    "subjects": {
        "math": 84,
        "science": 88,
        "english": 90
    },
    "attendance": 97.0,
    "activities": ["Piyano", "Voleybol"],
    "address": {
        "street": "Beshyog'och ko'chasi",
        "city": "Andijon",
        "state": "Andijon viloyati",
        "zip_code": "170200"
    }
},
students30 = {
    "id": 30,
    "name": "Javohirbek Karimov",
    "age": 16,
    "gender": "Male",
    "contact": "998-91-456-78-90",
    "grade_level": "Grade 10",
    "subjects": {
        "math": 87,
        "science": 92,
        "english": 85
    },
    "attendance": 94.5,
    "activities": ["Basketbol", "Shaxmat"],
    "address": {
        "street": "Gulbahor ko'chasi",
        "city": "Xiva",
        "state": "Xorazm viloyati",
        "zip_code": "220200"
    }
},
students31 = {
    "id": 31,
    "name": "Zaynab Sobirova",
    "age": 15,
    "gender": "Female",
    "contact": "998-90-567-89-01",
    "grade_level": "Grade 9",
    "subjects": {
        "math": 83,
        "science": 87,
        "english": 90
    },
    "attendance": 96.0,
    "activities": ["Futbol", "Debat klubi"],
    "address": {
        "street": "Navbahor ko'chasi",
        "city": "Farg'ona",
        "state": "Farg'ona viloyati",
        "zip_code": "150100"
    }
},
students32 = {
    "id": 32,
    "name": "Ikrombek Iskandarov",
    "age": 17,
    "gender": "Male",
    "contact": "998-92-123-45-67",
    "grade_level": "Grade 11",
    "subjects": {
        "math": 89,
        "science": 93,
        "english": 91
    },
    "attendance": 95.5,
    "activities": ["Basketbol", "Kompyuter o'yinlari"],
    "address": {
        "street": "Toshkent ko'chasi",
        "city": "Buxoro",
        "state": "Buxoro viloyati",
        "zip_code": "200300"
    }
},
students33 = {
    "id": 33,
    "name": "Sardorbek Abdullayev",
    "age": 15,
    "gender": "Male",
    "contact": "998-93-234-56-78",
    "grade_level": "Grade 10",
    "subjects": {
        "math": 90,
        "science": 85,
        "english": 84
    },
    "attendance": 96.5,
    "activities": ["Shaxmat", "Fotografiya"],
    "address": {
        "street": "Saylan ko'chasi",
        "city": "Samarqand",
        "state": "Samarqand viloyati",
        "zip_code": "140500"
    }
},
students34 ={
    "id": 34,
    "name": "Feruza Murodova",
    "age": 16,
    "gender": "Female",
    "contact": "998-91-345-67-89",
    "grade_level": "Grade 10",
    "subjects": {
        "math": 88,
        "science": 90,
        "english": 89
    },
    "attendance": 94.0,
    "activities": ["Raqs", "Kitob o'qish"],
    "address": {
        "street": "Amir Temur ko'chasi",
        "city": "Termiz",
        "state": "Surxondaryo viloyati",
        "zip_code": "190200"
    }
},
students35 = {
    "id": 35,
    "name": "Bekzod Tursunov",
    "age": 15,
    "gender": "Male",
    "contact": "998-94-234-56-78",
    "grade_level": "Grade 9",
    "subjects": {
        "math": 86,
        "science": 87,
        "english": 92
    },
    "attendance": 95.0,
    "activities": ["Shaxmat", "Futbol"],
    "address": {
        "street": "Qoraqalpoq ko'chasi",
        "city": "Buxoro",
        "state": "Buxoro viloyati",
        "zip_code": "200400"
    }
},
students36 = {
    "id": 36,
    "name": "Malika Umarova",
    "age": 14,
    "gender": "Female",
    "contact": "998-91-123-45-67",
    "grade_level": "Grade 9",
    "subjects": {
        "math": 85,
        "science": 88,
        "english": 83
    },
    "attendance": 96.5,
    "activities": ["Raqs", "Kitob o'qish"],
    "address": {
        "street": "Yusuf Turobov ko'chasi",
        "city": "Toshkent",
        "state": "Toshkent shahri",
        "zip_code": "100001"
    }
},
students37 = {
    "id": 37,
    "name": "Dostonbek Makhmudov",
    "age": 17,
    "gender": "Male",
    "contact": "998-90-345-67-89",
    "grade_level": "Grade 11",
    "subjects": {
        "math": 91,
        "science": 93,
        "english": 92
    },
    "attendance": 94.5,
    "activities": ["Shaxmat", "Fotografiya"],
    "address": {
        "street": "Mirzo Ulug'bek ko'chasi",
        "city": "Namangan",
        "state": "Namangan viloyati",
        "zip_code": "160100"
    }
},
students38 = {
    "id": 38,
    "name": "Dilorom Abdurahmanova",
    "age": 15,
    "gender": "Female",
    "contact": "998-92-456-78-90",
    "grade_level": "Grade 9",
    "subjects": {
        "math": 82,
        "science": 84,
        "english": 86
    },
    "attendance": 95.0,
    "activities": ["Piyano", "Basketbol"],
    "address": {
        "street": "Buxoro ko'chasi",
        "city": "Samarqand",
        "state": "Samarqand viloyati",
        "zip_code": "140700"
    }
},
students39 = {
    "id": 39,
    "name": "Sherzodbek Kadirov",
    "age": 17,
    "gender": "Male",
    "contact": "998-90-567-89-01",
    "grade_level": "Grade 11",
    "subjects": {
        "math": 95,
        "science": 88,
        "english": 90
    },
    "attendance": 96.0,
    "activities": ["Basketbol", "Kompyuter o'yinlari"],
    "address": {
        "street": "Chorvoq ko'chasi",
        "city": "Farg'ona",
        "state": "Farg'ona viloyati",
        "zip_code": "150200"
    }
},
students40 = {
    "id": 40,
    "name": "Nodira Abdug'aniyeva",
    "age": 16,
    "gender": "Female",
    "contact": "998-94-567-89-01",
    "grade_level": "Grade 10",
    "subjects": {
        "math": 88,
        "science": 91,
        "english": 89
    },
    "attendance": 97.0,
    "activities": ["Voleybol", "Kitob o'qish"],
    "address": {
        "street": "Nasaf ko'chasi",
        "city": "Termiz",
        "state": "Surxondaryo viloyati",
        "zip_code": "190300"
    }
},
students41 = {
    "id": 41,
    "name": "Shahzod Abdullayev",
    "age": 16,
    "gender": "Male",
    "contact": "998-94-111-22-33",
    "grade_level": "Grade 10",
    "subjects": {
        "math": 85,
        "science": 88,
        "english": 80
    },
    "attendance": 96.0,
    "activities": ["Shaxmat", "Robototexnika"],
    "address": {
        "street": "Navoi ko'chasi",
        "city": "Andijon",
        "state": "Andijon viloyati",
        "zip_code": "170100"
    }
},
students42 = {
    "id": 42,
    "name": "Nodira Rasulova",
    "age": 15,
    "gender": "Female",
    "contact": "998-97-555-66-77",
    "grade_level": "Grade 9",
    "subjects": {
        "math": 90,
        "science": 84,
        "english": 86
    },
    "attendance": 98.5,
    "activities": ["Rasm chizish", "Tennis"],
    "address": {
        "street": "Bog' ko'chasi",
        "city": "Namangan",
        "state": "Namangan viloyati",
        "zip_code": "160200"
    }
},
students43 = {
    "id": 43,
    "name": "Javohir Qodirov",
    "age": 17,
    "gender": "Male",
    "contact": "998-99-333-44-55",
    "grade_level": "Grade 11",
    "subjects": {
        "math": 93,
        "science": 91,
        "english": 88
    },
    "attendance": 92.0,
    "activities": ["Futbol", "IT klubi"],
    "address": {
        "street": "Mustaqillik shohko'chasi",
        "city": "Farg'ona",
        "state": "Farg'ona viloyati",
        "zip_code": "150300"
    }
},
students44 = {
    "id": 44,
    "name": "Dilnoza Saidova",
    "age": 14,
    "gender": "Female",
    "contact": "998-95-777-88-99",
    "grade_level": "Grade 8",
    "subjects": {
        "math": 80,
        "science": 86,
        "english": 91
    },
    "attendance": 97.0,
    "activities": ["She'r yozish", "Piyano"],
    "address": {
        "street": "Zarafshon ko'chasi",
        "city": "Navoiy",
        "state": "Navoiy viloyati",
        "zip_code": "210100"
    }
},
students45 = {
    "id": 45,
    "name": "Akmalbek Usmonov",
    "age": 16,
    "gender": "Male",
    "contact": "998-93-666-77-88",
    "grade_level": "Grade 10",
    "subjects": {
        "math": 88,
        "science": 89,
        "english": 82
    },
    "attendance": 94.5,
    "activities": ["Boks", "Raqs"],
    "address": {
        "street": "Do'stlik ko'chasi",
        "city": "Jizzax",
        "state": "Jizzax viloyati",
        "zip_code": "130400"
    }
}