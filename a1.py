# -*- coding: utf-8 -*-
import psycopg2
from psycopg2 import OperationalError, errorcodes, errors

def create_tables(cursor):
    create_table_queries = [
        """
        CREATE TABLE IF NOT EXISTS auth_permission (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            content_type_id INTEGER NOT NULL,
            codename VARCHAR(100) NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS beta_observatory_country_region (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            color VARCHAR(7),
            text_color VARCHAR(7)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS observatory_story (
            story_id SERIAL PRIMARY KEY,
            story_name VARCHAR(200) NOT NULL,
            story_desc VARCHAR(2000),
            published BOOLEAN DEFAULT FALSE,
            featured BOOLEAN DEFAULT FALSE,
            likecount INTEGER DEFAULT 0,
            user_id INTEGER DEFAULT 1,
            number_of_chapters INTEGER DEFAULT 0
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS observatory_story_chapter (
            chapter_id SERIAL PRIMARY KEY,
            story_id INTEGER NOT NULL,
            chapter_details VARCHAR(2000),
            chapter_url VARCHAR(500) NOT NULL,
            chapter_desc VARCHAR(500),
            chapter_title VARCHAR(300) NOT NULL,
            chapter_js_details VARCHAR(2000),
            serial_number INTEGER NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS observatory_user (
            user_id SERIAL PRIMARY KEY,
            user_name VARCHAR(200) NOT NULL,
            user_email VARCHAR(50),
            user_auth_type VARCHAR(100),
            isadmin BOOLEAN DEFAULT FALSE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS observatory_likemode (
            user_id INTEGER NOT NULL,
            story_id INTEGER NOT NULL,
            PRIMARY KEY (user_id, story_id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS beta_observatory_country (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            name_numeric INTEGER,
            name_2char VARCHAR(2),
            name_3char VARCHAR(3),
            continent VARCHAR(255),
            region_id INTEGER REFERENCES beta_observatory_country_region(id),
            capital_city VARCHAR(255),
            longitude FLOAT,
            latitude FLOAT,
            coordinates VARCHAR(255),
            name_ar VARCHAR(255),
            name_de VARCHAR(255),
            name_el VARCHAR(255),
            name_en VARCHAR(255),
            name_es VARCHAR(255),
            name_fr VARCHAR(255),
            name_he VARCHAR(255),
            name_hi VARCHAR(255),
            name_it VARCHAR(255),
            name_ja VARCHAR(255),
            name_ko VARCHAR(255),
            name_nl VARCHAR(255),
            name_ru VARCHAR(255),
            name_pt VARCHAR(255),
            name_tr VARCHAR(255),
            name_zh_cn VARCHAR(255),
            originally_included BOOLEAN
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS beta_observatory_sitc4_cy (
            id SERIAL PRIMARY KEY,
            country_id INTEGER REFERENCES beta_observatory_country(id),
            year SMALLINT NOT NULL,
            eci FLOAT,
            eci_rank SMALLINT,
            oppvalue FLOAT,
            leader VARCHAR(100),
            magic FLOAT,
            pc_constant FLOAT,
            pc_current FLOAT,
            notpc_constant FLOAT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS beta_observatory_sitc4_community (
            id SERIAL PRIMARY KEY,
            code VARCHAR(4) NOT NULL,
            name VARCHAR(100),
            color VARCHAR(7),
            text_color VARCHAR(7),
            img VARCHAR(255)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS beta_observatory_sitc4 (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            code VARCHAR(4) NOT NULL,
            conversion_code VARCHAR(4),
            leamer_id INTEGER REFERENCES beta_observatory_sitc4_community(id),
            community_id INTEGER REFERENCES beta_observatory_sitc4_community(id),
            ps_x FLOAT,
            ps_y FLOAT,
            ps_size FLOAT,
            ps_x_classic FLOAT,
            ps_y_classic FLOAT,
            ps_size_classic FLOAT,
            name_ar TEXT,
            name_de TEXT,
            name_el TEXT,
            name_en TEXT,
            name_es TEXT,
            name_fr TEXT,
            name_he TEXT,
            name_hi TEXT,
            name_it TEXT,
            name_ja TEXT,
            name_ko TEXT,
            name_nl TEXT,
            name_ru TEXT,
            name_pt TEXT,
            name_tr TEXT,
            name_zh_cn TEXT,
            color TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS beta_observatory_sitc4_py (
            id SERIAL PRIMARY KEY,
            product_id INTEGER REFERENCES beta_observatory_sitc4(id),
            year SMALLINT NOT NULL,
            pci FLOAT,
            pci_rank SMALLINT,
            world_trade FLOAT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS beta_observatory_hs4_community (
            id SERIAL PRIMARY KEY,
            code VARCHAR(4) NOT NULL,
            name VARCHAR(100),
            color VARCHAR(7),
            text_color VARCHAR(7)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS beta_observatory_hs4 (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            code VARCHAR(4) NOT NULL,
            conversion_code VARCHAR(4),
            community_id INTEGER REFERENCES beta_observatory_hs4_community(id),
            ps_x FLOAT,
            ps_y FLOAT,
            ps_size FLOAT,
            name_ar TEXT,
            name_de TEXT,
            name_el TEXT,
            name_en TEXT,
            name_es TEXT,
            name_fr TEXT,
            name_he TEXT,
            name_hi TEXT,
            name_it TEXT,
            name_ja TEXT,
            name_ko TEXT,
            name_nl TEXT,
            name_ru TEXT,
            name_pt TEXT,
            name_tr TEXT,
            name_zh_cn TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS beta_observatory_hs4_py (
            id SERIAL PRIMARY KEY,
            product_id INTEGER REFERENCES beta_observatory_hs4(id),
            year SMALLINT NOT NULL,
            pci FLOAT,
            pci_rank SMALLINT,
            world_trade FLOAT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS auth_group (
            id SERIAL PRIMARY KEY,
            name VARCHAR(80) NOT NULL UNIQUE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS auth_group_permissions (
            id SERIAL PRIMARY KEY,
            group_id INTEGER NOT NULL REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED,
            permission_id INTEGER NOT NULL REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS auth_user (
            id SERIAL PRIMARY KEY,
            password VARCHAR(128) NOT NULL,
            last_login TIMESTAMPTZ NULL,
            is_superuser BOOLEAN NOT NULL,
            username VARCHAR(30) NOT NULL UNIQUE,
            first_name VARCHAR(30) NOT NULL,
            last_name VARCHAR(30) NOT NULL,
            email VARCHAR(75) NOT NULL,
            is_staff BOOLEAN NOT NULL,
            is_active BOOLEAN NOT NULL,
            date_joined TIMESTAMPTZ NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS auth_user_groups (
            id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED,
            group_id INTEGER NOT NULL REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS auth_user_user_permissions (
            id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED,
            permission_id INTEGER NOT NULL REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS django_content_type (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            app_label VARCHAR(100) NOT NULL,
            model VARCHAR(100) NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS django_session (
            session_key VARCHAR(40) NOT NULL PRIMARY KEY,
            session_data TEXT NOT NULL,
            expire_date TIMESTAMPTZ NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS django_site (
            id SERIAL PRIMARY KEY,
            domain VARCHAR(100) NOT NULL,
            name VARCHAR(50) NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS beta_observatory_hs4_cpy (
            id SERIAL PRIMARY KEY,
            country_id INTEGER REFERENCES beta_observatory_country(id),
            product_id INTEGER REFERENCES beta_observatory_hs4(id),
            year SMALLINT NOT NULL,
            export_value FLOAT,
            import_value FLOAT,
            export_rca FLOAT,
            distance FLOAT,
            opp_gain FLOAT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS beta_observatory_hs4_ccpy (
            id SERIAL PRIMARY KEY,
            year SMALLINT NOT NULL,
            origin_id INTEGER REFERENCES beta_observatory_country(id),
            destination_id INTEGER REFERENCES beta_observatory_country(id),
            product_id INTEGER REFERENCES beta_observatory_hs4(id),
            export_value FLOAT,
            import_value FLOAT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS beta_observatory_wdi (
            id SERIAL PRIMARY KEY,
            code VARCHAR(200) NOT NULL,
            name VARCHAR(200) NOT NULL,
            desc_short VARCHAR(255),
            desc_long TEXT,
            source VARCHAR(50),
            topic VARCHAR(50),
            aggregation VARCHAR(50)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS beta_observatory_wdi_cwy (
            id SERIAL PRIMARY KEY,
            country_id INTEGER REFERENCES beta_observatory_country(id),
            wdi_id INTEGER REFERENCES beta_observatory_wdi(id),
            year SMALLINT NOT NULL,
            value FLOAT
        );
        """
    ]

    for query in create_table_queries:
        cursor.execute(query)

def insert_specific_country_data():
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

        # Criar as tabelas se não existirem
        create_tables(cursor)
        connection.commit()

        # Verificar se o registro na tabela beta_observatory_country_region já existe
        cursor.execute("SELECT COUNT(*) FROM beta_observatory_country_region WHERE id=1;")
        count = cursor.fetchone()[0]

        if count == 0:
            # Inserir dados na tabela beta_observatory_country_region
            insert_region_query = """
            INSERT INTO beta_observatory_country_region (id, name, color, text_color)
            VALUES (1, 'North America', '#FFFFFF', '#000000');
            """
            cursor.execute(insert_region_query)
            connection.commit()
            print("Dados da região 'North America' inseridos na tabela 'beta_observatory_country_region' com sucesso!")
        else:
            print("A região 'North America' já existe na tabela 'beta_observatory_country_region'.")

        # Verificar se o registro já existe na tabela beta_observatory_country
        cursor.execute("SELECT COUNT(*) FROM beta_observatory_country WHERE name_2char='us';")
        count = cursor.fetchone()[0]

        if count == 0:
            # Inserir dados do país 'US'
            insert_country_query = """
            INSERT INTO beta_observatory_country (name, name_numeric, name_2char, name_3char, continent, region_id, capital_city, longitude, latitude, coordinates, name_ar, name_de, name_el, name_en, name_es, name_fr, name_he, name_hi, name_it, name_ja, name_ko, name_nl, name_ru, name_pt, name_tr, name_zh_cn, originally_included)
            VALUES
            ('United States', 840, 'us', 'USA', 'North America', 1, 'Washington D.C.', -77.0369, 38.9072, 'Coordinates', 'Arabic', 'German', 'Greek', 'English', 'Spanish', 'French', 'Hebrew', 'Hindi', 'Italian', 'Japanese', 'Korean', 'Dutch', 'Russian', 'Portuguese', 'Turkish', 'Chinese', TRUE);
            """
            cursor.execute(insert_country_query)
            connection.commit()
            print("Dados do país 'US' inseridos na tabela 'beta_observatory_country' com sucesso!")
        else:
            print("O país 'US' já existe na tabela 'beta_observatory_country'.")

    except OperationalError as oe:
        print("Erro de conexão ao banco de dados: {}".format(oe))
    except Exception as e:
        print("Erro ao inserir dados na tabela: {}".format(e))
    finally:
        if connection:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    insert_specific_country_data()