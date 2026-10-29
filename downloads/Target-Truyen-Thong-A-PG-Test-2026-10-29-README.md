# Target Truyền thông theo số bài/PG (A) — bản Test 29/10/2026

Mở https://centraltraining.github.io/Test/ → đăng nhập Admin → Cài đặt → Chiến dịch.

1. Tại dòng chiến dịch nhóm **Truyền thông**, loại **Nội bộ** hoặc **Đối tác**, bấm **Số bài/PG (A)**.
2. Nếu Target đang chốt, bấm **Sửa Target** trong cửa sổ.
3. Nhập A là số nguyên lớn hơn 0. Ví dụ A=2: Trainer phụ trách 50 PG OPPO Đang làm có Target 100 bài.
4. Kiểm tra bảng xem trước: Trainer, Khu vực, số PG đang làm, phép tính và Target; có tổng PG và tổng bài.
5. Bấm **Lưu Target**. Chỉ chiến dịch đó được cập nhật, cùng luồng dữ liệu mediaTargets hiện có nên các bảng KPI/Home đọc được Target mới.

Target được chốt theo nhân sự tại thời điểm lưu, không tự thay đổi ngầm. Khi nhân sự thay đổi, mở cùng nút và tính lại. A đã dùng hiển thị ngay trên nút của chiến dịch. Target nhập tay vẫn sửa được ở Cài đặt → Target; lưu nhập tay sẽ bỏ nhãn công thức A đã dùng trước đó.

## Quy tắc đếm

- Dùng Nhân sự của đúng tháng chiến dịch, dù tháng đang xem trên trang khác.
- Chỉ PG OPPO có trạng thái **Đang làm**, gán đúng Trainer trong cấu hình; không tính Thai sản, CODE ĐẠI LÝ, OFF hoặc thương hiệu khác.
- Mỗi Code PG tính một lần. Các dòng trùng giống hệt phân công/trạng thái được gộp; nếu cùng Code khác Trainer hoặc trạng thái thì dừng để kiểm tra dữ liệu trùng.
- PG thiếu Code dùng mã dòng đã lưu; nếu thiếu cả hai thì dừng, không tự sinh mã.
- PG đang làm chưa gán Trainer hợp lệ được cảnh báo và chưa đưa vào Target của Trainer nào. Trainer không có PG đủ điều kiện có Target 0.
- Hai loại Truyền thông đều dùng cùng công thức PG OPPO đang làm do Trainer care. Không lấy danh sách nhân viên đối tác thay cho nguồn PG này.

Tháng khóa chỉ xem, không lưu. Chưa có nhân sự đúng tháng, thiếu nguồn, lỗi đọc/lưu hoặc dữ liệu đổi trong khi xem trước đều báo rõ; không thay bằng Target 0 giả. Khi roster/Target vừa thay đổi, bảng xem trước được tải mới và cần kiểm tra trước khi bấm lưu lại. Đổi tháng hoặc tài khoản trong lúc kiểm tra lưu sẽ không ghi dữ liệu ở ngữ cảnh cũ.

## Thay đổi và kiểm thử

Chỉ thêm module model/UI/CSS trên Test, nút ở danh sách chiến dịch và xử lý Target truyền thông. Lưu theo công thức/nhập tay dùng một upsert gồm campaigns + mediaTargets:<campaignId>; cập nhật cache sau khi lưu thành công. Không ghi records hoặc danh sách PG trong luồng này. Giữ metadata chiến dịch và Target của các chiến dịch khác. Các giá trị Trainer đã lưu nhưng không còn trong cấu hình được giữ lại, chỉ Trainer trong cấu hình xuất hiện trong bảng tính.

Các trường bổ sung trên campaign là mediaTargetPostsPerPg, mediaTargetPgCounts, mediaTargetCalculatedAt; Target thực vẫn là bảng số theo Trainer trong mediaTargets:<campaignId>. Không thay Edge Function, schema, Secrets, TikTok, FindMaster, FTF hay KPI Ollie. Không tự chọn A hoặc cập nhật Target của chiến dịch thật trong quá trình triển khai.

Đã kiểm thử bằng dữ liệu giả lập: đếm PG đang làm/dedup/không gán/giới hạn số nguyên; cả hai loại chiến dịch độc lập; đúng tháng; khóa tháng/Target; lỗi đọc/lưu và nguồn thay đổi; quyền Admin; Target nhập tay; các bảng đọc Target snapshot. Trình duyệt ở 1440/390/320 px không tràn trang. Có kiểm tra riêng thay tháng/tài khoản khi chờ lưu.

HTML đầy đủ tải riêng: Dashboard-Test-2026-10-29-Target-Truyen-Thong-A-PG.html. Source ZIP chứa model.js, media-target-a.js, style.css, README và proof; không có Secrets/dữ liệu người dùng thật. Dashboard chính chưa cập nhật tính năng mới này.
