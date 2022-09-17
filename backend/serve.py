from typing import Dict

import uvicorn
from fastapi import FastAPI
from fastapi.responses import Response, StreamingResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from dtos.Payload import Payload
from services.prompt_extractor import PromptExtractor
from services.stable_diffusion_consumer import StableDiffusionConsumer

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/imageFromPromt")
async def image_from_promt(prompt: str):
    consumer = StableDiffusionConsumer()
    image_bytes = next(consumer.fetch_image(prompt))

    return StreamingResponse(consumer.parse_to_bytesio(image_bytes), media_type="image/png")



@app.post("/base64FromPrompt")
async def base64_from_prompt(payload: Payload) -> JSONResponse:
    print(payload)
    consumer = StableDiffusionConsumer()
    img_json = {
        "image": next(consumer.fetch_image(payload.prompt))
    }

    return JSONResponse(content=img_json)


@app.post("/promptsFromText")
async def prompts_from_text(prompt: str) -> Dict[str, str]:
    prompt_extractor = PromptExtractor()
    return prompt_extractor.extract_paragraphs_with_prompts(prompt)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
