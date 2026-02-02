from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from PIL import Image
import io

app = FastAPI(title="Image Preprocessing API")

@app.post("/preprocess")
async def preprocess_image(
    file: UploadFile = File(...),
    width: int = 256,
    height: int = 256
):
    # Read uploaded image
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes))

    # Preprocess (resize)
    resized_image = image.resize((width, height))

    # Save image to memory
    buffer = io.BytesIO()
    resized_image.save(buffer, format="PNG")
    buffer.seek(0)

    # Return processed image
    return StreamingResponse(
        buffer,
        media_type="image/png"
    )
