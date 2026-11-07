BẢN TEST — SỬA EXPORT GÁN SHOP CENTER — 07/11/2026

Nguyên nhân: nút “Export gán shop hiện tại” là nút gửi biểu mẫu GET. Bộ đọc cũ chỉ tìm đường dẫn href/onclick nên bỏ sót nút này.
Đã sửa bộ đọc trên máy chủ Test: vào đúng trang /trainer; đọc biểu mẫu và gửi đúng nút Export gán shop hiện tại, giữ các bộ lọc mặc định của form. Giữ phương thức GET và giới hạn cùng tên miền Center.
Các trường không được chọn/đã vô hiệu hóa và nút Export chung không được gửi nhầm.
Đã kiểm tra thực tế tải và đọc được Excel đúng mẫu từ Center bằng phiên đang lưu; không ghi Google Sheet hoặc cập nhật nhân sự/KPI trong lượt kiểm tra này.

NGHĨA LÀM TIẾP
1. Mở https://centraltraining.github.io/Test/ → DATA → Nhân sự → Nội bộ → khung Đồng bộ Center lúc 08:00.
2. Bấm lại Kiểm tra Center. Khi nhận đúng Excel sẽ báo xanh “Đã lấy được Excel gán shop đúng mẫu từ Center. Chưa ghi vào Google Sheet.”
3. Bấm Kiểm tra Sheet.
4. Nếu cả hai đạt, bấm Chạy thử — ghi Sheet & nhập thử. Bước này thay toàn bộ giá trị trong tab DS GÁN SHOP PGS của Sheet Test đã lưu.
5. Kiểm tra danh sách nhân sự nhập thử. Chỉ khi chạy thử thực tế thành công mới bật lịch 08:00.

Không cần đổi lại các kết nối hoặc link tháng đã lưu để dùng bản sửa này. Khi Center báo phiên hết hạn, đăng nhập trực tiếp vào Center để cập nhật Cookie qua ô bảo mật.
Chỉ Test; Dashboard chính giữ nguyên. Lịch chưa được bật và chưa có dữ liệu nào ghi vào Google Sheet bởi lượt kiểm tra.
HTML tải về là toàn bộ Test hiện tại, giữ nguyên giao diện bản trước; thay đổi nằm trong Edge Function center-hr-sync-test v6.
ZIP mã nguồn đầy đủ được cung cấp riêng cho chủ dự án, không đưa source xác thực hoặc thông tin riêng lên kho công khai.
