import re
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10) # Dùng wait để web không bị "out" do load chậm

def loginForm():
    Url = 'https://www.automationexercise.com/login'
    driver.get(Url)
    # Đợi element xuất hiện để tránh lỗi NoSuchElementException lúc đầu
    element_username = wait.until(EC.presence_of_element_located((By.NAME, 'email')))
    element_username.send_keys("vominhhien1732005@gmail.com")

    element_password = driver.find_element(By.NAME, 'password')
    element_password.send_keys("SalamanderH")

    element_btn = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    element_btn.click()
    time.sleep(1) 

def intoProduct():
    Url = 'https://www.automationexercise.com/products'
    driver.get(Url)
    time.sleep(1) 

def timKiem_Shirt():
    element_search = wait.until(EC.visibility_of_element_located((By.NAME, "search")))
    element_search.send_keys('shirt')
    element_btn = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-default.btn-lg")
    element_btn.click()
    time.sleep(1) 

def locSanPhamTrangDau():
    container = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.features_items")))
    products = container.find_elements(By.CLASS_NAME, "productinfo")
    danh_sach = []
    for product in products:
        name = product.find_element(By.TAG_NAME, 'p').text
        price_text = product.find_element(By.TAG_NAME, 'h2').text
        price = int(re.sub(r"\D", "", price_text))
        danh_sach.append((name, price, product))
    return danh_sach

def sanPhamGiaMIN(danh_sach):
    if not danh_sach: return None
    low_product = min(danh_sach, key=lambda x: x[1])
    return low_product  

# def clearCart():
#     driver.get('https://www.automationexercise.com/view_cart')
#     delete_buttons = driver.find_elements(By.CSS_SELECTOR, "a.cart_quantity_delete")
#     for btn in delete_buttons:
#         try:
#             btn.click()
#             time.sleep(0.5)
#         except: pass


def addToCart(product_tuple):
    print(f"Đang thêm sản phẩm: {product_tuple[0]}")
    add_btn = product_tuple[2].find_element(By.CSS_SELECTOR, 'a.add-to-cart')
    
    driver.execute_script("arguments[0].click();", add_btn)
    continue_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-success.close-modal")))
    continue_btn.click()
    time.sleep(1)

def intoView_Cart():
    driver.get('https://www.automationexercise.com/view_cart')
    element_quantity = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'td.cart_quantity button')))
    quantity_text = element_quantity.text.strip()
    quantity = int(quantity_text)
    
    print(f"Số lượng hiện tại trong giỏ: {quantity}")
    assert quantity >= 1, f"Lỗi: Giỏ hàng trống!"

def checkout():
    driver.find_element(By.CSS_SELECTOR, "a.btn.btn-default.check_out").click()

def reviewOrder():
    comment_area = wait.until(EC.presence_of_element_located((By.NAME, "message")))
    comment_area.send_keys("Bot mua hàng tự động.")

def placeOrder():
    btn_place = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/payment']")))
    driver.execute_script("arguments[0].click();", btn_place)

def fillInformation():
    wait.until(EC.presence_of_element_located((By.NAME, "name_on_card"))).send_keys("Minh Hien")
    driver.find_element(By.NAME, "card_number").send_keys("4242424242424242")
    driver.find_element(By.NAME, "cvc").send_keys("311")
    driver.find_element(By.NAME, "expiry_month").send_keys("12")
    driver.find_element(By.NAME, "expiry_year").send_keys("2026")

def confirm():
    btn_submit = wait.until(EC.presence_of_element_located((By.ID, "submit")))
    driver.execute_script("arguments[0].click();", btn_submit)
    print("--- Đặt hàng thành công! ---")

def send_email_notification():
    print("--- Đang gửi email xác nhận ---")
    sender_email = "vominhhien1732005@gmail.com"
    receiver_email = "hienvo17032005@gmail.com"
    password = "rcls zipx exyv qzgk"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "XÁC NHẬN ĐẶT HÀNG THÀNH CÔNG"
    msg.attach(MIMEText("Chào Hiển, đơn hàng đã được bot đặt thành công.", 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)
        server.quit()
        print("Email gửi thành công!")
    except Exception as e:
        print(f"Lỗi gửi email: {e}")

#THỰC THI FLOW
try:
    loginForm()
    # clearCart()
    intoProduct()
    timKiem_Shirt()
    ds = locSanPhamTrangDau()
    MIN_SP = sanPhamGiaMIN(ds)
    
    if MIN_SP:
        addToCart(MIN_SP)
        intoView_Cart()
        checkout()
        reviewOrder()
        placeOrder()
        fillInformation()
        confirm()
        send_email_notification()
    else:
        print("Không tìm thấy sản phẩm.")

finally:
    time.sleep(5)
    driver.quit()