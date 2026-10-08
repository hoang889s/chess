# Design Specification — Sign Up Page

## 1. Overview

### Page

**Tên màn hình:** Đăng ký tài khoản (Sign Up)

### Mục tiêu

Thiết kế giao diện đăng ký tài khoản cho website cờ vua trực tuyến.

Màn hình cần cung cấp:

* Tiêu đề chào mừng người dùng.
* Form đăng ký tài khoản.
* Trường tên đăng nhập.
* Trường mật khẩu.
* Trường email.
* Nút đăng ký.
* Đăng ký/đăng nhập bằng Google.
* Nút quay lại.

### Ngôn ngữ giao diện

Vietnamese.

---

# 2. Visual Design

## 2.1. Main Background

Màn hình sử dụng background màu xanh teal:

```text
#76ABAE
```

Background bao phủ toàn bộ khu vực thiết kế.

Thiết kế gốc có kích thước:

```text
Width: 668px
Height: 509px
```

Tuy nhiên khi triển khai trên web, không nên cố định kích thước toàn trang ở `668px × 509px`.

Background nên responsive và bao phủ viewport.

---

# 3. Sign Up Card

## 3.1. Card

Form đăng ký nằm bên trong một card màu cam:

```text
Background: #FF5722
Border: 1px solid #000000
Border radius: 10px
```

Kích thước thiết kế gốc:

```text
Width: 340px
Height: 450px
```

Card:

* Bo góc 10px.
* Không để nội dung tràn ra ngoài.
* Sử dụng `overflow: hidden`.
* Nằm trên background.
* Có thể căn giữa theo chiều ngang/dọc trên màn hình responsive.

### Recommended implementation

```css
.signup-card {
  width: 340px;
  min-height: 450px;
  background: #ff5722;
  border: 1px solid #000;
  border-radius: 10px;
  overflow: hidden;
}
```

---

# 4. Typography

## 4.1. Font

Thiết kế sử dụng:

```text
Source Sans Pro
```

Font family:

```css
font-family: "sourcesanspro";
```

Font style:

```text
normal
```

Font weight:

```text
400
```

Font display trong thiết kế gốc:

```css
font-display: block;
```

Nếu project chưa có font local, có thể sử dụng Source Sans Pro tương đương từ font provider phù hợp.

---

# 5. Page Header

## 5.1. Welcome Text

Text:

```text
Chào mừng trở lại !
```

### Design properties

```text
Font: Source Sans Pro
Size: 24px
Weight: 400
Color: #000000
Line height: 1.2
Text align: left
```

Vị trí tương đối trong thiết kế gốc:

```text
Left: 370px
Top: 42px
Width: 245px
Height: 29px
```

Khi chuyển sang responsive layout, không sử dụng `position: absolute` với `left: 370px`.

Thay vào đó, header nên nằm trong card hoặc layout container.

---

# 6. Back Button

## 6.1. Back Icon

Icon:

```text
Arrow Left
```

Kích thước:

```text
24px × 24px
```

Vị trí thiết kế gốc:

```text
Left: 632px
Top: 26px
```

Icon màu:

```text
#000000
```

### Behavior

Khi người dùng click:

```text
Back → quay lại màn hình trước
```

### Recommended implementation

Sử dụng icon component thay vì copy toàn bộ SVG export từ công cụ thiết kế.

Ví dụ:

```text
ArrowLeft
```

Kích thước:

```text
24px
```

---

# 7. Form Title

## 7.1. Title

Text:

```text
Đăng ký
```

### Design properties

```text
Font: Source Sans Pro
Font size: 24px
Font weight: 400
Color: #000000
Line height: 1.2
```

Kích thước vùng text trong thiết kế:

```text
Width: 119px
Height: 32px
```

Vị trí gốc:

```text
Left: 444px
Top: 88px
```

Trong implementation thực tế nên căn giữa title trong card.

---

# 8. Form Fields

Form gồm ba trường:

1. Tên đăng nhập
2. Mật khẩu
3. Email

---

## 8.1. Username

### Label

```text
Tên đăng nhập :
```

Typography:

```text
Font: Source Sans Pro
Size: 18px
Weight: 400
Color: #000000
Line height: 1.2
```

Thiết kế gốc:

```text
Left: 367px
Top: 146px
Width: 135px
Height: 21px
```

### Input

Input cần nằm bên dưới label.

Khuyến nghị:

```text
Type: text
Name: username
Placeholder: Nhập tên đăng nhập
```

Input phải hỗ trợ:

* Focus state.
* Validation state.
* Error message.
* Keyboard navigation.

---

# 8.2. Password

### Label

```text
Mật khẩu:
```

Typography:

```text
Font: Source Sans Pro
Size: 18px
Weight: 400
Color: #000000
Line height: 1.2
```

Thiết kế gốc:

```text
Left: 370px
Top: 208px
Width: 135px
Height: 21px
```

### Input

```text
Type: password
Name: password
Placeholder: Nhập mật khẩu
```

Nên hỗ trợ:

* Hiện/ẩn mật khẩu.
* Focus state.
* Validation.
* Error message.

---

# 8.3. Email

### Label

```text
Email:
```

Typography:

```text
Font: Source Sans Pro
Size: 18px
Weight: 400
Color: #000000
Line height: 1.2
```

Thiết kế gốc:

```text
Left: 367px
Top: 258px
Width: 135px
Height: 21px
```

### Input

```text
Type: email
Name: email
Placeholder: Nhập email
```

Input phải hỗ trợ:

* Email validation.
* Focus state.
* Error message.

---

# 9. Primary Register Button

## 9.1. Button

Text:

```text
Đăng ký
```

Button nằm phía dưới các trường nhập liệu.

Thiết kế gốc sử dụng màu:

```text
#303841
```

### Typography

```text
Font: Source Sans Pro
Font size: 18px
Font weight: 400
Color: #FFFFFF
```

### Button behavior

Normal:

```text
Background: #303841
Text: #FFFFFF
```

Hover:

```text
Background: slightly lighter/different visual state
Cursor: pointer
```

Active:

```text
Button visually pressed
```

Disabled:

```text
Button visually disabled
cursor: not-allowed
```

### Functional behavior

Khi click:

```text
1. Validate username
2. Validate password
3. Validate email
4. Submit registration request
5. Hiển thị loading state
6. Nếu thành công → chuyển sang màn hình đăng nhập
7. Nếu thất bại → hiển thị lỗi
```

---

# 10. Google Authentication

## 10.1. Separator

Text:

```text
Hoặc
```

Typography:

```text
Font: Source Sans Pro
Size: 18px
Weight: 400
Color: #000000
Text align: center
```

Thiết kế gốc:

```text
Left: 438px
Top: 386px
Width: 135px
Height: 21px
```

Trong responsive layout:

```text
width: 100%
text-align: center
```

Có thể sử dụng divider:

```text
──────── Hoặc ────────
```

nếu muốn giao diện trực quan hơn, nhưng không bắt buộc vì thiết kế gốc chỉ thể hiện text "Hoặc".

---

# 11. Google Login Button

## 11.1. Button

Text trong thiết kế:

```text
Đăng nhập băng Google
```

Nên sửa chính tả thành:

```text
Đăng nhập bằng Google
```

### Button dimensions

Thiết kế gốc:

```text
Width: 263px
Height: 40px
```

Background:

```text
#303841
```

### Border

Không có border nổi bật trong thiết kế gốc.

### Typography

```text
Font: Source Sans Pro
Size: 18px
Weight: 400
Color: #FFFFFF
```

### Google Icon

Kích thước:

```text
24px × 24px
```

Icon nằm phía bên phải button trong thiết kế gốc.

Vị trí tương đối:

```text
Left: 215px
Top: 10px
```

### Layout

Nên implement bằng flexbox:

```text
[Đăng nhập bằng Google              G]
```

hoặc:

```text
[      G  Đăng nhập bằng Google     ]
```

Tùy theo việc giữ chính xác thiết kế gốc.

### Behavior

Khi click:

```text
Start Google OAuth authentication.
```

Frontend không tự xử lý mật khẩu Google.

---

# 12. Layout Structure

Không nên triển khai giao diện bằng hàng loạt:

```css
position: absolute;
left: xxx;
top: xxx;
```

như CSS export từ công cụ thiết kế.

CSS export chỉ được sử dụng làm **reference**.

Component structure đề xuất:

```text
SignUpPage
│
├── Background
│
├── SignUpCard
│   │
│   ├── BackButton
│   │
│   ├── Header
│   │   ├── WelcomeText
│   │   └── Title
│   │
│   ├── SignUpForm
│   │   ├── UsernameField
│   │   ├── PasswordField
│   │   ├── EmailField
│   │   └── SubmitButton
│   │
│   ├── OAuthDivider
│   │
│   └── GoogleButton
```

---

# 13. Recommended Responsive Layout

## Desktop

Card:

```text
Width: 340px
Height: 450px
```

Center card:

```css
display: flex;
align-items: center;
justify-content: center;
```

---

## Tablet

Card giữ chiều rộng khoảng:

```text
340px
```

nhưng có margin hai bên.

---

## Mobile

Không để card vượt quá viewport.

Recommended:

```css
width: min(340px, calc(100vw - 32px));
```

Các form elements:

```text
width: 100%
```

Không sử dụng fixed `left` / `top`.

---

# 14. Color Palette

| Element         | Color     |
| --------------- | --------- |
| Page background | `#76ABAE` |
| Sign-up card    | `#FF5722` |
| Dark button     | `#303841` |
| Primary text    | `#000000` |
| Button text     | `#FFFFFF` |
| Card border     | `#000000` |

---

# 15. Spacing

Thiết kế gốc sử dụng khoảng cách tương đối lớn giữa các label.

Khi triển khai lại bằng CSS layout, ưu tiên spacing nhất quán thay vì copy tọa độ tuyệt đối.

Recommended:

```text
Card padding: 24px
Header margin-bottom: 24px
Form field gap: 16–20px
Button margin-top: 20–24px
OAuth divider margin: 20px 0
Google button height: 40px
```

Các giá trị này có thể điều chỉnh nhẹ để đạt visual match với thiết kế gốc.

---

# 16. Accessibility

Các input phải có label rõ ràng.

Ví dụ:

```html
<label for="username">
  Tên đăng nhập:
</label>
<input id="username" name="username" />
```

Yêu cầu:

* Keyboard accessible.
* Focus state rõ ràng.
* Button có trạng thái disabled khi đang submit.
* Error message phải liên kết được với input.
* Icon button phải có `aria-label`.

Back button:

```text
aria-label="Quay lại"
```

Password visibility button:

```text
aria-label="Hiện mật khẩu"
```

Google button:

```text
aria-label="Đăng nhập bằng Google"
```

---

# 17. Frontend Behavior

## Registration

Form submit:

```text
POST /api/auth/register
```

Payload:

```json
{
  "username": "...",
  "password": "...",
  "email": "..."
}
```

Frontend cần xử lý:

```text
idle
↓
submitting
↓
success / error
```

---

# 18. Validation

## Username

Theo validation của backend:

```text
Required
3–50 characters
Letters / numbers / underscore
```

## Password

```text
Required
Minimum 8 characters
```

## Email

```text
Required
Valid email format
Maximum 100 characters
```

Frontend validation chỉ giúp UX.

Backend vẫn phải là nơi validation cuối cùng.

---

# 19. Error States

Các lỗi cần thể hiện ngay dưới field tương ứng.

Ví dụ:

```text
Tên đăng nhập:
[_____________________]
Tên đăng nhập phải có ít nhất 3 ký tự.
```

Không làm layout bị nhảy quá mạnh khi error xuất hiện.

---

# 20. Loading State

Khi đăng ký:

```text
Đăng ký → Đang đăng ký...
```

Disable submit button để tránh gửi request nhiều lần.

Google button cũng cần loading state khi OAuth đang được khởi tạo.

---

# 21. Design-to-Code Rules

Các CSS class được export từ công cụ thiết kế như:

```text
.signup-bb884cd47c17
.board-bb833f8cd4e2
.ng-k-bb84baaa4ce7
.cho-mng-bb837cc90f7e
```

**KHÔNG sử dụng trực tiếp trong production code.**

Thay bằng semantic class/component names:

```text
.signup-page
.signup-card
.signup-header
.signup-title
.signup-form
.form-field
.form-label
.form-input
.register-button
.oauth-divider
.google-button
.back-button
```

SVG export của icon có thể được chuyển thành React component hoặc sử dụng icon library tương đương.

---

# 22. Visual Fidelity Priority

Khi implement, ưu tiên theo thứ tự:

1. Tổng thể background và card.
2. Card size và vị trí.
3. Typography.
4. Form spacing.
5. Button dimensions.
6. Google icon/button.
7. Back button.
8. Responsive behavior.
9. Hover/focus/validation states.

Không đánh đổi responsive behavior chỉ để giữ nguyên pixel coordinates của file thiết kế.

---

# 23. Implementation Goal

Mục tiêu cuối cùng là tạo một màn hình đăng ký:

* Giữ đúng visual identity của thiết kế gốc.
* Có background `#76ABAE`.
* Có card màu `#FF5722`.
* Có dark buttons `#303841`.
* Sử dụng Source Sans Pro.
* Có form username/password/email.
* Có đăng ký tài khoản.
* Có Google authentication.
* Có nút quay lại.
* Responsive trên desktop/tablet/mobile.
* Accessible.
* Dễ bảo trì.
* Không phụ thuộc vào absolute positioning của file export.
* Có thể kết nối trực tiếp với Flask authentication API hiện tại.
