from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from Summary import return_summary
from Topics import return_topic
import os
from dotenv import load_dotenv
import time

load_dotenv()
app = FastAPI()

ALLOWED_HOST = os.environ.get("CLIENT_HOST").strip()
ALLOWED_PORT = os.environ.get("CLIENT_PORT").strip()
ALLOWED = "*"

if ALLOWED_HOST != "" and ALLOWED_PORT != "":
    ALLOWED = f"{ALLOWED_HOST}:{ALLOWED_PORT}"

app.add_middleware(

    CORSMiddleware,
    allow_origins=ALLOWED,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)


# Tạo một lớp Pydantic để đại diện cho dữ liệu đầu vào
class DataItem(BaseModel):
    text: str
    lang: str


@app.post("/summarize/")
async def summarize_text(data_item: DataItem):
    epoch = int(round(time.time() * 1000))
    summary = return_summary(data_item.text)
    end = int(round(time.time() * 1000))
    # Trả về kết quả phân tích
    return {
        "summarized": summary,  # Gọi hàm để lấy tóm tắt
        "process_time": end - epoch
    }


@app.post("/extract/")
async def extract_topics(data_item: DataItem):
    epoch = int(round(time.time() * 1000))
    topic = return_topic(data_item.text)
    end = int(round(time.time() * 1000))
    # Trả về kết quả phân tích
    return {
        "keywords": topic,  # Gọi hàm để lấy chủ đề
        "process_time": end - epoch
    }


@app.get("/")
async def redirect_to_swagger():
    return RedirectResponse("/docs#/default/analyze_data_analyze__post")


PORT = 8001

# Mở thực thi ứng dụng FastAPI
if __name__ == "__main__":
    import uvicorn

    print(f"Allowing inbound connection from: {ALLOWED}")
    uvicorn.run(app, host="0.0.0.0", port=PORT)
