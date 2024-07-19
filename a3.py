# -*- coding: utf-8 -*-
import pandas as pd
import psycopg2
from psycopg2 import OperationalError, errorcodes, errors

# Carregar os dados dos arquivos
country_codes = pd.read_excel('country_code_baci92.xlsx')
country_names = pd.read_stata('country_names.dta')

# Verificar os dados carregados
print("Country Codes:")
print(country_codes.head())

print("\nCountry Names:")
print(country_names.head())

# Merge dos dados usando 'iso3'
country_data = pd.merge(country_codes, country_names, left_on='iso3', right_on='iso3')

# Verificar os dados mesclados
print("\nMerged Country Data:")
print(country_data.head())

def to_utf8(value):
    if isinstance(value, str):
        return value.encode('utf-8')
    if isinstance(value, unicode):
        return value.encode('utf-8')
    return str(value).encode('utf-8')

def create_country_objects(cursor, country_data):
    for index, row in country_data.iterrows():
        # Verificar se o registro já existe
        cursor.execute("SELECT COUNT(*) FROM beta_observatory_country WHERE name_3char = %s;", (to_utf8(row['iso3']),))
        count = cursor.fetchone()[0]

        if count == 0:
            insert_query = """
            INSERT INTO beta_observatory_country (
                name, name_numeric, name_2char, name_3char, continent,
                region_id, capital_city, longitude, latitude, coordinates,
                name_ar, name_de, name_el, name_en, name_es, name_fr, name_he,
                name_hi, name_it, name_ja, name_ko, name_nl, name_ru, name_pt,
                name_tr, name_zh_cn, originally_included
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            );
            """
            cursor.execute(insert_query, (
                to_utf8(row['name_observatory'])[:255],  # name
                int(row['i']) if not pd.isnull(row['i']) else None,  # name_numeric
                to_utf8(row['iso2'])[:2],  # name_2char
                to_utf8(row['iso3'])[:3],  # name_3char
                to_utf8('Unknown'),  # continent
                None,  # region_id
                to_utf8('Unknown')[:255],  # capital_city
                None,  # longitude
                None,  # latitude
                to_utf8('Unknown')[:255],  # coordinates
                to_utf8('Arabic')[:255],  # name_ar
                to_utf8('German')[:255],  # name_de
                to_utf8('Greek')[:255],  # name_el
                to_utf8('English')[:255],  # name_en
                to_utf8('Spanish')[:255],  # name_es
                to_utf8('French')[:255],  # name_fr
                to_utf8('Hebrew')[:255],  # name_he
                to_utf8('Hindi')[:255],  # name_hi
                to_utf8('Italian')[:255],  # name_it
                to_utf8('Japanese')[:255],  # name_ja
                to_utf8('Korean')[:255],  # name_ko
                to_utf8('Dutch')[:255],  # name_nl
                to_utf8('Russian')[:255],  # name_ru
                to_utf8('Portuguese')[:255],  # name_pt
                to_utf8('Turkish')[:255],  # name_tr
                to_utf8('Chinese')[:255],  # name_zh_cn
                True  # originally_included
            ))

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

        # Criar objetos Country a partir dos dados
        create_country_objects(cursor, country_data)
        connection.commit()
        print("Dados dos países inseridos na tabela 'beta_observatory_country' com sucesso!")

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
