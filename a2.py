# -*- coding: utf-8 -*-
import psycopg2
from psycopg2 import OperationalError, errorcodes, errors

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

        # Inserir dados do país 'BR' manualmente
        insert_query = """
        INSERT INTO beta_observatory_country (
            name, name_numeric, name_2char, name_3char, continent, region_id,
            capital_city, longitude, latitude, coordinates, name_ar, name_de,
            name_el, name_en, name_es, name_fr, name_he, name_hi, name_it,
            name_ja, name_ko, name_nl, name_ru, name_pt, name_tr, name_zh_cn,
            originally_included
        ) VALUES (
            'Brazil', 76, 'br', 'BRA', 'South America', 2, 'Brasilia', -47.9292,
            -15.7801, 'Coordinates', 'Arabic', 'German', 'Greek', 'English',
            'Spanish', 'French', 'Hebrew', 'Hindi', 'Italian', 'Japanese',
            'Korean', 'Dutch', 'Russian', 'Portuguese', 'Turkish', 'Chinese', TRUE
        );
        """
        cursor.execute(insert_query)
        connection.commit()
        print("Dados do país 'BR' inseridos na tabela 'beta_observatory_country' com sucesso!")

    except OperationalError as oe:
        print("Erro de conexão ao banco de dados: {}".format(oe))
    except Exception as e:
        print("Erro ao inserir dados na tabela: {}".format(e))
    finally:
        if connection:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    insert_country_data()
