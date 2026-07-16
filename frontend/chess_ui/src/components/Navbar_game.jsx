const NavbarGame = ({ onBack }) => {
    const handleBack = () => {
        if (onBack) {
            onBack()
        } else {
            window.history.back()
        }
    }

    return (
        <header className="game-header">
            <button className="game-header__back" type="button" onClick={handleBack}>
                Quay lại <span aria-hidden="true">›</span>
            </button>
        </header>
    )
}

export default NavbarGame