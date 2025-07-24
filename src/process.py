# src/process.py
import pandas as pd
import numpy as np
import logging

# Configure logging for the module
logger = logging.getLogger(__name__)

def clean_and_process_inventory(df: pd.DataFrame) -> pd.DataFrame:
    # Cleans, deduplicates, and processes the inventory DataFrame.
    if df.empty:
        logger.warning("Input DataFrame for processing is empty.")
        return pd.DataFrame()

    initial_rows = len(df)

    # 1. Remove duplicate SKUs
    df.drop_duplicates(subset=['SKU'], keep='first', inplace=True)
    if len(df) < initial_rows:
        logger.info(f"Removed {initial_rows - len(df)} duplicate SKUs.")

    # 2. Ensure numeric types and handle non-numeric values
    for col in ['OnHandQty', 'ReorderPoint']:
        # Coerce non-numeric values to NaN, then fill NaN
        df[col] = pd.to_numeric(df[col], errors='coerce')
        # 3. Fill missing numeric values with 0 
        if df[col].isnull().any():
            missing_count = df[col].isnull().sum()
            logger.warning(f"Found and filled {missing_count} missing/non-numeric values in '{col}' with 0.")
            df[col] = df[col].fillna(0)
        # Ensure quantities are non-negative
        if (df[col] < 0).any():
            negative_count = (df[col] < 0).sum()
            logger.warning(f"Found and corrected {negative_count} negative values in '{col}' to 0.")
            df[col] = np.maximum(0, df[col])


    # 4. Calculate ReorderQty
    df['ReorderQty'] = np.maximum(0, df['ReorderPoint'] - df['OnHandQty'])
    logger.info("Calculated 'ReorderQty' for all items.")

    return df

if __name__ == '__main__':
    from extract import load_inventory_data # Import from extract module

    # Create a dummy DataFrame with some edge cases for testing
    dummy_data = {
        "SKU": ["SKU001", "SKU002", "SKU001", "SKU003", "SKU004", "SKU005"],
        "Description": ["Item A", "Item B", "Item A", "Item C", "Item D", "Item E"],
        "Location": ["WH1", "WH2", "WH1", "WH3", "WH1", "WH2"],
        "OnHandQty": [100, 20, "abc", 50, -5, 10], # 'abc' and -5 as edge cases
        "ReorderPoint": [50, 30, 50, 100, 20, None], # None as edge case
        "UnitCost": [10.5, 5.0, 10.5, 20.0, 15.0, 25.0]
    }
    dummy_df = pd.DataFrame(dummy_data)
    print("Dummy DataFrame before processing:")
    print(dummy_df)
    print("-" * 30)

    processed_dummy_df = clean_and_process_inventory(dummy_df.copy())
    print("\nDummy DataFrame after processing:")
    print(processed_dummy_df)
    print("-" * 30)

    # Test with generated data
    inventory_df = load_inventory_data("../../data/inventory_raw.csv")
    if not inventory_df.empty:
        processed_inventory_df = clean_and_process_inventory(inventory_df.copy())
        print("\nInventory Data (first 5 rows) after processing:")
        print(processed_inventory_df.head())
        print(f"Total rows after processing: {len(processed_inventory_df)}")
    else:
        print("Cannot test with inventory data: Data not loaded.")