# src/update.py
import pandas as pd
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def save_processed_data(df: pd.DataFrame, output_filepath: str):
    # Saves the processed DataFrame to a CSV file.
    if df.empty:
        logger.warning("Attempted to save an empty DataFrame. No file written.")
        return

    try:
        output_path = Path(output_filepath)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(output_filepath, index=False)
        logger.info(f"Successfully saved processed data to {output_filepath}. Rows: {len(df)}")
    except Exception as e:
        logger.critical(f"Failed to save processed data to {output_filepath}: {e}")

if __name__ == '__main__':
    dummy_data = {
        # Testing with dummy data 
        "SKU": ["SKU001", "SKU002"],
        "Description": ["Test A", "Test B"],
        "OnHandQty": [10, 20],
        "ReorderPoint": [5, 25],
        "ReorderQty": [5, 0]
    }
    dummy_df = pd.DataFrame(dummy_data)
    test_output_path = "../../data/inventory_processed_test.csv" # Adjust path
    save_processed_data(dummy_df, test_output_path)
    print(f"Check {test_output_path} for test output.")

    # Clean up test file 
    Path(test_output_path).unlink(missing_ok=True)