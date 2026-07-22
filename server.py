from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
def baca_root():
    return{"Halow ini api pertama sayah"}

@app.get("/sapa/{nama}")
def sapa(nama: str):
    return {"pesan": f"Halo, {nama}!"}

# Data dummy di memory (nanti bisa diganti database)
posts = [
    {"id": 1, "judul": "Belajar Python", "isi": "Hari ini belajar HTTP"},
    {"id": 2, "judul": "Belajar API", "isi": "Hari ini belajar FastAPI"},
    {"id": 3, "judul": "Belajar JSON", "isi": "Format universal"},
]




@app.post("/posts")
def buat_post(data: dict):
    id_baru = posts[-1]["id"] + 1 if posts else 1
    data["id"] = id_baru
    posts.append(data)
    return data



@app.get("/posts")
def ambil_semua_post():
    return posts


@app.get("/posts/{post_id}")
def ambil_post(post_id: int):
    for post in posts:
        if post["id"] == post_id:
            return post
    return {"pesan": "Post tidak ditemukan"}