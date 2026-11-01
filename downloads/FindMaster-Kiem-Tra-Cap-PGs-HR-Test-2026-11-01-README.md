# Find Master — Kiểm tra thành viên bắt cặp — Test 01/11/2026

Vào Tiến độ KPI → Nội bộ → Find Master → Bắt cặp thi đua.

- PG đã loại khỏi danh sách Master, có cờ manualRemove, hoặc HR khác Đang làm sẽ không được chọn để ghép mới. Thành viên không hợp lệ và cặp cũ có thành viên đó hiện đỏ, kèm mã PG và lý do.
- Mở Sửa để bỏ chọn thành viên lỗi, rồi ghép lại. Thành viên cũ bị loại không còn trong roster vẫn được hiển thị trong trình sửa để có thể bỏ chọn. Có thể xóa nhóm nháp cũ rồi ghép lại. Nhóm đang chờ/đã duyệt cần Admin Trả lại chỉnh sửa trước, đúng quy trình hiện có.
- Lưu nhóm, gửi duyệt và duyệt final đều kiểm tra tại máy chủ với dữ liệu mới; thay HR sau khi mở trình sửa hoặc sau khi gửi sẽ chặn thao tác khi danh sách không còn hợp lệ. Có thể Tải lại để xem lý do mới nhất.
- Quy tắc nhóm 2 hoặc một nhóm 3 khi lẻ tính theo số PG **hợp lệ** của Trainer. PG bị loại/HR không hợp lệ không buộc phải được ghép để gửi. Cặp cũ chứa thành viên lỗi chưa được tính đạt các mốc, dù từng người đã có kết quả cá nhân.

HR lấy từ DATA OPPO của đúng tháng chiến dịch và đối chiếu Code (giữ mã gốc trong cặp/Excel, chuẩn hóa định dạng mã khi tra HR). Chưa có DATA HR, PG vắng HR, trạng thái HR trống hoặc trùng mã có trạng thái mâu thuẫn sẽ báo chưa xác minh được điều kiện và chặn lưu/gửi/duyệt; không tự gán Đã nghỉ. Chuẩn hóa chữ hoa/thường, dấu và khoảng trắng của Đang làm.

Giữ Target và danh sách Master đã chốt, kết quả M1–M5 cá nhân, lý do/luồng duyệt, cột Thâm niên và cảnh báo HR ở bảng cá nhân, xuất Excel, quyền khu vực và chỉ sửa cặp của chính Trainer. Chỉ tiêu PG hợp lệ dùng cho bắt cặp, không tự đổi mẫu số Target cá nhân. Cặp đã duyệt trước đây và HR vẫn hợp lệ giữ nguyên trạng thái; digest tương thích phiên bản v2. HR không còn hợp lệ làm trạng thái hiển thị stale và yêu cầu trả lại để ghép lại, không tự sửa/xóa/phê duyệt bản ghi đã lưu.

Function thay duy nhất `pgsm-pairs-test` v3, verify_jwt=true; mã đầy đủ gồm index.ts/access.ts/model.js. Namespace ghi literal `test`; chỉ đọc nguồn legacy pgsm_pair_groups và KV, chỉ ghi bảng workflow bằng thao tác người dùng đã xác thực. Không chạy schema, không sửa Secrets, không tự migrate hoặc tạo nhóm thật. Main `pgsm-pairs` v2 và giao diện chính giữ nguyên.

Kiểm thử bằng fixture gồm regression backend, HR/removal/đổi trạng thái giữa thao tác, luồng lưu/gửi/final/trả lại, v2 approval compatibility, namespace isolation, browser 1440/768/390/320 px, sửa/bỏ chọn thành viên mất khỏi roster, export XLSX và kiểm tra quyền. Live chỉ probe phiên thiếu/giả trả 401, không đọc hoặc sửa nhóm thật. Full HTML tải riêng; ZIP gồm source function, UI/CSS và hướng dẫn, không kèm Secrets hoặc dữ liệu người dùng.

Khi Nghĩa yêu cầu chuyển chính, triển khai đúng source v3 dưới tên `pgsm-pairs` với ENVIRONMENT='main' trước HTML. Không chạy lại schema, không mang workflow Test sang Main, không thay function TikTok/callback hoặc các nguồn khác.
