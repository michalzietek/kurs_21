import requests

get_url = "https://reqres.in/api/users"
post_url = "https://reqres.in/api/users"
put_url = "https://reqres.in/api/users/264"

users = requests.get(url=get_url)
print(users.content)

post_method = requests.post(url=post_url, data={
    "user": "Michal",
    "job": "programmer"
})
print(post_method.text)
put_method = requests.put(url=put_url, data={
    "user": "Michal",
    "job": "firefighter"
})
print(put_method.text)