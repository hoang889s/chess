# Login Page Enhancement Specification

## 1. Mục tiêu

Nâng cấp giao diện Login hiện tại thành một trang đăng nhập hiện đại, nổi bật và có nhận diện rõ ràng về chủ đề **Online Chess + AI**.

Không thay đổi kiến trúc React hiện tại và không thay đổi API authentication.

Ưu tiên:

* Modern Chess UI
* Clean
* Professional
* Responsive
* Có điểm nhấn thị giác
* Animation nhẹ
* UX rõ ràng
* Không gây rối mắt
* Không sử dụng quá nhiều hiệu ứng

---

# 2. Định hướng thiết kế

Trang Login nên tạo cảm giác:

> Modern Chess Platform + AI Technology

Phong cách:

* Dark / elegant
* Minimal
* Futuristic nhẹ
* Chess-inspired
* Professional

Không thiết kế theo phong cách gaming quá mạnh.

Không sử dụng quá nhiều gradient hoặc animation.

---

# 3. Color Palette

Giữ `#76ABAE` làm màu nền/accent chính hiện tại nhưng cải thiện cách sử dụng.

### Primary

```css
--color-primary: #76ABAE;
```

### Dark

```css
--color-dark: #303841;
```

### Darker

```css
--color-darkest: #1F2933;
```

### Light

```css
--color-light: #F8F5EC;
```

### White

```css
--color-white: #FFFFFF;
```

### Accent

```css
--color-accent: #E04A14;
```

### Text

```css
--color-text: #111827;
```

---

# 4. Background

Không sử dụng background màu phẳng hoàn toàn.

Giữ nền `#76ABAE` nhưng bổ sung:

## 4.1 Chessboard pattern

Tạo một pattern bàn cờ rất mờ.

Pattern phải:

* opacity thấp
* không gây mất tập trung
* nằm phía sau login card
* không ảnh hưởng đến click

Ví dụ:

```css
.login-page::before {
  content: "";
  position: absolute;
  inset: 0;

  background-image:
    linear-gradient(
      45deg,
      rgba(255,255,255,0.05) 25%,
      transparent 25%
    ),
    linear-gradient(
      -45deg,
      rgba(255,255,255,0.05) 25%,
      transparent 25%
    );

  background-size: 64px 64px;
  opacity: 0.5;

  pointer-events: none;
}
```

Có thể sử dụng giải pháp khác nếu tạo ra pattern đẹp hơn.

---

# 5. Decorative Chess Pieces

Thêm một số quân cờ trang trí ở background.

Ví dụ:

* ♟
* ♞
* ♜
* ♝

Các quân cờ phải:

* opacity thấp
* không che login card
* pointer-events: none
* animation rất nhẹ

Ví dụ:

```text
              ♞

      ♟                 ♜


                LOGIN CARD


          ♝                 ♟
```

Không để quân cờ quá lớn.

Không để animation gây khó chịu.

---

# 6. Login Card

Login card hiện tại có màu cam `#FF5722`.

Thay đổi thành giao diện hiện đại hơn.

Khuyến nghị:

```css
background: #F8F5EC;
```

hoặc:

```css
background: rgba(248, 245, 236, 0.96);
```

Card nên có:

* border nhẹ
* border-radius khoảng 14–18px
* shadow mềm
* không sử dụng shadow quá nặng

Ví dụ:

```css
box-shadow:
  0 20px 50px rgba(31, 41, 51, 0.25);
```

---

# 7. Chess Logo

Thêm một khu vực logo phía trên title.

Ví dụ:

```text
              ♞
       AI POWERED CHESS
```

HTML/React:

```jsx
<div className="login-brand">
  <div className="login-brand__icon">
    ♞
  </div>

  <span className="login-brand__text">
    AI POWERED CHESS
  </span>
</div>
```

Icon quân cờ có thể sử dụng Unicode hoặc SVG.

Nếu sử dụng SVG thì ưu tiên SVG đơn giản.

---

# 8. Logo Animation

Khi page load:

* icon fade in
* translateY khoảng 8px → 0
* duration khoảng 400–500ms

Không sử dụng animation lặp liên tục quá mạnh.

Ví dụ:

```css
@keyframes chessLogoIn {
  from {
    opacity: 0;
    transform: translateY(8px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

---

# 9. Header

Header hiện tại:

```text
Chào mừng trở lại !
Đăng nhập
```

Giữ nội dung này.

Nhưng cải thiện typography.

Khuyến nghị:

```text
Chào mừng trở lại!
Đăng nhập
```

Không có khoảng trắng trước dấu `!`.

Title:

```css
font-size: 28px;
font-weight: 700;
```

Subtitle:

```css
font-size: 15px;
opacity: 0.7;
```

---

# 10. Username Input

Bổ sung icon user.

Layout:

```text
Tên đăng nhập

┌────────────────────────────┐
│ 👤  Nhập tên đăng nhập... │
└────────────────────────────┘
```

Icon không được làm input quá chật.

Có thể sử dụng SVG inline.

Input:

```css
height: 48px;
border-radius: 8px;
```

Focus:

```css
border-color: #76ABAE;

box-shadow:
  0 0 0 3px rgba(118, 171, 174, 0.2);
```

---

# 11. Password Input

Bổ sung:

* lock icon
* show/hide password button

Layout:

```text
Mật khẩu

┌────────────────────────────┐
│ 🔒  •••••••••••••••     👁 │
└────────────────────────────┘
```

React cần thêm state:

```jsx
const [showPassword, setShowPassword] = useState(false)
```

Input:

```jsx
type={showPassword ? "text" : "password"}
```

Button:

```jsx
<button
  type="button"
  onClick={() => setShowPassword(!showPassword)}
  aria-label={
    showPassword
      ? "Ẩn mật khẩu"
      : "Hiển thị mật khẩu"
  }
>
```

Không submit form khi click button này.

---

# 12. Remember Me

Thêm khu vực:

```text
☐ Ghi nhớ đăng nhập                 Quên mật khẩu?
```

HTML:

```jsx
<div className="login-options">

  <label className="remember-me">
    <input
      type="checkbox"
      name="remember"
    />

    <span>Ghi nhớ đăng nhập</span>
  </label>

  <button
    type="button"
    className="forgot-password"
  >
    Quên mật khẩu?
  </button>

</div>
```

Hiện tại `forgot-password` chỉ là UI.

Chưa cần implement API reset password.

---

# 13. Login Button

Nút hiện tại quá nhỏ:

```css
width: 100px;
height: 30px;
```

Thay đổi thành:

```css
width: 100%;
height: 48px;
```

Ví dụ:

```text
┌──────────────────────────────┐
│          Đăng nhập           │
└──────────────────────────────┘
```

Button nên sử dụng:

```css
background: #303841;
color: #FFFFFF;
border-radius: 8px;
```

Hover:

```css
transform: translateY(-1px);
```

Không sử dụng transform quá mạnh.

---

# 14. Loading State

Chuẩn bị UI cho API login.

Thêm state:

```jsx
const [loading, setLoading] = useState(false)
```

Khi submit:

```text
┌──────────────────────────────┐
│          Đang đăng nhập...   │
└──────────────────────────────┘
```

Button phải disabled trong lúc request.

Không cho user click nhiều lần.

---

# 15. Error Message

Thêm khu vực hiển thị lỗi.

Ví dụ:

```text
⚠ Tên đăng nhập hoặc mật khẩu không chính xác
```

React:

```jsx
const [error, setError] = useState('')
```

Hiển thị:

```jsx
{error && (
  <div className="login-error" role="alert">
    {error}
  </div>
)}
```

CSS:

```css
.login-error {
  padding: 10px 12px;
  border-radius: 8px;
  font-size: 14px;
  background: rgba(220, 38, 38, 0.08);
  color: #B91C1C;
}
```

Không để error làm layout nhảy quá mạnh.

---

# 16. Google Login

Giữ Google Login.

Thay đổi button thành:

```text
      G     Tiếp tục với Google
```

Không dùng:

```text
Đăng ký bằng Google
```

vì đây là Login page.

Text:

```text
Tiếp tục với Google
```

Button nên có:

* white background
* dark text
* border
* Google logo thật
* hover nhẹ

Ví dụ:

```css
.google-login-button {
  width: 100%;
  height: 46px;

  background: #FFFFFF;
  color: #303841;

  border: 1px solid rgba(0,0,0,0.15);
  border-radius: 8px;
}
```

---

# 17. Divider

Thay:

```text
Hoặc
```

thành:

```text
────────── Hoặc ──────────
```

CSS:

```css
.login-or {
  display: flex;
  align-items: center;
  gap: 12px;
}

.login-or::before,
.login-or::after {
  content: "";
  flex: 1;
  height: 1px;
  background: rgba(0,0,0,0.15);
}
```

---

# 18. Register Section

Giữ:

```text
Chưa có tài khoản? Đăng ký
```

Nhưng làm `Đăng ký` nổi bật hơn.

Ví dụ:

```css
.login-switch__link {
  color: #1B425B;
  font-weight: 700;
}
```

Hover:

```css
.login-switch__link:hover {
  color: #E04A14;
}
```

---

# 19. Back Button

Giữ nút Back hiện tại.

Nhưng thêm background hover dạng circle:

```css
.login-back {
  width: 36px;
  height: 36px;
  border-radius: 50%;
}
```

Hover:

```css
.login-back:hover {
  background: rgba(0,0,0,0.08);
}
```

---

# 20. Page Entrance Animation

Khi Login page xuất hiện:

Card:

```text
opacity: 0 → 1
translateY: 20px → 0
```

Duration:

```text
450–550ms
```

Ví dụ:

```css
@keyframes loginCardIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.login-card {
  animation: loginCardIn 500ms ease-out;
}
```

Không sử dụng animation liên tục.

---

# 21. Accessibility

Phải giữ:

* label cho input
* `htmlFor`
* `aria-label`
* `aria-hidden`
* keyboard navigation
* focus state
* button type rõ ràng

Password visibility button phải có `aria-label`.

Error message dùng:

```html
role="alert"
```

---

# 22. Responsive

Desktop:

```text
Login card khoảng 380–420px
```

Mobile:

```text
width: calc(100vw - 32px)
```

Không để horizontal scrolling.

Card không được vượt quá viewport height.

Nếu màn hình quá thấp:

```css
.login-page {
  overflow-y: auto;
}
```

Không nên dùng:

```css
overflow: hidden;
```

trên toàn bộ page nếu điều đó khiến mobile không thể scroll.

---

# 23. Reduced Motion

Hỗ trợ người dùng không muốn animation.

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

# 24. Không được thay đổi

Không thay đổi:

* API endpoint
* authentication logic
* routing architecture
* JWT logic
* Google OAuth implementation hiện tại
* database logic

Nếu API chưa được implement thì chỉ chuẩn bị UI/state.

Không hard-code access token.

Không lưu password vào localStorage.

---

# 25. Component Structure đề xuất

Có thể giữ một file `Login.jsx`, nhưng JSX nên được tổ chức theo:

```text
Login
│
├── Back Button
│
├── Brand
│   ├── Chess Icon
│   └── AI Powered Chess
│
├── Header
│   ├── Welcome
│   └── Title
│
├── Login Form
│   ├── Username
│   ├── Password
│   ├── Login Options
│   └── Login Button
│
├── Divider
│
├── Google Login
│
└── Register Link
```

Nếu project lớn hơn sau này có thể tách thành:

```text
components/
├── AuthInput.jsx
├── PasswordInput.jsx
├── GoogleLoginButton.jsx
└── ChessBrand.jsx
```

Nhưng hiện tại **không bắt buộc tách component**.

---

# 26. Files cần chỉnh sửa

Ưu tiên chỉnh:

```text
Login.jsx
Login.css
```

Không tạo thêm dependency nếu không cần.

Không cài thêm icon library chỉ để tạo vài icon đơn giản.

Ưu tiên:

* SVG inline
* CSS
* Unicode chess pieces nếu phù hợp

---

# 27. Kết quả mong muốn

Sau khi hoàn thành, Login page phải có cảm giác:

```text
        ♞
  AI POWERED CHESS

┌───────────────────────────┐
│ ←                         │
│                           │
│   Chào mừng trở lại!      │
│       Đăng nhập           │
│                           │
│ 👤 Tên đăng nhập          │
│ ┌───────────────────────┐ │
│ │ Nhập tên đăng nhập... │ │
│ └───────────────────────┘ │
│                           │
│ 🔒 Mật khẩu           👁  │
│ ┌───────────────────────┐ │
│ │ •••••••••••••••       │ │
│ └───────────────────────┘ │
│                           │
│ ☑ Ghi nhớ   Quên mật khẩu │
│                           │
│ ┌───────────────────────┐ │
│ │       Đăng nhập       │ │
│ └───────────────────────┘ │
│                           │
│ ───────── Hoặc ─────────  │
│                           │
│ ┌───────────────────────┐ │
│ │  G  Tiếp tục với      │ │
│ │     Google             │ │
│ └───────────────────────┘ │
│                           │
│ Chưa có tài khoản?        │
│          Đăng ký          │
└───────────────────────────┘

       ♟           ♜
```

Overall design phải **sạch, hiện đại, có chất chess/AI nhưng không biến thành gaming UI**.

---

# 28. Quality Checklist

Trước khi hoàn thành cần kiểm tra:

* [ ] Login card responsive
* [ ] Không horizontal scroll
* [ ] Chess background không gây rối
* [ ] Logo hiển thị đúng
* [ ] Username icon
* [ ] Password icon
* [ ] Show/hide password
* [ ] Remember me
* [ ] Forgot password UI
* [ ] Login loading state
* [ ] Login error state
* [ ] Google login button
* [ ] Divider
* [ ] Register link
* [ ] Back button
* [ ] Hover states
* [ ] Focus states
* [ ] Keyboard navigation
* [ ] Accessibility labels
* [ ] Reduced motion
* [ ] Mobile layout
* [ ] Desktop layout
* [ ] Không thay đổi authentication API
* [ ] Không thêm dependency không cần thiết

# 29. Important

Không chỉ làm cho giao diện "đẹp hơn" bằng cách tăng màu sắc hoặc thêm animation.

Mục tiêu chính là tạo **visual identity cho một nền tảng cờ vua trực tuyến tích hợp AI**.

Thiết kế phải khiến người dùng nhìn vào Login page và ngay lập tức cảm nhận được:

> Chess + AI + Modern Web Application
