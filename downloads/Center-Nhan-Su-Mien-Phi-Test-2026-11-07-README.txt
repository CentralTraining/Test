ĐỒNG BỘ CENTER 08:00 — APPS SCRIPT MIỄN PHÍ — BẢN TEST 07/11/2026

Mở https://centraltraining.github.io/Test/ bằng tài khoản Admin.
Chọn tháng hiện tại → DATA → Nhân sự → Nội bộ → kéo xuống cuối:
Đồng bộ Center lúc 08:00 — Chạy thử.
Bấm Tải trạng thái, mở Thiết lập miễn phí bằng Gmail — làm một lần.

1. LƯU TÀI KHOẢN CENTER
Nhập tên đăng nhập và mật khẩu Center trực tiếp trong khung thiết lập → Lưu tài khoản Center.
Máy chủ mã hóa trong Supabase Vault. Mật khẩu không được trả lại khi tải cấu hình; không gửi mật khẩu qua chat.
Khi bấm Sửa tài khoản, để trống mật khẩu sẽ giữ mật khẩu cũ.

2. TẠO GOOGLE APPS SCRIPT MỘT LẦN
Dùng tài khoản Google có quyền Chỉnh sửa bản sao Sheet Test.
Mở https://script.new → đặt tên Center HR Test.
Trong Dashboard bấm Sao chép mã Apps Script hoặc Tải Code.gs.
Thay toàn bộ mã Code.gs trong Apps Script bằng mã vừa lấy, bấm Lưu.
Trong Apps Script bấm dấu + cạnh Dịch vụ / Services → chọn Google Sheets API, phiên bản v4 → Thêm / Add.
Dự án Google mặc định được tạo tự động. Không cần tự tạo Service Account, JSON key, mở Cloud Console hay thêm thẻ thanh toán.

Trở lại Dashboard → Tạo khóa kết nối → Sao chép khóa.
Trong Apps Script: Cài đặt dự án / Project Settings → Thuộc tính tập lệnh / Script properties → Thêm.
Tên: CENTER_HR_BRIDGE_SECRET
Giá trị: dán đúng khóa vừa tạo → Lưu thuộc tính.
Khóa giữ trong ô Dashboard cho đến khi lưu kết nối. Không chia sẻ khóa, không đưa khóa vào Code.gs hay link công khai.

Trong Apps Script chọn hàm kiemTraCauHinh → Chạy / Run → cấp quyền Google một lần cho dự án của chính bạn.
Triển khai / Deploy → Bản triển khai mới / New deployment.
Chọn loại Ứng dụng web / Web app.
Thực thi bằng / Execute as: Tôi / Me.
Ai có quyền truy cập / Who has access: Bất kỳ ai / Anyone.
Triển khai, sao chép URL kết thúc bằng /exec.
Nếu tài khoản cơ quan không cho chọn Anyone, dùng Gmail cá nhân có quyền sửa Sheet Test.

Trở lại Dashboard: dán URL /exec, giữ cùng khóa đã lưu trong Script properties → Lưu kết nối Apps Script.
Dashboard xóa ô khóa sau khi lưu; chỉ hiện URL và trạng thái kết nối.
Bấm Sửa kết nối nếu cần đổi; để trống khóa sẽ giữ khóa cũ.
Đổi mã Apps Script sau này cần Deploy → Manage deployments → Edit → New version → Deploy; URL /exec vẫn dùng bản triển khai đó.
Hệ thống chỉ xử lý yêu cầu có chữ ký HMAC hợp lệ, khóa chống chạy lại, đúng tháng, đúng file và đúng tab.
Không cần tạo trigger trong Apps Script; Supabase Cron hiện có đảm nhận lịch 08:00.

3. LƯU LINK THÁNG VÀ KIỂM THỬ
Tạo bản sao Sheet riêng cho Test, có tab DS GÁN SHOP PGS; không dùng nguồn đang chạy trên Dashboard chính.
Nhập URL Google Sheet → Lưu link tháng này. Ô khóa lại; có Sửa link và Hủy sửa.
Mỗi tháng có link riêng. Sang tháng mới cần lưu link tháng đó; không tự ghi vào link tháng trước.
Bấm Kiểm tra Center: thử đăng nhập và tìm Export gán shop hiện tại tại Đào Tạo → Danh sách PGs PB Sales. Chưa ghi Sheet.
Bấm Kiểm tra Sheet: đọc đúng file và tab. Chưa ghi Sheet.
Bấm Chạy thử — ghi Sheet & nhập thử, xác nhận thay toàn bộ giá trị tab DS GÁN SHOP PGS của Sheet Test.
Excel được kiểm tra mẫu trước khi ghi; dữ liệu được ghi vào đúng một tab, rồi đọc lại và đối chiếu toàn bộ giá trị.
Các tab khác được giữ nguyên; mã có số 0 đầu và chuỗi bắt đầu bằng dấu = được ghi dưới dạng văn bản.
Nếu không có xác nhận ghi hoặc đọc lại không khớp, trạng thái là cần đối soát, không báo thành công.
Bấm Xem nhân sự nhập thử để kiểm tra kết quả.
Mã nhân viên lấy cột Code, ưu tiên shop chính, giữ trạng thái HR/sao/size có sẵn, không tự chuyển Off những người vắng khỏi Excel.

4. BẬT LỊCH TEST
Chỉ khi chạy thử thực tế thành công, bấm Bật lịch chạy thử 08:00.
Máy chủ khởi chạy lúc 01:00 GMT = 08:00 Asia/Saigon, không cần mở Dashboard hoặc bật máy tính.
08:00 là giờ bắt đầu; thời gian hoàn tất tùy Center và Google. Chọn link theo tháng hiện tại ở Việt Nam.
Chỉ một lượt cron mỗi ngày, khóa lượt chạy đồng thời; khi lỗi cần đối soát trước khi chạy lại thủ công.
Đổi link hoặc kết nối sẽ tắt lịch và yêu cầu chạy thử lại.

CHI PHÍ VÀ PHẠM VI
Apps Script dùng hạn mức miễn phí của tài khoản Google; luồng này chỉ có vài yêu cầu Google mỗi ngày. Không bật dịch vụ Google trả phí.
Lịch và lưu cấu hình dùng dự án Supabase đang có, chịu hạn mức/gói Supabase hiện tại. Không thay đổi gói thanh toán.
Phiên bản này chỉ triển khai Test và lưu nhân sự thử riêng; chưa ghi vào các bảng HR, Trainer, Sale hoặc KPI hiện có.
Chưa đưa lên Dashboard chính; chờ Nghĩa kiểm tra Test.

TRẠNG THÁI BÀN GIAO
Đã kiểm thử bằng dữ liệu giả lập: đăng nhập, Excel, Apps Script, HMAC, chống chạy lại, ghi/đọc Sheet, lỗi, phân quyền, Lưu/Sửa và giao diện 1440/390/320px.
Đã kiểm thử SQL bằng giao dịch rollback và kiểm tra function triển khai khớp mã nguồn; yêu cầu thiếu/giả phiên đăng nhập bị từ chối.
Chưa có tài khoản Center, URL Apps Script/khóa thật, link Sheet tháng thật. Chưa chạy export Center thật, chưa ghi Google Sheet thật và chưa bật lịch tháng nào.
Cần Nghĩa nhập kết nối và cấp quyền Google một lần. Không gửi mật khẩu hoặc khóa qua chat.

TÀI LIỆU GOOGLE
https://developers.google.com/apps-script/guides/web
https://developers.google.com/apps-script/advanced/sheets
https://developers.google.com/apps-script/guides/services/quotas
