# Truyền thông FM — bản Test 28/10/2026

Trên https://centraltraining.github.io/Test/:

1. Đăng nhập Admin, chọn đúng tháng và chiến dịch trong **Tiến độ KPI → Truyền thông → Nội bộ**.
2. Bấm **Sửa** cạnh các ô ID.
3. Chọn **Nguồn: FM**, nhập **ID chiến dịch 6**, **Program ID 8**.
4. Bấm **Lưu** rồi **Cập nhật Truyền thông từ hệ thống**.

API đã xác nhận Program 8 là **DIỆN MẠO MỚI - TRẢI NGHIỆM MỚI**. Program 9 và 10 không được cộng vào kết quả Program 8. Chỉ tính bài được approved như trước.

Nguồn được lưu theo từng chiến dịch tại trường `mediaCampaignType`. Chiến dịch chưa có trường này giữ mặc định **Nội bộ (cũ)** (`noibo`). Các ô nguồn/ID được khóa sau khi lưu; Trainer dùng cấu hình Admin đã lưu. Quyền ghi dữ liệu của Trainer vẫn giữ phạm vi khu vực hiện tại.

## Triển khai

Bản Test dùng function mới `otraining-media-test`, chỉ đọc endpoint cố định `https://otraining.io.vn/api/media-dashboard/employees`, truyền đủ `campaignType`, `campaignId` và `programId`. Function giữ JWT verification ở gateway, giới hạn nguồn `noibo` hoặc `fm`, ID nguyên dương và vùng Miền Trung. Secret `OTRAINING_USER_INFO` được sử dụng ở phía máy chủ theo cấu hình hiện có, không đọc hoặc xuất giá trị Secret.

Source đầy đủ nằm trong `supabase/functions/otraining-media-test/index.ts`; không có phụ thuộc bên ngoài. `supabase/config.toml` ghi rõ `verify_jwt=true`. Gói kèm toàn bộ HTML, mã nguồn function và chứng cứ kiểm thử được xuất thành các tệp tải riêng; ZIP này chứa source function và manifest/README/chứng cứ.

Function sản xuất `otraining-testonline` không thay đổi. Không thay Secrets, schema, mốc KPI, callback TikTok, code hoặc HTML Dashboard chính. Release không tự cập nhật nguồn hoặc data chiến dịch trong database; thao tác Lưu/Cập nhật do người dùng chủ động trên Test.

Khi được yêu cầu chuyển Main, cần triển khai cùng source adapter dưới tên `otraining-media` trước, rồi chuyển đúng HTML đã kiểm thử; các chức năng khác vẫn dùng `otraining-testonline` như cũ. Không chuyển chỉ riêng HTML khi chưa có adapter Main.

## Kiểm chứng

- Gọi thực tế function Test với `fm / 6 / 8` trả HTTP 200, đúng tên chương trình; không ghi database. Không gửi JWT trả 401.
- Kiểm thử giả lập xác minh lưu nguồn/ID cùng nhau, chỉ tính đúng Program 8, giữ dữ liệu cũ khi API lỗi/không có dữ liệu/không khớp nguồn hoặc chương trình/lưu thất bại, bỏ phản hồi cũ khi đổi Program ID và giữ dữ liệu khu vực khác khi Trainer cập nhật.
- Kiểm tra giao diện desktop 1440px và mobile 390px.
- Không có Cookie, dữ liệu PG thật hoặc giá trị Secret trong source hay gói tải.
