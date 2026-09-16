import { useState } from 'react';

const LeftBar = () => {
  const [toast, setToast] = useState(null);
  const showToast = (message) => {
    setToast(message);
    setTimeout(() => setToast(null), 3000);
  };

  const gameModes = ['Chơi mới', 'Người chơi', 'Đấu máy'];
  const timeOptions = ['Cờ siêu chớp', 'Cờ chớp', 'Cờ nhanh', 'Cờ thường'];

  return (
    <aside className="game-side-panel" aria-label="Tùy chọn ván đấu">
      {toast && (
        <div style={{
          position: 'absolute',
          bottom: '20px',
          left: '50%',
          transform: 'translateX(-50%)',
          background: '#333',
          color: '#fff',
          padding: '10px 20px',
          borderRadius: '5px',
          fontSize: '14px',
          zIndex: 1000,
        }}>
          {toast}
        </div>
      )}
      <div className="game-mode-list">
        {gameModes.map((mode) => (
          <button
            className="game-option-button"
            key={mode}
            type="button"
            onClick={mode === 'Người chơi' ? () => showToast('Người chơi bạn phải đăng ký hoặc đăng nhập để chọn chức năng này') : undefined}
          >
            {mode}
          </button>
        ))}
      </div>

      <p className="game-side-panel__label">Chọn thời gian</p>

      <div className="game-time-grid">
        {timeOptions.map((option) => (
          <button
            className="game-time-button"
            key={option}
            type="button"
            onClick={() => showToast(`${option} bạn phải đăng ký hoặc đăng nhập để chọn chức năng này`)}
          >
            {option}
          </button>
        ))}
      </div>

      <button
        className="game-custom-button"
        type="button"
        onClick={() => showToast('Tùy chỉnh bạn phải đăng ký hoặc đăng nhập để chọn chức năng này')}
      >
        Tùy chỉnh
      </button>
    </aside>
  );
};

export default LeftBar;