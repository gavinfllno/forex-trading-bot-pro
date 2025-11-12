from fastapi import FastAPI
import numpy as np
from datetime import datetime

app = FastAPI(title="Forex Trading Bot")

@app.get("/")
async def root():
    return {
        "message": "Forex Bot is Running!",
        "status": "ACTIVE",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/analyze/{pair}")
async def analyze_pair(pair: str):
    price = 1.0850 + np.random.random() * 0.01
    return {
        "pair": pair,
        "price": round(price, 5),
        "signal": "BUY" if np.random.random() > 0.5 else "SELL",
        "timestamp": datetime.now().isoformat()
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
