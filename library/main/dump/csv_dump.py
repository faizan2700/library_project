import psycopg2

# PostgreSQL connection parameters
DB_HOST = 'localhost'
DB_NAME = 'library_db'
DB_USER = 'postgres'
DB_PASSWORD = 'admin'

# Function to dump table to CSV
def dump_table_to_csv(table_name, output_file):
    try:
        connection = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
        cursor = connection.cursor()

        # Execute SQL query to fetch data from table
        cursor.execute(f"COPY (SELECT * FROM {table_name}) TO '{output_file}' WITH CSV HEADER;")

        print(f"Table '{table_name}' dumped to '{output_file}' successfully.")

    except (Exception, psycopg2.Error) as error:
        print(f"Error while dumping table '{table_name}' to CSV:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()

# Dump all tables to CSV files
tables_to_dump = ['books_author',
                    'books_book',
                    'books_book_authors',
                    'books_book_shelves',
                    'books_book_languages',
                    'books_book_subjects',
                    'books_bookshelf',
                    'books_format',
                    'books_language',
                    'books_format']  # List of tables to dump
for table_name in tables_to_dump:
    output_file = f"C:/Users/lenovo/OneDrive/Documents/library_project/dump/{table_name}.csv" 
    print(output_file) 
    dump_table_to_csv(table_name, output_file)