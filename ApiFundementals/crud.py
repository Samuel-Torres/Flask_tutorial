"""
CRUD Requests:

Get: requests.get()
post: requests.post()
put/patch: requests.put()
delete: requests.delete()

"""

import requests

# GET

# getRes = requests.get(
#     "https://api.sunrise-sunset.org/json", params={"lat": 41.554260, "lng": -73.043068}
# )
# data = getRes.json()
# print("RESP: ", data)

# getRes = requests.get("https://jsonplaceholder.typicode.com/posts/101")
# data = getRes.status_code
# print("FETCH POST 101 RESP: ", data)

# ____________________________________________

# POST:

# payload = {
#     "userId": 1,
#     "title": "Test post by Samuel Torres.",
#     "body": "Here is my test post",
# }
# postRes = requests.post(
#     "https://jsonplaceholder.typicode.com/posts",
#     json=payload,
#     headers={"Content-type": "application/json; charset=UTF-8"},
#     timeout=10,
# )
# postData = print({"status": postRes.status_code, "response": postRes.json()})


# _____________________________________________

# PUT/PATCH:


getRes = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=10)
data = getRes.json()
# print("FETCH POST 101 RESP: ", data)

postId = data["id"]

# payload = {
#     "userId": data["userId"],
#     "id": data["id"],
#     "title": "New Title",
#     "body": "This is my new post",
# }
patchPayload = {
    # using patch you can just put the fields you're updating in the payload and ignore all others
    "title": "New Title",
    "body": "This is my new post",
}
# print("payload to update: ", payload)
# putRes = requests.put(
putRes = requests.patch(
    f"https://jsonplaceholder.typicode.com/posts/{postId}",
    timeout=10,
    headers={"Content-type": "application/json; charset=UTF-8"},
    json=patchPayload,
    # json=payload,
)
putData = putRes.json()
print("FINAL: ", {"status": putRes.status_code, "response": putData})

# DELETE

# deleteRes = requests.delete("https://jsonplaceholder.typicode.com/posts/1", timeout=10)
# deleteData = deleteRes.json()
# print("DELETION RESPONSE: ", deleteRes)
