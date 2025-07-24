# src/extract.py
import pandas as pd
import logging

# Configure logging for the module
logger = logging.getLogger(__name__)

def load_inventory_data(filepath: str) -> pd.DataFrame:
    # Loads inventory data from a CSV file into a pandas DataFrame.
    try:
        df = pd.read_csv(filepath)
        logger.info(f"Successfully loaded inventory data from {filepath}. Rows: {len(df)}")
        return df
    except FileNotFoundError:
        logger.error(f"Error: Inventory file not found at {filepath}")
        return pd.DataFrame() # Return empty DataFrame on error
    except pd.errors.EmptyDataError:
        logger.warning(f"Warning: The file at {filepath} is empty.")
        return pd.DataFrame()
    except Exception as e:
        logger.critical(f"An unexpected error occurred while loading data from {filepath}: {e}")
        return pd.DataFrame()

if __name__ == '__main__':
    # Example usage for testing
    test_df = load_inventory_data("../../data/inventory_raw.csv") 
    if not test_df.empty:
        print("Data loaded successfully (first 5 rows):")
        print(test_df.head())
    else:
        print("Failed to load data.")