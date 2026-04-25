import requests
import json

BASE_URL = "https://jsonplaceholder.typicode.com"

# 1. Tạo một bài viết (POST)
def create_post():
    payload = {
        "title": "Tiêu đề mới",
        "body": "Nội dung bài viết mới",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    print("--- 1. Tạo bài viết ---")
    print(response.json())

# 2. Lấy danh sách bài viết (GET)
def get_all_posts():
    response = requests.get(f"{BASE_URL}/posts")
    print("\n--- 2. Danh sách bài viết (10 bài đầu) ---")
    print(response.json()[:10])

# 3. Lấy chi tiết một bài viết (GET)
def get_single_post(post_id):
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    print(f"\n--- 3. Chi tiết bài viết {post_id} ---")
    print(response.json())

# 4. Cập nhật một bài viết (PUT)
def update_post(post_id):
    payload = {
        "id": post_id,
        "title": "Tiêu đề đã cập nhật",
        "body": "Nội dung đã thay đổi",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/posts/{post_id}", json=payload)
    print(f"\n--- 4. Cập nhật bài viết {post_id} ---")
    print(response.json())

# 5. Xóa một bài viết (DELETE)
def delete_post(post_id):
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    print(f"\n--- 5. Xóa bài viết {post_id} ---")
    print(f"Status Code: {response.status_code} (200 nghĩa là thành công)")

if __name__ == "__main__":
    create_post()
    get_all_posts()
    get_single_post(1)
    update_post(1)
    delete_post(1)