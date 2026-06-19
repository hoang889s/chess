# CLAUDE.md

Tệp này cung cấp hướng dẫn cho Claude Code khi làm việc với frontend của dự án chess game.

## Tổng quan dự án

Frontend nằm trong thư mục `frontend/chess_ui` và sử dụng:

- ReactJS với JavaScript, không dùng TypeScript.
- Vite để chạy dev server, build, preview và cấu hình React plugin.
- CSS thuần cho giao diện.
- Component React viết bằng cú pháp `const Component = () => { ... }`.
- Không sử dụng `function Component() { ... }` khi khai báo component.

## Quy tắc làm việc bắt buộc

Trước khi thực hiện bất kỳ yêu cầu mới nào, phải hỏi lại người dùng để làm rõ phạm vi, luồng nghiệp vụ, giao diện, dữ liệu cần dùng và kết quả mong muốn.

Chỉ được tiếp tục chỉnh sửa code sau khi người dùng đã duyệt rõ ràng. Không tự ý triển khai thêm tính năng, refactor, đổi kiến trúc, cài dependency, hoặc sửa nhiều file khi chưa được duyệt.

Khi yêu cầu chưa rõ, hãy đưa ra câu hỏi ngắn gọn và chờ phản hồi trước khi hành động.

## Quy ước code

### Component

- Viết component bằng `const` và arrow function.
- Không dùng `function` để khai báo component.
- Tên component viết theo `PascalCase`.
- Mỗi component nên có trách nhiệm rõ ràng, tránh component quá lớn.
- Tách component nhỏ khi màn hình có nhiều phần độc lập như header, sidebar, modal, card, form, table hoặc section.

Ví dụ đúng:

```jsx
const Header = () => {
  return (
    <header>
      <h1>Chess UI</h1>
    </header>
  )
}

export default Header
```

Ví dụ không dùng:

```jsx
function Header() {
  return <h1>Chess UI</h1>
}
```

### File và thư mục

Tổ chức code theo từng phần rõ ràng, ví dụ:

```text
src/
  components/
    layout/
    board/
    modals/
    forms/
  pages/
  styles/
  utils/
  assets/
```

Nếu dự án chưa có cấu trúc thư mục này, chỉ tạo thêm khi đã được người dùng duyệt.

### CSS

- Ưu tiên CSS thuần.
- Tên class rõ nghĩa, mô tả đúng thành phần hoặc chức năng.
- Tránh style inline nếu có thể.
- Nếu CSS của một component chỉ dùng riêng cho component đó, có thể đặt cạnh component hoặc gom vào thư mục styles phù hợp.

### JavaScript

- Dùng JavaScript thông thường, không thêm TypeScript nếu chưa được duyệt.
- Ưu tiên code dễ đọc, rõ luồng xử lý.
- Hạn chế logic phức tạp đặt trực tiếp trong JSX; nên tách thành biến hoặc hàm helper nhỏ.
- Không cài thêm thư viện mới nếu chưa hỏi và được người dùng duyệt.
- Không dùng `function` để khai báo component hoặc helper nếu có thể thay bằng arrow function.

### State và truyền tham số

- Ưu tiên dùng `useContext` khi cần chia sẻ state hoặc cấu hình cho nhiều component để giảm prop drilling.
- Các dữ liệu phù hợp để đưa vào context gồm theme, thông tin người dùng, cấu hình bàn cờ, trạng thái ván đấu, lịch sử nước đi, trạng thái modal, hoặc dữ liệu chung của màn hình.
- Không truyền quá nhiều prop qua nhiều tầng component nếu có thể gom vào một context phù hợp.
- Khi tạo context, nên tách file rõ ràng, ví dụ `src/context/ChessGameContext.jsx` hoặc theo đúng phạm vi nghiệp vụ.
- Chỉ dùng context cho dữ liệu thật sự cần chia sẻ rộng. Dữ liệu chỉ dùng giữa cha-con gần nhau vẫn có thể truyền prop bình thường.

Ví dụ đúng:

```jsx
const ChessGameProvider = ({ children }) => {
  const value = {
    board,
    selectedSquare,
    moveHistory,
  }

  return (
    <ChessGameContext.Provider value={value}>
      {children}
    </ChessGameContext.Provider>
  )
}

const Board = () => {
  const { board, selectedSquare } = useContext(ChessGameContext)

  return <div>{/* render board */}</div>
}
```

## Component rõ ràng

Khi phát triển màn hình mới, nên chia theo các phần:

1. Layout chính của màn hình.
2. Các section lớn.
3. Các component tái sử dụng.
4. Modal, dialog hoặc form riêng nếu có.
5. CSS tương ứng.

Mỗi component nên có một mục đích cụ thể. Không nhồi toàn bộ giao diện vào `App.jsx` nếu màn hình có nhiều phần.

## Quy trình đề xuất khi nhận yêu cầu

1. Đọc yêu cầu và xác định phạm vi.
2. Hỏi lại người dùng nếu thiếu thông tin.
3. Đưa ra kế hoạch ngắn gọn nếu cần.
4. Chờ người dùng duyệt.
5. Sau khi được duyệt, mới chỉnh sửa code.
6. Nếu có thể, chạy lệnh kiểm tra phù hợp sau khi sửa.

## Lệnh thường dùng

Từ thư mục `frontend/chess_ui`:

```bash
# Chạy dev server
npm run dev

# Build production
npm run build

# Chạy lint
npm run lint

# Preview bản build
npm run preview
```

Nếu cần kiểm tra thủ công giao diện, ưu tiên chạy `npm run dev` và xem kết quả trong trình duyệt.

## Lưu ý với dự án chess

Frontend hiện là ReactJS + JavaScript + CSS. Khi tích hợp với backend chess engine, cần hỏi rõ:

- Backend có API chưa.
- Endpoint cần gọi là gì.
- Dữ liệu trả về có định dạng nào.
- Bàn cờ cần hiển thị theo chuẩn nào.
- Người dùng cần thao tác nào: chọn ô, kéo thả, undo, redo, chơi với AI, xem lịch sử nước đi, v.v.

Không tự giả định luồng chơi cờ nếu chưa được người dùng xác nhận.
