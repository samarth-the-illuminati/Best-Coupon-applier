from flask import Flask, request, jsonify
from flask_cors import CORS
from restaurant_agent import find_best_restaurant
from coupons import coupons

app = Flask(__name__)
CORS(app)   # <-- VERY IMPORTANT

@app.route("/")
def home():
    return "SmartFood AI API is running"

@app.route("/deals", methods=["POST"])
def deals():

    data = request.json

    user_lat = data["lat"]
    user_lon = data["lon"]

    results = find_best_restaurant(
        coupons,
        (user_lat, user_lon)
    )

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)