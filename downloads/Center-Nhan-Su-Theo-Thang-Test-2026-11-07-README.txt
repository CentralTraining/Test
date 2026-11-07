ĐỒNG BỘ NHÂN SỰ CENTER — BẢN TEST — 07/11/2026

Mở https://centraltraining.github.io/Test/ bằng tài khoản Admin.
Chọn tháng hiện tại ở đầu trang → DATA → Nhân sự → Nội bộ → kéo xuống cuối, khung Đồng bộ Center lúc 08:00 — Chạy thử.

1. LINK THÁNG
Tạo một bản sao Google Sheet riêng cho Test. Giữ tab DS GÁN SHOP PGS.
Bấm Tải trạng thái (xác thực Admin nếu được hỏi), nhập link → Lưu link tháng này.
Sau khi lưu ô sẽ khóa; Sửa link để đổi; Hủy sửa giữ link cũ. Mỗi tháng lưu riêng, không tự lấy link của tháng trước.
Đổi link sẽ tắt lịch tháng đó; chạy thử lại thành công trước khi bật lịch.
Test chặn ghi nếu mã file trùng nguồn DS gán Shop đang dùng chung với Dashboard chính.

2. LƯU KẾT NỐI MỘT LẦN TRONG VAULT
Mở https://supabase.com/dashboard/project/qruxqlsbhyhwiqjdkyyc/integrations/vault/secrets
Đây là giao diện quản trị Supabase của chủ dự án; mật khẩu/key không gửi qua chat.
Tạo mục tên center_hr_test_erp_credentials.
Giá trị JSON theo mẫu: {"username":"TÀI KHOẢN CENTER","password":"MẬT KHẨU CENTER"}.
Tên người dùng là tài khoản đăng nhập Center, không phải tài khoản Dashboard.
JSON phải đúng cú pháp (ký tự dấu nháy hoặc gạch chéo trong mật khẩu cần escape đúng JSON).

Tạo mục tên center_hr_test_google_service_account.
Giá trị là toàn bộ JSON key tải từ tài khoản dịch vụ Google.
Nếu chưa có: Google Cloud Console → chọn/tạo dự án → APIs & Services → bật Google Sheets API → IAM & Admin → Service Accounts → tạo tài khoản dịch vụ → Keys → Add key → Create new key → JSON.
Tài khoản dịch vụ không cần thêm quyền quản trị dự án để chỉ sửa file được chia sẻ.
Chia sẻ quyền Chỉnh sửa bản sao Google Sheet cho địa chỉ client_email có trong JSON.
Hướng dẫn chính thức: https://developers.google.com/identity/protocols/oauth2/service-account

3. KIỂM TRA VÀ CHẠY THỬ
Trở về Dashboard Test → Tải trạng thái. Khung chỉ hiện trạng thái đã lưu và email tài khoản dịch vụ; không trả mật khẩu/private key.
Bấm Kiểm tra Center: đăng nhập bằng form chính thức, đi tới danh sách PGs PB Sales và tìm Export gán shop hiện tại. Nếu menu thay đổi hoặc Center yêu cầu MFA/CAPTCHA, hệ thống báo cần kiểm tra, không vượt xác minh.
Bấm Kiểm tra Sheet: đọc đúng file và tab (lượt này chưa ghi).
Bấm Chạy thử — ghi Sheet & nhập thử; xác nhận rõ việc thay toàn bộ giá trị trong tab DS GÁN SHOP PGS của file Test.
Hệ thống kiểm tra Excel đúng mẫu trước khi ghi, ghi bằng một batch của Google, đọc lại đối chiếu toàn bộ giá trị, rồi lưu bản nhân sự nhập thử riêng.
Mã nhân viên lấy cột Code, không lấy Staff ID. Ưu tiên shop chính; giữ trạng thái, sao, Size shop của PG có sẵn. Không tự gán Off cho PG vắng khỏi file.
Nhân sự thử chỉ thuộc các khu vực Miền Trung; nội dung Excel đầy đủ được giữ trong tab đích của file Test.
Bấm Xem nhân sự nhập thử để kiểm tra. Không cập nhật các bảng pgs/config/Sale/KPI hiện có của Dashboard chính hoặc Test cũ.

4. LỊCH CHẠY THỬ 08:00
Chỉ sau một lượt chạy thử thực tế thành công mới bấm Bật lịch chạy thử 08:00.
Lịch Supabase Cron là 01:00 GMT = 08:00 Asia/Saigon; chạy phía máy chủ, không cần mở Dashboard hoặc giữ máy tính bật.
Lịch đọc link của tháng hiện tại. Sang tháng chưa có link hoặc chưa bật lịch tháng mới thì bỏ qua.
Mỗi ngày một lượt cron, khóa chạy đồng thời; lỗi/không xác nhận không tự lặp gửi lại cùng ngày. Có thể Tải trạng thái để xem giai đoạn và kết quả.
Thời gian hoàn tất tùy Center và Google; 08:00 là thời điểm khởi chạy.

TRẠNG THÁI KHI PHÁT HÀNH
Đã kiểm thử với dữ liệu giả lập: mô hình nhập, đăng nhập, Google JWT, batch/readback, lỗi, phân quyền và giao diện 1440/390/320px. Đã kiểm thử SQL bằng giao dịch rollback, đối chiếu source function và kiểm tra phiên thiếu/giả bị từ chối.
CHƯA có link tháng, tài khoản Center hoặc key Google thật; CHƯA lấy Excel thật hoặc ghi Sheet thật; CHƯA bật lịch tháng nào. Cần nhập kết nối trong Vault rồi xác minh lần chạy thực tế.
Chỉ triển khai Test. Chưa chuyển lên Dashboard chính; chờ Nghĩa kiểm tra và yêu cầu rõ.
HTML đầy đủ giữ cấu hình Test hiện có, không phải bản độc lập dữ liệu riêng.
