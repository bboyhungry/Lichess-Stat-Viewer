import requests # type: ignore

username = 'MagnusCarlsen'
url = f'https://lichess.org/api/user/{username}'

response = requests.get(url)

print("Status code: ", response.status_code)

if response.status_code == 200:
    print(response.json())
    print(response.json()['id'])