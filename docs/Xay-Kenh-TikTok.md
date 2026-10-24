# Bật tự đồng bộ TikTok — Team Trainer Miền Trung

Dashboard: https://centraltraining.github.io/Dashboard/
Vào **Mở rộng → Xây kênh → Hướng dẫn kết nối** để xem lại các bước này.

## 1. Tạo ứng dụng TikTok

1. Mở https://developers.tiktok.com/, đăng nhập và vào **Manage apps → Create app**.
2. Đặt tên phù hợp, ví dụ **Team Trainer Miền Trung — Xây kênh**, chọn nền tảng **Web**.
3. Thêm **Login Kit** và **Display API**.
4. Yêu cầu đủ ba quyền: `user.info.basic`, `user.info.profile`, `video.list`.
5. Website URL: `https://centraltraining.github.io/Dashboard/`.
6. Redirect URI cho bản chính (chép nguyên dòng):

   `https://qruxqlsbhyhwiqjdkyyc.supabase.co/functions/v1/trainer-channel/oauth/callback`

   Redirect URI cho bản Test, nếu muốn thử bằng Sandbox trước:

   `https://qruxqlsbhyhwiqjdkyyc.supabase.co/functions/v1/trainer-channel-test/oauth/callback`

7. Điền Privacy Policy/Terms of Service và các thông tin đơn vị đúng thực tế. Các tài liệu pháp lý cần được đơn vị duyệt; không dùng đường dẫn giả. Hoàn tất xác minh website và các yêu cầu video demo/xét duyệt mà TikTok hiển thị.
8. Sandbox chỉ hoạt động với các tài khoản thử nghiệm được TikTok cấp quyền. Muốn triển khai đầy đủ 13 Trainer, phải đáp ứng yêu cầu truy cập và xét duyệt của TikTok. Không thể bỏ qua bước cấp quyền chỉ bằng link @kênh.

## 2. Lưu khóa trên Supabase

Mở https://supabase.com/dashboard/project/qruxqlsbhyhwiqjdkyyc/functions/secrets

Thêm hai Secrets:

- `TIKTOK_CLIENT_KEY`: Client Key của ứng dụng vừa tạo.
- `TIKTOK_CLIENT_SECRET`: Client Secret tương ứng.

Không dán Client Secret vào chat, GitHub, HTML hoặc ô nhập trang TikTok. Không thay các Secrets đang dùng cho Ollie_MT hay OTraining.

## 3. Gán và kết nối kênh

1. Admin mở **Mở rộng → Xây kênh → Gán trang TikTok**.
2. Chọn Trainer, nhập `@tenkenh` hoặc `https://www.tiktok.com/@tenkenh`, chọn ngày bắt đầu tính target, bấm **Lưu trang TikTok**.
3. Trainer đăng nhập dashboard bằng tài khoản của mình và bấm **Kết nối** ở kênh của mình. Nếu cần, nhập lại mật khẩu dashboard để máy chủ xác minh quyền.
4. Đăng nhập đúng tài khoản TikTok đã gán và đồng ý đủ ba quyền. Hệ thống đối chiếu username TikTok; đăng nhập nhầm kênh sẽ bị từ chối.
5. Khi quay lại dashboard, trang tự lấy danh sách video. Mỗi Trainer có một kênh; một kênh không được gán trùng cho Trainer khác.

## Cách đọc báo cáo

- Tuần: thứ Hai đến Chủ nhật, theo giờ Việt Nam; target 3 video/tuần.
- Tháng/khoảng ngày: target = `ceil(3 × số ngày theo dõi / 7)`. Ví dụ theo dõi đủ tháng 10 có 31 ngày → 14 video/Trainer.
- Nếu ngày bắt đầu theo dõi nằm trong kỳ thì target chỉ tính số ngày kể từ ngày đó.
- Video được lọc theo ngày đăng. Like/share là tổng mới nhất của các video đăng trong kỳ, **không phải** lượt tương tác tăng riêng trong kỳ.
- Chỉ đọc video công khai mà TikTok cấp qua Display API. Không lấy số liệu từ việc quét trang web.
- Chưa kết nối/chưa đồng bộ: hiển thị dấu `—`, không giả thành 0.
- Tự đồng bộ khi mở trang và mỗi 15 phút khi đang xem. Có nút đồng bộ ngay. Không có tác vụ chạy nền khi đóng trang trong phiên bản này.
- Khi TikTok lỗi/giới hạn lượt truy cập, giữ số liệu lần đồng bộ thành công gần nhất và hiển thị thời điểm đó.
- Admin xem toàn đội; Trainer xem báo cáo khu vực của mình, chỉ kết nối TikTok của chính mình.

## Nguồn chính thức

- https://developers.tiktok.com/doc/display-api-overview/
- https://developers.tiktok.com/doc/login-kit-web/
- https://developers.tiktok.com/doc/oauth-user-access-token-management/
- https://developers.tiktok.com/doc/tiktok-api-v2-video-list/
- https://developers.tiktok.com/doc/tiktok-api-v2-get-user-info/

## Ghi chú mã nguồn

HTML đã bao gồm giao diện và bộ lọc; không chứa Client Secret hoặc token TikTok.
Edge Function có `verify_jwt=false` để nhận callback OAuth, nhưng các thao tác riêng đều xác minh phiên dashboard ký HMAC và quyền hiện tại trên máy chủ. Bảng `trainer_channel_private` bật RLS, không cho `anon`/`authenticated` đọc ghi trực tiếp. Payload và OAuth token được mã hóa AES-GCM; namespace Test và bản chính tách biệt.
