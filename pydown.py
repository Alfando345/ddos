import requests

def download_file(url, save_path):
    response = requests.get(url)
    file_name = url.split("/")[-1]  # Mengambil nama file dari URL
    file_path = save_path + "/" + file_name

    with open(file_path, 'wb') as file:
        file.write(response.content)
    print("File berhasil diunduh dan disimpan di:", file_path)

url = input("Masukkan URL file yang ingin diunduh: ")
save_path = "~"

download_file(url, save_path)