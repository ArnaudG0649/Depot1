#!/bin/env python3

import sys
import logging
import psycopg


try:# Connect to an existing database
    connection = psycopg.connect("host=data port=5432 dbname=agonin user=agonin password=agonin")
    cursor = connection.cursor()

    with open('pokedex_05.20.csv','r') as file : 
        flag=False
        for f in file :
            if flag : 
                E=f.split(",")
                if E[12]=="" : E[12]=None
                print(E[0], E[2], E[3],E[11],E[12],"affiché")
                cursor.execute("INSERT INTO pokemon(pokemon_id, name, name_de,generation,height,weight) VALUES(%s,%s,%s,%s,%s,%s);""",
                (E[0], E[2], E[3],E[5],E[11],E[12]))
                
                # cursor.execute("INSERT INTO employee(lastname, firstname, email) VALUES(%s,%s,%s);""",
                # ('TAYLOR ', 'Mark', 'mark.taylor@enron.com'))
                
                # cursor.execute("INSERT INTO employee(lastname, firstname, email) VALUES(%s,%s,%s);""",
                # ('TAYLOR ', 'Mark', 'mark.taylor@enron.com'))
            flag=True
    #cursor.execute("""SELECT * FROM customer;""")
    #records = cursor.fetchall()
    #print(records)
    connection.commit()
    
    connection.close()
except Exception as e:
    logging.error("database connection failed")
    logging.error(e) 


def afficheliste() : 
    with open('pokedex_05.20.csv','r') as file :
        k=False
        for f in file :
            if k : break
            for i in range(len(f.split(","))) : 
                print(i,f.split(",")[i])
            k=True

def affichetout() : 
    with open('pokedex_05.20.csv','r') as file :
        k=0
        for f in file : 
            print(f.split(","))
            
            
affichetout()


