import uvicorn
from fastapi import FastAPI

from backend.serivces.stable_diffusion_consumer import StableDiffusionConsumer

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/imageForPromt")
async def image_from_promt(prompt: str):
    consumer = StableDiffusionConsumer()
    return consumer.fetch_image(prompt)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
