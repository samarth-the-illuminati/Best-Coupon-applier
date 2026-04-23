# 🍔 SmartFood AI – Food Deal Optimizer

SmartFood AI is an intelligent food recommendation system that finds the **cheapest meal combinations** from nearby restaurants by analyzing menus, applying coupon strategies, and optimizing total cost.

---

## 🚀 Features

* 📍 **Location-based filtering** – finds nearby restaurants using user coordinates
* 🍽️ **Menu optimization** – generates different meal combinations
* 💸 **Coupon engine** – applies multiple coupon strategies (FREEDEL, SAVE50, etc.)
* 🧠 **Decision engine** – selects the cheapest valid order
* 📊 **Ranking system** – shows top deals sorted by price and distance
* 🌐 **Web interface** – interactive frontend to explore deals

---

## 🧠 How It Works

1. User enters location (or uses live GPS)
2. Frontend sends request to Flask API
3. Backend loads restaurant data
4. System filters nearby restaurants
5. Generates possible meal combinations
6. Applies coupon strategies
7. Calculates final price
8. Returns top cheapest deals

---

## 🏗️ Architecture

```
Frontend (HTML + JS)
        ↓
Fetch API Request
        ↓
Flask Backend (/deals)
        ↓
Restaurant Agent
        ↓
Optimization Engine
   - Menu combinations
   - Coupon strategies
   - Cost evaluation
        ↓
Restaurant Data (JSON)
```

---

## 🖥️ Demo

### Example Output

```
Wrap City
Items: 1 x Paneer Wrap
Price: ₹160
Distance: 0.64 km
Strategy: Apply FREEDEL

Burger Hub
Items: 1 x Veg Burger + 1 x Coke
Price: ₹160
Distance: 0 km
Strategy: Apply FREEDEL
```

---

## 🛠️ Tech Stack

### Backend

* Python
* Flask
* REST API

### Frontend

* HTML
* JavaScript (Fetch API)

### Data

* JSON (restaurant database)

---

## 📂 Project Structure

```
smartfood-ai/
│
├── app.py
├── restaurant_agent.py
├── quantity_optimizer.py
├── coupon_engine.py
├── strategy_search.py
├── geo_utils.py
├── data_loader.py
│
├── data/
│   └── restaurants.json
│
├── frontend/
│   └── index.html
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Run

### 1. Clone the repo

```
git clone https://github.com/your-username/smartfood-ai.git
cd smartfood-ai
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the backend

```
python app.py
```

Server will start at:

```
http://127.0.0.1:5000
```

### 4. Open frontend

Open:

```
frontend/index.html
```

---

## 📌 Future Improvements

* 🗺️ Map-based restaurant visualization
* 🤖 Smarter coupon unlocking strategies
* 📦 Integration with real restaurant APIs
* ⏱️ Delivery time prediction
* 🎯 Personalized recommendations

---

## 💡 Key Learnings

* Building a full-stack application
* Designing optimization-based decision systems
* Working with APIs and frontend-backend communication
* Applying constraint-based search logic

---

## ⭐ Acknowledgment

This project was built as a hands-on exploration of combining **AI decision-making with real-world applications** like food delivery optimization.

---

## 📬 Feedback

Feel free to open issues or suggest improvements!

---
