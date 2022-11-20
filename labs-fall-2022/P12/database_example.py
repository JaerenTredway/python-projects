def build_database():
    '''
    This function builds a database of locations with 
    each place's latitude, longitude, and description.
    '''
    #make connection to database file:
    print("\nDATABASE LOCATION: ", database_location)
    database_connection = sqlite3.connect(database_location)

    #make a cursor to execute SQL querries:
    my_cursor = database_connection.cursor()

    #delete the old table:
    my_cursor.execute('''
    DROP TABLE IF EXISTS my_table
    ''')

    #create a new table in the database:
    my_cursor.execute('''
    CREATE TABLE my_table(
        LatColumn FLOAT,
        LongColumn FLOAT,
        NameColumn TEXT,
        TypeColumn TEXT
    )
    ''')

    database_connection.commit()

    #insert data into the table:
    my_cursor.execute('''
    INSERT INTO my_table(
        LatColumn,
        LongColumn,
        NameColumn,
        TypeColumn
    )
    VALUES 
        (100.200, 123.456, "Chang's", 'Chinese'),
        (120.330, 142.345, 'East Ocean', 'Chinese'),
        (153.230, 322.345, 'Hunan', 'Chinese'),
        (133.230, 143.345, 'Qwon Wong', 'Chinese'),
        (153.420, 122.345, 'Spicy Wonton', 'Chinese'),
        (100.200, 123.456, "McDonald's", 'American'),
        (120.330, 142.345, 'Burger King', 'American'),
        (153.230, 322.345, "Wendy's", 'American'),
        (133.230, 143.345, 'Sonic', 'American'),
        (153.420, 122.345, "Carl's Jr.", 'American'),
        (100.200, 123.456, "Garcia's", 'Mexican'),
        (120.330, 142.345, 'Taco House', 'Mexican'),
        (153.230, 322.345, "Sadie's", 'Mexican'),
        (133.230, 143.345, 'Frontier', 'Mexican'),
        (153.420, 122.345, 'Green Chili Monster', 'Mexican')
    ''')

    database_connection.commit()
    
    #see if there is anything in the database:
    with database_connection:
        my_cursor.execute("SELECT * FROM my_table")
        print("Database contents: ")
        print(my_cursor.fetchall())
    database_connection.close()
#**** END build_database() ****