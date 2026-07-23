posts = [
    {"id": 1, "judul": "A", "isi": "a"},
    {"id": 2, "judul": "B", "isi": "b"},
]


def hapus_post(post_id):
    for index, post in enumerate(posts):
        if post["id"] == post_id:
            posts.pop(index)
            return {"pesan: post diapus"}
    return {"pesan: post tida ditemukanh"}