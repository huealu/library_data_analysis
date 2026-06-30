import os
import pandas as pd
import numpy as np
import logging

Call_Number_Pattern = r'([A-Z]{1,3}\s?\d{1,4}\.?\d*\s?[A-Z]?)'


Call_Numbers = ["JFICTION*", "JMYSTERY*", "JSCIENCE*", "JSPORTS*",
                "J FICTION*", "J MYSTERY*", "J SCIENCE*", "J SPORTS*",
                "YFICTION*", "YSCIENCE*", "FICTION*",
                "MYST*", "SCIENCE FIC*", "WESTERN*", "SHORT STORY*",
                "EASY *", "READER*", "TWEEN*", "BOARD*",
                ".* LARGE PRINT.*", ".* LP",
                "MOVIE", "TV", "791.43.*", "791.45.*",
                "J0.*", "J1.*", "J2.*", "J3.*", "J4.*","J5.*","J6.*", "J7.*", "J8.*", "J9.*",
                "Y0.*", "Y1.*", "Y2.*", "Y3.*", "Y4.*","Y5.*", "Y6.*", "Y7.*", "Y8.*", "Y9.*",
                "0.*", "1.*", "3.*", "6.*", "9.*","2.*", "4.*", "5.*", "7.*", "8.*"]

def extract_call_number(df: pd.DataFrame, call_number_col: str) -> pd.DataFrame:
    """
    Extract the call number from the specified column in the DataFrame.
    
    Args:
        df (pd.DataFrame): The input DataFrame containing the call number column.
        call_number_col (str): The name of the column containing call numbers.
        
    Returns:
        pd.DataFrame: A DataFrame with an additional column 'extracted_call_number' containing the extracted call numbers.
        
    Raises:
        ValueError: If the specified column does not exist in the DataFrame.
    """
    if call_number_col not in df.columns:
        raise ValueError(f"Column '{call_number_col}' does not exist in the DataFrame.")
    
    call_number_group_df = pd.DataFrame()

    for word in Call_Numbers:
        sub_df = df[df[call_number_col].str.match(word) == True]
        sub_df['CN_Group'] = word
        call_number_group_df = pd.concat([call_number_group_df, sub_df], ignore_index=True)
    
    return call_number_group_df


def extract_call_number_with_regex(df: pd.DataFrame, call_number_col: str) -> pd.DataFrame:
    """
    Extract the call number from the specified column in the DataFrame using regex.
    
    Args:
        df (pd.DataFrame): The input DataFrame containing the call number column.
        call_number_col (str): The name of the column containing call numbers.
        
    Returns:
        pd.DataFrame: A DataFrame with an additional column 'extracted_call_number' containing the extracted call numbers.
        
    Raises:
        ValueError: If the specified column does not exist in the DataFrame.
    """
    if call_number_col not in df.columns:
        raise ValueError(f"Column '{call_number_col}' does not exist in the DataFrame.")
    
    df['extracted_call_number'] = df[call_number_col].str.extract(Call_Number_Pattern, expand=False)
    
    return df

