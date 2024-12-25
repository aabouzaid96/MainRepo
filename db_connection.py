import psycopg2
from PIPELINE_POC.settings import DATABASES


def get_connection():
    """
    Establishes a connection to the PostgreSQL database using settings from DATABASES['default'].

    Returns:
        connection (psycopg2.extensions.connection): Database connection object if successful.
        None: If the connection fails.
    """
    try:
        # Extract database configuration from Django settings
        db_config = DATABASES['default']

        # Debugging logs (can be removed in production)
        print(f"Connecting to database: host={db_config['HOST']}, port={db_config['PORT']}")

        # Connect to the database
        connection = psycopg2.connect(
            host=db_config['HOST'],
            port=db_config['PORT'],
            user=db_config['USER'],
            password=db_config['PASSWORD'],
            database=db_config['NAME']
        )

        # Log success
        print("Database connection successful")
        return connection

    except Exception as e:
        # Log the error with details
        print(f"Error connecting to the database: {type(e).__name__}: {e}")
        return None
