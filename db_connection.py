import psycopg2
from PIPELINE_POC.settings import DATABASES

def get_connection():
    try:
        db_config = DATABASES['default']

        print('db_config[HOST]', db_config['HOST'])
        print('db_config[PORT]', db_config['PORT'])
        print('db_config[USER]', db_config['USER'])
        print('db_config[NAME]', db_config['NAME'])
        connection = psycopg2.connect(
            host=db_config['HOST'],
            port=db_config['PORT'],
            user=db_config['USER'],
            password=db_config['PASSWORD'],
            database=db_config['NAME']
        )
        print("Database connection successful")
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None