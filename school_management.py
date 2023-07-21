# school_management.py

import sqlite3

# Create the database and table
def create_database():
    connector = sqlite3.connect('school_db_test.db')
    cursor = connector.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS SCHOOL_MANAGEMENT (
            STUDENT_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            NAME TEXT,
            EMAIL TEXT,
            PHONE_NO TEXT,
            GENDER TEXT,
            DOB TEXT,
            STREAM TEXT
        )
    ''')

    connector.commit()
    connector.close()

# Other functions and configurations here

def update_record(admission_no, new_data):
    connector = sqlite3.connect('school_db_test.db')
    cursor = connector.cursor()

    try:
        cursor.execute('UPDATE SCHOOL_MANAGEMENT SET NAME=?, EMAIL=?, PHONE_NO=?, GENDER=?, DOB=?, STREAM=? WHERE STUDENT_ID=?',
                       (new_data['name'], new_data['email'], new_data['phone_no'], new_data['gender'], new_data['dob'], new_data['stream'], admission_no))
        connector.commit()
    except sqlite3.Error as e:
        connector.rollback()
        raise e
    finally:
        connector.close()
