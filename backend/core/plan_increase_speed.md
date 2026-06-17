Tối ưu hóa lõi của công cụ cờ vua
Kế hoạch này phác thảo việc tối ưu hóa quá trình tạo nước đi, biểu diễn bàn cờ và thuật toán tìm kiếm của công cụ cờ vua để giảm thời gian suy nghĩ/tìm kiếm của thuật toán Minimax từ khoảng 30 giây xuống dưới 1 giây.

Các thay đổi đề xuất
Thành phần cốt lõi
Chúng tôi sẽ tối ưu hóa gói cốt lõi bằng cách đưa ra các cải tiến có mục tiêu cho cấu trúc dữ liệu, trình tạo nước đi, phát hiện chiếu/tấn công và tra cứu hoán vị.

[SỬA ĐỔI]
constants.py
Chúng tôi sẽ thêm các bảng và từ điển được tính toán trước vào constants.py để tránh thao tác chuỗi và tra cứu từ điển tốn kém trong quá trình đánh giá và tìm kiếm.

Tính toán trước PIECE_SCORES: Một từ điển ánh xạ mỗi quân cờ (P, N, B, R, Q, K, p, n, b, r, q, k) đến một bảng 8x8 chứa giá trị vị trí được tính toán trước của nó (giá trị cơ bản + điểm thưởng bảng ô quân cờ).
Tính toán trước MVV_LVA_PRECOMPUTED: Một từ điển ánh xạ bất kỳ sự kết hợp nào của kẻ tấn công và nạn nhân đến điểm số MVV-LVA.

[SỬA ĐỔI]
board.py
Chúng ta sẽ sửa đổi lớp Board để theo dõi vị trí vua trong
O
( 1

) O(1) và ủy thác việc tạo nước đi/truy vấn tính hợp lệ được tối ưu hóa.

Thêm các thuộc tính self.white_king_pos và self.black_king_pos, được khởi tạo lần lượt là (7, 4) và (0, 4).

Cập nhật make_move(self, move) để cập nhật vị trí vua tương ứng khi vua di chuyển và ghi lại các vị trí vua trước đó trong ngăn xếp move_history.

Cập nhật undo_move(self) để khôi phục white_king_pos và black_king_pos từ ngăn xếp lịch sử.

Ủy thác has_legal_moves(self, color) cho trình tạo nước đi.

[SỬA ĐỔI]
move_generator.py
Chúng ta sẽ tối ưu hóa logic tạo nước đi và phát hiện tấn công:

Tối ưu hóa is_square_attacked(board, r, c, by_color):
Viết lại hàm này để dò tia/nhìn ra ngoài từ (r, c) thay vì quét tất cả 64 ô vuông và tạo ra các nước đi giả cho tất cả các quân cờ của đối phương.

Các phép tìm kiếm cần thực hiện:
Nước đi của Mã từ (r, c).

Các ô bắt quân Tốt liền kề.

Các ô Vua liền kề.

Dò tia trượt (thẳng và chéo) dừng lại ở quân cản đầu tiên.

Tối ưu hóa find_king(board, color):
Trả về board.white_king_pos hoặc board.black_king_pos trong O

( 1

) O(1).

Kiểm tra chiếu hết/hòa sớm:
Thực hiện has_legal_moves(board, color): lặp qua các quân cờ của người chơi và trả về True ngay khi tìm thấy nước đi hợp lệ đầu tiên. Triển khai hàm `is_checkmate(board, color)` dưới dạng `is_in_check(board, color)` và không phải `has_legal_moves(board, color)`.

Triển khai hàm `is_stalemate(board, color)` dưới dạng không phải `is_in_check(board, color)` và không phải `has_legal_moves(board, color)`.

Nước đi chỉ bắt quân cho Tìm kiếm Trạng thái Yên tĩnh:
Cập nhật tất cả các trình tạo nước đi (generate_pawn_moves, generate_knight_moves, v.v.) và hàm điều phối để chấp nhận cờ tùy chọn `captures_only: bool = False`.

Khi `captures_only=True`, bỏ qua việc thêm các nước đi không bắt quân (ví dụ: nước đi tiến của quân tốt, nước đi trống của quân mã/vua, nhập thành) để tránh phân bổ danh sách và kiểm tra các trạng thái không hợp lệ.

Từ điển Điều phối:
Sử dụng bảng ánh xạ `MOVE_GENERATORS` để thay thế nhiều nhánh `if/elif`.
[SỬA ĐỔI]
minimax.py
Chúng ta sẽ tích hợp các tối ưu hóa vào quá trình tìm kiếm:

Sử dụng PIECE_SCORES và MVV_LVA_PRECOMPUTED đã được tính toán trước thay vì tính toán động.

Cập nhật _check_terminal_nodes(board, current_color, maximizing):

Lưu vào bộ nhớ cache in_check = board.is_in_check(current_color).

Kiểm tra has_legal_moves(current_color). Nếu trả về False, hãy trả về điểm chiếu hết hoặc hòa dựa trên in_check.

Truyền captures_only=True để generate_all_pseudo_moves khi biên dịch các nước đi cho tìm kiếm trạng thái tĩnh.

Kế hoạch xác minh
Kiểm thử tự động
Chúng ta sẽ viết một tập lệnh kiểm thử và đánh giá hiệu năng benchmark_perf.py để:

Khẳng định rằng kết quả tìm kiếm (nước đi tốt nhất, điểm đánh giá) vẫn chính xác và giống hệt nhau sau khi tối ưu hóa.
Đo tốc độ tìm kiếm (số nút mỗi giây và thời gian suy nghĩ) ở độ sâu 1, 2, 3 và 4.
Xác minh rằng lệnh `python -m compileall core` biên dịch thành công.

Xác minh thủ công
Chúng tôi sẽ xác minh rằng thời gian tìm kiếm dưới 1 giây ở độ sâu 3 và 4, cho thấy tốc độ tăng hiệu suất hơn 30 lần.