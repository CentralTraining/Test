# Target theo danh sách PGs — Bản Test 03/11/2026

Phạm vi: Cài đặt → Target → chiến dịch Nội bộ Test Online hoặc Tư vấn AI & Check shop.

## Thao tác

1. Mở https://centraltraining.github.io/Test/ bằng tài khoản Admin, chọn đúng tháng.
2. Vào Cài đặt → Target, chọn chiến dịch. Nếu đã chốt, bấm **Sửa Target**.
3. Chọn **Tất cả PGs** hoặc **Theo danh sách**. Target vẫn là số PG OPPO **Đang làm**, không nhân ngưỡng X.
4. Với Theo danh sách, bấm **Import Target từ Google Sheet**, dán link Google Sheet và nhập đúng tên tab.
5. Sheet cần cột **Code / Mã PG / Mã PGs** (hoặc **Mã NV** khi không có Code) và **Họ tên / Họ và tên / Tên PGs**. Nếu có cả Code và Mã NV, ưu tiên Code. Giữ mã dạng văn bản để không mất số 0 đầu.
6. Bấm **Lấy dữ liệu & Xem trước**. Kiểm tra PG khớp, phân bổ Trainer/Khu vực, dòng trùng và PG không Đang làm. Lỗi mã/tên hoặc phân công chưa rõ phải được sửa trước khi tiếp tục.
7. Bấm **Dùng danh sách này**, sau đó **Lưu Target** để áp dụng và chốt. Bấm Hủy hoặc chỉ xem trước chưa thay đổi Target.
8. Khi Sheet thay đổi, bấm Sửa Target và import lại. Link/tên tab được ghi nhớ theo chiến dịch. Đây là cập nhật bằng nút, không tự quét định kỳ.

## Cách tính

- Mã PG đối chiếu chính; tên dùng kiểm tra khớp. Trainer và Khu vực lấy từ nhân sự của tháng, không lấy cột phân công tự ghi trong Sheet.
- Mỗi PG hợp lệ chỉ tính một lần; PG Off hoặc không Đang làm không tính Target.
- Theo danh sách: mẫu số, số hoàn thành và bảng chi tiết cùng giới hạn trong danh sách. Kết quả gốc của PG ngoài danh sách vẫn giữ nguyên.
- Test Online đạt theo X lần; Tư vấn AI đạt theo X lần; Check shop đạt khi Pass. Chế độ của chiến dịch AI & Check shop áp dụng cho cả hai chỉ số trong chiến dịch đó.
- Home và sheet tiến độ trong báo cáo tháng dùng cùng cách tính. Mỗi chiến dịch/tháng có danh sách riêng; tạo chiến dịch mới mặc định Tất cả PGs, không tự sao chép danh sách cũ.
- Chuyển lại Tất cả PGs rồi Lưu Target sẽ tính toàn bộ PG OPPO Đang làm. Danh sách đã nhập trước đó vẫn được giữ để dùng lại.

## Triển khai và giới hạn

Chỉ triển khai giao diện và endpoint mới trên Test. Phạm vi danh sách lưu riêng environment=test; Main và các endpoint đang có giữ nguyên. Không nhập danh sách thật hoặc thay Target thật trong quá trình kiểm thử.

Function mới: campaign-target-roster-test, JWT gateway bật và bắt buộc phiên Dashboard. Admin nhập/lưu; Trainer chỉ đọc phạm vi khu vực. Bảng campaign_target_rosters bật RLS, thu hồi quyền trực tiếp anon/authenticated, chỉ endpoint server có quyền truy cập. Thông báo advisor RLS không có policy là chủ ý của bảng service-only; không có quyền đọc/ghi công khai.

Bản Test không ghi các Target theo danh sách vào snapshot records dùng chung của Main. Khi có yêu cầu chuyển Main sau này, cần triển khai endpoint campaign-target-roster với environment=main, xác định chuyển cấu hình danh sách nào, và kiểm tra bộ tổng hợp báo cáo tự động đọc cùng phạm vi trước khi xuất bản.

Mã nguồn server có xác thực được cung cấp bằng ZIP riêng, không đăng công khai trong repository. File HTML đầy đủ được xuất riêng kèm phiên bản.
