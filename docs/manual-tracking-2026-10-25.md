# Xây kênh — cập nhật tiến độ thủ công

Phiên bản **Test, 25/10/2026 — v2**. Website: https://centraltraining.github.io/Test/.
Chưa áp dụng chức năng này lên Dashboard chính.

## Cách dùng

1. Đăng nhập bản Test, mở **Mở rộng → Xây kênh**.
2. Bấm **Cập nhật tiến độ thủ công** (điện thoại: **Quét thủ công**).
3. Chọn các kênh đã gán, hoặc chọn file Excel/CSV có cột `Url` như mẫu.
   File chỉ chọn đúng kênh theo username; không sửa ánh xạ Trainer hay mốc Admin.
4. Bấm **Quét và cập nhật**. Danh sách cập nhật lần lượt, có kết quả riêng từng kênh.
5. Bảng tự cập nhật từng kênh ngay khi quét thành công; nguồn mặc định **Tự động** ưu tiên dữ liệu Web tracking đã lưu. Xem theo tuần, tháng hoặc khoảng ngày.
   Có thể chọn riêng **TikTok API** để đối chiếu dữ liệu kết nối trước đó. Nút làm mới TikTok API không tự đổi nguồn đang xem.

## Thay đổi hiển thị v2

- Cập nhật bảng ngay sau mỗi kênh, không chờ quét xong cả danh sách.
- Kết quả vừa lưu vẫn hiển thị khi tải lại danh sách lỗi hoặc phản hồi cũ đến chậm.
- Hiển thị tổng video, follower hiện tại và tổng like kênh đã quét; phân biệt với phần tăng trong kỳ.
- Giữ nguyên mốc Admin và cách ghi nhận tăng/giảm theo ngày Việt Nam.
- Không thay Edge Function phiên bản 8, dữ liệu lưu, Secrets hoặc Dashboard chính.

## Ý nghĩa số liệu

- Giữ nguyên mốc follower ngày 01/10/2026 do Admin nhập và lịch sử TikTok API.
- Nguồn tracking hiện chỉ trả bộ đếm tổng follower, like và video của kênh.
- Mỗi ngày Việt Nam giữ mốc mở đầu và mốc cuối; quét lặp không cộng trùng.
- Lần quét đầu làm mốc cho like/video chưa có lịch sử; không đưa toàn bộ video cũ
  vào tiến độ đăng hôm nay. Follower đối chiếu được với mốc thực tế đã có.
- Phần tăng/giảm giữa các lần quét được ghi nhận vào ngày quét kế tiếp.
  Không suy ra ngày đăng thực tế hoặc lịch sử tương tác chưa quan sát.
- View/Share không có từ nguồn này, hiển thị chưa có dữ liệu. Không tự điền số 0.
- Giảm bộ đếm vẫn được giữ; dữ liệu thiếu được phân biệt với số 0 hợp lệ.
- Lỗi từng kênh giữ nguyên dữ liệu trước. Các kênh còn lại có thể tiếp tục quét.

## Triển khai và phạm vi

- HTML gọi HTTPS Supabase; chỉ Edge Function gọi endpoint tracking HTTP cố định
  do Admin cung cấp. Chỉ gửi URL TikTok công khai, không gửi phiên dashboard,
  mật khẩu, token TikTok, thông tin Trainer hoặc dữ liệu KPI/PGs cho tracker.
- Excel được đọc trong trình duyệt; không tải nguyên file lên tracker.
- Edge Function `trainer-channel-test` phiên bản 8 kiểm tra phiên dashboard,
  tài khoản còn hiệu lực và phạm vi Trainer/khu vực trước và sau khi gọi nguồn.
- Dữ liệu quét nằm riêng trong payload kênh đã mã hóa hiện có. Không cần đổi
  schema, Secrets, khóa kết nối hoặc dữ liệu baseline.
- Giữ cấu hình `verify_jwt=false` hiện có vì function tự xác thực phiên dashboard
  và phục vụ OAuth callback; không bỏ kiểm tra xác thực của ứng dụng.
- Không thay `trainer-channel` chính, mã KPI/Ollie, sổ gửi hoặc nhánh dữ liệu bot.

## Nội dung bản tải

- `index.html`: toàn bộ HTML đã kiểm thử.
- `supabase/functions/trainer-channel-test/`: đủ 5 file function và phụ thuộc.
- `channel-source/`: mã giao diện/model của Xây kênh để bảo trì.
- `terms.html`, `privacy.html`: nội dung chính sách bản Test đã cập nhật nguồn tracking.
- `verification/`: kết quả kiểm tra tổng hợp bằng dữ liệu giả lập và kiểm tra endpoint.

Không kèm file Excel kênh thật, dữ liệu đã quét, cookie hoặc Secrets.
