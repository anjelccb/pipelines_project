import requests

if __name__ == "__main__":
    url = "https://www.google.com.es"
    response = request.get(url)

    if repsonse.status_code == 200:
        print (response.content)
