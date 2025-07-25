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

To generate the 'data/inventory_processed.csv' file, run:

```bash
python generate_fake_inventory.py
```

---

## KPIs & Metrics

| Metric              | Baseline (Manual)              | Target (Automated)                 |
| :------------------ | :----------------------------- | :--------------------------------- |
| **Time Spent** | 45 min/warehouse/day           | $\geq 90\%$ reduction              |
| **Error Rate** | $\sim 15\%$ data entry errors | $\geq 80\%$ elimination            |
| **Inventory Accuracy** | Existing (e.g., 85%)          | $\geq 10\%$ improvement            |
| **Stockouts** | Avg. 5 critical stockouts/week | $\geq 50\%$ reduction (high-demand)|

---