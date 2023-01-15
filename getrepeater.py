import requests

url = input("Enter the URL: ")
headers = {
    'Authorization': input("Enter the Authorization key: "),
    'User-Agent': input("Enter the User-Agent: "),
    'Content-Type': input("Enter the Content-Type: "),
    'Another-Header': input("Enter another header if necessary: ")
}

try:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open("directoryweb.txt", "w") as file:
            file.write(response.text)
            print("The file directoryweb.txt was created")
    else:
        print("The request was not successful, the status code is:", response.status_code)
except requests.exceptions.RequestException as e:
    print("Error connecting to the URL:", e)
