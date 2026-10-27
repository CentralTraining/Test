# Sửa Tracking hashtag — bản Test, 27/10/2026

Mở **Mở rộng → Xây kênh TikTok → Tracking hashtag** trên https://centraltraining.github.io/Test/.

1. Chọn **Tháng**, tháng **10/2026**, khu vực và Trainer ở bộ lọc của trang Xây kênh.
2. Chọn hashtag **#VNOPPOA7PRO** đã lưu. Dòng “Kỳ đang theo dõi” cho biết khoảng ngày thực sự được áp dụng.
3. Bấm **Cập nhật hashtag** để đọc lại nội dung và chỉ số bằng kết nối TikTok hiện có.

Hashtag được khớp trong cả tiêu đề và caption, không phân biệt hoa/thường. Khớp đúng hashtag đầy đủ, giữ dấu tiếng Việt. Một video có nhiều hashtag chỉ được tính một lần trong tổng. Phạm vi vẫn là video của các kênh Trainer đã kết nối, không tìm toàn TikTok.

## Thay đổi

- Sửa trường hợp mô tả rỗng nhưng tiêu đề chứa hashtag bị bỏ sót.
- Chuẩn hóa bộ đếm nguyên không âm do API trả dưới dạng số hoặc chuỗi số. Dữ liệu thiếu vẫn là dấu —.
- Tận dụng tiêu đề và chỉ số thật trong snapshot đã đồng bộ nếu lượt đọc mới chưa cung cấp dữ liệu. Những video này ghi “Theo mốc đồng bộ” và thời điểm lưu; không coi đó là số liệu vừa đọc từ TikTok. Bình luận chưa có trong snapshot vẫn chưa xác định.
- Hiển thị rõ kỳ ngày đăng, số video có nội dung, số kênh đã đọc lại và lỗi từng kênh.
- Thêm chẩn đoán số lượng trường dữ liệu trong máy chủ, không ghi token, video ID, Trainer, tên kênh, hashtag hoặc nội dung video vào log.

View/like/bình luận/share là số tích lũy đã quan sát của các video đăng trong kỳ, không phải phần tăng tương tác riêng trong tháng. Mỗi video có nhãn nguồn và thời điểm. Kênh chưa kết nối hoặc thiếu dữ liệu không được coi là đã đọc đủ.

## Mã nguồn

HTML đầy đủ được xuất riêng theo phiên bản. ZIP đi kèm chứa toàn bộ `supabase/functions/trainer-channel-test/` cùng các file phụ thuộc và cấu hình function, trích từ đúng source đã triển khai. Không có Secrets, token hay dữ liệu riêng. Kiểm thử dùng dữ liệu giả lập.

Trong function Test, bản sửa chỉ thay `team-overview.ts`. Các route xác thực, callback, kết nối và đồng bộ giữ nguyên. Action `hashtag_videos` chỉ đọc video có trong snapshot của Trainer được cấp quyền, tối đa 20 video/yêu cầu; không ghi grant, refresh token, đổi mốc follower hoặc ghi dữ liệu tiến độ. `verify_jwt=false` giữ như trước; function tự xác thực tài khoản Dashboard trong `access.ts`.

Danh sách hashtag hiện có tại `channelHashtagWatchlist:v1` được giữ nguyên. Không thay schema hoặc Secrets. Không cần Trainer cấp quyền TikTok lại cho bản sửa này.

`trainer-channel` Main và `trainer-channel-api` dùng chung không thay đổi. Khi được yêu cầu chuyển lên Main, cần giữ native owner routes và callback Main; không chép nguyên facade Test đè lên Main.

Các kiểm thử tái hiện được lỗi bỏ sót tiêu đề và xác minh số liệu giả lập. Chưa thể xác nhận số view thực tế của hashtag trên phiên đăng nhập của Nghĩa chỉ từ log HTTP.
