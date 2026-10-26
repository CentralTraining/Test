# TikTok — Trainer xem toàn team — Test 26/10/2026

Trainer đã đăng nhập và hợp lệ được xem chỉ số của mình cùng tất cả Trainer khác trong riêng mục Mở rộng → Xây kênh TikTok. Bộ lọc Khu vực/Trainer, bài đăng, follower hiện tại/tăng trưởng, View/Like/Share, lịch sử follower và trung bình toàn team đều dùng phạm vi mới.

## Quyền hạn

- trainer-channel-test xử lý riêng action overview qua team-overview.ts, xác thực bằng tài khoản Dashboard hiện có. Các vai trò khác, tài khoản khóa, token giả/hết hạn hoặc token không còn hợp lệ sau đổi mật khẩu/quyền bị từ chối.
- overview chỉ đọc, trả DTO chỉ số công khai của kênh. Không trả token TikTok, refresh token, Client Secret, openId hoặc hồ sơ đăng nhập.
- Các thao tác gán kênh, đặt mốc Admin, kết nối, đồng bộ và callback vẫn chuyển đến trainer-channel-api với đúng quyền cũ. Trainer chỉ kết nối kênh của mình. Quyền đồng bộ vẫn trong khu vực được giao; frontend không gửi yêu cầu đồng bộ kênh ngoài phạm vi. Khi đang xem kênh ngoài khu vực, nút Đồng bộ chỉ tải lại các chỉ số đã lưu.
- Mọi phần khác của Dashboard giữ phạm vi quyền hiện có. Bộ xử lý trainer-channel-api và trainer-channel của Dashboard chính không sửa.
- Nơi lưu kết nối, lịch sử và mốc Admin vẫn là các bản ghi mã hóa dùng chung hiện có. Không sao chép hay tạo grant/refresh token mới khi đọc. Tái sử dụng cùng logic chọn grant Sandbox và mốc Admin mới nhất của shared API.

## Giao diện đi kèm

Giữ bản Test bố cục bảng: trái khoảng 41%, phải khoảng 59%; bộ lọc dùng kiểu Dashboard, chia hàng thích hợp trên điện thoại. Giữ tổng tăng Follow, trung bình và mốc ngày 01 theo logic đã kiểm thử.

## Nguồn triển khai

Supabase project qruxqlsbhyhwiqjdkyyc, chỉ function trainer-channel-test, version 15, source hash 4cee48c27986c43ed08dae7bbeb1a2abd489a92b36610af2f713785a45a1bca6. Runtime gồm đúng 7 file trong thư mục function. verify_jwt=false giữ cấu hình cũ, handler tự kiểm tra session Dashboard bằng HMAC cùng mật khẩu/quyền/khu vực mới nhất.

Callback giữ nguyên: https://qruxqlsbhyhwiqjdkyyc.supabase.co/functions/v1/trainer-channel-test/oauth/callback

Bản chính chưa nhận thay đổi quyền xem và bố cục này; chỉ chuyển khi Nghĩa yêu cầu sau khi test.

## Kiểm tra

Backend dùng dữ liệu giả lập: Trainer khác khu vực xem đủ 13; không có bản ghi hoặc token bị đổi khi đọc; 7 grant Main và 3 kênh Sandbox 2 được ghép đúng; không gọi TikTok khi đọc; không trả thông tin xác thực; mọi thao tác ghi ngoài quyền bị chặn; session giả/khóa/đổi mật khẩu/vai trò và ngày không hợp lệ bị từ chối. Main vẫn giới hạn khu vực.

Trình duyệt 390/1440 px: Trainer thấy 13 hàng và các bộ lọc toàn team; trung bình toàn team; chỉ có nút kết nối của bản thân; không tự đồng bộ ngoài khu vực; xem được lịch sử; không tràn ngang hoặc ghi dữ liệu. Bố cục và bộ lọc trước đó đã kiểm tra 320/390/1024/1440/1920 px.

Gói này chứa HTML đầy đủ và toàn bộ source/dependencies thực sự triển khai của function Test; không kèm Secrets, thông tin đăng nhập hoặc dữ liệu Trainer thật.
