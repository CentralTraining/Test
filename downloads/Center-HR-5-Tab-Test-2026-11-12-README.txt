SAO PGS — LỌC NHIỀU MỨC SAO / THÊM TAB LÊN SAO
Bản Test và bản xem trước, 12/11/2026

Giao diện xem trước:
https://centraltraining.github.io/Test/previews/2026-11-12-sao-pgs/

Lọc danh sách:
- Tích nhiều mức trong Từ sao và Lên sao, ví dụ từ 0,1,2 lên 2,3,4.
- Trong một nhóm: khớp một trong các mức đã tích. Giữa hai nhóm: phải khớp cả hai.
- Không tích mức nào = mọi mức. Bỏ lọc danh sách sẽ bỏ cả tìm kiếm và lựa chọn sao.
- Số PGs, số lượt và CSV xuất theo đúng bộ lọc. PGs vẫn phải Đang làm ở tháng đang xem.

LÊN SAO sử dụng chính Google Sheet DATA tháng đã lưu tại Data nhân sự.
Nguồn Center: /staff/staff-scores-new, nút Xuất Excel (export=1).
SAO PGS vẫn là Hạng sao hiện tại (export=2), không thay quy tắc cũ.
LÊN SAO giữ đủ lộ trình có trong file xuất, không lọc bỏ lịch sử trước tháng hiện tại.
File phải có Mã NV, Hạng sao hiện tại, Ngày lên sao, Sao. Dòng PG chưa có mốc được giữ.
File lỗi, thiếu mẫu hoặc không có nhân sự không được xóa dữ liệu LÊN SAO cũ.

BƯỚC CẦN CHỦ GOOGLE THỰC HIỆN MỘT LẦN
1. Mở Google Sheet DATA tháng → Tiện ích mở rộng → Apps Script.
2. Thay toàn bộ Code.gs bằng tệp Center-HR-5-Tab-Test-2026-11-12-Code.gs.txt.
   Giữ nguyên khóa kết nối đang có trong Thuộc tính tập lệnh, URL /exec và dịch vụ Sheets.
3. Triển khai → Quản lý các bản triển khai → biểu tượng bút chì → Phiên bản mới → Triển khai.
   Chỉnh bản triển khai hiện có để giữ nguyên URL, không tạo kết nối hay khóa mới.
4. Quay lại Data nhân sự trên Dashboard, bấm Kiểm tra Sheet.
   Đúng khi thông báo đã kết nối bộ ghi 5 tab và có LÊN SAO.
   Nếu tab chưa có, lần ghi tiếp theo sẽ tạo đúng tab LÊN SAO trong cùng batch.

Máy chủ đã hỗ trợ tương thích hai chiều:
- Apps Script hiện tại v3: 4 tab và lịch đang bật tiếp tục chạy; LÊN SAO đang chờ bước trên.
- Sau cập nhật v4: các lượt chạy sẽ lấy đủ 5 file, kiểm tra trước ghi,
  ghi/đọc lại 5 tab trong cùng một batch rồi nhập Data nhân sự theo quy tắc cũ.
- Lịch vẫn 23:59 Asia/Saigon, ON/OFF tự lấy đầu-cuối tháng đang cập nhật.
- Dữ liệu mỗi tab được thay bằng bản mới nhất, xóa giá trị cũ dư, giữ các tab khác.
- Giữ mã hóa kết nối, kiểm tra quyền Admin, kiểm tra nguồn/tháng/phiên bản và mã tiếp nhận.
- Không thay quy tắc trạng thái đã được duyệt, ghép gán shop/sao, Trainer, size và On/Off.
- Chưa có lần ghi 5 tab thực tế được xác nhận vì Apps Script đang công bố vẫn là v3.

Giao diện xem trước dùng tên, mã và số liệu giả lập. Chưa gắn SAO PGS vào tab thật
của Dashboard, chưa đưa giao diện SAO PGS lên bản chính. Máy chủ Center dùng chung
đã được nâng cấp tương thích, không reset nguồn hoặc tắt lịch đang bật.

Mã Edge Function và phụ thuộc được cung cấp trong ZIP riêng của workspace,
không đưa mã xác thực máy chủ hay dữ liệu nhân sự thật lên GitHub công khai.
