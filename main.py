# main.py
import argparse
import logging
from pathlib import Path
import time
from dotenv import load_dotenv # For python-dotenv if you decide to use it for secrets

# Load environment variables from .env file (if it exists)
load_dotenv()

# --- Logging Setup ---
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "run.log"

# Clear previous log file content on each run for simplicity during development
if LOG_FILE.exists():
    with open(LOG_FILE, 'w') as f:
        f.truncate(0)

# Configure the root logger
logging.basicConfig(
    level=logging.INFO, # Set overall logging level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),  # Log to file
        logging.StreamHandler()         # Log to console
    ]
)

# Set pandas logger to a higher level to reduce verbosity in logs
logging.getLogger('pandas').setLevel(logging.WARNING)

# Import our custom modules
from src.extract import load_inventory_data
from src.process import clean_and_process_inventory
from src.update import save_processed_data

logger = logging.getLogger(__name__) # Logger for main.py

def main():
    # Orchestrates the inventory automation workflow:
    # 1. Parses command-line arguments for input and output file paths.
    # 2. Loads raw inventory data.
    # 3. Cleans and processes the inventory data.
    # 4. Saves the processed data to a new CSV file.
    # 5. (Optional) Sends low-stock alerts.

    parser = argparse.ArgumentParser(description="Automates inventory data processing.")
    parser.add_argument(
        "--input",
        type=str,
        default="data/inventory_raw.csv",
        help="Path to the raw inventory CSV file."
    )
    parser.add_argument(
        "--output",
        type=str,
        default="data/inventory_processed.csv",
        help="Path to save the processed inventory CSV file."
    )

    args = parser.parse_args()

    logger.info("--- Inventory Automation Workflow Started ---")
    start_time = time.time()

    # --- Step 1: Data Extraction ---
    logger.info(f"Loading raw inventory data from: {args.input}")
    raw_df = load_inventory_data(args.input)
    if raw_df.empty:
        logger.error("No data loaded. Exiting workflow.")
        return

    # --- Step 2: Data Processing ---
    logger.info("Cleaning and processing inventory data...")
    processed_df = clean_and_process_inventory(raw_df.copy())
    if processed_df.empty:
        logger.error("No data after processing. Exiting workflow.")
        return

    # --- Step 3: Data Update / Output ---
    logger.info(f"Saving processed inventory data to: {args.output}")
    save_processed_data(processed_df, args.output)
    end_time = time.time()
    runtime = end_time - start_time
    logger.info(f"--- Inventory Automation Workflow Completed in {runtime:.2f} seconds ---")
    logger.info(f"Processed data saved to {args.output}")

if __name__ == "__main__":
    main()