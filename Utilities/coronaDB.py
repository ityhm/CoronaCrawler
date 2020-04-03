import mysql.connector


class MyCoronaDB:
    db_name = 'coronaDB'
    table_name = 'coronaTable'
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
        if ([item[0] for item in self.db_cursor].count(self.db_name) == 0):
            print("Create DB " + self.db_name)
            self.db_cursor.execute("CREATE DATABASE " + self.db_name)
        else:
          pass
          #print("DB " + self.db_name + " exists")

        # Put a list of tuples [(<Table Name>, <>), ...]
        self.db_cursor.execute("SHOW TABLES")

        # If table doesn't exist, create it
        if ([item[0] for item in self.db_cursor].count(self.table_name) == 0):
          print("Create Table " + self.table_name)
          self.db_cursor.execute(self.CREATE_TABLE_STR)
        else:
          pass
          # print("Table " + self.table_name + " exists")

    def close(self):
        # print("Close DB")
        self.db_cursor.close()
        self.my_db.close()

    def print_records(self, records):
      # print records
      for row in records:
        print(", ".join(map(str, row)))

      print()

    def print_db(self):
        print("Table " + self.table_name + ":")
        # get all records from table
        self.db_cursor.execute("SELECT * from " + self.table_name)
        records = self.db_cursor.fetchall()
        # print("There are ", len(records), " records")

        # print columns names
        print(*[i[0].upper() for i in self.db_cursor.description])

        self.print_records(records)

    def print_columns(self):
      self.db_cursor.execute("SELECT * from " + self.table_name)
      records = self.db_cursor.fetchall()
      print("There are ", len(records), " records")
      print(*[i[0] for i in self.db_cursor.description])

    def insert_record(self, source, sick, date):
        if self.check_if_record_exists(source, sick, date):
            print("\nRecord ({}, {}) exists already\n".format(source, sick))
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
      print("\nReset table\n")
      sql = "DROP TABLE " + self.table_name
      self.db_cursor.execute(sql)
      self.db_cursor.execute(self.CREATE_TABLE_STR)

    def delete_all_table(self):
      print("\nDelete all table\n")
      sql = "DELETE FROM " + self.table_name
      self.db_cursor.execute(sql)
      self.my_db.commit()

    def get_last_record_date(self):
        sql = "SELECT MAX(date) FROM %s" % (self.table_name)
        self.db_cursor.execute(sql)
        result = self.db_cursor.fetchone()
        date = None

        if ((result is not None) and len(result)) > 0:
            date = str(result[0])
        else:
            print("Table is empty! Can't return last record's date")

        return date

    def print_all_after_date_including(self, date):
        sql = f"SELECT * FROM {self.table_name} WHERE date >= '{date}'"
        self.db_cursor.execute(sql)
        records = self.db_cursor.fetchall()
        self.print_records(records)