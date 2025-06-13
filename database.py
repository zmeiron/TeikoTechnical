import os
import csv
import sqlite3

class Database:
    connection: sqlite3.Connection
    cursor: sqlite3.Cursor
    
    def __str__(self):
        results = self.cursor.execute("SELECT * FROM samples")
        return_string = ""
        for result in results:
            return_string += result.__str__() + '\n'
            
        return return_string

    def load(self, new_database):
        # if create new database 
        if new_database:
            print("Creating new database")
            if os.path.exists("cell_count.db"):
                os.remove("cell_count.db")
            
            connection, cursor = self._create_database()

        # use existing database
        else:
            if not os.path.exists("cell_count.db"):
                print("No existing database, creating new database")
                connection, cursor = self._create_database()
            else:
                print("Using existing database")
                connection = sqlite3.connect("cell_count.db")
                cursor = connection.cursor()

        self.connection = connection
        self.cursor = cursor
        

    def _create_database(self):
        connection = sqlite3.connect("cell_count.db")
        cursor = connection.cursor()
        
        # create table
        cursor.execute("""CREATE TABLE samples(
                        project text,
                        subject text,
                        condition text,
                        age integer,
                        sex text,
                        treatment text,
                        response text,
                        sample text,
                        sample_type text,
                        time_from_treatment_start integer,
                        b_cell integer,
                        cd8_t_cell integer,
                        cd4_t_cell integer,
                        nk_cell integer,
                        monocyte integer
        )""")
        
        # add csv data to table
        with open("cell-count.csv", mode="r", encoding="utf-8-sig") as file:
            data = csv.reader(file)
            for line in data:
                cursor.execute("INSERT INTO samples VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", line)
        
        connection.commit()
        return (connection, cursor)


    def add_sample(self, sample):
        self.cursor.execute("INSERT INTO samples VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", sample)
        self.connection.commit()
        
    def delete_sample(self, sampleid):
        self.cursor.execute("DELETE FROM samples WHERE sample = ?", (sampleid,))
        self.connection.commit()
        
    def get_sample(self, index):
        result = self.cursor.execute("SELECT * FROM samples WHERE rowid = ?", (index,))
        return result.fetchone()
    
    def get_all_samples(self):
        results = self.cursor.execute("SELECT rowid, * FROM samples")
        return results.fetchall()
    
    def get_all_mel_samples(self):
        results = self.cursor.execute("SELECT rowid, * FROM samples WHERE condition='melanoma' AND treatment='tr1' AND sample_type='PBMC'")
        return results.fetchall()
    
    def get_mel_population_counts(self, population):
        results = self.cursor.execute(f"SELECT {population},response FROM samples WHERE condition='melanoma' AND treatment='tr1' AND sample_type='PBMC'")
        return results.fetchall()
        
        
