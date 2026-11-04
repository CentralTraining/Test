Bản Test ngày 04/11/2026 — Nhân bản chiến dịch sang tháng khác.

Thao tác: Cài đặt → Chiến dịch → chọn Nhân bản → chọn tháng mới → giữ ô Giữ Target, cấu hình và danh sách đã cài đặt → Nhân bản.
Giữ tên, các Campaign/Program ID nguồn, ngưỡng X, A bài/PG, trạng thái chốt Target và các thiết lập hiện có.
Sao chép Target theo Trainer/khu vực, danh sách import riêng Test/AI; không lấy danh sách HR tháng đang mở thay cho nguồn.
Find Master: giữ danh sách PGs/shop, ngưỡng 5 mốc, kết quả tích lũy, cặp PGs và trạng thái duyệt đã lưu. Biên nhận duyệt cũ giữ nguyên; không tạo người duyệt/thời điểm duyệt mới.
HR tháng đích tiếp tục xác minh Off/đã loại/thiếu HR; nhóm không hợp lệ cảnh báo và không coi đạt.
Đổi nguồn OTraining sang Campaign ID khác không tiếp tục gộp mốc của nguồn cũ.
Các kết quả tháng thông thường (khảo sát/FTF/Truyền thông...) không sao chép thành kết quả tháng mới. Target trùng hạng mục nhưng khác số ở tháng đích bị chặn để giữ dữ liệu đã cài.
Các bản sao đã tạo từ trước không tự bị sửa; thao tác mới chỉ chạy khi Admin bấm Nhân bản.

Backend: campaign-clone-test v2, JWT gateway true + Dashboard Admin auth mới; RPC clone_campaign_test_v1 security invoker, chỉ service_role. Một transaction CAS cho campaigns/KV/private scopes/pairs. Test chỉ ghi environment=test; không sửa legacy/Main pair rows.
Kiểm thử fixture: PostgreSQL PGlite 0.3.14 (gồm rollback lỗi giữa chừng), crypto/session auth, scope/lock/stale/idempotency, tích lũy và Off, browser 1440/768/390/320. Không nhân bản chiến dịch thật khi kiểm thử.
Mã nguồn backend chỉ cung cấp riêng, không đăng ZIP xác thực lên repo công khai.
Main chưa triển khai tính năng này.
