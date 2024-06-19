from scraper import scrape_school_data
from database import *

def main():
    # key is the ID, value is a tuple. first value is the link to the exam schedule, second value is the name of the school
    universities = {
        1 : ("https://aggie.tamu.edu/registration-and-records/classes/final-examination-schedules", "Texas A&M University")
        # add more universities
    }

    # make this dynamic
    chosen_university_id = 1

    # store the tuple with link and id
    uni = universities.get(chosen_university_id)

    # update to only do this periodically
    scraped_data = scrape_school_data(uni[0], chosen_university_id)

    # connect to the database
    db_name = "examsched"
    db_user = "postgres"
    db_password = "sundown"
    db_host = "localhost"
    db_port = "5432"

    connection = create_connection(db_name, db_user, db_password, db_host, db_port)

    
    # verify connection to the database, then insert the information to the database
    '''if connection is not None:
        # create the data tables if not already created
        create_tables(connection)


        insert_university(connection, chosen_university_id, uni[1])
        for schedule in scraped_data:
            class_id = insert_class(connection, chosen_university_id, schedule['class_name'])
            '''
            


    #for schedule in scraped_data:

if __name__ == "__main__":
    main()