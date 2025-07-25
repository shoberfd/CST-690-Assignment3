# CST 690 Assignment 2

## Project Overview

This project aims to automate the manual inventory management process at Retail Innovations Inc. by developing a Python-based solution. The automation will handle data import, cleaning, low stock flagging, and restock alerts.

## Toolchain

* **VS Code**: Integrated Development Environment
* **Python 3.11+**: Programming Language
* **Git/GitHub**: Version Control
* **GitHub Copilot**: AI-powered coding assistant

## Setup & Run

### Prerequisites

* Python 3.11+ installed

### Installation

1.    **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Generating Synthetic Data

To generate the initial `data/inventory_raw.csv` file, run:

```bash
python generate_fake_inventory.py
```