import requests
import json

BASE_URL = "https://jsonplaceholder.typicode.com"

# 1. Get all users
response = requests.get(BASE_URL + "/users")
users = response.json()

print("Users:", len(users))


# 2. Get posts of user 1 using params
response = requests.get(
    BASE_URL + "/posts",
    params={"userId": 1}
)

posts = response.json()

print("Posts by user 1:", len(posts))


# 3. Create a new post
data = {
    "title": "HTTP report",
    "body": "Done",
    "userId": 1
}

response = requests.post(BASE_URL + "/posts", json=data)

new_post = response.json()

print("Created:", response.status_code)
print("New ID:", new_post["id"])


# 4. Check user 99
try:
    response = requests.get(BASE_URL + "/users/99")
    response.raise_for_status()

except requests.exceptions.HTTPError:
    print("User 99 not found")


# 5. Save report in JSON file
report = {
    "users": len(users),
    "posts_by_user_1": len(posts),
    "created_post_id": new_post["id"]
}

with open("report.json", "w") as file:
    json.dump(report, file, indent=4)

print(report)