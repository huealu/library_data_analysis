import os
import re 
import pandas as pd 
from datetime import datetime, timedelta, date

# Set up the weekdays in order for categorical data
Weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']



def add_week_day(df: pd.DataFrame, date_col: str) -> pd.DataFrame:
  """
  Add day of week for date values
  """
  df[date_col] = pd.to_datetime(df[date_col])
  df['day_of_week'] = df[date_col].dt.day_name()
  df['day_of_week'] = df['day_of_week'].astype('category')
  df['day_of_week'] = df['day_of_week'].cat.reorder_categories(Weekdays)
  return df


def add_month(df: pd.DataFrame, date_col: str) -> pd.DataFrame:
  """
  Add month for date values
  """
  df[date_col] = pd.to_datetime(df[date_col])
  df['month'] = df[date_col].dt.month
  return df


def add_year(df: pd.DataFrame, date_col: str) -> pd.DataFrame:
  """
  Add year for date values
  """
  df[date_col] = pd.to_datetime(df[date_col])
  df['year'] = df[date_col].dt.year
  return df