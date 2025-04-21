from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os
from tiktok_downloader import snaptik  # Thư viện tiktok-downloader
from bs4 import BeautifulSoup

def get_tiktok_video_urls(username, max_videos=25):
    print(f"Bắt đầu lấy URL video từ @{username}...")
    
    # Cấu hình Selenium
    chrome_options = Options()
    # chrome_options.add_argument("--headless=new")  # Bỏ comment để debug
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-features=NetworkService,NetworkServiceInProcess")
    
    # Sử dụng profile Chrome chính
    chrome_profile = os.path.expanduser("~/Library/Application Support/Google/Chrome/Default")
    chrome_options.add_argument(f"--user-data-dir={chrome_profile}")

    # Đường dẫn đến chromedriver
    service = Service('/Users/tunguyen/Desktop/chromedriver')
    print("Khởi tạo ChromeDriver...")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Tăng timeout
    driver.set_page_load_timeout(300)
    driver.set_script_timeout(300)

    try:
        # URL trang TikTok
        url = f"https://www.tiktok.com/@{username}"
        print(f"Truy cập {url}...")
        start_time = time.time()
        driver.get(url)
        
        # Chờ trang tải
        print("Chờ trang tải (tối đa 30 giây)...")
        time.sleep(10)
        print(f"Thời gian tải trang: {time.time() - start_time:.2f} giây")

        # Lưu HTML để debug
        html_path = os.path.join(os.path.expanduser("~/Desktop/tool tiktok"), "tiktok_page.html")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        print(f"Đã lưu nội dung trang vào {html_path}")

        # Kiểm tra nội dung
        page_content = driver.page_source
        if "rapvietvevo" not in page_content.lower():
            print("Cảnh báo: Trang có thể không tải đúng (thiếu nội dung @rapvietvevo).")
        
        # Tìm link trang video
        print("Tìm link trang video từ trang đầu tiên...")
        selectors = [
            'div.css-1uqux2o-DivItemContainerV2 a.css-1mdo0pl-AVideoContainer[href*="/video/"]',
            'a.css-1mdo0pl-AVideoContainer[href*="/video/"]',
            'div.video-feed-item a[href*="/video/"]',
            'div.tiktok-yz6ijl-DivWrapper a[href*="/video/"]',
            'a[href*="/video/"]'
        ]
        page_urls = []
        for selector in selectors:
            video_elements = driver.find_elements(By.CSS_SELECTOR, selector)
            print(f"Tìm thấy {len(video_elements)} phần tử với selector: {selector}")
            for element in video_elements[:max_videos]:
                video_url = element.get_attribute('href')
                if video_url and video_url not in page_urls and f"/@{username}/video/" in video_url:
                    page_urls.append(video_url)
            if page_urls:
                break
        
        print(f"Lấy được {len(page_urls)} link trang video.")

    except Exception as e:
        print(f"Lỗi: {e}")
        page_urls = []
    
    finally:
        driver.quit()

    return page_urls

def download_video(page_url, output_file):
    print(f"Xử lý {page_url}...")
    try:
        downloader = snaptik(page_url)
        downloader.download(output_file)
        print(f"Đã tải video vào {output_file}")
    except Exception as e:
        print(f"Lỗi khi tải video {page_url}: {e}")

def console_interface(page_urls, username):
    print(f"\nDanh sách video từ @{username}:")
    for i, url in enumerate(page_urls, 1):
        print(f"{i}. {url}")
    
    while True:
        try:
            choice = input("\nNhập số thứ tự video để tải (0 để thoát, hoặc nhập nhiều số cách nhau bằng dấu cách): ")
            if choice == "0":
                break
            choices = [int(c) for c in choice.split()]
            for choice in choices:
                if 1 <= choice <= len(page_urls):
                    video_url = page_urls[choice - 1]
                    output_file = f"video_{choice}.mp4"
                    download_video(video_url, output_file)
                else:
                    print(f"Số thứ tự {choice} không hợp lệ, vui lòng thử lại.")
        except ValueError:
            print("Vui lòng nhập số hợp lệ hoặc các số cách nhau bằng dấu cách.")

# Lấy video từ @rapvietvevo
username = "rapvietvevo"
max_videos = 25
page_urls = get_tiktok_video_urls(username, max_videos)

if page_urls:
    console_interface(page_urls, username)
else:
    print("Không tìm thấy video nào.")