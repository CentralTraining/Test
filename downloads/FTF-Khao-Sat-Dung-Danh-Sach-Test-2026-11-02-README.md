# FTF — Khảo sát theo danh sách check-in của chiến dịch — Test 02/11/2026

Tiến độ KPI → Đối tác → FTF → Cập nhật FTF từ hệ thống.

Khảo sát được lấy từ cùng snapshot download-all: danh sách allAttendees xác định người thuộc từng shop và surveyMap quyết định trạng thái đã/chưa khảo sát. Mỗi cặp shop_id + user_id chỉ tính một lần; cùng một người có mặt ở hai shop vẫn tính theo từng shop giống báo cáo xuất nguồn. Không dùng bộ đếm survey_count của luồng f2f-shops-v2 để tạo các dòng khảo sát HV 1, HV 2…

Trong cùng một lần cập nhật, tổng khảo sát, số liệu theo Trainer/khu vực/kênh, danh sách shop và chi tiết khảo sát dùng cùng tập người/trạng thái. Bấm ô Khảo sát để xem tên và trạng thái từ snapshot đã lưu; không gọi endpoint khác để tạo một số tổng khác. Nguồn thiếu map, trạng thái không nhận diện, shop/campaign/month không khớp hoặc trùng người sẽ dừng cập nhật và giữ dữ liệu đã lưu. Chi tiết có thể hiển thị trạng thái chưa xác định để người dùng kiểm tra; trạng thái đó không tự tính hoàn thành.

Giữ quy tắc Target khảo sát động theo HR Training hiện có, chỉ tiêu theo kênh Admin đã nhập, đếm HR/Test hiện có, trạng thái Tư vấn AI và các chức năng khác. File nhập thủ công vẫn dùng các dòng khảo sát thực trong file, có nhãn nguồn file. Quyền Admin/Trainer, kiểm tra tháng/chiến dịch và xác thực phiên Dashboard giữ nguyên.

Thay duy nhất function Test `otraining-ftf-ai-test` (index.ts/access.ts), verify_jwt=true. API AI cũ tương thích khi thiếu surveyMap; luồng cập nhật khảo sát mới yêu cầu surveySource=surveyMap và dữ liệu đầy đủ. Nguồn AI và khảo sát lấy trong cùng một yêu cầu upstream đã được xác thực; không thêm Secrets. Function chỉ đọc KV và upstream, không ghi dữ liệu. Chỉ thao tác cập nhật FTF chủ động từ giao diện mới lưu dữ liệu tháng/khu vực hiện có.

Chỉ xuất bản Test. Không sửa function hoặc HTML Main, không tự cập nhật dữ liệu thật, không sửa tháng khác, Target, nhóm, KPI automation hoặc Secrets. Khi chuyển Main theo yêu cầu rõ, triển khai đúng source adapter dưới tên otraining-ftf-ai trước khi chuyển HTML. Không chạy schema và không sao chép dữ liệu giữa môi trường.

Kiểm chứng bằng dữ liệu minh họa gồm auth/scope/campaign/transport, người trùng trong shop và cùng người ở hai shop, surveyMap độc lập với AI/Test, số tổng và chi tiết cùng snapshot, lỗi/thiếu/trạng thái lạ bảo toàn dữ liệu, Target Admin giữ nguyên, stale tháng/tài khoản và desktop/mobile. Full HTML và source ZIP không chứa dữ liệu thật hoặc Secrets.

Gói mã nguồn máy chủ được cung cấp riêng cho chủ tài khoản trong cuộc trò chuyện; không đăng source ZIP lên repository công khai. Trang tải công khai chỉ gồm HTML, tài liệu, manifest và kiểm chứng.
