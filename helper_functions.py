import csv
import pandas as pd
import glob


def write_csv(fn, columns, data):
    """
    fn: file_name -> str
    columns: column_names -> list
    data: file contents -> list or set

    """
    with open(fn, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(columns)

        if isinstance(data, set):
            data = list(data)

        for line in data:
            writer.writerow(line)

        print(f"File written to {fn}")


def combine_like_files(fn, func):

    f_names = glob.glob(fn)

    df = pd.concat(map(func, f_names)).reset_index(drop=True)

    return df
