import uvicorn
from fastapi import FastAPI
from fastapi.responses import Response, StreamingResponse


from services.stable_diffusion_consumer import StableDiffusionConsumer

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/imageFromPromt")
async def image_from_promt(prompt: str):
    consumer = StableDiffusionConsumer()
    image_bytes = next(consumer.fetch_image(prompt))

    return StreamingResponse(image_bytes, media_type="image/png")

@app.post("/base64FromPrompt")
async def base64_from_prompt(prompt: str) -> str:
    pass

@app.post("/promptsFromText")
async def prompts_from_text(prompt: str) -> str:
    pass

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
