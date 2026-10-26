# Xây kênh TikTok — bản Test, 26/10/2026

Phiên bản chỉ dùng **TikTok API**, hỗ trợ **Sandbox 1 + Sandbox 2** trong cùng bảng
tiến độ. Không triển khai thay đổi này lên Dashboard chính.

## Thay đổi

- Bỏ nút quét thủ công, chọn file, chọn nguồn Web tracking và mã gọi dịch vụ tracking.
- Máy chủ ngừng nhận thao tác `manual_scan`; chỉ đọc số liệu TikTok API cho báo cáo.
- Dùng một nút Đồng bộ TikTok để cập nhật các kênh đã kết nối từ cả hai Sandbox.
- Admin chọn Sandbox cho từng Trainer tại Quản lý kênh → Gán trang TikTok.
- Kênh chưa có trường Sandbox tiếp tục dùng bộ khóa cũ ở Sandbox 1. Không đổi khóa,
  xóa kết nối hoặc chuyển kênh đang dùng chỉ vì triển khai phiên bản mới.
- Giữ mốc Admin ngày 01/10/2026 và dữ liệu đã lưu. Dữ liệu quét cũ không được đưa
  vào bảng TikTok API và không bị tự xóa khỏi bản lưu mã hóa hiện có.
- Giữ nguyên callback chung đã đăng ký và chuyển tiếp cho Dashboard chính.

## Thiết lập Sandbox 2

1. TikTok Developers → ứng dụng → Sandbox → chọn Sandbox 2.
2. Bật Login Kit và các scope `user.info.basic`, `user.info.profile`, `video.list`.
   Thêm `user.info.stats` để đọc follower.
3. Điền URL:
   - Terms: https://centraltraining.github.io/Test/terms.html
   - Privacy: https://centraltraining.github.io/Test/privacy.html
   - Web/Desktop: https://centraltraining.github.io/Test/
   - Login Kit Web Redirect URI:
     https://qruxqlsbhyhwiqjdkyyc.supabase.co/functions/v1/trainer-channel-test/oauth/callback
4. Apply changes. Thêm đúng 3 tài khoản còn lại vào Target users của Sandbox 2.
5. Trong Supabase → Edge Functions → Secrets, thêm **hai mục mới**:
   - `TIKTOK_TEST_SANDBOX2_CLIENT_KEY`
   - `TIKTOK_TEST_SANDBOX2_CLIENT_SECRET`
   Dùng khóa của Sandbox 2. Không thay `TIKTOK_CLIENT_KEY`, `TIKTOK_CLIENT_SECRET`
   hoặc bộ `TIKTOK_TEST_CLIENT_KEY` / `TIKTOK_TEST_CLIENT_SECRET` hiện có.
6. Mở bản Test, tải lại trang. Vào Quản lý kênh → Thiết lập Sandbox để kiểm tra.
   Khi Sandbox 2 báo Sẵn sàng, gán đúng 3 Trainer sang Sandbox 2. Không ghép tự động
   theo thứ tự danh sách vì phải khớp tài khoản đã thêm vào Target users.
7. Mỗi Trainer đăng nhập kênh của mình, bấm Kết nối và cấp quyền. Sau đó dùng Đồng bộ
   TikTok để xem chung toàn bộ kênh trong bảng theo tuần, tháng hoặc khoảng ngày.

Đổi Sandbox giữ số liệu cũ nhưng yêu cầu kết nối lại trước khi đồng bộ tiếp.
Việc có đủ hai biến khóa chỉ xác nhận cấu hình đã được nhập; TikTok vẫn xác minh
đúng tài khoản Target users và quyền đã cấp khi Trainer kết nối thực tế.

## Phạm vi và bảo vệ

- Function `trainer-channel-test`, giữ cấu hình `verify_jwt=false` hiện có để phục vụ
  callback; các thao tác tài khoản xác thực bằng phiên dashboard và quyền hiện tại.
- Hai bộ khóa nằm trên máy chủ. State OAuth và token gắn với Sandbox sở hữu chúng.
  Đổi mã và refresh token dùng đúng bộ khóa; không tự thử khóa của Sandbox khác.
- Chỉ Admin gán Sandbox; Trainer chỉ kết nối kênh của chính mình và xem dữ liệu
  trong khu vực được cấp quyền. Kiểm tra lại tài khoản/kênh khi callback quay về.
- Callback, tài khoản bị khóa, state hết hạn/dùng lại, đổi cấu hình trong lúc đăng
  nhập, tài khoản TikTok sai và biến khóa thiếu không tạo kết nối giả.
- Không sửa schema, Secrets, dữ liệu KPI/Ollie, sổ gửi hoặc nhánh `ollie-kpi-state`.

Kiểm thử tự động dùng 13 kênh giả lập, không đăng nhập thay Trainer. Không dựng lịch sử
follower trước khi được ghi nhận. View/like/share là tổng mới nhất của video đăng
trong kỳ, không phải tương tác tăng riêng trong kỳ.

## Bản tải

HTML đầy đủ; toàn bộ function đã sửa và các file phụ thuộc; mã giao diện Xây kênh;
chính sách bản Test và kết quả kiểm tra tổng hợp. Không kèm Secrets hay dữ liệu riêng.
