import requests

def ambil_post(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    try:
        response = requests.get(url, timeout=5)
    except requests.exceptions.RequestException:
        print("Gagal terhubung ke server.")
        return None
    
    if response.status_code != 200:
        print(f"Post tidak ditemukan (status: {response.status_code})")
        return None
    
    return response.json()

# Tes
print(ambil_post(1))      # harusnya sukses
print(ambil_post(9999))   # harusnya 404