# test_school_management.py

from datetime import datetime
import unittest
import school_management

class TestUpdateRecord(unittest.TestCase):

    def setUp(self):
        # Create the database and tables
        Base.metadata.create_all(engine)
        self.session = Session()

    def tearDown(self):
        # Clean up after the test
        self.session.close()
        Base.metadata.drop_all(engine)

    def are_students_equal(self, student1, student2):
        return student1 == student2

    def test_update_record(self):
        student = Student(
            name='John Doe',
            email='john.doe@example.com',
            phone_no='1234567890',
            gender='Male',
            dob=datetime.strptime('2000-01-01', '%Y-%m-%d').date(),  # Convert to Python date object
            stream='Science'
        )
        self.session.add(student)
        self.session.commit()

        # Call the update_record function
        updated_data = {
            'name': 'Jane Doe',
            'email': 'jane.doe@example.com',
            'phone_no': '9876543210',
            'gender': 'Female',
            'dob': '2000-02-02',
            'stream': 'Arts'
        }
        admission_no = student.admission_no
        update_record(admission_no, updated_data)

        #Fetch the updated record from the database
        updated_student = self.session.query(Student).get(admission_no)

        #Create an expected student object
        expected_updated_student = Student(admission_no=admission_no, **updated_data)

        # Check if the updated record values are the same
        are_equal = self.are_students_equal(updated_student, expected_updated_student)

        # You can now use 'are_equal' as a boolean to check if both objects are the same
        return are_equal
if __name__ == '__main__':
    unittest.main()
