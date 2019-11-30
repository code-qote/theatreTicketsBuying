import sqlite3

class Import_export:
    def import_table(self, data_base, table):
        con = sqlite3.connect("data/" + data_base + ".db")
        cursor = con.cursor()
        result = list(cursor.execute("SELECT * FROM " +  table))
        con.close()
        return result
    
    def instert_table(self, data_base, table, q, a):
        con = sqlite3.connect("data/" + data_base + ".db")
        cursor = con.cursor()
        cursor.execute(q, a)
        con.commit()
        con.close()
    
    def update_table(self, data_base, table, q):
        con = sqlite3.connect("data/" + data_base + ".db")
        cursor = con.cursor()
        cursor.execute(q)
        con.commit()
        con.close()
    
    def create_table(self, data_base, q):
        con = sqlite3.connect("data/" + data_base + ".db")
        cursor = con.cursor()
        cursor.execute(q)
        con.commit()
        con.close()
