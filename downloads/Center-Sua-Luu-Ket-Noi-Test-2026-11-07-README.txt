BẢN TEST — SỬA LƯU KẾT NỐI CENTER / APPS SCRIPT — 07/11/2026

Lỗi “Chưa đọc/lưu được cấu hình” xuất phát từ câu lệnh lưu kết nối trên máy chủ.
Log xác định PostgreSQL 21000: UPDATE requires a WHERE clause.
Câu lệnh tắt lịch Test khi đổi kết nối thiếu điều kiện WHERE nên bị safeupdate của Data API chặn.
Đã thêm điều kiện chỉ cập nhật các cấu hình Test đang bật lịch hoặc đã xác minh kết nối.
Giữ mã hóa Vault, xác thực Admin, khóa chạy đồng thời và kiểm tra phiên bản kết nối.
Không tắt safeupdate hoặc mở quyền công khai.

Mở https://centraltraining.github.io/Test/ → DATA → Nhân sự → Nội bộ → Đồng bộ Center lúc 08:00.
Bấm lại Lưu tài khoản Center / Lưu kết nối Apps Script với thông tin của mình.
Nếu đã tải lại trang: Tải trạng thái rồi nhập lại kết nối. Lần lưu lỗi đã được hủy toàn bộ.
Link Google Sheet theo tháng đã lưu được giữ nguyên. Dùng URL Apps Script và khóa đã cấu hình trong Script properties.
Lưu đủ kết nối → Kiểm tra Center → Kiểm tra Sheet → Chạy thử → bật lịch sau khi thành công.
Mật khẩu và khóa nhập trực tiếp trong giao diện, không gửi qua chat.

Đã kiểm thử RPC bằng service_role: tạo/sửa hai kết nối, mã hóa/đọc lại nội bộ, chặn phiên bản cũ, vô hiệu hóa lịch để kiểm tra lại và giữ quyền công khai bị từ chối.
Kiểm thử dùng giao dịch rollback. Không lưu tài khoản giả; hash nguồn trước/sau giống nhau; không có lượt đồng bộ hoặc snapshot nhân sự thật.
Chưa đăng nhập Center thật hoặc ghi Google Sheet thật. Lịch chưa bật.
Chỉ sửa RPC Test. HTML và Edge Function v4 giữ nguyên; Dashboard chính giữ nguyên.
HTML tải về là toàn bộ Test hiện tại, byte-exact bản đã kiểm thử. ZIP riêng kèm đầy đủ source và SQL đã sửa.
