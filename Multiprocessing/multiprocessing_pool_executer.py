import concurrent.futures
import requests

def downloadFile(url, name):
    print(f"started downloading{name}")
    responce = requests.get(url)
    open(f"files1/file{name}.jpg","wb").write(responce.content)
    print(f"finished downloading{name}")

if __name__ == "__main__":
    url = "https://picsum.photos/2000/3000"

    with concurrent.futures.ProcessPoolExecutor() as executor:
        l1 = [url for i in range(60)]
        l2 = [i for i in range(60)]
        result = executor.map(downloadFile, l1, l2)
        for r in result:
            print(r)
