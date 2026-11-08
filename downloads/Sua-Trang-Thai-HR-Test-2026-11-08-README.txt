BẢN TEST — SỬA CHUNG LƯU TRẠNG THÁI HR — 08/11/2026

Địa chỉ: https://centraltraining.github.io/Test/
- Các thao tác lưu HR dùng API có xác thực Dashboard và kiểm tra quyền mới nhất.
- Trạng thái HR và ghi chú ON/OFF được lưu trong một giao dịch. Lỗi một bước sẽ không lưu một phần.
- Dữ liệu ở tab cũ hoặc file import không được ghi đè trạng thái đã duyệt mới hơn.
- Khi dữ liệu vừa đổi ở phiên khác, thông báo tải lại thay vì tiếp tục ghi đè.
- Vẫn giữ quy tắc trạng thái HR cố định; Trainer gửi yêu cầu, Admin duyệt. Dòng OFF từ file chưa có duyệt không tự đổi trạng thái HR.
- Chỉ đồng bộ quyết định đã duyệt khi khớp chính xác mã PG, Trainer, thời điểm và tháng hiệu lực. Mã không rõ hoặc trùng được bỏ qua để kiểm tra.
- Không sửa các snapshot tháng đã khóa. Không thay Target, chiến dịch, lịch Center 23:59, lịch thông báo/KPI 08:00 hoặc Google Apps Script.

Cách kiểm tra: mở Test, Tổng quan HR > Nhân sự. Admin đổi trạng thái một nhân sự thử bằng dropdown hoặc form Sửa. Kiểm tra PGs Dev hiển thị cùng trạng thái. Trainer chỉ gửi yêu cầu, không tự áp dụng. Sau duyệt, một lượt import hoặc tab cũ không được đưa trạng thái về giá trị cũ.
Dùng dữ liệu thử khi kiểm tra tự động. Bản Test vẫn dùng kho HR chung theo cấu hình đang có; thao tác thực của người dùng có thể cập nhật kho chung.

CHƯA chuyển Dashboard chính. Chưa thực hiện đợt đối soát/đổi trạng thái dữ liệu thật.
Mã nguồn đầy đủ API, SQL và kiểm thử được cung cấp riêng trong tệp ZIP; không đưa mã máy chủ xác thực lên kho công khai.
