from typing import Dict

import uvicorn
from fastapi import FastAPI
from fastapi.responses import Response, StreamingResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from dtos.Payload import PromptPayload, TextPayload
from services.prompt_extractor import PromptExtractor
from services.stable_diffusion_consumer import StableDiffusionConsumer

app = FastAPI()
cache = {}
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/imageFromPromt")
def image_from_promt(payload: PromptPayload):
    consumer = StableDiffusionConsumer()
    image_bytes = consumer.fetch_image(payload.prompt)

    return StreamingResponse(consumer.parse_to_bytesio(image_bytes), media_type="image/png")

@app.post("/base64FromPrompt")
def base64_from_prompt(payload: PromptPayload):
    consumer = StableDiffusionConsumer()
    img_json = {
        "image": consumer.fetch_image(payload.prompt)
    }

    return JSONResponse(content=img_json)

@app.post("/promptsFromText")
def prompts_from_text(text_payload: TextPayload):
    prompt_extractor = PromptExtractor()

    prompts = prompt_extractor.extract_paragraphs_with_prompts(text_payload.text)
    return [{"snippet": key, "prompt": value} for key, value in prompts.items()]


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
