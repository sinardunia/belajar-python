import requests


def ambil_post(id):
    url = f"https://jsonplaceholder.typicode/{id}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError:
            print(f"post dengan {id} gada")
            return None
    except requests.exceptions.RequestException:
            print("gagal terhubung ke server euy")
            return None


print(ambil_post(1))