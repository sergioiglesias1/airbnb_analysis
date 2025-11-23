# Airbnb Junior Mini-Project

## Overview

This mini-project demonstrates data aggregation and visualization using **MongoDB** and **Python** with real Airbnb listing data. The goal is to analyze trends in listings, prices, and room types across different cities and property types, providing insights for basic market analysis.

## Dataset

**Source:** Airbnb dataset containing listings and reviews (example: `listingsAndReviews.json`).
**Structure:** Each document includes fields such as:

* `name`: Listing name
* `address` / `city`: Location information
* `type_of_food` / `property_type`: Property or cuisine type
* `price`: Listing price
* `room_type`: Type of room
* `review_scores`: Ratings and reviews

**Note:** The dataset is structured as JSON documents and stored in MongoDB.

## Project Structure

```
.
├── visualizations/          # All plots
├── .gitignore            
├── charts.py                # Code for all plots
├── listingsAndReviews.json  # Original JSON data plugged into MongoDB
├── load_data.py             # Load data from MongoDB
├── main.py                  # Entry point: connects to DB and generates plots
├── pymongo_queries.py       # MongoDB aggregation queries
├── README.md
└── requirements.txt         # Python dependencies
```

## Methodology

* Count listings per city (`Top Markets`)
* Average price by property type
* Room type distributions
* Price distributions

**Visualization:**

* Bar charts for top markets
* Horizontal bars for average prices
* Donut charts for room types
* Histograms for price distributions

**Data Handling:**

* Converts price strings to numeric values
* Filters outliers for better visualization

## How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Make sure MongoDB is running locally and contains the database `Airbnb` with the collection `airbnb_db`.
3. Run the main script:

```bash
python main.py
```

## Key Insights

* Top cities with the highest number of listings
* Property types with the highest average prices
* Distribution of room types
* Typical price ranges and outlier detection
