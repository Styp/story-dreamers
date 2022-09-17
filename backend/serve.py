import uvicorn
from fastapi import FastAPI
from fastapi.responses import Response


from serivces.stable_diffusion_consumer import StableDiffusionConsumer

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/imageForPromt")
async def image_from_promt(prompt: str):
    consumer = StableDiffusionConsumer()
    image_bytes = next(consumer.fetch_image(prompt))

    return Response(content=image_bytes, media_type="image/png")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
