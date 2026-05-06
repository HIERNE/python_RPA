import pandas as pd
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


SENDER_EMAIL = "vominhhien1732005@gmail.com"
APP_PASSWORD = "rcls zipx exyv qzgk"
RECEIVER_EMAIL = "hienvo17305@gmail.com"

def gui_email_canh_bao(bien_so, thoi_gian, dia_diem, loi):
    """Hàm gửi email thông báo khi có vi phạm phạt nguội"""
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg['Subject'] = f"Cảnh báo phạt nguội - Biển số: {bien_so}"
    
    body = f"""Cảnh báo phạt nguội!
    - Biển số: {bien_so}
    - Trạng thái: Có vi phạm

    Chi tiết:
    - Thời gian: {thoi_gian}
    - Địa điểm: {dia_diem}
    - Lỗi vi phạm: {loi}
    """
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)
        server.quit()
        print(f"      [+] Đã gửi email cảnh báo thành công cho xe {bien_so}.")
    except Exception as e:
        print(f"      [-] Lỗi gửi email: {e}")

# 1. Đọc danh sách biển số
try:
    df = pd.read_excel('danh_sach_xe.xlsx')
    danh_sach_xe = df['BienSo'].dropna().tolist()
except FileNotFoundError:
    print("Không tìm thấy file Excel, sử dụng danh sách mẫu...")
    danh_sach_xe = ["51F-777.77", "43D1-47792", "43A-99999"]

print(f"Bắt đầu kiểm tra {len(danh_sach_xe)} biển số...\n")

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

for bien_so in danh_sach_xe:
    print(f"\n[*] Đang kiểm tra: {bien_so}")
    
    try:
        driver.get("https://www.phatnguoixe.com/")
        time.sleep(2) 
        XPATH_O_NHAP = "/html/body/div[1]/div/div[1]/div/div/div/div/form/div[1]/input"
        XPATH_NUT_BAM = "/html/body/div[1]/div/div[1]/div/div/div/div/form/div[2]/input"
        
        input_bien_so = wait.until(EC.presence_of_element_located((By.XPATH, XPATH_O_NHAP)))
        input_bien_so.clear()
        input_bien_so.send_keys(bien_so)

        btn_kiem_tra = wait.until(EC.element_to_be_clickable((By.XPATH, XPATH_NUT_BAM)))
        btn_kiem_tra.click()

        time.sleep(5) 
        page_source = driver.page_source
        
        if "Không tìm thấy" in page_source or "Không có lỗi" in page_source or "chưa ghi nhận" in page_source:
            print("   -> Kết quả: Không vi phạm")
        else:
            print("   -> Kết quả: CÓ VI PHẠM! Đang trích xuất dữ liệu và gửi Email...")
            try:
                tables = driver.find_elements(By.TAG_NAME, "table")
                if len(tables) > 0:
                    td_elements = tables[0].find_elements(By.TAG_NAME, "td")
                    
                    thoi_gian = td_elements[0].text if len(td_elements) > 0 else "Chưa rõ"
                    dia_diem = td_elements[1].text if len(td_elements) > 1 else "Chưa rõ"
                    loi_vi_pham = td_elements[2].text if len(td_elements) > 2 else "Chưa rõ"
                else:
                    thoi_gian = dia_diem = loi_vi_pham = "Đang cập nhật (Không lấy được từ bảng)"

                gui_email_canh_bao(bien_so, thoi_gian, dia_diem, loi_vi_pham)
                
            except Exception as ex:
                print(f"   -> Lỗi khi lấy dữ liệu bảng: {ex}")
                
    except Exception as e:
        print(f"   -> LỖI: Không tìm thấy phần tử web.")
        print(f"   -> Chi tiết: {e}")

print("\nHoàn tất quy trình kiểm tra!")
driver.quit()