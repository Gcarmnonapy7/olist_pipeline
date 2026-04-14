---

# Olist Data Engineering Pipeline (PySpark Lakehouse)

![Python](https://img.shields.io/badge/Python-3.12-blue)
![PySpark](https://img.shields.io/badge/PySpark-3.5.1-orange)
![Architecture](https://img.shields.io/badge/Architecture-Lakehouse-green)
![Status](https://img.shields.io/badge/Status-Production--Ready-brightgreen)

---

## Overview

This project implements an end-to-end **Data Engineering pipeline** using the **Brazilian E-Commerce Public Dataset by Olist**, following a **Lakehouse architecture**.

The pipeline ingests raw data, performs distributed transformations using **PySpark**, and produces **analytics-ready datasets**. It is designed to simulate real-world workflows aligned with modern cloud platforms such as Azure.

---

## Architecture

The pipeline follows the **Bronze → Silver → Gold** data model.

```
            ┌──────────────┐
            │   Raw Data   │
            └──────┬───────┘
                   │
                   ▼
            ┌──────────────┐
            │   Bronze     │  (Raw Parquet)
            └──────┬───────┘
                   │
                   ▼
            ┌──────────────┐
            │   Silver     │  (Clean + Joined)
            └──────┬───────┘
                   │
                   ▼
            ┌──────────────┐
            │    Gold      │  (Aggregations)
            └──────────────┘
```

---

## Data Source

* Brazilian E-Commerce Public Dataset by Olist
* ~100k orders (2016–2018)
* Multi-table relational structure (orders, customers, products, payments, logistics)

---

## Tech Stack

* PySpark (distributed data processing)
* Parquet (columnar storage)
* Spark SQL (analytical queries)
* Python (pipeline orchestration)
* kagglehub (data ingestion)
* logging (observability)

---

## Pipeline Design

### 1. Ingestion (Bronze Layer)

* Reads raw CSV files
* Converts to Parquet format
* Stores data in a structured Data Lake layout

### 2. Transformation (Silver Layer)

* Joins multiple datasets:

  * orders
  * order_items
  * customers
  * products
  * payments
* Cleans and validates data
* Feature engineering:

  * total_price = price + freight
  * delivery_time (days)

### 3. Serving (Gold Layer)

Creates business-level datasets:

* Revenue by product category
* Orders per state
* Average delivery time by region

### 4. Query Layer

Supports SQL-based analytics using Spark SQL.

---

## Project Structure

```
olist_pipeline/
├── data/
│   ├── raw/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── pipelines/
│   ├── ingest.py
│   ├── transform.py
│   └── serve.py
│
├── utils/
│   ├── spark.py
│   └── logger.py
│
├── logs/
├── download_data.py
├── main.py
└── README.md
```

---

## Logging and Observability

The pipeline includes structured logging for:

* Execution tracking
* Error handling
* Step-level monitoring
* Data volume tracking

Example:

```
2026-04-14 10:00:01 | PIPELINE | INFO | Pipeline started
2026-04-14 10:00:05 | INGEST   | INFO | Saved orders to bronze
2026-04-14 10:00:10 | TRANSFORM| INFO | Join completed
2026-04-14 10:00:15 | PIPELINE | INFO | Completed successfully
```

---

## Data Quality

Basic validation rules:

* No negative prices
* Null value handling
* Schema consistency
* Row count validation

---

## How to Run

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Download dataset

```
python download_data.py
```

### 3. Execute pipeline

```
python main.py
```

---

## Example Query (Spark SQL)

```
SELECT customer_state, SUM(total_price) AS revenue
FROM ecommerce
GROUP BY customer_state
ORDER BY revenue DESC;
```

---

## Azure Mapping (Real-World Equivalent)

| Project Component | Azure Equivalent   |
| ----------------- | ------------------ |
| Python pipeline   | Azure Data Factory |
| PySpark           | Azure Databricks   |
| Parquet files     | Data Lake Storage  |
| Spark SQL         | Synapse Analytics  |
| Logging           | Azure Monitor      |

---

## Key Concepts Demonstrated

* ETL / ELT pipeline design
* Data Lakehouse architecture
* Distributed processing with PySpark
* Data validation and quality checks
* Logging and observability
* SQL-based analytics

---

## Future Improvements

* Incremental data ingestion
* Partitioning strategy optimization
* Delta Lake integration
* Workflow orchestration (Airflow)
* Streaming pipelines (Kafka)

---

## Author

Gabriel Carmona
Computer Science student focused on Data Engineering and Machine Learning

---

## Final Note

This project demonstrates a production-oriented approach to Data Engineering, focusing on:

* Scalability
* Reliability
* Observability

---
