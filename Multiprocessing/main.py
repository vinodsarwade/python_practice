import multiprocessing
import requests

def downloadFile(url, name):
    print(f"started downloading{name}")
    responce = requests.get(url)
    open(f"files1/file{name}.jpg","wb").write(responce.content)
    print(f"finished downloading{name}")


if __name__ == "__main__":
    url = "https://picsum.photos/2000/3000"
    pros = []
    for i in range(5):
        p = multiprocessing.Process(target=downloadFile,args=[url,i])
        p.start()
        pros.append(p)

    for p in pros:
        p.join()

