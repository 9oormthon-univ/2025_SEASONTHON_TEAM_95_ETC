from fastapi import FastAPI, HTTPException
from schemas.request_schema import ImageRequest
from services.inference_service import run_inference

app = FastAPI()

@app.post("/analyze")
async def analyze_image(request: ImageRequest):
    try:
        result = run_inference(request.image_url)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
