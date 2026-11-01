# Find Master — Cảnh báo trạng thái HR — Test 01/11/2026

Tiến độ KPI → Nội bộ → Find Master → Cá nhân → Danh sách PGs Master và tiến độ từng mốc.

PG Master có trạng thái HR khác **Đang làm** sẽ bôi đỏ tương tự dòng Trainer loại, ghi rõ `HR: <trạng thái>` ở cột Trạng thái. Xem trong bộ lọc **Loại / HR khác Đang làm**, hoặc chỉ xem nhóm này bằng **HR khác Đang làm**. Trên điện thoại có nền/tên đỏ; chạm tên PG để xem đầy đủ trạng thái HR trong chi tiết.

Đối chiếu mã PG với DATA nhân sự OPPO của tháng đang xem. Giá trị Đang làm được chuẩn hóa khoảng trắng, chữ hoa/thường và dấu. Nếu thiếu bản ghi HR hoặc trạng thái trống, không tự suy ra PG đã nghỉ. Khi cập nhật HR trở lại Đang làm và tải lại danh sách, cảnh báo HR tự hết.

Giữ nguyên lịch sử và lý do Trainer Thêm/Loại, nhãn Chờ duyệt và quyền Admin/Trainer. Nếu đồng thời có yêu cầu thêm và HR không Đang làm, ưu tiên tô đỏ cảnh báo, vẫn ghi đủ yêu cầu đang chờ và trạng thái HR. Excel tiến độ cùng màu đỏ và trạng thái như danh sách. Giữ cột Thâm niên và các chức năng có sẵn.

Đây là dấu cảnh báo hiển thị từ HR. Target đã chốt, danh sách đăng ký Master, tiến độ M1–M5, các nhóm bắt cặp và quyết định duyệt vẫn theo dữ liệu chính thức; không tự xóa PG, tạo yêu cầu thay Trainer, phê duyệt hoặc thay đổi mẫu số Target khi đọc trang. Muốn loại chính thức vẫn thực hiện quy trình Loại PGs/duyệt hiện có.

Chỉ thay HTML trên Test; không sửa backend, schema, Secrets, dữ liệu HR/Target/kết quả thật, KPI trigger hoặc ledger. Kiểm tra bằng dữ liệu giả lập ở 1440/390/320 px, bộ lọc/khôi phục trạng thái/quyền/lịch sử và tải Excel có màu. Không xuất dữ liệu người dùng thật qua công cụ. Dashboard chính chỉ được chuyển theo yêu cầu rõ của Nghĩa.
