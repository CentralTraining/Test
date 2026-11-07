CENTER HR — SỬA Ô GỘP GOOGLE SHEET — BẢN TEST 07/11/2026

Bản Test: https://centraltraining.github.io/Test/
Data → Nhân sự → Nội bộ → Đồng bộ Center lúc 08:00 — Chạy thử.

Lý do lỗi
Tab nhận dữ liệu có ô gộp. Bộ ghi cũ chỉ thay giá trị, không tách ô gộp,
nên có thể làm mất giá trị ở cột nằm trong vùng gộp. Bản mới tách ô gộp
và ghi toàn bộ giá trị của tab DS GÁN SHOP PGS trong cùng một batch,
sau đó đọc lại và đối chiếu từng ô. Các tab khác giữ nguyên.

Cần cập nhật Apps Script một lần bằng tài khoản Google của Nghĩa
1. Trên Test bấm Tải trạng thái. Mở “Cập nhật Apps Script — sửa lỗi dữ liệu
   ô gộp”, bấm “Sao chép mã đã sửa” (hoặc tải file Code.gs đã sửa).
2. Mở dự án Center HR Test đã tạo ở https://script.google.com/.
   Thay toàn bộ nội dung Code.gs bằng mã mới, rồi Lưu.
3. Triển khai / Deploy → Quản lý bản triển khai / Manage deployments →
   chọn bản đang dùng → bút chì → Phiên bản mới / New version → Deploy.
   Giữ nguyên URL /exec, tài khoản thực thi và khóa trong Script properties.
   Không cần tạo dự án, khóa hoặc bản triển khai khác.
4. Quay lại Dashboard Test, tải lại trang, bấm Tải trạng thái → Kiểm tra Sheet.
   Cần thấy “bộ ghi đã có bản sửa ô gộp”. Nếu vẫn báo cần cập nhật,
   kiểm tra đã Deploy New version cho đúng bản /exec đã lưu hay chưa.
5. Bấm Chạy thử và xác nhận: các ô gộp trong đúng tab DS GÁN SHOP PGS
   sẽ được tách, toàn bộ giá trị trong tab được thay bằng Excel mới.
   Chờ kết quả ghi + đọc lại + nhập thử thành công, xem nhân sự nhập thử.
   Chỉ bật lịch 08:00 sau lần thử thành công.

Trạng thái bàn giao
- Dashboard Test và Edge Function đã có phần sửa; mã Apps Script mới được
  cung cấp trên giao diện. Kết nối đang lưu vẫn trỏ bản Apps Script cũ
  cho đến khi chủ tài khoản cập nhật bước 1–3.
- Đã kiểm thử hồi quy bằng dữ liệu giả lập: ô Channel trong vùng gộp,
  ghi cùng một batch, lỗi batch giữ dữ liệu cũ, đối chiếu chính xác,
  khóa HMAC, replay, quyền Admin, phiên Center, bảo toàn trạng thái HR.
- Đã kiểm tra giao diện 1440 / 390 / 320px, tải Code.gs và nội dung chính xác.
- Chẩn đoán nguồn thật chỉ đọc; không ghi lại Sheet, không tạo snapshot
  nhân sự mới, không bật lịch, không sửa Dashboard chính.
- Chưa tuyên bố lần đồng bộ thực tế đã thành công. Cần chủ tài khoản
  triển khai Apps Script mới rồi kiểm thử bước 4–5.

Lưu ý về nhân sự
Dữ liệu thử được lưu riêng. Không tự thay HR, sao, trạng thái Off,
Trainer, Sale, KPI hoặc dữ liệu chính. Lịch 08:00 là giờ khởi chạy tại
Việt Nam, thời gian hoàn tất phụ thuộc Center và Google.

Tệp bàn giao
- HTML đầy đủ theo phiên bản ở downloads.
- Code.gs đã sửa không chứa khóa hoặc tài khoản.
- Full Source ZIP riêng trong workspace chứa toàn bộ Edge Function,
  dependencies, vendor/license, Apps Script, HTML và kiểm thử.
  Không đưa ZIP chứa mã xác thực máy chủ lên repository công khai.
