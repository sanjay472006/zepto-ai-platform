from sqlalchemy import create_engine


def load_data(df):

    engine = create_engine(
        "sqlite:///data_pipeline/data/processed/zepto.db"
    )

    df.to_sql(
        "orders",
        engine,
        if_exists="replace",
        index=False
    )

    print("Data loaded into database successfully!")