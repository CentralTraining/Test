# Xây kênh TikTok — bố cục bảng và bộ lọc — Test 26/10/2026

- Máy tính: bảng Tiến độ bài đăng bên trái chiếm khoảng 41%, bảng Follow · View · Like · Share bên phải khoảng 59%. Hai bảng giữ chiều cao đồng đều và thứ tự Trainer.
- Tăng chỗ cho tên Trainer và cặp số follower hiện tại / mức tăng trong bảng phải. Giảm độ dài thanh tiến độ và gọn cột Bài/Target trong bảng trái.
- Bộ lọc dùng bề mặt, nhãn xanh, viền xanh bo góc và trạng thái focus theo các bộ lọc Dashboard. Các ô tuần/tháng/ngày, khu vực và Trainer thẳng hàng; chế độ tuần/tháng/khoảng ngày dùng một nhóm nút.
- Điện thoại: nhóm chọn kỳ trên một hàng, các ô dưới tự chia lưới; khoảng ngày có hai cột. Giữ bảng chỉ số tổng hợp gồm cả Bài đăng, Follow, View, Like, Share, không phát sinh cuộn ngang.

Chỉ thay CSS và markup bộ lọc trong hai khối Xây kênh của HTML. Logic tính KPI, video, follow, trung bình team, mốc Admin và quyền xem không đổi. Không sửa backend dùng chung, kết nối, khóa, callback hoặc dữ liệu.

Kiểm tra trình duyệt bằng dữ liệu giả lập ở 320, 390, 1024, 1440, 1920 px: bảng phải rộng hơn; cặp số và tên Trainer dài vừa chỗ; nhãn/ô lọc cân đối; tuần/tháng/khoảng ngày, lọc Trainer, lịch sử follower, quản lý kênh và quyền khu vực hoạt động; không cuộn ngang hay ghi dữ liệu. Trên điện thoại 320/390 px, cả 13 hàng số liệu vẫn nằm trên màn hình đầu ở chế độ tháng. Kiểm tra hồi quy menu và trạng thái tháng KPI đã đạt.

Bản này triển khai ở CentralTraining/Test. Dashboard chính chỉ cập nhật khi Nghĩa yêu cầu chuyển bản đã test.
