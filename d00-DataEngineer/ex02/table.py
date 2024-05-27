import pandas as pd
from sqlalchemy import create_engine


def create_db():
    # replace with your own database credentials
    DATABASE_URI = 'postgresql://amaaiza:mysecretpassword@localhost:5432/piscineds'
    print("engine created")
    engine = create_engine(DATABASE_URI)

    print("reading csv file")
    # read the CSV file
    df = pd.read_csv("../../utils/subject/customer/data_2022_oct.csv")

    # convert event_time to datetime
    df['event_time'] = pd.to_datetime(df['event_time'])

    print("creating the table and exporting the data")
    # create the table in postgres using the data frame
    df.to_sql('data_2022_oct', engine, if_exists='replace', index=False)
    print("table created")


if __name__ == "__main__":
    create_db()
