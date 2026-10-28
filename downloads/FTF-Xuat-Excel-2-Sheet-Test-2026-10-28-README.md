# Xuất Excel FTF Đối tác — bản Test 28/10/2026

Đã thêm nút **⇩ Xuất Excel (2 sheet)** ở góc trái phía trên danh sách shop Đối tác → FTF.

## Thao tác

1. Mở https://centraltraining.github.io/Test/ và đăng nhập Dashboard.
2. Chọn tháng và vào Tiến độ KPI → Đối tác → FTF, kéo đến danh sách shop.
3. Chọn Trainer, kênh, trạng thái training và Chưa đủ (Test/KS) nếu cần.
4. Bấm **Xuất Excel (2 sheet)**. Xác thực lại bằng mật khẩu Dashboard khi được yêu cầu.
5. Tải file `BaoCao_FTF_<ID chiến dịch>_<tháng>.xlsx`.

Xuất toàn bộ shop khớp bộ lọc, bao gồm các trang chưa mở. Trainer chỉ xuất shop của chính Trainer được phân công trong Target FTF; Admin xuất các shop trong phạm vi đang xem.

## Hai sheet

- `Tong Hop F2F`: Mã Shop, Tên Shop, Kênh, Vùng, Khu vực, Tỉnh/Thành, Quận/Huyện, Ngày, Giờ, Người Train, SĐT Người Train, Sale QL, SL Dự Kiến, Số Đã Train, Trạng Thái.
- `Chi Tiet Check-in`: Chiến dịch, Mã Shop, Kênh, Vùng, Khu vực, Tỉnh, Shop, Sale Quản lý, Người Train, Tên học viên, Trạng thái tư vấn mẫu, Test online, Khảo sát, Điểm Hài lòng.

Hai sheet lấy từ cùng một phản hồi nguồn FTF của chiến dịch đã cấu hình. Người Train là người thực hiện tại nguồn FTF, có thể khác Trainer phụ trách shop. Học viên lấy từ check-in thực tế; không xuất các dòng đếm tổng hợp “HV 1…” của bộ import cũ. Trùng cùng shop/học viên được gộp; một người check-in ở hai shop vẫn có hai dòng tương ứng.

AI dùng riêng simulationStatusMap: dat=Đạt, chua_dat=Chưa đạt; không dùng kết quả test làm AI. Test là Pass/Fail/Chưa làm, khảo sát là Done/Chưa. Giá trị trạng thái lạ ghi Chưa xác định. Điểm hài lòng không có sẽ để trống, không tự điền 5. Mã shop và điện thoại giữ dạng text, số lượng và điểm là number. Ngày/giờ theo Việt Nam; shop Done dùng thời điểm cập nhật, shop còn lại dùng lịch kế hoạch như báo cáo gốc.

Nguồn thiếu map, shop/chiến dịch không khớp, quyền thay đổi hoặc kết nối lỗi sẽ báo rõ và không tạo file thiếu. Nếu Admin thay ID chiến dịch, cần cập nhật FTF để danh sách shop khớp nguồn mới trước khi xuất. Đổi tháng/bộ lọc trong lúc đang xuất sẽ hủy kết quả cũ.

## Mã nguồn

- HTML đầy đủ: `Dashboard-Test-2026-10-28-FTF-Xuat-Excel-2-Sheet.html` (tải riêng).
- `ftf-export.js`: module giao diện được nhúng trong HTML đầy đủ.
- `supabase/functions/otraining-ftf-export-test/index.ts`, `access.ts`, `model.js`: toàn bộ source adapter mới và phụ thuộc.
- `supabase/config.toml`: verify_jwt=true.
- Không kèm Secrets hoặc dữ liệu người dùng thực. Các fixture/Excel kiểm thử là dữ liệu giả lập.

Adapter bắt buộc phiên Dashboard đã ký, đọc lại quyền và phân công trước/sau khi đọc nguồn. Nó dùng cấu hình OTRAINING_USER_INFO đã có trên server, không nhận danh tính Leader từ trình duyệt, không trả credential. Không thay Secrets, schema, Target, dữ liệu FTF, callback TikTok, các Edge Function cũ hoặc KPI.

Chỉ bản Test gọi `otraining-ftf-export-test` v1. **Chưa chuyển tính năng này sang Dashboard chính.** Khi được yêu cầu chuyển chính, cần triển khai adapter tương ứng tên `otraining-ftf-export` trước HTML và giữ các thay đổi Main riêng. Nếu lấy toàn bộ HTML Test hiện tại, phải xử lý đúng cả luồng duyệt cặp FindMaster v2 của Test trước khi chuyển, không tự mang trạng thái duyệt Test sang Main.

## Kiểm thử

Handler và trình duyệt dùng dữ liệu giả lập, xuất XLSX thực rồi đọc lại ở 1440/390/320 px: đúng 2 sheet/15 và 14 cột, đầy đủ nhiều trang và các bộ lọc, phạm vi Trainer, mã/điện thoại giữ số 0, số lượng/điểm dạng number, tên giống công thức được lưu text, thiếu điểm để trống, lỗi/đổi tháng không tải file. Các thao tác xuất không ghi dữ liệu.

Adapter triển khai được đối chiếu source chính xác. Kiểm tra trực tiếp endpoint chỉ với phiên Dashboard thiếu/giả đều trả 401 và không trả bản ghi. Không thực hiện xuất dữ liệu riêng bằng tài khoản Trainer/Admin thật trong kiểm thử tự động.
