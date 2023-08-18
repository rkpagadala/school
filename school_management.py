# school_management.py

from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the SQLite engine
engine = create_engine('sqlite:///school_management_data.db', echo=True)  # Change the database name if needed

# Create a Session class
Session = sessionmaker(bind=engine)

# Rest of your code...



# Define the Student model
Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'
    admission_no = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone_no = Column(String)
    gender = Column(String)
    dob = Column(Date)
    stream = Column(String)

    def update_data(self, new_data):
        self.name = new_data['name']
        self.email = new_data['email']
        self.phone_no = new_data['phone_no']
        self.gender = new_data['gender']
        self.dob = new_data['dob']
        self.stream = new_data['stream']

# Other functions and configurations here

# Define the update_record function
def update_record(admission_no, new_data):
    session = Session()
    student = session.query(Student).get(admission_no)
    
    if student:
        student.update_data(new_data)
        session.commit()
        session.close()
        return True
    else:
        session.close()
        return False


    try:
        cursor.execute('UPDATE SCHOOL_MANAGEMENT SET NAME=?, EMAIL=?, PHONE_NO=?, GENDER=?, DOB=?, STREAM=? WHERE STUDENT_ID=?',
                       (new_data['name'], new_data['email'], new_data['phone_no'], new_data['gender'], new_data['dob'], new_data['stream'], admission_no))
        connector.commit()
    except sqlite3.Error as e:
        connector.rollback()
        raise e
    finally:
        connector.close()
