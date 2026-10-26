# Dùng lại kết nối TikTok từ Dashboard chính trên Test

Phiên bản **Test, 26/10/2026**. Chỉ sửa máy chủ `trainer-channel-test`; HTML và máy chủ
Dashboard chính giữ nguyên. Bản Test tiếp tục chỉ dùng TikTok API với hai Sandbox.

## Hành vi

Khi tài khoản có quyền mở Xây kênh, Test tự đọc kết nối đã có ở Dashboard chính nếu:

- Sandbox 1 trên Test dùng đúng cùng bộ khóa ứng dụng với bản chính.
- Kênh được gán trùng khớp; Trainer nằm trong khu vực tài khoản được phép xem.
- Test chưa có kết nối riêng cho kênh đó và kênh chưa được gán sang Sandbox 2.
- Kết nối và mốc đối chiếu không bị ràng buộc với một tài khoản TikTok khác.

Trainer không cần đăng nhập TikTok lại chỉ để hiển thị những kết nối hợp lệ này.
Mở lại https://centraltraining.github.io/Test/, vào Mở rộng → Xây kênh.

Đồng bộ hoặc kết nối lại các kênh dùng chung được chuyển tới máy chủ chính với đúng
phiên dashboard hiện tại. Máy chủ chính tiếp tục tự kiểm tra quyền và giữ một bản
token có thẩm quyền; không nhân bản token/refresh token vào vùng dữ liệu Test.
Đọc danh sách trên Test không ghi dữ liệu vào hai vùng lưu. Đồng bộ qua giao diện
cập nhật dữ liệu qua chức năng đồng bộ bình thường của nguồn đang sở hữu kết nối.

## Giữ nguyên dữ liệu và phạm vi

- Kết nối Test đã có vẫn được ưu tiên. Các kênh Sandbox 2 hoạt động riêng.
- Mốc Admin hợp lệ trên Test được giữ nguyên, không bị thay bằng mốc từ bản chính.
- Khi Admin chủ động chuyển một kênh đang dùng chung sang Sandbox 2, mốc Admin được
  giữ cho đúng kênh; kênh đó cần cấp quyền riêng của Sandbox 2 trước khi đồng bộ tiếp.
- Khác bộ khóa ứng dụng hoặc khác kênh đã gán thì không dùng lại kết nối.
- Không trả token, mã tài khoản riêng của TikTok hoặc Client Secret về trình duyệt.
- Không thay schema, Secrets, mã/giao diện Dashboard chính, KPI/Ollie hay sổ gửi.
- Giữ callback chung đã đăng ký. Không bật lại tính năng Web tracking.

## Kiểm tra

Kiểm thử giả lập gồm bảy kết nối chính hiển thị trên Test mà không đăng nhập mới;
đọc danh sách nhiều lần không ghi dữ liệu; không sao chép token; refresh dùng đúng
máy chủ sở hữu; kết nối Test/Sandbox 2 không bị ghi đè; mốc Admin được giữ; khác kênh,
khác ứng dụng, khác khu vực hoặc sai chủ tài khoản bị chặn; lỗi nguồn giữ dữ liệu cũ.

Đã kiểm tra endpoint triển khai nhận đúng cấu hình hai Sandbox và bật khả năng dùng
lại kết nối chính. Không giả mạo phiên đăng nhập hoặc đọc danh sách kết nối riêng
bằng một tài khoản ngoài phiên dashboard của người dùng.

Bản tải có toàn bộ function đã sửa và phụ thuộc, cùng kết quả kiểm tra tổng hợp.
HTML đầy đủ được cung cấp riêng; không kèm Secrets, cookie hay dữ liệu Trainer.
