# Tư vấn mẫu AI — FTF Đối tác, bản Test 28/10/2026

Mở https://centraltraining.github.io/Test/ → **Tiến độ KPI → Đối tác → FTF**. Chọn tháng và ID chiến dịch đã lưu (chiến dịch đang kiểm tra: **22**), rồi bấm **Cập nhật FTF từ hệ thống**. Nếu hệ thống yêu cầu xác thực, nhập mật khẩu Dashboard vào hộp xác thực trên trang; không gửi mật khẩu qua chat.

## Quy tắc tính

- Dùng `detailSheetData.simulationStatusMap` của endpoint `api/qrcode/f2f-visits/download-all` cho Tư vấn mẫu AI. `statusMap` là kết quả bài test, không dùng để tính AI.
- `dat` → **Đạt**, được tính hoàn thành.
- `chua_dat` → **Chưa đạt**, đã thực hiện nhưng chưa đáp ứng yêu cầu; không tính hoàn thành.
- Không có trạng thái → **Chưa làm**. Giá trị không nhận diện được hiển thị **Chưa xác định**, không tự coi là Đạt.
- Ghép người với shop bằng `allAttendees.user_id/shop_id`, tên lấy từ `nameMap`. Khử trùng cùng người trong cùng shop; một người có tham gia nhiều shop được gán cho từng shop tương ứng.
- Bấm số ở cột **Tư vấn AI** của shop để xem tên, trạng thái và thời điểm đồng bộ. Trên điện thoại, chạm tên shop rồi bấm chỉ số Tư vấn AI trong thẻ thông tin.

File Excel nhập thủ công cũng dùng quy tắc chỉ **Đạt** mới hoàn thành. HR, bài test, khảo sát và các Target theo kênh Admin đã đặt giữ quy tắc hiện có. Nếu Target Tư vấn AI đang là 0, bản sửa vẫn giữ 0; số Đạt được cập nhật, không tự tạo Target mới.

## Triển khai và quyền

Function mới `otraining-ftf-ai-test` chỉ đọc nguồn dữ liệu, không ghi database. Gateway giữ `verify_jwt=true`; bên trong còn bắt buộc phiên tài khoản Dashboard hợp lệ, kiểm tra tài khoản hiện tại, chữ ký, mật khẩu/quyền/khu vực còn hiệu lực, và chiến dịch FTF đã được cấu hình đúng tháng. JWT gateway đơn lẻ không đủ quyền đọc.

Admin được xem dữ liệu chiến dịch miền Trung. Trainer chỉ nhận các shop khớp Target FTF do Admin quản lý trong khu vực được cấp quyền. Không nhận `userId`, `userType`, header nguồn hoặc URL tùy ý từ client. Header dịch vụ otraining hiện có chỉ được dùng trong máy chủ; không xuất giá trị header, Cookie hay Secrets ra client/log/source.

HTML gọi `otraining-ftf-ai-test` ở `/Test/`; khi chuyển Main sẽ gọi `otraining-ftf-ai`. **Chưa triển khai adapter Main**. Chỉ chuyển lên Main khi Nghĩa yêu cầu rõ; phải triển khai cùng source dưới tên `otraining-ftf-ai` trước khi chuyển đúng HTML đã kiểm thử. Bản HTML này cũng chứa thay đổi FM trước đó: Main cần adapter `otraining-media` theo README bản FM.

`otraining-testonline` sản xuất không thay đổi. Không thay Secrets, schema, dữ liệu thật hoặc mốc Target trong lần phát hành này. Cập nhật số liệu thật chỉ diễn ra khi người dùng chủ động bấm cập nhật và đã xác thực.

ZIP gồm đầy đủ `index.ts`, `access.ts`, cấu hình function, README và chứng cứ kiểm thử. HTML đầy đủ được xuất thành tệp riêng. Không có dữ liệu PG/Trainer thật, token hay giá trị Secret trong gói.

## Kiểm chứng

- Dữ liệu nguồn và trang xuất Excel của otraining xác nhận đúng `simulationStatusMap`, `allAttendees`, `nameMap` và liên kết shop.
- Kiểm thử giả lập chạy trên hàm máy chủ thực tế và toàn bộ HTML ở 1440px/390px: tách Đạt/Chưa đạt/Chưa làm, khử trùng, không lấy kết quả test thay AI; không ghi khi dữ liệu lỗi/thiếu/không khớp hoặc phản hồi cũ; giữ khu vực khác và Target Admin.
- Kiểm thử phiên giả, tài khoản bị khóa/đổi mật khẩu, sai tháng/campaign, shop ngoài khu vực đều bị từ chối. Kiểm tra trực tiếp function đã triển khai xác nhận không có JWT, thiếu phiên Dashboard hoặc phiên giả đều trả 401 và không có dữ liệu đối tác.
- Không giả mạo phiên tài khoản thật để kiểm tra. Chưa khẳng định đã cập nhật số liệu thật trong Dashboard của Nghĩa trước thao tác cập nhật có xác thực.
