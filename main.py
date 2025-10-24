from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Algo Trade Bot is live on Railway 🚀"}

@app.post("/webhook")
async def webhook(data: dict):
    print("Signal received:", data)
    return {"status": "ok", "data": data}
