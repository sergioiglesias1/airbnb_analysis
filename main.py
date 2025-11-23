import pymongo
from pymongo_queries import get_top_cities, get_avg_price_by_property_type, get_room_type_distribution, get_price_distribution
from charts import plot_top_cities, plot_avg_price_by_property_type, plot_room_type_distribution, plot_price_distribution

def main():
    # Connect To MongoDB Database (Airbnb)
    try:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["Airbnb"]
        collection = db["airbnb_db"]
        count = collection.count_documents({})
        print(f"Connected to 'Airbnb' database, 'airbnb_db' collection.")
        print(f"Total documents: {count}")
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return

    # Run Queries & Generate Plots
    print("\nTop Markets by Listings...")
    top_cities = get_top_cities(collection)
    plot_top_cities(top_cities)

    print("\nAverage Price by Property Type (Top 10)...")
    avg_prices = get_avg_price_by_property_type(collection)
    plot_avg_price_by_property_type(avg_prices)

    print("\nRoom Type Distribution...")
    room_types = get_room_type_distribution(collection)
    plot_room_type_distribution(room_types)
    
    print("\nPrice Distribution...")
    prices = get_price_distribution(collection)
    plot_price_distribution(prices)

if __name__ == "__main__":
    main()
