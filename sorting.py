import pandas as pd

def qs_to_dataframe(qs_filename):
    """

    :param qs_filename:
    :return:
    """
    df = pd.read_excel(qs_filename)
    return df

if __name__ == "__main__":
    qs_input_filename = "./QS_2021.xlsx"
    qs_df = qs_to_dataframe(qs_input_filename)