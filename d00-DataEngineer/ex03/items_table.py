import os
import pandas as pd
from sqlalchemy import Engine, MetaData, create_engine


def create_table(data,engine,table_name):

    data['event_time'] = pd.to_datetime(data['event_time'])
    print("creating the table and exporting the data")
    data.to_sql(table_name, engine, if_exists='replace', index=False)
    print("table created")


def create_db_engine(db_uri):
    engine = create_engine(db_uri)
    return engine

def table_exist(table_name,engine :Engine) -> bool:
    metadata = MetaData()
    metadata.reflect(bind=engine)
    if table_name in metadata.tables:
        return True
    return False



def create_all_tables(folder,uri):
    engine = create_db_engine(uri)
    for filename in os.listdir(folder):
        if filename.endswith(".csv"):
            print(filename)
            table_name = os.path.splitext(filename)[0]
            file_path = os.path.join(folder,filename)
            print(table_name)
            print(file_path)
            if not table_exist(table_name,engine):
                print(f"table {table_name}")
                print("reading file")
                data = pd.read_csv(file_path)
                print(f"creating the table {table_name}")
                create_table(data,engine,table_name)

def main():
    folder_path = "../../utils/subject/customer/"
    DATABASE_URI = 'postgresql://amaaiza:mysecretpassword@localhost:5432/piscineds'

    create_all_tables(folder_path,DATABASE_URI)


if __name__ == "__main__":
    main()
