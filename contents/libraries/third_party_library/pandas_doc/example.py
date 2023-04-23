import pandas as pd

# Create a Pandas dataframe from some data.
df = pd.DataFrame(
    {
        "name": ["John Smith", "Jane Doe", "Mary Johnson"],
        "age": [34, 28, 29],
        "gender": ["M", "F", "F"],
    }
)


def csv_example():
    global df

    # Write the dataframe to a CSV file.
    df.to_csv("example.csv", index=False)

    # Read the CSV file back into a dataframe.
    df = pd.read_csv("example.csv")

    # Print the dataframe.
    print("\nCSV:")
    print(df)
    print()


def json_example():
    global df

    # Write the dataframe to a JSON file.
    df.to_json("example.json")

    # Read the JSON file back into a dataframe.
    df = pd.read_json("example.json")

    # Print the dataframe.
    print("\nJson:")
    print(df)
    print()


def excel_example():
    global df

    # Write the dataframe to an Excel file.
    df.to_excel("example.xlsx", sheet_name="Sheet1", index=False)

    # Read the Excel file back into a dataframe.
    df = pd.read_excel("example.xlsx", "Sheet1", index_col=None, na_values=["NA"])

    # Print the dataframe.
    print("\nExcel:")
    print(df)
    print()


def apply_example():
    global df

    # Create a new column with a default value.
    df["is_old"] = False

    # Apply a function to a column to update the values.
    df["is_old"] = df["age"].apply(lambda age: age > 30)

    print("\Apply:")
    print(df["is_old"])
    print()


def groupby_example():
    global df

    # Group the dataframe by gender.
    grouped = df.groupby("gender")

    # Print the mean age for each gender.
    print("\Groupby:")
    print(grouped["age"].mean())
    print()


def df_intersection_example():
    global df

    # Create a second dataframe.
    df2 = pd.DataFrame(
        {
            "name": ["John Smith", "Jane Doe"],
            "age": [34, 28],
            "gender": ["M", "F"],
        }
    )

    # Find the intersection of the two dataframes.
    intersection = pd.merge(df, df2, how="inner", on=["name", "age", "gender"])

    # Print the intersection.
    print("\nIntersection:")
    print(intersection)
    print()


def df_union_example():
    global df

    # Create a second dataframe.
    df2 = pd.DataFrame(
        {
            "name": ["John Smith", "Jane Doe"],
            "age": [34, 28],
            "gender": ["M", "F"],
        }
    )

    # Find the union of the two dataframes.
    union = pd.merge(df, df2, how="outer", on=["name", "age", "gender"])

    # Print the union.
    print("\nUnion:")
    print(union)
    print()


def df_difference_example():
    global df

    # Create a second dataframe.
    df2 = pd.DataFrame(
        {
            "name": ["John Smith", "Jane Doe"],
            "age": [34, 28],
            "gender": ["M", "F"],
        }
    )

    # Find the difference of the two dataframes.
    difference = pd.merge(df, df2, how="left", indicator=True).query(
        "_merge == 'left_only'"
    )

    print("\nDifference:")
    print(difference)
    print()


csv_example()
json_example()
excel_example()
apply_example()
groupby_example()
df_intersection_example()
df_union_example()
df_difference_example()
