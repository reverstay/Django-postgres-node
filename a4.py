# -*- coding: utf-8 -*-
import csv
import psycopg2
from psycopg2 import sql

def insert_country_data():
    connection = None
    try:
        connection = psycopg2.connect(
            host='painel-ifrs9-database',
            user='postgres',
            password='1234',
            dbname='ifrs9',
            port=5432
        )

        cursor = connection.cursor()

        # Leia o arquivo CSV
        with open('country-list.csv', mode='r') as file:
            csv_reader = csv.DictReader(file)
            headers = csv_reader.fieldnames

            if 'name' not in headers or 'capital_city' not in headers:
                raise ValueError("CSV does not contain the required headers 'name' and 'capital_city'")

            for row in csv_reader:
                country = row['name']
                capital_city = row['capital_city']

                # Insira os dados na tabela
                insert_query = sql.SQL("""
                    INSERT INTO beta_observatory_country (name, capital_city)
                    VALUES (%s, %s)
                """)

                cursor.execute(insert_query, (country, capital_city))

        connection.commit()
        print("Dados inseridos com sucesso.")

    except Exception as error:
        print("Erro ao inserir dados: " + str(error))

    finally:
        if connection is not None:
            cursor.close()
            connection.close()

insert_country_data()
