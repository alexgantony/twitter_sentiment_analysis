def data_audit(df):
    print("Checking for duplicates...")
    print(f"Total duplicates: {df.duplicated().sum()}")
    print("*" * 50)

    print("Checking for missing values...")
    print(df.isna().sum())
    print("*" * 50)

    print('Checking for value counts in column "sentiment_label"...')
    print(df["sentiment_label"].value_counts())
    print("*" * 50)

    print('Checking for value counts in column "entity"...')
    print(df["entity"].value_counts())
    print("*" * 50)
