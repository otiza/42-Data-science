


import pandas as pd
from sqlalchemy import create_engine


def create_table(data,engine,table_name):

    print("creating the table and exporting the data")
    data.to_sql(table_name, engine, if_exists='replace', index=False)
    print("table created")


def create_db_engine(db_uri):
    engine = create_engine(db_uri)
    return engine



def main():
    DATABASE_URI = 'postgresql://amaaiza:mysecretpassword@localhost:5432/piscineds'
    file_path = "../../utils/subject/item/item.csv"
    engine = create_engine(DATABASE_URI)
    print("loading csv file")
    data = pd.read_csv(file_path)
    create_table(data,engine,"items")



if __name__ == "__main__":
    main()