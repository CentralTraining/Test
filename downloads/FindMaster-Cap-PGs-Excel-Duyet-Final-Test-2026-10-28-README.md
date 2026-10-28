# Find Master — Cặp PGs, xuất Excel và Admin duyệt final

Phiên bản **Test · 28/10/2026**. Mở https://centraltraining.github.io/Test/ → Tiến độ KPI → Nội bộ → PGs Master → Bắt cặp thi đua.

## Trainer

1. Chọn đúng tháng/chiến dịch. Bấm **Tạo nhóm**, chọn 2 PG mình phụ trách; danh sách lẻ được có một nhóm 3.
2. Bấm **Lưu nhóm nháp**. Lặp lại đến khi tất cả PG của Trainer đều có nhóm. Tên nhóm tự ghép từ tên thành viên.
3. Tại **Danh sách cặp của tôi**, bấm **Lưu & gửi Admin duyệt** và xác nhận. Mỗi lần gửi là toàn bộ danh sách cặp của Trainer trong chiến dịch.
4. Trạng thái chuyển thành **Chờ Admin duyệt**; Trainer chưa thể sửa hoặc xóa nhóm trong lúc chờ.
5. Sau khi Admin duyệt final, danh sách tiếp tục khóa chỉnh sửa. Nếu Admin trả lại, đọc lý do, sửa nhóm, lưu nháp rồi gửi lại.

Một PG chỉ nằm trong một nhóm, cùng Trainer. Chỉ cho gửi khi ghép đủ toàn bộ roster đã chốt và các nhóm hợp lệ. Không tự bỏ PG để gửi thiếu danh sách.

## Admin

1. Mở **Admin duyệt final** trong khung Bắt cặp. Có số danh sách đang chờ.
2. Kiểm tra đúng Trainer, số cặp/PG, mở dấu + để xem đủ thành viên; có thể xuất Excel đối chiếu.
3. Bấm **Duyệt final** và xác nhận; hoặc bấm **Trả lại chỉnh sửa**, nhập lý do tối đa 500 ký tự.
4. Admin cũng có thể trả lại một danh sách đã duyệt để Trainer chỉnh sửa. Không sửa thầm danh sách đang chờ/đã chốt.

Nếu roster Master thay đổi sau khi gửi, trạng thái hiện **Danh sách PG đã thay đổi**; không tự coi là duyệt final. Admin trả lại để ghép/gửi lại. Cập nhật kết quả M1–M5 đơn thuần không làm mất duyệt final.

## Xuất Excel

Bấm **Xuất Excel** ở đầu khung. Xuất tất cả cặp khớp bộ lọc hiện tại, không chỉ trang đang mở. Nếu lọc kênh và một cặp có nhiều kênh, vẫn xuất đủ thành viên của cặp đó.

Mỗi PG một dòng; cột theo thứ tự:

`STT | Code PG | Mã NV | Họ tên PG | Mã shop | Tên shop | Khu vực | Tỉnh/TP | Kênh | Trainer | Trạng thái duyệt | Tên cặp`

**Tên cặp luôn ở cột cuối.** Code PG/Mã NV/Mã shop được ghi dạng chữ để giữ số 0 đầu. Dữ liệu Dashboard hiện dùng Code để đối chiếu Mã NV; nếu chưa có employeeCode riêng thì hai cột cùng mã gốc. Không tự tạo ID shop hoặc thông tin nhân sự thiếu.

Chọn **Trạng thái → Đã duyệt final** để lấy danh sách chính thức. Các trạng thái nháp, chờ duyệt, trả lại được ghi rõ trong file nếu xuất chúng. Trainer chỉ xuất phạm vi khu vực được cấp quyền; Admin toàn bộ.

## Triển khai và dữ liệu

- Function Test `pgsm-pairs-test` v2, verify_jwt=true và bắt buộc phiên Dashboard được kiểm tra lại phía máy chủ.
- Bảng mới `pgsm_pair_workflows`: RLS bật, anon/authenticated không có quyền trực tiếp; chỉ service_role. Thông báo advisor INFO không có policy là chủ ý cho bảng chỉ backend truy cập.
- Test chỉ ghi namespace `environment=test`. Bản chính và `pgsm_pair_groups` cũ chỉ được đọc làm nguồn ban đầu, không bị sửa/xóa. Không tự duyệt các cặp đã lưu trước đây.
- Chưa có workflow row thì giữ nguyên cặp cũ dưới trạng thái Nháp; lần lưu/gửi đầu tạo bản riêng của Test. Xem dữ liệu không tự tạo bản ghi.
- Mỗi thao tác đổi nhóm, gửi, duyệt/trả lại dùng version + sourceRevision + rosterRevision, kiểm tra quyền/tháng/roster lại trước khi ghi. Một bản ghi chứa cả nhóm và trạng thái để không có hai lần commit rời.
- Không sửa Target, kết quả thi, phân công nhân sự, TikTok, Secrets, Main HTML/function, KPI hoặc sổ gửi.
- Bản HTML đầy đủ để lưu/khôi phục lên đúng GitHub Pages; không phải bản cài độc lập. `schema.sql` đã áp dụng trên dự án hiện tại, không chạy lại trên bảng đang tồn tại.
- Khi có yêu cầu riêng đưa Main: triển khai `pgsm-pairs` với hằng ENVIRONMENT='main' trước HTML; giữ nguồn nhóm live cũ, không tự chuyển trạng thái duyệt thử nghiệm sang chính.

ZIP gồm đủ ba file function, schema, cấu hình, UI và kết quả kiểm thử. Không kèm khóa hay dữ liệu nhân sự thật. Kiểm thử sử dụng dữ liệu giả lập; không tự gửi/duyệt bất kỳ danh sách thật nào.
