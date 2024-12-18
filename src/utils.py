import pandas as pd

def clean_data(df):
    """
    Cleans the input DataFrame by handling missing values and standardizing data.
    """
    try:
        # Replace missing values with zeros for numeric fields
        df.fillna(0, inplace=True)
        
        # Additional cleaning logic (if needed) can be added here
        return df
    except Exception as e:
        raise Exception(f"Error cleaning data: {e}")
