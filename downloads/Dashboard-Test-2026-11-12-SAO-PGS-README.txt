SAO PGS — DASHBOARD TEST THẬT, 12/11/2026

https://centraltraining.github.io/Test/
Mở Tổng quan HR → Nhân Sự Nội Bộ → SAO PGS.
Dùng bộ lọc tháng, khu vực, Trainer, Sale hiện có ở Dashboard.

Giữ năm thẻ theo giao diện đã duyệt; biểu đồ so tháng đang chọn với tháng liền trước,
có số trên cả hai cột. Bảng chất lượng theo khu vực/Trainer giữ đủ 8 cột.
Danh sách lên sao có lọc nhiều mức Từ sao và Lên sao, tìm kiếm, phân trang,
lộ trình từng PG và xuất Excel theo đúng bộ lọc. Mã NV là text, giữ số 0 đầu.

Chỉ tính PG OPPO Đang làm ở từng tháng riêng biệt, không lấy giao của hai tháng.
PG đã Off hiện tại vẫn tính trong tháng trước nếu tháng đó còn Đang làm.
Hạng sao thiếu hoặc thiếu dữ liệu tháng không bị thay bằng 0. Tổng Miền Trung
hiển thị thêm khi xem phạm vi khu vực/Trainer/Sale. Không có báo cáo Off theo sao
hay phân loại lên sao tự nhiên/sát hạch.

Nguồn lộ trình: tab LÊN SAO trong Google Sheet DATA tháng đã lưu ở Data → Nhân sự.
Nút Cập nhật LÊN SAO chỉ đọc lại nguồn, không ghi Google Sheet hoặc nhân sự.
Hiện kiểm tra thực tế: chưa có tab LÊN SAO trong nguồn tháng. Các chỉ số lên sao
sẽ hiện dấu — kèm thông báo cho đến khi đồng bộ đủ nguồn. Không coi đây là 0 lượt.
Lịch HR 23:59 giờ Việt Nam đang bật và giữ nguyên. Máy chủ Center đã hỗ trợ tab thứ 5;
lần đồng bộ đủ nguồn sẽ cung cấp dữ liệu để bấm đọc lại. Không chạy lại HR thật để thử UI.
Bản Apps Script 5 tab được giữ sẵn trong mục kết nối nếu cần cập nhật bản triển khai.

Dữ liệu đọc trên máy chủ theo tài khoản đã xác thực. Admin được toàn miền;
Trainer chỉ nhận danh sách trong khu vực được cấp, kèm tổng hợp toàn miền không có danh tính.
Endpoint mới chỉ đọc; giữ lớp JWT và xác thực Dashboard. Không đổi trạng thái PG,
quy tắc nhập HR, Target, lịch, Secrets, bot hoặc KPI. Dashboard chính chưa được cập nhật.

Đã kiểm tra Admin/Trainer ở 1440, 390, 320 px; số liệu hai cột, bộ lọc, lộ trình,
Excel tải/đọc lại, thiếu nguồn, đổi tháng/tài khoản, đăng xuất, các tab HR cũ.
Các kiểm thử tự động dùng dữ liệu giả lập. Không có dữ liệu nhân sự thật trong mã công khai.
HTML đầy đủ đi kèm để lưu phiên bản. Mã máy chủ và phụ thuộc nằm trong ZIP riêng,
không công bố trên GitHub. HTML vẫn cần kết nối mạng và tài khoản Dashboard hợp lệ.
