import pandas as pd
import numpy as np
from datetime import datetime, timedelta, date
import logging


def volume_count(df: pd.DataFrame, date_col: str) -> list:
    """
    Count the number of volumes in the dataframe based on the specified column.
    """
    if date_col not in df.columns:
        raise ValueError(f"Column '{date_col}' does not exist in the DataFrame.")
    
    count = np.where(df[date_col].notnull(), 1, 0)
    return count


def items_have_no_circulations_after_inventory(
        df: pd.DataFrame, 
        creation_date_col: str, 
        circulation_history_col: str) -> list:
    """
    Check if items have no circulation after the inventory date.
    """
    if creation_date_col not in df.columns:
        raise ValueError(f"Column '{creation_date_col}' does not exist in the DataFrame.")
    if circulation_history_col not in df.columns:
        raise ValueError(f"Column '{circulation_history_col}' does not exist in the DataFrame.")
    
    no_circulation = np.where((df[creation_date_col] > datetime.now()) 
                              & (df[circulation_history_col] == 0), 1, 0)
    
    return no_circulation