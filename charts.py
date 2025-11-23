import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_top_cities(data):
    if not data:
        print("No data for Top Cities")
        return
        
    df = pd.DataFrame(data)
    df['_id'] = df['_id'].fillna('Unknown')
    colors = plt.cm.viridis(np.linspace(0, 1, len(df)))

    plt.figure(figsize=(12, 6))
    plt.bar(df['_id'], df['count'], color=colors)
    plt.title('Top Markets by Listings', fontsize=14, fontweight='bold')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_avg_price_by_property_type(data):
    if not data:
        print("No data for Avg Price")
        return

    df = pd.DataFrame(data)
    df['avg_price'] = pd.to_numeric(df['avg_price'].astype(str).str.replace('[$,]', '', regex=True), errors='coerce')
    df = df.dropna(subset=['avg_price']).sort_values('avg_price', ascending=True)
    colors = plt.cm.plasma(np.linspace(0, 1, len(df)))

    plt.figure(figsize=(10, 6))
    plt.barh(df['_id'], df['avg_price'], color=colors)
    plt.title('Average Price by Property Type', fontsize=14, fontweight='bold')
    plt.xlabel('Price ($)')
    plt.tight_layout()
    plt.show()

def plot_room_type_distribution(data):
    if not data:
        print("No data for Room Types")
        return

    df = pd.DataFrame(data)
    colors = plt.cm.Set3(np.linspace(0, 1, len(df)))

    plt.figure(figsize=(6, 6))
    plt.pie(df['count'], labels=df['_id'], autopct='%1.1f%%', colors=colors, wedgeprops={'edgecolor': 'white'})
    plt.gca().add_artist(plt.Circle((0,0),0.70,fc='white'))
    plt.title('Room Type Distribution', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()

def plot_price_distribution(data):
    if not data:
        print("No data for Price Distribution")
        return

    df = pd.DataFrame(data)
    df['price'] = pd.to_numeric(df['price'].astype(str).str.replace('[$,]', '', regex=True), errors='coerce')
    # Filter outliers
    df = df[df['price'] < 1200]

    plt.figure(figsize=(10, 6))
    plt.hist(df['price'], bins=30, color='teal', edgecolor='white', alpha=0.7)
    plt.title('Price Distribution (< $1200)', fontsize=14, fontweight='bold')
    plt.xlabel('Price ($)')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()