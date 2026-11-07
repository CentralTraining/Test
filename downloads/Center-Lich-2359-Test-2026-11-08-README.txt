LỊCH ĐỒNG BỘ CENTER — BẢN TEST 08/11/2026

Đồng bộ tự động lúc 23:59 hằng ngày theo Asia/Saigon, thay lịch 08:00 trước đây.
Phạm vi: Center → 4 tab Google Sheet → Data nhân sự dùng chung: Gán shop PGs, Sao PGs, ON, OFF.
Trạng thái bật lịch và cấu hình link tháng/kết nối giữ nguyên. Không chạy thêm một lượt nhập Data khi đổi giờ.
Giao diện Test: https://centraltraining.github.io/Test/ → Data → Nhân sự → Nội bộ → cuối trang. Tải lại trang và bấm Tải trạng thái để thấy giờ mới.

Các quy tắc dữ liệu, phân quyền, bảo vệ trạng thái HR, đối soát bốn tab, chốt thành công trước khi bật lịch và một lượt tự động mỗi ngày được giữ nguyên. Apps Script v3 không đổi; không cần triển khai lại Code.gs.
Lịch dùng múi giờ máy chủ GMT: 59 16 * * * tương ứng 23:59 Việt Nam. Chốt giờ ở máy chủ cũng đã đổi sang 23:59. Tên job nội bộ cũ được giữ để bảo toàn lịch sử; lịch chạy thực tế là 23:59.
Giao diện mới chỉ ở Test. Kho Data nhân sự dùng chung vẫn theo xác nhận trước đó của Nghĩa.
