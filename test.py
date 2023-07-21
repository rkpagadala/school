# test_school_management.py
import sqlite3
import unittest
import school_management

class TestUpdateRecord(unittest.TestCase):

    def setUp(self):
        # Set up the test database
        school_management.create_database()  # Create the database before each test
        school_management.connector = sqlite3.connect('school_db_test.db')
        school_management.cursor = school_management.connector.cursor()

    def tearDown(self):
        # Clean up after the test
        school_management.cursor.execute("DROP TABLE SCHOOL_MANAGEMENT")
        school_management.connector.close()


    def test_update_record(self):
        # Insert a test record into the database
        school_management.cursor.execute("INSERT INTO SCHOOL_MANAGEMENT (NAME, EMAIL, PHONE_NO, GENDER, DOB, STREAM) VALUES (?, ?, ?, ?, ?, ?)",
                                         ('John Doe', 'john.doe@example.com', '1234567890', 'Male', '2000-01-01', 'Science'))
        school_management.connector.commit()

        # Call the update_record function
        updated_data = {
            'name': 'Jane Doe',
            'email': 'jane.doe@example.com',
            'phone_no': '9876543210',
            'gender': 'Female',
            'dob': '2000-02-02',
            'stream': 'Arts'
        }
        admission_no = 1  # Assuming the student with ID 1 was inserted in the previous step
        school_management.update_record(admission_no, updated_data)

        # Fetch the updated record from the database
        school_management.cursor.execute(
            "SELECT * FROM SCHOOL_MANAGEMENT WHERE STUDENT_ID=?", (admission_no,))
        updated_record = school_management.cursor.fetchone()

        # Assert the updated record values
        self.assertEqual(updated_record[1], 'Jane Doe')
        self.assertEqual(updated_record[2], 'jane.doe@example.com')
        self.assertEqual(updated_record[3], '9876543210')
        self.assertEqual(updated_record[4], 'Female')
        self.assertEqual(updated_record[5], '2000-02-02')
        self.assertEqual(updated_record[6], 'Arts')

if __name__ == '__main__':
    unittest.main()
