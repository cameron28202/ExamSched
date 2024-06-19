import psycopg2
from psycopg2 import OperationalError

def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database = db_name,
            user = db_user,
            password = db_password,
            host = db_host,
            port = db_port,
        )
        print("Successfully connected")
    except OperationalError as e:
        print(f"the error {e} occured bro")
    return connection

def create_tables(connection):
    cursor = connection.cursor()

    create_universities_table = """
        CREATE TABLE IF NOT EXISTS universities (
        university_id SERIAL PRIMARY KEY,
        university_name VARCHAR(255) UNIQUE NOT NULL
        );
    """

    create_class_schedule_table = """
        CREATE TABLE IF NOT EXISTS courses (
        course_id SERIAL PRIMARY KEY,
        university_id INTEGER NOT NULL,
        course_name VARCHAR(255) NOT NULL,
        FOREIGN KEY (university_id) REFERENCES universities (university_id)
    );
    """

    create_exam_schedules_table = """
        CREATE TABLE IF NOT EXISTS exam_schedules (
        schedule_id SERIAL PRIMARY KEY,
        course_id INTEGER NOT NULL,
        regular_class_time VARCHAR(255),
        final_exam_time VARCHAR(255),
        FOREIGN KEY (course_id) REFERENCES courses(course_id)
    );
    """
    try:
        cursor.execute(create_universities_table)
        cursor.execute(create_class_schedule_table)
        cursor.execute(create_exam_schedules_table)
        connection.commit()
        print("query executed successfully")
    except OperationalError as e:
        print(f"The error {e} occured")

def insert_university(connection, university_id, university_name):
    try:
        cursor = connection.cursor()
        cursor.execute("""
                INSERT INTO universities (university_name, university_id)
                VALUES (%s, %s);
        """,  (university_name, university_id))
        connection.commit()
        print("inserted to table!")
    except OperationalError as e:
        print(f"The error {e} occured")
        connection.rollback()
    finally:
        cursor.close()

def insert_class(connection, university_id, class_id):
    try:
        cursor = connection.cursor()
        cursor.execute("""
                INSERT INTO classes (university_id, class_name)
                VALUES (%s, %s) RETURNING class_id;
        """, (university_id, class_name))
        class_id = cursor.fetchone()[0]
        connection.commit()
    except OperationalError as e:
        print(f"Error {e} occured")
    finally:
        cursor.close()