from fastapi import FastAPI
from pydantic import BaseModel
import json
import os

app = FastAPI(title="V60 MagnaRise AI")

class TrangThaiHoSo(BaseModel):
    rm_name: str
    ma_hs_v60: str      
    trang_thai: str     
    thoi_gian: str

DATA_FILE = "v60_database.json"

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

@app.post("/api/v1/cap-nhat-ho-so")
def nhan_du_lieu(hoso: TrangThaiHoSo):
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    data.append(hoso.dict())
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)
    return {"message": "Thành công!", "data": hoso}

@app.get("/api/v1/lay-du-lieu")
def lay_du_lieu():
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    return {"tong_so": len(data), "danh_sach": data}