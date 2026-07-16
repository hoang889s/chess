const gameModes = ['Chơi mới', 'Người chơi', 'Đấu máy']
const timeOptions = ['Cờ siêu chớp', 'Cờ chớp', 'Cờ nhanh', 'Cờ thường']

const LeftBar = () => {
    return (
        <aside className="game-side-panel" aria-label="Tùy chọn ván đấu">
            <div className="game-mode-list">
                {gameModes.map((mode) => (
                    <button className="game-option-button" key={mode} type="button">
                        {mode}
                    </button>
                ))}
            </div>

            <p className="game-side-panel__label">Chọn thời gian</p>

            <div className="game-time-grid">
                {timeOptions.map((option) => (
                    <button className="game-time-button" key={option} type="button">
                        {option}
                    </button>
                ))}
            </div>

            <button className="game-custom-button" type="button">
                Tùy chỉnh
            </button>
        </aside>
    )
}

export default LeftBar