# 🚀 TradePilot AI Backend

TradePilot AI is an AI-powered trading backend built using FastAPI and the Upstox API.

The backend provides:

- Live market data
- Historical candle data
- Technical indicators
- AI-generated trading signals
- Market trend analysis
- Live market cache
- REST APIs for frontend and mobile applications

---

# Technologies Used

- Python 3.14
- FastAPI
- Uvicorn
- Pandas
- Requests
- Upstox API
- Pydantic

---

# Project Structure

Backend/

├── app/

│ ├── auth/

│ ├── brokers/

│ ├── config/

│ ├── core/

│ ├── market/

│ ├── models/

│ ├── routers/

│ ├── services/

│ ├── strategy/

│ ├── utils/

│ └── websocket/

├── requirements.txt

├── .env

└── README.md

---

# Installation

Clone the project.

Create virtual environment.

```bash
python -m venv venv
```

Activate it.

Windows:

```bash
venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# Run Backend

```bash
python -m uvicorn app.main:app --reload
```

Backend will start at

```
http://127.0.0.1:8000
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# Environment Variables

Create a `.env` file.

Example:

```env
APP_NAME=TradePilot AI
VERSION=1.0.0

UPSTOX_CLIENT_ID=YOUR_CLIENT_ID
UPSTOX_CLIENT_SECRET=YOUR_CLIENT_SECRET
UPSTOX_REDIRECT_URI=http://127.0.0.1:8000/auth/callback

UPSTOX_ACCESS_TOKEN=YOUR_ACCESS_TOKEN
```

---

# API Endpoints

## Health

```
GET /
GET /health
GET /status
```

## Market

```
GET /market/nifty
GET /market/banknifty
GET /market/live
GET /market/live/nifty
GET /market/live/banknifty
GET /market/history
```

## Strategy

```
GET /market/signal
```

## Authentication

```
GET /auth/login
GET /auth/callback
```

---

# Current Features

- Live NIFTY Market Data
- Live BANKNIFTY Market Data
- Historical Candles
- EMA
- RSI
- MACD
- Trend Detection
- Confidence Engine
- AI Signal Engine
- Live Market Cache
- Logging
- Exception Handling
- Status Monitoring

---

# Roadmap

Version 1.0

- Backend ✅

Version 2.0

- React Dashboard

Version 3.0

- Paper Trading

Version 4.0

- Android Application

---

Developed using FastAPI ❤️