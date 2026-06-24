import os
import glob 
import pandas as pd
import numpy as np
import logging
from pathlib import Path


# Configure logging
logger = logging.getLogger(__name__)



def load_data_file(filename: str) -> pd.DataFrame:
    """
    Load a data file (CSV or Excel) into a pandas DataFrame.
    
    Args:
        filename (str): The path to the data file.
        
    Returns:
        pd.DataFrame: The loaded DataFrame.
        
    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If the file format is unsupported or cannot be read.
    """
    # Validate input files exist
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Data file not found: {filename}")
    
    try:
        return pd.read_csv(filename, encoding='latin-1')
    except Exception as e:
        logger.error(f"Error loading file {filename}: {e}")
        raise ValueError(f"Unsupported file format or unable to read the file: {filename}")



def read_csv_files_from_directory(
        directory_path: str, 
        file_pattern: str = "*.csv") -> pd.DataFrame:
    """
    Read all CSV files from a specified directory and concatenate them into a single DataFrame.
    Args:
        directory_path (str): The path to the directory containing CSV files.
        file_pattern (str): The pattern to match CSV files. Default is "*.csv".
    Returns:
        pd.DataFrame: A concatenated DataFrame containing data from all CSV files.
    """
    directory = Path(directory_path)
    csv_files = glob.glob(str(directory / file_pattern))
    
    if not csv_files:
        logger.warning(f"No CSV files found in directory: {directory_path}")
        return pd.DataFrame()

    dataframes = []
    for file in csv_files:
        df = pd.read_csv(file)
        dataframes.append(df)

    return pd.concat(dataframes, ignore_index=True)