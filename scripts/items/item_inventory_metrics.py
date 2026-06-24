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