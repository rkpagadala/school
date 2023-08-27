import unittest
import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from school_management import create_database  # Replace with the actual module name

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
class TestCreateDatabase(unittest.TestCase):
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

    def test_create_database(self):
        # Call the create_database function
        create_database(self.session)

        # Check if the table exists in the database
        table_exists = self.engine.dialect.has_table(self.engine, "SCHOOL_MANAGEMENT")
        self.assertTrue(table_exists)


if __name__ == "__main__":
    unittest.main()
