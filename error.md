+# Nguyên nhân và hướng dẫn khắc phục lỗi 404 trong dự án Chess (frontend + backend)
+
+> **Lưu ý:** File này chỉ cung cấp hướng Dẫn khắc phục **không sửa code**. Các bước dưới đây là các biện pháp bạn có thể áp dụng để tránh hoặc xử lý lỗi 404 khi hệ thống được vận hành.
+
+---
+
+## 1. Backend (Flask)
+
+### 1.1 Thêm các route API cần thiết
+- **Nguyên nhân:** Frontend có thể gọi các endpoint như `/api/game/rooms`, `/api/game/moves`, `/api/game/state`… mà hiện chưa tồn tại.
+- **Khắc phục:** 
+  - Định nghĩa blueprint mới (ví dụ: `game_bp`) với prefix `/api/game`.
+  -Trong mỗi blueprint, khai báo đầy đủ các route phù hợp với luỹ игры (tạo phòng, tham gia phòng, gửi nước đi, lấy trạng thái, ...).
+  - Đảm bảo mọi route đều có decorator `@jwt_required()` nếu cần xác thực, để tránh trả lời 401/403 thay vì 404.
+
+### 1.2 Đúng prefix `/api` trong mọi yêu cầu
+- **Nguyên nhân:** Một số endpoint được gọi thiếu prefix `/api` (ví dụ `/auth/login`).
+- **Khắc phục:** 
+  - Kiểm tra mọi nơi frontend thực hiện `fetch` hoặc `axios`; luôn bắt đầu bằng `/api` nếu mục tiêu là API backend.
+  - Nếu không chắc chắn, xem lại tài liệu API (hoặc file routes) để dùng prefix chuẩn.
+### 1.3 Sửa lỗi logic trong hàm `get_current_user`
+- **Nguyên nhân:** Sai chiamata `get_jwt_identity(user_id)` gây ra ngoại lệ → Flask trả về 500, nhưng có thể bị nhầm là 404 nếu không xem log.
+- **Khắc phục:** 
+  - Thay `user_id = get_jwt_identity(user_id)` bằng `user_id = get_jwt_identity()`.
+  - Bọc toàn bộ hàm trong `try/except` để trả về JSON lỗi rõ ràng thay vì để Flask sinh ra HTML lỗi mặc định.
+
+### 1.4 Kiểm tra decorator `@role_required`
+- **Nguyên nhân:** Decorator có thể trả về 404 thay vì 403 để “giấu” tồn tại route.
+- **Khắc phục:** 
+  - Đọc source của `utils.decorators.role_required` để chắc chắn mã trạng thái trả về.
+  - Nếu decorator trả về 404, điều chỉnh để trả về 403 (hoặc 401) và cung cấp thông điệp lỗi phù hợp.
+
+### 1.5 Phục vụ file tĩnh frontend từ backend (nếu cần deploy cùng origin)
+- **Nguyên nhân:** Backend không có route trả về `index.html` cho các đường dẫn frontend => truy cập `/`, `/game`... nhận 404.
+- **Khắc phục:** 
+  - Thêm một route “catch‑all” sau tất cả API routes: `@app.route('/', defaults={'path': ''})` và `@app.route('/<path:path>')` trả về `send_from_directory(app.static_folder, 'index.html')` nếu `path` không bắt đầu bằng `/api/`.
+  - Đặt `static_folder` trỏ tới thư mục `frontend/chess_ui/dist` sau khi build.
+
+---
+
+## 2. Frontend (React + Vite)
+
+### 2.1 Sử dụng thư viện định tuyến chuẩn (react-router-dom)
+- **Nguyên nhân:** Logic `App.jsx` so sánh `window.location.pathname` với chuỗi có chứa `/page/...` gây ra mismatch; navigation không đúng dẫn tới hiển thị component sai và việc gọi API có thể được thực hiện từ sai context.
+- **Khắc phục:** 
+  - Thay thế logic hand‑made bằng `<BrowserRouter>`, `<Routes>`, `<Route path="/login" element={<Login />} />` ….
+  - Đảm bảo `<Link>` hoặc `navigate` dùng để chuyển trang thay vì thay đổi `history` thủ công.
+
+### 2.2 Đúng đường dẫn API trong mọi lệnh `fetch`
+- **Nguyên nhân:** Các tính năng login, chơi game… hiện chỉ là `TODO`; khi thực hiện, dễ viết sai URL (thiếu `/api` hoặc sai endpoint).
+- **Khắc phục:** 
+  - Định nghĩa một hằng `API_BASE = '/api'` (hoặc lấy từ `import.meta.env.VITE_API_BASE` nếu sử dụng env).
+  - Mọi request đều dùng `${API_BASE}/auth/register`, `${API_BASE}/auth/login`….
+  - Khi gọi từ các component khác, import hằng này hoặc dùng một helper `api(url)`.
+
+### 2.3 Kiểm tra đường dẫn tài nguyên tĩnh (ảnh, font, CSS)
+- **Nguyên nhân:** Nếu cấu trúc thư mục thay đổi và đường dẫn trong JSX/CSS không được cập nhật, trình duyệt sẽ 404 khi cố tải tài nguyên.
+- **Khắc phục:** 
+  - Sử dụng phép import relativo (`import './Login.css'`) hoặc đường dẫn công khai từ folder `public` (`/logo.png`).
+  - Tránh hard‑code đường dẫn tuyệt đối dựa trên vị trí hiện tại nếu có thể di chuyển file.
+
+### 2.4 Đặt `base` đúng trong `vite.config.js` (nếu deploy dưới sub‑path)
+- **Nguyên nhân:** Khi build và phục vụ dưới đường dẫn như `/chess/` mà `base` vẫn là `/`, các đường dẫn assets sẽ bị thiếu prefix → 404.
+- **Khắc phục:** 
+  - Trong `vite.config.js`, đặt:
+    ```js
+    export default defineConfig({
+      base: process.env.BASE_URL || '/', // hoặc '/chess/' nếu biết sub‑path
+      plugins: [react()],
