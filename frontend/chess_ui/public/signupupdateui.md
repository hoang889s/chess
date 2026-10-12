# Signup Page Enhancement Specification

## 1. Mục tiêu

Nâng cấp giao diện trang **Đăng ký** hiện tại thành một trang:

* Modern
* Professional
* Chess-inspired
* AI-themed
* Clean
* Responsive
* Có animation nhẹ
* UX rõ ràng
* Đồng bộ visual với Login page

Trang đăng ký phải tạo cảm giác đây là một:

> Modern Online Chess Platform powered by AI

Không biến giao diện thành gaming UI quá mạnh.

Không sử dụng quá nhiều hiệu ứng, gradient hoặc animation.

---

# 2. Nguyên tắc quan trọng

Chỉ nâng cấp:

* UI
* UX
* Visual design
* Accessibility
* Responsive
* Micro-interactions

Không thay đổi business logic hiện tại.

Không thay đổi:

* API `/api/auth/register`
* HTTP method `POST`
* `formData`
* Validation username
* Validation email
* Validation password
* Error handling
* `registerState`
* `googleState`
* Navigation
* Password visibility logic

Không thay đổi cấu trúc authentication backend.

---

# 3. Visual Identity

Login và Signup phải nhìn như cùng một hệ thống.

Signup sử dụng cùng color palette với Login.

```css
:root {
  --color-primary: #76ABAE;
  --color-dark: #303841;
  --color-darkest: #1F2933;
  --color-light: #F8F5EC;
  --color-white: #FFFFFF;
  --color-accent: #E04A14;
  --color-text: #111827;
  --color-error: #B91C1C;
}
```

---

# 4. Background

Background hiện tại:

```css
background: #76ABAE;
```

Có thể giữ màu này nhưng phải làm background có chiều sâu hơn.

Thêm:

* Chessboard pattern
* Grain nhẹ
* Decorative chess pieces
* Soft radial lighting

Background không được ảnh hưởng tới khả năng đọc form.

---

# 5. Chessboard Background

Tạo pattern bàn cờ rất nhẹ.

Ví dụ:

```css
.signup-page::before {
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

Có thể sử dụng implementation khác nếu visual tốt hơn.

Pattern phải nằm phía sau card.

---

# 6. Decorative Chess Pieces

Thêm các quân cờ trang trí:

```text
             ♞

     ♟                 ♜


             SIGN UP


     ♝                 ♟
```

Có thể sử dụng:

* ♟
* ♞
* ♜
* ♝
* ♛

Không sử dụng quá nhiều.

Các quân cờ phải:

```css
pointer-events: none;
```

Opacity thấp khoảng:

```css
opacity: 0.08 - 0.15;
```

---

# 7. Decorative Animation

Các quân cờ có thể chuyển động rất nhẹ.

Ví dụ:

```css
@keyframes chessFloat {
  0% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(-8px);
  }

  100% {
    transform: translateY(0);
  }
}
```

Animation:

```css
animation: chessFloat 5s ease-in-out infinite;
```

Không cho tất cả quân cờ chuyển động cùng lúc.

Có thể sử dụng:

```css
animation-delay
```

khác nhau cho từng quân.

---

# 8. Signup Card

Card hiện tại:

```css
background: #FF5722;
```

Nên thay bằng màu sáng trung tính để dễ đọc form.

Khuyến nghị:

```css
background: #F8F5EC;
```

hoặc:

```css
background: rgba(248, 245, 236, 0.97);
```

Card:

```css
width: min(400px, calc(100vw - 32px));
```

Border radius:

```css
border-radius: 16px;
```

Shadow:

```css
box-shadow:
  0 20px 50px rgba(31, 41, 51, 0.25);
```

Không sử dụng shadow quá đậm.

---

# 9. Card Entrance Animation

Khi Signup page xuất hiện:

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
@keyframes signupCardIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.signup-card {
  animation: signupCardIn 500ms ease-out;
}
```

---

# 10. Chess Brand

Thêm brand phía trên header.

Ví dụ:

```text
             ♞
       AI POWERED CHESS
```

React:

```jsx
<div className="signup-brand">

  <div className="signup-brand__icon">
    ♞
  </div>

  <span className="signup-brand__text">
    AI POWERED CHESS
  </span>

</div>
```

Icon có thể dùng Unicode hoặc SVG.

Ưu tiên SVG nếu cần thiết kế chính xác hơn.

---

# 11. Brand Icon

Icon:

```css
.signup-brand__icon {
  width: 52px;
  height: 52px;

  display: flex;
  align-items: center;
  justify-content: center;

  font-size: 36px;

  color: #303841;

  border: 1px solid rgba(48,56,65,0.2);

  border-radius: 50%;

  background: rgba(255,255,255,0.35);
}
```

Không cần glow quá mạnh.

---

# 12. Brand Text

```css
.signup-brand__text {
  margin-top: 8px;

  font-size: 11px;
  font-weight: 700;

  letter-spacing: 2px;

  color: #303841;
}
```

---

# 13. Header

Header hiện tại:

```text
Chào mừng trở lại !
Đăng ký
```

Nội dung này không phù hợp hoàn toàn với Signup.

Đổi thành:

```text
Tạo tài khoản
Tham gia bàn cờ
```

Hoặc:

```text
Chào mừng bạn!
Tạo tài khoản
```

Khuyến nghị:

```text
Chào mừng bạn!
Tạo tài khoản
```

Không sử dụng:

```text
Chào mừng trở lại!
```

cho trang đăng ký.

---

# 14. Header Typography

Welcome:

```css
.signup-welcome {
  margin: 0 0 4px;

  font-size: 15px;
  font-weight: 500;

  color: rgba(17,24,39,0.65);

  text-align: center;
}
```

Title:

```css
.signup-title {
  margin: 0;

  font-size: 28px;
  font-weight: 700;

  line-height: 1.2;

  color: #111827;

  text-align: center;
}
```

---

# 15. Back Button

Giữ chức năng:

```jsx
onClick={() => window.history.back()}
```

Nhưng cải thiện visual.

Kích thước:

```css
width: 36px;
height: 36px;
```

Border radius:

```css
border-radius: 50%;
```

Hover:

```css
.signup-back:hover {
  background: rgba(0,0,0,0.08);
  transform: translateX(-2px);
}
```

Icon:

```text
←
```

hoặc SVG hiện tại.

Không thay đổi logic.

---

# 16. Username Field

Hiện tại:

```text
Tên đăng nhập :
[ Nhập tên đăng nhập ]
```

Nâng cấp thành:

```text
Tên đăng nhập

┌──────────────────────────────┐
│ 👤  Nhập tên đăng nhập       │
└──────────────────────────────┘
```

Thêm user icon bằng SVG.

Không dùng icon library nếu không cần.

---

# 17. Username Input

```css
.form-input {
  min-height: 48px;

  padding: 12px 14px;

  border: 1px solid rgba(17,24,39,0.2);

  border-radius: 9px;

  background: #FFFFFF;
}
```

Focus:

```css
.form-input:focus {
  outline: none;

  border-color: #76ABAE;

  box-shadow:
    0 0 0 3px rgba(118,171,174,0.2);
}
```

Không sử dụng màu orange làm focus chính.

Accent orange chỉ dùng cho các trạng thái đặc biệt.

---

# 18. Password Field

Giữ tính năng:

```jsx
showPassword
```

Giữ:

```jsx
EyeIcon
EyeOffIcon
```

Nhưng cải thiện UI.

Layout:

```text
Mật khẩu

┌──────────────────────────────┐
│ 🔒  Nhập mật khẩu        👁  │
└──────────────────────────────┘
```

Password toggle:

```css
.password-toggle {
  width: 34px;
  height: 34px;

  border-radius: 50%;
}
```

Hover:

```css
.password-toggle:hover {
  background: rgba(118,171,174,0.12);
}
```

---

# 19. Password Strength Indicator

Đây là thành phần nên bổ sung.

Ngay bên dưới password input:

```text
Độ mạnh mật khẩu

████████░░  Tốt
```

Các trạng thái:

```text
Rất yếu
Yếu
Trung bình
Tốt
Mạnh
```

Có thể tính dựa trên:

* length
* uppercase
* lowercase
* number
* special character

Ví dụ:

```text
Mật khẩu: abc
→ Rất yếu

Mật khẩu: abcdefgh
→ Trung bình

Mật khẩu: Abcdef12
→ Tốt

Mật khẩu: Abcd@1234
→ Mạnh
```

Quan trọng:

Password strength indicator chỉ là UX.

Backend vẫn là nơi quyết định validation cuối cùng.

Không được thay đổi rule backend:

```text
password >= 8
```

---

# 20. Password Requirements

Thêm hint nhỏ:

```text
Mật khẩu tối thiểu 8 ký tự
```

Có thể hiển thị:

```text
✓ Ít nhất 8 ký tự
```

Nếu muốn nâng cao:

```text
✓ 8 ký tự
○ Chữ hoa
○ Chữ số
○ Ký tự đặc biệt
```

Nhưng không bắt buộc frontend phải enforce những rule mà backend chưa yêu cầu.

---

# 21. Email Field

Thêm icon email.

Layout:

```text
Email

┌──────────────────────────────┐
│ ✉  Nhập địa chỉ email       │
└──────────────────────────────┘
```

Input:

```jsx
type="email"
```

Giữ nguyên.

Không thay đổi validation:

```text
email không được rỗng
email phải đúng format
email tối đa 100 ký tự
```

---

# 22. Field Spacing

Khoảng cách giữa các field:

```css
.signup-form {
  gap: 18px;
}
```

Không nên để form quá thưa.

Signup có 3 field nên card cần compact hơn Login.

---

# 23. Error Message

Giữ:

```jsx
errors.username
errors.email
errors.password
```

Không thay đổi state structure.

Visual mới:

```text
⚠ Tên đăng nhập phải có từ 3-50 ký tự...
```

CSS:

```css
.form-error {
  display: flex;
  align-items: flex-start;
  gap: 6px;

  font-size: 13px;

  color: #B91C1C;

  line-height: 1.4;
}
```

Có thể thêm icon cảnh báo bằng SVG.

---

# 24. Error Input

Khi có lỗi:

```css
.form-input--error {
  border-color: #B91C1C;

  box-shadow:
    0 0 0 3px rgba(185,28,28,0.08);
}
```

Giữ animation shake hiện tại nhưng giảm độ mạnh.

Không shake liên tục.

Chỉ animate khi lỗi mới xuất hiện.

---

# 25. Register Button

Button hiện tại đã có kích thước tốt.

Giữ:

```css
width: 100%;
```

Tăng height:

```css
height: 48px;
```

Style:

```css
background: #303841;
color: #FFFFFF;
border-radius: 9px;
```

Hover:

```css
.register-button:hover:not(:disabled) {
  background: #3E4852;
  transform: translateY(-1px);
}
```

---

# 26. Loading State

Giữ:

```jsx
registerState === 'submitting'
```

Nhưng thay text:

```text
Đang đăng ký...
```

bằng UI:

```text
◌ Đang tạo tài khoản...
```

Nếu muốn dùng spinner:

```css
.signup-spinner {
  width: 18px;
  height: 18px;

  border: 2px solid rgba(255,255,255,0.35);
  border-top-color: #FFFFFF;

  border-radius: 50%;

  animation: spin 700ms linear infinite;
}
```

Không tạo spinner bằng thư viện ngoài.

---

# 27. OAuth Divider

Giữ:

```text
──────── Hoặc ────────
```

Nhưng làm nhẹ hơn.

```css
.oauth-divider::before,
.oauth-divider::after {
  background: rgba(17,24,39,0.15);
}
```

Text:

```css
.oauth-divider__text {
  font-size: 13px;
  color: rgba(17,24,39,0.55);
}
```

Không cần font-size 18px cho "Hoặc".

---

# 28. Google Button

Thay:

```text
Đăng ký bằng Google
```

bằng:

```text
Tiếp tục với Google
```

Lý do:

"Tiếp tục với Google" phù hợp hơn với authentication UI hiện đại.

Button:

```css
.google-button {
  width: 100%;
  height: 46px;

  background: #FFFFFF;

  color: #303841;

  border:
    1px solid rgba(17,24,39,0.15);

  border-radius: 9px;
}
```

Google icon:

```text
G
```

vẫn sử dụng SVG hiện tại.

Hover:

```css
.google-button:hover:not(:disabled) {
  background: #FAFAFA;

  transform: translateY(-1px);

  box-shadow:
    0 6px 16px rgba(31,41,51,0.12);
}
```

---

# 29. Google Loading State

Giữ:

```jsx
googleState === 'loading'
```

Nhưng hiển thị:

```text
Đang kết nối Google...
```

Không sử dụng:

```text
Đang xử lý...
```

vì thông báo mới cụ thể hơn.

---

# 30. Login Switch

Cuối card:

```text
Đã có tài khoản?
Đăng nhập
```

Thiết kế:

```text
Đã có tài khoản?  Đăng nhập →
```

`Đăng nhập` sử dụng màu:

```css
color: #1B425B;
```

Hover:

```css
color: #E04A14;
```

Không thay đổi:

```jsx
navigateTo('/login')
```

---

# 31. Terms / Privacy

Có thể thêm phía trên phần "Đã có tài khoản?":

```text
Bằng việc đăng ký, bạn đồng ý với
Điều khoản sử dụng và Chính sách bảo mật.
```

Thiết kế nhỏ:

```css
font-size: 11px;
color: rgba(17,24,39,0.55);
```

Các link:

```text
Điều khoản sử dụng
Chính sách bảo mật
```

Hiện tại chỉ là UI.

Không cần tạo route nếu chưa có.

Nếu project chưa có Terms/Privacy thì có thể để placeholder.

---

# 32. Success State

Hiện tại đăng ký thành công sẽ:

```jsx
navigateTo('/login')
```

Giữ nguyên behavior này.

Có thể thêm một hiệu ứng ngắn trước khi navigation:

```text
✓ Đăng ký thành công!
```

Nhưng không được trì hoãn navigation quá lâu.

Nếu không cần thiết thì giữ navigation trực tiếp.

---

# 33. Accessibility

Phải giữ:

* `label`
* `htmlFor`
* `aria-invalid`
* `aria-describedby`
* `role="alert"`
* `aria-label`
* `aria-busy`

Password toggle phải có:

```jsx
aria-label={
  showPassword
    ? 'Ẩn mật khẩu'
    : 'Hiện mật khẩu'
}
```

Back button:

```jsx
aria-label="Quay lại"
```

Google button:

```jsx
aria-label="Tiếp tục với Google"
```

---

# 34. Mobile

Mobile width:

```css
.signup-card {
  width: min(400px, calc(100vw - 32px));
}
```

Padding:

```css
padding: 22px;
```

Nếu màn hình thấp:

```css
.signup-page {
  min-height: 100dvh;
  overflow-y: auto;
}
```

Không sử dụng:

```css
overflow: hidden;
```

trên `.signup-page` nếu nó làm mất khả năng scroll.

Signup có nhiều field nên mobile scrolling phải hoạt động tốt.

---

# 35. Desktop

Desktop:

```text
Card width: 380–400px
```

Không nên để Signup card quá rộng.

Login có thể khoảng 380px.

Signup khoảng 400px vì có nhiều field.

---

# 36. Reduced Motion

Bắt buộc hỗ trợ:

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

# 37. Component Structure

Có thể giữ toàn bộ component trong:

```text
Signup.jsx
Signup.css
```

Không bắt buộc tạo component mới.

Logical structure:

```text
Signup
│
├── Background
│   ├── Chessboard
│   └── Decorative Chess Pieces
│
├── Signup Card
│
├── Back Button
│
├── Chess Brand
│
├── Header
│
├── Signup Form
│   ├── Username
│   ├── Password
│   │   ├── Password Toggle
│   │   ├── Strength Indicator
│   │   └── Requirements
│   │
│   ├── Email
│   ├── Error Messages
│   └── Register Button
│
├── OAuth Divider
│
├── Google Button
│
├── Terms
│
└── Login Switch
```

---

# 38. Không thêm dependency

Không cần cài:

```text
lucide-react
react-icons
framer-motion
```

nếu project hiện tại chưa sử dụng.

Các icon hiện tại đã có SVG.

Ưu tiên:

* SVG inline
* CSS
* React state hiện tại

---

# 39. Không thay đổi Backend Contract

Request hiện tại:

```json
{
  "username": "...",
  "email": "...",
  "password": "..."
}
```

Phải giữ nguyên.

Endpoint:

```text
POST /api/auth/register
```

Phải giữ nguyên.

Không thêm:

```text
confirmPassword
```

vào request backend nếu backend chưa hỗ trợ.

Nếu thêm confirm password thì chỉ dùng frontend để UX validation.

---

# 40. Validation hiện tại phải được giữ

Username:

```text
3–50 ký tự
a-z
A-Z
0-9
_
```

Regex hiện tại:

```js
/^[a-zA-Z0-9_]{3,50}$/
```

Password:

```text
>= 8 ký tự
```

Email:

```text
email format hợp lệ
<= 100 ký tự
```

Không được thay đổi các rule này trong quá trình redesign.

---

# 41. Error Mapping

Giữ logic hiện tại:

```jsx
getFieldFromError()
```

Không được làm mất khả năng:

```text
Username → username
Email → email
Password → password
```

Nếu backend trả lỗi tổng quát thì hiển thị ở khu vực submit/form-level.

---

# 42. Recommended Additional State

Có thể bổ sung:

```jsx
const [passwordStrength, setPasswordStrength] = useState(0)
```

hoặc tính trực tiếp từ:

```jsx
formData.password
```

Không cần state nếu có thể tính derived value.

Ví dụ:

```js
const getPasswordStrength = (password) => {
  let score = 0

  if (password.length >= 8) score++
  if (/[A-Z]/.test(password)) score++
  if (/[a-z]/.test(password)) score++
  if (/[0-9]/.test(password)) score++
  if (/[^A-Za-z0-9]/.test(password)) score++

  return score
}
```

Password strength chỉ dùng cho UI.

Không thay đổi backend requirement.

---

# 43. Final Visual Direction

Mục tiêu cuối cùng:

```text
                    ♞
              AI POWERED CHESS

       ┌───────────────────────────┐
       │ ←                         │
       │                           │
       │       Chào mừng bạn!      │
       │        Tạo tài khoản      │
       │                           │
       │  👤 Tên đăng nhập         │
       │  ┌─────────────────────┐  │
       │  │ Nhập tên đăng nhập  │  │
       │  └─────────────────────┘  │
       │                           │
       │  🔒 Mật khẩu          👁  │
       │  ┌─────────────────────┐  │
       │  │ •••••••••••••       │  │
       │  └─────────────────────┘  │
       │  Độ mạnh: ████████░░ Tốt  │
       │                           │
       │  ✉ Email                  │
       │  ┌─────────────────────┐  │
       │  │ Nhập email          │  │
       │  └─────────────────────┘  │
       │                           │
       │  ┌─────────────────────┐  │
       │  │      Đăng ký        │  │
       │  └─────────────────────┘  │
       │                           │
       │  ───────── Hoặc ────────  │
       │                           │
       │  ┌─────────────────────┐  │
       │  │ G  Tiếp tục Google  │  │
       │  └─────────────────────┘  │
       │                           │
       │  Bằng việc đăng ký...     │
       │                           │
       │  Đã có tài khoản?         │
       │       Đăng nhập →         │
       └───────────────────────────┘

             ♟             ♜
```

---

# 44. Quality Checklist

## Visual

* [ ] Background có chess identity
* [ ] Chess pieces trang trí nhẹ
* [ ] Chess logo
* [ ] AI Powered Chess branding
* [ ] Card hiện đại
* [ ] Typography rõ ràng
* [ ] Input đẹp
* [ ] Button đẹp
* [ ] Google button đẹp
* [ ] Error state đẹp
* [ ] Loading state đẹp

## UX

* [ ] Username validation
* [ ] Email validation
* [ ] Password validation
* [ ] Password visibility
* [ ] Password strength
* [ ] Error focus
* [ ] Loading state
* [ ] Google loading state
* [ ] Navigation
* [ ] Back button

## Responsive

* [ ] Desktop
* [ ] Tablet
* [ ] Mobile
* [ ] Small-height screen
* [ ] Không horizontal scroll
* [ ] Có thể scroll khi nội dung cao

## Accessibility

* [ ] Labels
* [ ] aria-invalid
* [ ] aria-describedby
* [ ] aria-label
* [ ] role="alert"
* [ ] aria-busy
* [ ] Keyboard navigation
* [ ] Focus state
* [ ] Reduced motion

## Code Safety

* [ ] Không thay đổi API
* [ ] Không thay đổi request body
* [ ] Không thay đổi validation backend
* [ ] Không thay đổi JWT
* [ ] Không thay đổi Google OAuth contract
* [ ] Không lưu password vào localStorage
* [ ] Không thêm dependency không cần thiết
