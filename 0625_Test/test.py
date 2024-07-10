from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse # 回傳圖片
import os

app = FastAPI() # FastAPI物件初始化

# 獲取圖片
@app.get("/get-image/{filename}")
def get_image(filename: str):
    if os.path.exists(filename):
        return FileResponse(filename)
    else:
        return {"message": "Image not found"}

# 上傳圖片
@app.post("/upload-image/")
async def upload_image(image: UploadFile = File(...)):
    with open(image.filename, "wb") as file:
        content = await image.read()
        file.write(content)
    return {"filename": image.filename}

# 刪除圖片
@app.delete("/delete-image/{filename}")
def delete_image(filename: str):
    try:
        os.remove(filename)
        return {"message": "Image deleted"}
    except FileNotFoundError:
        return {"message": "Image not found"}

# 更新圖片名稱
@app.put("/update-image-name/{old_filename}/{new_filename}")
def update_image_name(old_filename: str, new_filename: str):
    try:
        os.rename(old_filename, new_filename)
        return {"message": "Image name updated"}
    except FileNotFoundError:
        return {"message": "Image not found"}