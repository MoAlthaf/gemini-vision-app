from fastapi import APIRouter, UploadFile, File
from app.services.ai_service import AIService
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

router = APIRouter()
ai_service = AIService()

router.mount("/static", StaticFiles(directory="app/static"), name="static")

@router.get("/")
async def read_index():
    return FileResponse("app/static/index.html")

@router.post("/analyze")
async def analyze_upload(file: UploadFile = File(...)):
    image_data = await file.read()
    description = await ai_service.analyze_image_bytes(image_data, file.content_type)
    return {"description": description}