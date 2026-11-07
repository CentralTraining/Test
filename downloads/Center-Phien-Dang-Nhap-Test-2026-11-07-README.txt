BẢN TEST — CENTER CÓ CAPTCHA / PHIÊN ĐÃ ĐĂNG NHẬP — 07/11/2026

Đã kiểm tra form công khai của Center: có bước reCAPTCHA. Kết nối chỉ gửi tài khoản/mật khẩu chưa hoàn tất được bước xác minh này.
Bản mới dừng trước khi gửi mật khẩu nếu form có CAPTCHA; thông báo rõ cần xác minh trực tiếp.
Có thêm cách dùng phiên Center mà chính Nghĩa đã đăng nhập và xác minh.

THAO TÁC TRÊN MÁY TÍNH
1. Mở https://center.erp-portal.vn/ và đăng nhập bình thường. Hoàn tất CAPTCHA / bước xác minh của Center.
2. Trong cửa sổ Center đã đăng nhập, nhấn F12 (Mac: Command+Option+I) → Network.
3. Vào Đào Tạo → Danh sách PGs PB Sales hoặc tải lại trang đó. Chọn một yêu cầu tới đúng center.erp-portal.vn trong danh sách Network.
4. Mở Headers → Request Headers → Cookie. Sao chép riêng giá trị Cookie (một dòng). Không lấy Set-Cookie trong Response Headers và không lấy toàn bộ lệnh cURL.
5. Mở https://centraltraining.github.io/Test/ bằng Admin → chọn tháng hiện tại → DATA → Nhân sự → Nội bộ → cuối trang, khung Đồng bộ Center lúc 08:00.
6. Tải trạng thái → Thiết lập miễn phí bằng Gmail → Sửa kết nối Center.
7. Cách kết nối Center: chọn “Phiên Center đã đăng nhập — có CAPTCHA”. Dán Cookie vào ô bảo mật → Lưu kết nối Center.
8. Bấm Kiểm tra Center. Chỉ khi lấy được Excel đúng mẫu mới báo thành công; chưa ghi Sheet trong bước này.
9. Kiểm tra Sheet → Chạy thử — ghi Sheet & nhập thử → kiểm tra danh sách thử → Bật lịch 08:00 sau khi chạy thành công.

Cookie là thông tin đăng nhập nhạy cảm. Chỉ dán vào ô bảo mật của Test, không gửi vào chat, GitHub, Google Sheet hoặc log.
Máy chủ lưu phiên trong Vault mã hóa. Tải cấu hình chỉ trả trạng thái và cách kết nối, không trả Cookie. Ô được xóa sau khi lưu; không lưu trong localStorage/sessionStorage.
Khi Sửa kết nối Center, để trống Cookie sẽ giữ phiên đã lưu nếu vẫn chọn cùng phương thức.
Đổi phương thức và Lưu thành công sẽ thay bộ thông tin Center đang dùng; không tự đổi trước khi lưu.

GIỚI HẠN VẬN HÀNH
Lịch 08:00 dùng phiên Center đang lưu. Khi Center hết hạn hoặc thu hồi phiên, cần đăng nhập trực tiếp và cập nhật lại Cookie. Không tự giải CAPTCHA hoặc tự đăng nhập lại thay người dùng.
Nếu cần vận hành lâu dài không phải gia hạn phiên, cần phương thức tích hợp/API được đơn vị quản trị Center cung cấp.
Google Apps Script / URL / khóa và link Google Sheet đã lưu giữ nguyên.
Chỉ Test. Chưa chuyển lên Dashboard chính. Chưa bật lịch hoặc ghi Google Sheet thật.

KIỂM THỬ
Đã đối chiếu form đăng nhập công khai thật và nhận diện CAPTCHA, không gửi tài khoản/mật khẩu.
Đã kiểm thử bằng dữ liệu giả: dùng phiên hợp lệ, xoay Cookie trong lượt chạy, tìm trang danh sách/Export, hết hạn, chặn chuyển Cookie sang tên miền khác, chặn chèn header, không lộ Cookie trong phản hồi và không làm mất phiên Dashboard khi Center lỗi.
Luồng XLSX → Apps Script → readback → snapshot thử riêng vẫn qua kiểm thử; mã nhân viên, trạng thái/sao/size và phạm vi khu vực được giữ theo quy tắc cũ.
SQL fixture dùng hàm tạm sao từ source đang triển khai, bảng tạm và tên Vault ngẫu nhiên; service_role lưu/sửa/đọc lại phiên được mã hóa, chặn phiên bản cũ/newline, tương thích tài khoản mật khẩu và giữ chốt safeupdate. Mọi dữ liệu giả rollback, không chạm kết nối thật của Nghĩa.
Giao diện 1440/390/320px đã kiểm tra Lưu/Sửa/Hủy, chuyển phương thức, ẩn/hiện ô đúng và không tràn ngang.
Chưa có phiên Center thật để xác minh export đã đăng nhập. Chưa xác nhận lần đồng bộ dữ liệu thật.
