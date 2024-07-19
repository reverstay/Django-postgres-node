# -*- coding: utf-8 -*-
import psycopg2
from psycopg2 import OperationalError, errorcodes, errors

def copy_country_to_region():
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

        # Selecionar IDs e nomes únicos da tabela beta_observatory_country
        select_query = """
        SELECT DISTINCT id, name
        FROM beta_observatory_country
        """
        cursor.execute(select_query)
        countries = cursor.fetchall()

        # Inserir dados na tabela beta_observatory_country_region
        insert_query = """
        INSERT INTO beta_observatory_country_region (id, name)
        VALUES (%s, %s)
        ON CONFLICT (id) DO NOTHING;
        """
        for country in countries:
            cursor.execute(insert_query, country)

        connection.commit()
        print("Dados copiados com sucesso da tabela 'beta_observatory_country' para 'beta_observatory_country_region'!")

    except OperationalError as oe:
        print("Erro de conexão ao banco de dados: {}".format(oe))
    except Exception as e:
        print("Erro ao copiar dados: {}".format(e))
    finally:
        if connection:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    copy_country_to_region()
