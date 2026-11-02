# Find Master — Target tiến độ PGs còn hiệu lực — Test 02/11/2026

Tiến độ KPI → Nội bộ → PGs Master → Cá nhân → bảng tổng theo Khu vực hoặc Trainer.

Bảng tổng chỉ dùng PGs còn trong danh sách Master đã chốt và có trạng thái còn hiệu lực (Đang làm hoặc Trong danh sách). Dòng HR khác Đang làm, PG đã rời danh sách và mã có trong manualRemove đều không được tính. Lọc cùng một tập PG cho Target, số đạt từng mốc M1–M5, đủ 5 mốc và tổng Miền Trung/khu vực; không giữ số đạt của PG đã bị loại khỏi mẫu số.

Trong danh sách là nhãn hiện có khi PG còn đăng ký và không có cờ HR khác Đang làm. Bản ghi HR thiếu/trống vẫn giữ nhãn này, không tự gán Đã nghỉ hoặc Đang làm. Yêu cầu thêm chờ duyệt chưa được tính; yêu cầu loại đang chờ duyệt chưa thay đổi danh sách chính thức. Sau khi Admin duyệt loại thì PG không còn được tính. Chỉ tiêu ở bảng hiển thị thay đổi, không tự sửa dữ liệu Master, Target đã chốt, kết quả OTraining hoặc trạng thái duyệt/bắt cặp.

PG Off/đã loại vẫn giữ dòng và cảnh báo đỏ trong danh sách chi tiết để kiểm tra lịch sử và xuất Excel. Bộ lọc chi tiết, cột Thâm niên, quy trình gửi/duyệt và các chức năng khác giữ nguyên. Trainer chỉ xem các tổng trong khu vực được phân quyền; Admin xem toàn phạm vi. Kết quả đạt vẫn chỉ lấy cờ done của OTraining.

Thay đổi chỉ HTML trên CentralTraining/Test. Không đổi Edge Function, schema, Secrets hoặc dữ liệu thật; không cập nhật Dashboard chính. File HTML phiên bản là toàn bộ ứng dụng. Kiểm chứng dùng dữ liệu minh họa, kiểm tra tổng/số đạt/mẫu số theo khu vực và Trainer, pending/approved, HR thay đổi, Target bằng 0, phạm vi và bố cục desktop/mobile; không ghi dữ liệu thật.
