import mysql.connector
from Utilities.Logger import print_flush, log_to_file


class MyCoronaDB:
    db_name = 'coronaDB'
    table_name = 'coronaTable'
    # table_name = 'practiceCoronaTable'
    my_db = ''
    db_cursor = []

    CREATE_TABLE_STR = "CREATE TABLE " + table_name\
                       + " (id INT AUTO_INCREMENT PRIMARY KEY"\
                       + ", source VARCHAR(255)"\
                       + ", sick int(11)"\
                       + ", date DATETIME)"

    def __init__(self):
        self.init_db()

    def init_db(self, db_name='coronaDB'):
        self.db_name = db_name
        self.my_db = mysql.connector.connect(
            host="localhost",
            user="itay",
            passwd="Password1!",
            database=str(self.db_name)
        )
        self.db_cursor = self.my_db.cursor()

        # Put a list of tuples [(<Database Name>, <>), ...]
        self.db_cursor.execute("SHOW DATABASES")

        # If the DB doesn't exists in the given list (first index of each tuple in the list)
        if [item[0] for item in self.db_cursor].count(self.db_name) == 0:
            print_flush(f"Create DB {self.db_name}")
            self.db_cursor.execute("CREATE DATABASE " + self.db_name)
        else:
            pass
            # print_flush(f"DB {self.db_name} exists")

        # Put a list of tuples [(<Table Name>, <>), ...]
        self.db_cursor.execute("SHOW TABLES")

        # If table doesn't exist, create it
        if [item[0] for item in self.db_cursor].count(self.table_name) == 0:
            print_flush(f"Create Table {self.table_name}")
            self.db_cursor.execute(self.CREATE_TABLE_STR)
        else:
            pass
            # print_flush(f"Table {self.table_name} exists")

    def close(self):
        # print_flush("Close DB")
        self.db_cursor.close()
        self.my_db.close()

    def print_records(self, records):
        # print records
        for row in records:
            print_flush(", ".join(map(str, row)))

        print_flush()

    def print_db(self):
        print_flush(f"Table {self.table_name}:")
        # get all records from table
        self.db_cursor.execute(f"SELECT * from {self.table_name}")
        records = self.db_cursor.fetchall()
        # print_flush(f"There are ", len(records), " records")

        # print columns names
        print(*[i[0].upper() for i in self.db_cursor.description])
        print_flush()

        self.print_records(records)

    def print_columns(self):
        self.db_cursor.execute("SELECT * from " + self.table_name)
        records = self.db_cursor.fetchall()
        print_flush(f"There are {len(records)} records")
        print(*[i[0] for i in self.db_cursor.description])

    def insert_record(self, source, sick, date):
        if self.check_if_record_exists(source, sick, date):
            print_flush(f"\nRecord ({source}, {sick}) exists already\n")
        else:
            last_sick_by_source = self.get_last_sick_by_source(source)
            if int(sick) < int(last_sick_by_source):
                msg = f"Error! Source '{source} has higher sick value ({last_sick_by_source}) in the db. " \
                      f"Tried to insert {sick}."
                print_flush(msg)
                log_to_file(source, msg)
                raise Exception(msg)
            else:
                sql = "INSERT INTO " + self.table_name + " (source, sick, date) VALUES (%s, %s, %s)"
                val = (source, sick, date)
                self.db_cursor.execute(sql, val)
                self.my_db.commit()

    def check_if_record_exists(self, source, sick, date):
        sql = "SELECT * FROM %s WHERE source = '%s' AND sick = '%s'" % (self.table_name, source, sick)
        self.db_cursor.execute(sql)
        return len(self.db_cursor.fetchall()) > 0

    def reset_table(self):
        print_flush("\nReset table\n")
        sql = "DROP TABLE " + self.table_name
        self.db_cursor.execute(sql)
        self.db_cursor.execute(self.CREATE_TABLE_STR)

    def delete_all_table(self):
        print_flush("\nDelete all table\n")
        sql = "DELETE FROM " + self.table_name
        self.db_cursor.execute(sql)
        self.my_db.commit()

    def get_last_record_date(self):
        sql = "SELECT MAX(date) FROM %s" % self.table_name
        self.db_cursor.execute(sql)
        result = self.db_cursor.fetchone()
        date = None

        if ((result is not None) and len(result)) > 0:
            date = str(result[0])
        else:
            print_flush("Table is empty! Can't return last record's date")

        return date

    def get_last_sick_by_source(self, source):
        max_id = self.get_max_id_by_source(source)
        sql = f"SELECT sick FROM {self.table_name} WHERE id='{max_id}'"
        self.db_cursor.execute(sql)
        result = self.db_cursor.fetchone()
        last_sick = None

        if ((result is not None) and len(result)) > 0:
            last_sick = str(result[0])
        else:
            print_flush("Table is empty! Can't return last record's date")

        return last_sick

    def get_highest_sick_by_source(self, source):
        sql = f"SELECT MAX(sick) FROM {self.table_name} WHERE source='{source}'"
        self.db_cursor.execute(sql)
        result = self.db_cursor.fetchone()
        highest_sick = None

        if ((result is not None) and len(result)) > 0:
            highest_sick = str(result[0])
        else:
            print_flush("Table is empty! Can't return last record's date")

        return highest_sick

    def get_max_id_by_source(self, source):
        sql = f"SELECT MAX(id)FROM {self.table_name} WHERE source='{source}'"
        self.db_cursor.execute(sql)
        result = self.db_cursor.fetchone()
        max_id = None

        if ((result is not None) and len(result)) > 0:
            max_id = int(result[0])
        else:
            print_flush("Table is empty! Can't return last record's date")

        return max_id

    def print_all_after_date_including(self, date):
        sql = f"SELECT * FROM {self.table_name} WHERE date >= '{date}'"
        self.db_cursor.execute(sql)
        records = self.db_cursor.fetchall()
        self.print_records(records)

    def delete_by_id(self, el_id):
        print_flush(f"\nDelete ID {el_id}\n")
        sql = f"DELETE FROM {self.table_name} WHERE id = '{el_id}'"
        self.db_cursor.execute(sql)
        self.my_db.commit()
