# -*- coding: utf-8 -*-

from psycopg2 import connect


def createDB(db_name, db_user,db_password):
    """Reads commands from DataVaultV4.txt to build the data vault."""
    
    try:

        conn = connect(
          dbname=db_name,
          user=db_user,
          host="localhost",
          password=db_password)

        cursor = conn.cursor()

        with open("smdvault.txt") as f:
          vault_script = f.read()

        cursor.execute(vault_script)

        conn.commit()

        cursor.close()

        conn.close()
        print("Creating database...")
        
    except:
        print("Error: ")
        print("\nPlease check that the database name, user and password are the same as specified in the documentation."
              " If this is not the first time you are running main.py, you may need to drop the database in PostgreSQL shell.")
        quit()
