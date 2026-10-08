# Login Page — Design Specification

## 1. Tổng quan

Thiết kế trang **Đăng nhập** cho hệ thống trò chơi cờ vua trực tuyến.

Mục tiêu:

* Tạo giao diện đăng nhập đơn giản, rõ ràng.
* Giữ đúng màu sắc, kích thước, typography và bố cục từ thiết kế gốc.
* Có đăng nhập bằng tài khoản thông thường.
* Có tùy chọn đăng nhập bằng Google.
* Có nút quay lại.
* Giao diện phải được triển khai theo hướng responsive thay vì giữ nguyên tọa độ absolute của file export.

> Đây là specification cho frontend. Không sao chép nguyên các class name được sinh tự động từ công cụ thiết kế.

---

# 2. Layout tổng thể

## 2.1. Cấu trúc

```text
LoginPage
└── LoginBackground
    └── LoginCard
        ├── BackButton
        ├── WelcomeText
        ├── PageTitle
        ├── UsernameField
        ├── PasswordField
        ├── LoginButton
        ├── OrDivider
        └── GoogleLoginButton
```

---

# 3. Kích thước và vị trí thiết kế gốc

Thiết kế export có group:

```text
login
width: 668px
height: 509px
```

Background:

```text
width: 668px
height: 509px
background: #76ABAE
```

Login card:

```text
width: 340px
height: 450px
background: #FF5722
border: 1px solid #000000
border-radius: 10px
```

Tuy nhiên, **không nên triển khai group bằng `position: absolute` và tọa độ pixel của thiết kế export**.

Thay vào đó:

```css
.login-page {
    min-height: 100vh;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #76ABAE;
}

.login-card {
    width: 340px;
    min-height: 450px;
    background: #FF5722;
    border: 1px solid #000000;
    border-radius: 10px;
}
```

---

# 4. Color System

## 4.1. Background

```text
HEX: #76ABAE
RGBA: rgba(118, 171, 174, 1)
```

Tên đề xuất:

```css
--login-background: #76ABAE;
```

---

## 4.2. Login Card

```text
HEX: #FF5722
RGBA: rgba(255, 87, 34, 1)
```

Tên đề xuất:

```css
--login-card: #FF5722;
```

---

## 4.3. Dark Button

```text
HEX: #303841
RGBA: rgba(48, 56, 65, 1)
```

Tên đề xuất:

```css
--login-button: #303841;
```

Được sử dụng cho:

* nút Đăng nhập
* nút Đăng nhập bằng Google

---

## 4.4. Text

Text chính:

```text
HEX: #000000
```

Tên đề xuất:

```css
--login-text: #000000;
```

Text trên button:

```text
HEX: #FFFFFF
```

Tên đề xuất:

```css
--login-button-text: #FFFFFF;
```

---

## 4.5. Border

```text
HEX: #000000
```

```css
--login-border: #000000;
```

---

# 5. Typography

Font được sử dụng trong thiết kế:

```text
Source Sans Pro
```

Font family trong file export:

```css
font-family: "sourcesanspro";
```

Nếu font local tồn tại trong project, sử dụng font đó.

Nếu project chưa có font, có thể cấu hình fallback:

```css
font-family:
    "Source Sans Pro",
    "sourcesanspro",
    sans-serif;
```

---

# 6. Typography Scale

## 6.1. Welcome text

Nội dung:

```text
Chào mừng trở lại !
```

Thông số:

```text
font-size: 24px
font-weight: 400
line-height: 1.2
color: #000000
letter-spacing: 0px
```

Thiết kế gốc:

```text
width: 245px
height: 29px
left: 370px
top: 28px
```

Trong React/CSS nên chuyển thành layout bình thường:

```css
.login-welcome {
    font-size: 24px;
    font-weight: 400;
    line-height: 1.2;
    color: #000000;
    margin: 0;
}
```

---

# 7. Page Title

Nội dung:

```text
Đăng nhập
```

Thông số:

```text
font-size: 24px
font-weight: 400
line-height: 1.2
color: #000000
letter-spacing: 0px
```

Thiết kế gốc:

```text
left: 444px
top: 74px
width: 119px
height: 32px
```

CSS đề xuất:

```css
.login-title {
    font-size: 24px;
    font-weight: 400;
    line-height: 1.2;
    color: #000000;
    margin: 0;
}
```

---

# 8. Back Button

## 8.1. Vị trí

Icon:

```text
width: 24px
height: 24px
```

Thiết kế gốc:

```text
left: 632px
top: 12px
```

Icon nằm ở khu vực phía trên bên phải của login container.

---

## 8.2. Icon

Icon:

```text
Arrow Left
```

SVG:

```text
24 × 24
```

Màu:

```text
#000000
```

Stroke:

```text
1.5px
```

Line cap:

```text
round
```

Line join:

```text
round
```

Có thể sử dụng:

```jsx
<button className="back-button" aria-label="Quay lại">
    <ArrowLeft />
</button>
```

Không cần copy toàn bộ SVG export nếu project đã sử dụng icon library.

---

# 9. Username Field

## Label

Nội dung:

```text
Tên đăng nhập :
```

Thông số:

```text
font-size: 18px
font-weight: 400
color: #000000
line-height: 1.2
```

Thiết kế gốc:

```text
left: 367px
top: 132px
width: 135px
height: 21px
```

CSS đề xuất:

```css
.form-label {
    font-size: 18px;
    font-weight: 400;
    line-height: 1.2;
    color: #000000;
}
```

---

## Input

Thiết kế export không chứa trực tiếp hình dạng input trong đoạn HTML được cung cấp.

Do đó, input cần được tạo thành component thực tế:

```jsx
<label>
    <span>Tên đăng nhập :</span>
    <input
        type="text"
        name="username"
        autoComplete="username"
    />
</label>
```

Input phải:

* có thể focus bằng bàn phím
* có border rõ ràng
* có trạng thái focus
* không sử dụng absolute positioning
* responsive theo chiều rộng card

---

# 10. Password Field

## Label

Nội dung:

```text
Mật khẩu:
```

Thông số:

```text
font-size: 18px
font-weight: 400
color: #000000
line-height: 1.2
```

Thiết kế gốc:

```text
left: 370px
top: 194px
width: 135px
height: 21px
```

---

## Input

Sử dụng:

```html
<input type="password">
```

React:

```jsx
<label>
    <span>Mật khẩu:</span>
    <input
        type="password"
        name="password"
        autoComplete="current-password"
    />
</label>
```

Có thể bổ sung nút hiện/ẩn password nếu cần, nhưng **không tự ý thay đổi visual design nếu chưa có trong thiết kế**.

---

# 11. Login Button

## 11.1. Container

Button có:

```text
width: 100px
height: 30px
background: #303841
```

Thiết kế gốc:

```text
width: 100px
height: 30px
```

---

## 11.2. Text

Nội dung:

```text
Đăng nhập
```

Thông số:

```text
font-size: 18px
font-weight: 400
color: #FFFFFF
font-family: Source Sans Pro
```

---

## 11.3. CSS

```css
.login-button {
    width: 100px;
    height: 30px;
    background: #303841;
    color: #FFFFFF;
    border: none;
    font-family: "Source Sans Pro", "sourcesanspro", sans-serif;
    font-size: 18px;
    font-weight: 400;
    cursor: pointer;
}
```

Button nên được đặt ở giữa khu vực form.

Không sử dụng:

```css
position: absolute;
left: ...;
top: ...;
```

cho implementation cuối cùng.

---

# 12. "Hoặc"

Nội dung:

```text
Hoặc
```

Thông số:

```text
font-size: 18px
font-weight: 400
color: #000000
text-align: center
line-height: 1.2
```

Thiết kế gốc:

```text
width: 135px
height: 21px
left: 433px
top: 263px
```

CSS:

```css
.login-or {
    width: 100%;
    text-align: center;
    font-size: 18px;
    font-weight: 400;
    color: #000000;
    line-height: 1.2;
}
```

Có thể dùng:

```text
Hoặc
```

ở giữa hai phần đăng nhập.

Không thêm đường kẻ hai bên nếu thiết kế gốc không có.

---

# 13. Google Login Button

## 13.1. Container

Kích thước:

```text
width: 263px
height: 40px
```

Background:

```text
#303841
```

Thiết kế gốc:

```text
left: 405px
top: 0px
```

Tương ứng với khu vực Google button trong login group.

---

## 13.2. Text

Nội dung export:

```text
Đăng nhập băng Google
```

Đây có vẻ là lỗi chính tả trong text export.

Implementation nên sử dụng:

```text
Đăng nhập bằng Google
```

Thông số:

```text
font-size: 18px
font-weight: 400
color: #FFFFFF
font-family: Source Sans Pro
line-height: 1.2
```

---

## 13.3. Google icon

Kích thước:

```text
24px × 24px
```

Icon nằm bên phải button.

Thiết kế gốc:

```text
left: 215px
top: 10px
```

tính theo button:

```text
button width: 263px
icon width: 24px
right spacing: 24px
```

Icon có:

```text
stroke: #FFFFFF
stroke-width: 3px
```

---

## 13.4. Layout đề xuất

```jsx
<button className="google-login-button">
    <span>Đăng nhập bằng Google</span>
    <GoogleIcon />
</button>
```

CSS:

```css
.google-login-button {
    width: 263px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 24px 0 19px;

    background: #303841;
    color: #FFFFFF;
    border: none;

    font-family: "Source Sans Pro", "sourcesanspro", sans-serif;
    font-size: 18px;
    font-weight: 400;

    cursor: pointer;
}
```

---

# 14. Login Card Structure

Card chính:

```text
340px × 450px
```

CSS:

```css
.login-card {
    position: relative;

    width: 340px;
    min-height: 450px;

    background: #FF5722;

    border: 1px solid #000000;
    border-radius: 10px;

    overflow: hidden;
}
```

`position: relative` chỉ dùng để làm context cho các thành phần nếu cần, nhưng các thành phần chính nên được bố trí bằng Flexbox/Grid.

---

# 15. Recommended Internal Layout

Đề xuất bố cục:

```text
┌────────────────────────────────────┐
│                            ←       │
│                                    │
│       Chào mừng trở lại !          │
│                                    │
│           Đăng nhập                │
│                                    │
│  Tên đăng nhập :                   │
│  [____________________________]    │
│                                    │
│  Mật khẩu:                         │
│  [____________________________]    │
│                                    │
│           [ Đăng nhập ]            │
│                                    │
│              Hoặc                  │
│                                    │
│  [Đăng nhập bằng Google       G]  │
│                                    │
└────────────────────────────────────┘
```

Đây là cấu trúc triển khai đề xuất dựa trên thiết kế gốc, không phải yêu cầu sử dụng pixel positioning.

---

# 16. React Component Structure

Nên chia component như sau:

```text
src/
└── components/
    └── auth/
        ├── LoginPage.jsx
        ├── LoginForm.jsx
        ├── LoginInput.jsx
        ├── GoogleLoginButton.jsx
        └── BackButton.jsx
```

Hoặc nếu project hiện tại chưa cần chia nhỏ:

```text
src/
└── pages/
    └── LoginPage.jsx
```

---

# 17. Recommended JSX Structure

```jsx
<div className="login-page">
    <main className="login-card">

        <button
            type="button"
            className="back-button"
            aria-label="Quay lại"
        >
            <ArrowLeft />
        </button>

        <header className="login-header">
            <p className="login-welcome">
                Chào mừng trở lại !
            </p>

            <h1 className="login-title">
                Đăng nhập
            </h1>
        </header>

        <form className="login-form">

            <div className="form-group">
                <label htmlFor="username">
                    Tên đăng nhập :
                </label>

                <input
                    id="username"
                    name="username"
                    type="text"
                    autoComplete="username"
                />
            </div>

            <div className="form-group">
                <label htmlFor="password">
                    Mật khẩu:
                </label>

                <input
                    id="password"
                    name="password"
                    type="password"
                    autoComplete="current-password"
                />
            </div>

            <button
                type="submit"
                className="login-button"
            >
                Đăng nhập
            </button>

        </form>

        <div className="login-or">
            Hoặc
        </div>

        <button
            type="button"
            className="google-login-button"
        >
            <span>Đăng nhập bằng Google</span>
            <GoogleIcon />
        </button>

    </main>
</div>
```

---

# 18. API Integration

Login form phải kết nối với backend hiện tại.

Endpoint:

```http
POST /api/auth/login
```

Request:

```json
{
    "username": "example",
    "password": "password123"
}
```

Frontend không được lưu password plaintext sau khi request hoàn thành.

---

# 19. JWT Handling

Backend sử dụng JWT.

Sau khi login thành công:

```text
Login Form
    ↓
POST /api/auth/login
    ↓
Flask Backend
    ↓
Validate username/password
    ↓
Create JWT
    ↓
Frontend receives authentication result
```

Frontend cần xử lý:

* login thành công
* username/password sai
* validation error
* server error
* loading state
* network error

---

# 20. Google Login

Google login là một authentication flow riêng.

UI:

```text
[ Đăng nhập bằng Google       Google Icon ]
```

Khi người dùng click:

```text
Google Login Button
        ↓
Google OAuth
        ↓
Backend
        ↓
Check email
        ↓
Existing account?
    ├── Yes → Login
    └── No  → Create/continue registration flow
```

Không hard-code Google account hoặc token trong frontend.

---

# 21. Form Validation

Frontend nên validate trước khi gửi request.

## Username

Theo validation hiện tại của backend:

```text
3–50 characters
```

Cho phép:

```text
a-z
A-Z
0-9
_
```

Ví dụ hợp lệ:

```text
nguyenvana
nguyen_van_a
user123
```

---

## Password

Tối thiểu:

```text
8 characters
```

Frontend không nên kiểm tra quá khác backend để tránh UX không nhất quán.

---

# 22. Error States

Cần hỗ trợ:

### Invalid username

```text
Tên đăng nhập không hợp lệ
```

### Invalid password

```text
Mật khẩu phải có ít nhất 8 ký tự
```

### Wrong credentials

```text
Tên đăng nhập hoặc mật khẩu không chính xác
```

### Server error

```text
Có lỗi xảy ra. Vui lòng thử lại.
```

Error message nên nằm gần field hoặc khu vực form.

---

# 23. Loading State

Khi submit:

```text
Đăng nhập
```

có thể chuyển thành:

```text
Đang đăng nhập...
```

Button phải bị disabled trong thời gian request.

Ví dụ:

```jsx
<button
    type="submit"
    disabled={loading}
>
    {loading ? "Đang đăng nhập..." : "Đăng nhập"}
</button>
```

---

# 24. Accessibility

Phải đảm bảo:

* Mỗi input có `<label>`.
* `htmlFor` khớp với `id`.
* Button có `type`.
* Back button có `aria-label`.
* Google login button có text rõ ràng.
* Có keyboard navigation.
* Focus state phải nhìn thấy được.
* Không dùng text trong SVG thay cho semantic HTML.
* Heading chính sử dụng `<h1>`.

---

# 25. Responsive Design

Thiết kế gốc có card:

```text
340px × 450px
```

Desktop:

```css
.login-card {
    width: 340px;
    min-height: 450px;
}
```

Mobile:

```css
.login-card {
    width: min(340px, calc(100vw - 32px));
}
```

Google button:

```css
.google-login-button {
    width: min(263px, 100%);
}
```

Card không được vượt quá viewport.

Background phải luôn phủ toàn bộ màn hình:

```css
.login-page {
    width: 100%;
    min-height: 100vh;
}
```

---

# 26. Important Implementation Rule

Không copy nguyên các class generated từ design export như:

```text
.login-be47ecb6242c
.board-be47ecb6242e
.ng-nhp-be47ecb62431
.proicons-be47ecb62430
```

Các class này chỉ có giá trị đối với file export của công cụ thiết kế.

Trong React project nên sử dụng semantic class names:

```text
.login-page
.login-card
.login-header
.login-welcome
.login-title
.login-form
.form-group
.form-label
.form-input
.login-button
.login-or
.google-login-button
.back-button
```

---

# 27. Design Tokens

Có thể tập trung các giá trị thiết kế:

```css
:root {
    --login-background: #76ABAE;
    --login-card: #FF5722;
    --login-button: #303841;
    --login-text: #000000;
    --login-button-text: #FFFFFF;
    --login-border: #000000;

    --login-card-width: 340px;
    --login-card-height: 450px;
    --login-card-radius: 10px;

    --login-font-family:
        "Source Sans Pro",
        "sourcesanspro",
        sans-serif;

    --login-text-size: 18px;
    --login-heading-size: 24px;
}
```

---

# 28. Visual Requirements

AI coding agent phải giữ các đặc điểm quan trọng:

1. Background màu xanh xám `#76ABAE`.
2. Login card màu cam `#FF5722`.
3. Card kích thước gần `340 × 450px`.
4. Card có border đen 1px.
5. Card border-radius `10px`.
6. Typography sử dụng Source Sans Pro.
7. Text chính màu đen.
8. Button màu `#303841`.
9. Button text màu trắng.
10. Login button nhỏ, khoảng `100 × 30px`.
11. Google button khoảng `263 × 40px`.
12. Google icon kích thước `24 × 24px`.
13. Back icon kích thước `24 × 24px`.
14. Không thêm gradient nếu không có trong thiết kế.
15. Không thêm shadow nếu không có trong thiết kế.
16. Không thay đổi màu sắc chính.
17. Không sử dụng absolute positioning cho toàn bộ giao diện.
18. Responsive trên mobile.

---

# 29. Do Not Over-Design

Không tự ý thêm:

* Gradient.
* Glassmorphism.
* Box shadow lớn.
* Animation phức tạp.
* Background image.
* Pattern.
* Decorative illustration.
* Extra social login buttons.
* Remember me checkbox.
* Forgot password nếu chưa có trong design.
* Register link nếu chưa có trong design.

Nếu cần bổ sung các tính năng trên, phải giữ visual style hiện tại.

---

# 30. Implementation Priority

Khi chuyển thiết kế thành code, ưu tiên theo thứ tự:

### Priority 1 — Layout

```text
Background
↓
Card
↓
Header
↓
Form
↓
Buttons
```

### Priority 2 — Visual

```text
Colors
Typography
Sizes
Spacing
Border
Radius
Icons
```

### Priority 3 — Responsive

```text
Desktop
Tablet
Mobile
```

### Priority 4 — Behavior

```text
Validation
↓
API Login
↓
Loading
↓
Error
↓
JWT handling
```

### Priority 5 — Accessibility

```text
Labels
Keyboard navigation
Focus states
ARIA
Semantic HTML
```

---

# 31. Acceptance Criteria

Trang Login được xem là hoàn thành khi:

* [ ] Background đúng màu `#76ABAE`.
* [ ] Card đúng màu `#FF5722`.
* [ ] Card khoảng `340 × 450px`.
* [ ] Border `1px solid #000000`.
* [ ] Border radius `10px`.
* [ ] Welcome text là `Chào mừng trở lại !`.
* [ ] Title là `Đăng nhập`.
* [ ] Username field tồn tại.
* [ ] Password field tồn tại.
* [ ] Login button tồn tại.
* [ ] Text `Hoặc` tồn tại.
* [ ] Google login button tồn tại.
* [ ] Google icon tồn tại.
* [ ] Back arrow tồn tại.
* [ ] Font gần với Source Sans Pro.
* [ ] Không dùng layout absolute pixel-based cho toàn bộ page.
* [ ] Responsive trên mobile.
* [ ] Form kết nối được `POST /api/auth/login`.
* [ ] Loading state hoạt động.
* [ ] Error state hoạt động.
* [ ] JWT được xử lý đúng theo authentication architecture của project.
* [ ] Không hard-code credentials hoặc secrets.

---

# 32. Reference Values From Original Export

| Element         | Value             |
| --------------- | ----------------- |
| Main group      | `668 × 509px`     |
| Background      | `#76ABAE`         |
| Card            | `340 × 450px`     |
| Card background | `#FF5722`         |
| Card border     | `1px #000000`     |
| Card radius     | `10px`            |
| Button          | `#303841`         |
| Button text     | `#FFFFFF`         |
| Main text       | `#000000`         |
| Body font       | `Source Sans Pro` |
| Normal text     | `18px`            |
| Heading text    | `24px`            |
| Login button    | `100 × 30px`      |
| Google button   | `263 × 40px`      |
| Google icon     | `24 × 24px`       |
| Back icon       | `24 × 24px`       |

---

# 33. Final Instruction For AI Coding Agent

Khi triển khai Login Page:

> Read this `design_spec.md` together with the existing React codebase before modifying files.
>
> Preserve the existing project architecture, routing, authentication flow, API services, and component conventions.
>
> Recreate the visual design from this specification rather than copying the generated HTML/CSS export literally.
>
> Use semantic React components, Flexbox/Grid, responsive CSS, accessible form controls, and reusable components.
>
> Do not replace or rewrite unrelated parts of the project.
>
> Before implementing API integration, inspect the existing authentication API/service structure and use the existing conventions.
>
> The final implementation should visually match the provided design while remaining maintainable and responsive.
