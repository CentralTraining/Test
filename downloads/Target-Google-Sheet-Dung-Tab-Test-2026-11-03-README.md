# Sửa import Target Google Sheet — chọn đúng tab — Test 03/11/2026

## Nguyên nhân

Tên tab có dấu cách cuối bị `.trim()` cắt mất. Google Visualization có thể trả tab đầu tiên cùng HTTP 200 khi không tìm thấy tên tab. Vì vậy, `allowFallback:false` ở client không đủ bảo đảm đọc đúng tab.

## Bản sửa

- Thêm action `preview_sheet` trong endpoint Test có xác thực Dashboard, chỉ Admin được dùng. Máy chủ xác minh danh sách tab của đúng Google Sheet, giải tên tab và gid, rồi chỉ đọc CSV bằng gid đã xác minh.
- Giữ nguyên tên tab thật, kể cả dấu cách cuối. Link của tab đúng được giữ trong cấu hình nguồn. Nếu tên không tồn tại hoặc còn mơ hồ, dừng nhập; không đọc tab đầu thay thế.
- Gid trong link giúp phân biệt các tab chỉ khác dấu cách; tên tab được nhập vẫn dùng để chọn tab khi link workbook đang trỏ về tab khác.
- Bước xem trước hiển thị tên tab đã xác minh và danh sách PG đủ điều kiện cùng phân bổ Trainer/Khu vực.
- Những bản import cũ chưa xác minh gid phải tải lại và xem trước, không lưu nhầm dữ liệu từ tab đầu.
- Giữ xác thực, phân quyền, RLS, CAS, kiểm tra mã/tên/nhân sự và quy tắc PG Đang làm hiện có. Không sửa schema, Secrets hoặc endpoint Main.

## Thao tác trên Dashboard Test

1. Mở https://centraltraining.github.io/Test/ và tải lại bằng Ctrl+F5 (Mac: Cmd+Shift+R).
2. Vào Cài đặt → Target → chọn chiến dịch. Nếu đã chốt, bấm Sửa Target.
3. Chọn Theo danh sách → Import Target từ Google Sheet. Dán link tab cần nhập và tên tab.
4. Bấm Lấy dữ liệu & Xem trước. Kiểm tra tên tab đã xác minh, số PG và danh sách bên dưới.
5. Bấm Dùng danh sách này → Lưu Target.

Kiểm tra nguồn do người dùng cung cấp: đọc đúng 25 PG Đang làm, 0 lỗi, 0 dòng trùng. Đây là kiểm tra chỉ đọc; không tự lưu Target hoặc nhập danh sách thật trong quá trình sửa.

Giao diện, HTML đầy đủ và tài liệu xuất bản chỉ ở Test. Full source server và dependencies nằm trong ZIP riêng cho chủ sở hữu; không đăng auth source hoặc dữ liệu PG lên repository công khai.
