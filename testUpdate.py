import unittest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from school_management import update_record  # Replace with the actual module name

# Define the SQLAlchemy model
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SchoolManagement(Base):
    __tablename__ = "SCHOOL_MANAGEMENT"

    STUDENT_ID = Column(Integer, primary_key=True, autoincrement=True)
    NAME = Column(String)
    EMAIL = Column(String)
    PHONE_NO = Column(String)
    GENDER = Column(String)
    DOB = Column(String)
    STREAM = Column(String)


# Unit tests
class TestUpdateRecord(unittest.TestCase):
    def setUp(self):
        # Create an in-memory SQLite database for testing
        self.engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def tearDown(self):
        # Clean up the session and the in-memory database after each test
        self.session.close()
        Base.metadata.drop_all(self.engine)

    def test_update_record(self):
        # Add a sample record to the database
        sample_data = {
            "name": "John Doe",
            "email": "john@example.com",
            "phone_no": "123-456-7890",
            "gender": "Male",
            "dob": "1990-01-01",
            "stream": "Science",
        }
        student = SchoolManagement(**sample_data)
        self.session.add(student)
        self.session.commit()

        # Call the update_record function
        new_data = {
            "name": "Updated Name",
            "email": "updated@example.com",
            "phone_no": "987-654-3210",
            "gender": "Female",
            "dob": "1985-02-15",
            "stream": "Arts",
        }
        admission_no = (
            1  # Assuming this is a valid admission number in the test database
        )
        update_record(admission_no, new_data, self.session)

        # Fetch the updated record from the database
        updated_student = self.session.query(SchoolManagement).get(admission_no)

        # Check if the record was updated correctly
        self.assertEqual(updated_student.NAME, new_data["name"])
        self.assertEqual(updated_student.EMAIL, new_data["email"])
        self.assertEqual(updated_student.PHONE_NO, new_data["phone_no"])
        self.assertEqual(updated_student.GENDER, new_data["gender"])
        self.assertEqual(updated_student.DOB, new_data["dob"])
        self.assertEqual(updated_student.STREAM, new_data["stream"])


if __name__ == "__main__":
    unittest.main()
