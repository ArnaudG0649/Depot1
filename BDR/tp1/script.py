#!/bin/env python3

import sys
import sqlite3

if __name__ == '__main__':
    try:# Connexion à une bdd
        connection = sqlite3.connect('sakila.db')
        # Un curseur pour les opérations sur la bdd
        cursor = connection.cursor()
        print("Connecté au sqlite")
        
        # Récupérer des données
        cursor.execute("""SELECT * from actor""")
        records = cursor.fetchall()
        # Afficher les données
        print("nb lignes: ", len(records))
        for row in records:
            print(f"{row}")
            # Fermer la connexion
            cursor.close()
    except sqlite3.Error as error :
        print("Erreur", error)
    finally:
        if connection:
            connection.close()
            
  #   try:# Connexion à une bdd
  #       connection = sqlite3.connect('sakila.db')
  #       # # Un curseur pour les opérations sur la bdd
  #       cursor = connection.cursor()
  #       print("Connecté au sqlite")
        
  #       # # Récupérer des données
  #       cursor.execute("""SELECT name FROM sqlite_master  
  # WHERE type='table';""")
  #       records = cursor.fetchall()
  #       print(records)
  #       # # Afficher les données
  #       # print("nb lignes: ", len(records))
  #       # for row in records:
  #       #     print(f"{row}")
  #       #     # Fermer la connexion
  #       #     cursor.close()
  #   except sqlite3.Error as error :
  #       print("Erreur", error)
  #   finally:
  #       if connection:
  #           connection.close()
            
