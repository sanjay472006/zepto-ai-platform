from extract import extract_data
from transform import transform_data
from validate import validate_data
from load import load_data


FILE_PATH = "data_pipeline/data/raw/orders.csv"


def run_pipeline():

    print("\nStarting Zepto Data Pipeline...\n")

    # 1. Extract
    print("1. Extracting data...")
    df = extract_data(FILE_PATH)

    # 2. Transform
    print("2. Transforming data...")
    df = transform_data(df)

    # 3. Validate
    print("3. Validating data...")
    validate_data(df)

    # 4. Load
    print("4. Loading data into database...")
    load_data(df)

    print("\nPipeline completed successfully! ✅")


if __name__ == "__main__":
    run_pipeline()