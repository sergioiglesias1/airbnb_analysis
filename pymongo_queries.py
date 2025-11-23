def get_top_cities(collection):
    pipeline = [
        {"$group": {"_id": "$address.market", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        # Limit to top 20
        {"$limit": 20}
    ]
    return list(collection.aggregate(pipeline))

def get_avg_price_by_property_type(collection):
    pipeline = [
        {"$group": {"_id": "$property_type", "avg_price": {"$avg": "$price"}}},
        {"$sort": {"avg_price": -1}},
        {"$limit": 10}
    ]
    return list(collection.aggregate(pipeline))

def get_room_type_distribution(collection):
    pipeline = [
        {"$group": {"_id": "$room_type", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ]
    return list(collection.aggregate(pipeline))

def get_price_distribution(collection):
    query = {"price": {"$exists": True, "$ne": None}}
    projection = {"price": 1, "_id": 0}
    #db.airbnb_db.find({}, {price:1, _id:0}).sort({price:-1}).limit(1) <=> To see max. price (clear outlier here)
    return list(collection.find(query, projection))