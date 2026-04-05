from bs4 import BeautifulSoup
import requests
import pandas as pd

books_data = []

#1. Lấy 5 trang đầu tiên
#2. Lấy ra các thông tin
for page in range(1, 6):
    url = f"http://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    product_book = soup.find_all("article", class_="product_pod")
    print(f"\n===== Trang {page} =====")

    for i_book in product_book:
        name = i_book.h3.a["title"]
        price = i_book.find("p", class_="price_color").text
        star = i_book.find("p", class_="star-rating")["class"][1]
        instock = i_book.find("p", class_="instock availability").text.strip()

        books_data.append({
            "Tên sách": name,
            "Giá": price,
            "Đánh giá": star,
            "Tình trạng": instock
        })
    df_books = pd.DataFrame(books_data)
    print(df_books)
# 3. Xuất ra Excel
df_books.to_excel("books.xlsx", sheet_name="Danh sách Sách", index=False)
