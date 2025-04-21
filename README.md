🎬 Tải Video TikTok Hàng Loạt Không Logo
Một công cụ nhỏ sử dụng Python + Selenium + snaptik để:

Quét toàn bộ video từ một tài khoản TikTok.

Chọn video muốn tải.

Tải về không dính logo (no watermark).

🚀 Tính Năng:
Tự động lấy danh sách video mới nhất từ tài khoản TikTok.

Cho phép chọn tải từng video hoặc nhiều video cùng lúc.

Tải về file .mp4 chất lượng cao.

Dễ dùng, không cần mở trình duyệt thủ công.

Hỗ trợ Windows / MacOS / Linux.

⚙️ Yêu Cầu:
Python >= 3.8

Chrome đã cài sẵn.

chromedriver tương thích với bản Chrome.

💻 Cài Đặt:
Clone repo:

bash
Copy
Edit
git clone https://github.com/your_username/tai-tiktok-khong-logo.git
cd tai-tiktok-khong-logo
Cài thư viện Python:

bash
Copy
Edit
pip install selenium beautifulsoup4 tiktok-downloader
Kiểm tra chromedriver đã setup đúng đường dẫn trong file:

python
Copy
Edit
service = Service('/Users/tunguyen/Desktop/chromedriver')
⚠️ Thay đường dẫn này thành nơi bạn lưu chromedriver.

🐍 Cách Sử Dụng:
Mở terminal và chạy file Python:

bash
Copy
Edit
python your_script_name.py
Tool sẽ tự động:

Vào profile TikTok.

Quét danh sách link video.

Hiển thị danh sách link.

Nhập số thứ tự video cần tải:

css
Copy
Edit
Nhập số thứ tự video để tải (0 để thoát, hoặc nhập nhiều số cách nhau bằng dấu cách):
Ví dụ:
1 3 5 → tải video số 1, 3 và 5.

💡 Ghi chú:
Tool sử dụng snaptik API qua tiktok-downloader để tải về không logo.

Nếu bị lỗi không lấy được link, bạn nên kiểm tra lại user-agent hoặc đăng nhập TikTok bằng Chrome trước.

📄 Bản quyền:
Công cụ này phục vụ mục đích học tập, nghiên cứu, không khuyến khích reup nội dung vi phạm bản quyền TikTok