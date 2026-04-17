from fastapi import FastAPI
from app.api.schemas import ChatRequest
from app.agent.engine import engine
from fastapi import UploadFile, File
import base64

app = FastAPI()


@app.post("/chat")
def chat(req: ChatRequest):

    result = engine(
        input_type="text",
        data=req.data
    )

    return {
        "output": result
    }

@app.post("/chat/image-upload")
async def chat_image(file: UploadFile = File(...)):

    image_bytes = await file.read()
    image_base64 = base64.b64encode(image_bytes).decode("utf-8")

    result = engine("image", image_base64)

    return {"output": result}