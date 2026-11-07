CENTER — ĐỒNG BỘ 4 TAB NHÂN SỰ — BẢN TEST 07/11/2026

https://centraltraining.github.io/Test/
Data → Nhân sự → Nội bộ → Đồng bộ Center lúc 08:00 — Chạy thử.
Dùng file Google Sheet tháng đã lưu. Mỗi lần thay mới toàn bộ dữ liệu,
xóa giá trị cũ dư, không cộng dồn. Các tab ngoài danh sách giữ nguyên.

1. DS GÁN SHOP PGS: Center /trainer → Export gán shop hiện tại.
2. SAO PGS: /staff/staff-scores-new → Hạng sao hiện tại (export=2).
   Giữ bộ lọc mặc định Còn làm việc của trang này.
3. ON: danh sách /staff/index, Working status: Choose,
   Joined at from/to từ ngày đầu tới ngày cuối tháng đang cập nhật.
4. OFF: cùng danh sách, Working status: Choose,
   Off date from/to từ ngày đầu tới ngày cuối tháng đang cập nhật.
ON bỏ trống bộ lọc Off date; OFF bỏ trống bộ lọc Joined at.
Ngày cuối tháng được tính tự động, gồm tháng 2 và năm nhuận.

Hệ thống kiểm tra đủ 4 file và ngày ON/OFF trước khi ghi. Sau đó tách
ô gộp và thay giá trị cả 4 tab trong cùng batch, đọc lại từng ô.
Tab SAO PGS, ON hoặc OFF còn thiếu sẽ được tạo khi Chạy thử;
DS GÁN SHOP PGS cần có sẵn để xác định đúng file Test.
Nếu ON/OFF không có phát sinh, file Excel đúng tiêu đề và không có
bản ghi vẫn hợp lệ, sẽ xóa giá trị cũ của tab tương ứng.
File lỗi, sai mẫu hoặc sai tháng dừng trước khi ghi Sheet.
Luồng nhân sự nhập thử gán shop giữ quy tắc hiện tại, không tự thay
trạng thái HR, sao, Sale, Trainer hay KPI từ ba tab nguồn mới.

CẬP NHẬT APPS SCRIPT MỘT LẦN
Bản cũ chỉ có một tab; cần dùng Code.gs bản 4 tab (writerVersion 3).
1. Tải lại Dashboard Test → Tải trạng thái → mở “Cập nhật Apps Script —
   4 tab nhân sự” → Sao chép mã 4 tab (hoặc Tải Code.gs 4 tab).
2. Mở dự án Center HR Test đang dùng trong https://script.google.com/.
   Thay toàn bộ Code.gs bằng mã mới rồi Lưu.
3. Deploy → Manage deployments → chọn bản đang dùng → bút chì →
   New version → Deploy. Giữ nguyên URL /exec và khóa hiện tại.
   Không cần tạo dự án hoặc khóa khác. Dịch vụ Google Sheets API v4
   và tài khoản thực thi vẫn dùng cấu hình đã thiết lập.
4. Quay lại Test → Kiểm tra Center → Kiểm tra Sheet.
   Kiểm tra Center chỉ tải/đối chiếu 4 file; chưa ghi dữ liệu.
   Kiểm tra Sheet cần xác nhận “bộ ghi 4 tab”.
5. Chạy thử — cập nhật 4 tab → xem dữ liệu ở 4 tab và nhân sự nhập thử.
   Khi thành công, bấm Bật lịch chạy thử 08:00 cho tháng đang chọn.
   Lịch cũ chỉ xác nhận một tab không đủ điều kiện bật bản 4 tab.

KẾT QUẢ KIỂM TRA
- Đã tải/kiểm tra đủ 4 nguồn Center thật, chỉ đọc, ON/OFF đúng tháng.
- Kiểm thử giả lập ghi cùng batch, ô gộp, xóa dư cả 4 tab, tự tạo tab,
  ON/OFF rỗng hợp lệ, lỗi nguồn/ngày/batch/readback, quyền và HMAC đạt.
- Giao diện 1440/390/320px và tải Code.gs chính xác đã kiểm tra.
- Mã Dashboard Test và Edge Function đã cập nhật. Chủ tài khoản Google
  còn cần triển khai Code.gs mới; chưa xác nhận lượt ghi thật đủ 4 tab.
- Chưa bật lịch 08:00, chưa chuyển Dashboard chính. Kết quả nhân sự
  thử cũ được giữ nguyên đến khi lần chạy bản 4 tab thành công.

Tệp HTML theo phiên bản và Code.gs ở downloads.
Full Source ZIP riêng trong workspace có đủ Edge Function/dependencies,
Apps Script, HTML, kiểm thử và vendor/license. Không kèm Cookie/khóa
hay dữ liệu nhân sự thật; không công bố ZIP xác thực máy chủ lên GitHub.
