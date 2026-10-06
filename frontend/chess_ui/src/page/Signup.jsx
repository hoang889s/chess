import { useState } from 'react'
import './Login_Signup.css'

const Signup = () => {
    const navigateTo = (page) => {
        window.history.pushState({}, '', `/${page}`)
        window.dispatchEvent(new (window.PopStateEvent || Event)('popstate'))
    }
    const [name, setName] = useState('')
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [confirmPassword, setConfirmPassword] = useState('')

    const handleSubmit = (event) => {
        event.preventDefault()
        // TODO: gọi API đăng ký tại đây
        console.log('Đăng ký:', { name, email, password })
    }

    const handleGoogleSignup = () => {
        // TODO: tích hợp Google OAuth
        console.log('Đăng ký bằng Google')
    }

    return (
        <main className="auth-page">
            <div className="auth-page__grain" aria-hidden="true" />

            {/* ===== PANEL TRÁI: chào mừng ===== */}
            <section className="auth-panel auth-panel--left">
                <div className="auth-panel__illustration">
                    <div className="auth-panel__board" aria-hidden="true">
                        <div className="auth-panel__square auth-panel__square--light">
                            <img src="/icons/pawn.svg" width={32} height={32} alt="" />
                        </div>
                        <div className="auth-panel__square auth-panel__square--dark" />
                        <div className="auth-panel__square auth-panel__square--dark" />
                        <div className="auth-panel__square auth-panel__square--light">
                            <img src="/icons/king.svg" width={32} height={32} alt="" />
                        </div>
                        <div className="auth-panel__square auth-panel__square--light" />
                        <div className="auth-panel__square auth-panel__square--dark">
                            <img src="/icons/rook.svg" width={32} height={32} alt="" />
                        </div>
                        <div className="auth-panel__square auth-panel__square--light" />
                        <div className="auth-panel__square auth-panel__square--dark" />
                        <div className="auth-panel__square auth-panel__square--dark" />
                        <div className="auth-panel__square auth-panel__square--light">
                            <img src="/icons/queen.svg" width={32} height={32} alt="" />
                        </div>
                        <div className="auth-panel__square auth-panel__square--dark" />
                        <div className="auth-panel__square auth-panel__square--light" />
                        <div className="auth-panel__square auth-panel__square--light">
                            <img src="/icons/knight.svg" width={32} height={32} alt="" />
                        </div>
                        <div className="auth-panel__square auth-panel__square--dark" />
                        <div className="auth-panel__square auth-panel__square--dark" />
                        <div className="auth-panel__square auth-panel__square--light">
                            <img src="/icons/bishop.svg" width={32} height={32} alt="" />
                        </div>
                    </div>
                </div>

                <div className="auth-panel__content">
                    <span className="auth-panel__eyebrow">Chào mừng trở lại!</span>
                    <h1 className="auth-panel__title">Đăng ký</h1>
                    <p className="auth-panel__desc">
                        Tạo tài khoản mới để bắt đầu hành trình cờ vua của bạn
                    </p>
                </div>
            </section>

            {/* ===== FORM BÊN PHẢI ===== */}
            <section className="auth-panel auth-panel--right">
                <div className="auth-card">
                    <h2 className="auth-card__title">Đăng ký</h2>

                    <form className="auth-form" onSubmit={handleSubmit}>
                        <div className="auth-field">
                            <label htmlFor="signup-name" className="auth-field__label">
                                Tên đăng nhập :
                            </label>
                            <input
                                id="signup-name"
                                type="text"
                                className="auth-field__input"
                                placeholder="Nhập tên đăng nhập của bạn"
                                value={name}
                                onChange={(event) => setName(event.target.value)}
                                required
                            />
                        </div>

                        <div className="auth-field">
                            <label htmlFor="signup-email" className="auth-field__label">
                                Email:
                            </label>
                            <input
                                id="signup-email"
                                type="email"
                                className="auth-field__input"
                                placeholder="Nhập địa chỉ email của bạn"
                                value={email}
                                onChange={(event) => setEmail(event.target.value)}
                                required
                            />
                        </div>

                        <div className="auth-field">
                            <label htmlFor="signup-password" className="auth-field__label">
                                Mật khẩu:
                            </label>
                            <input
                                id="signup-password"
                                type="password"
                                className="auth-field__input"
                                placeholder="Nhập mật khẩu của bạn"
                                value={password}
                                onChange={(event) => setPassword(event.target.value)}
                                required
                            />
                        </div>

                        <div className="auth-field">
                            <label htmlFor="signup-confirm" className="auth-field__label">
                                Nhập lại mật khẩu:
                            </label>
                            <input
                                id="signup-confirm"
                                type="password"
                                className="auth-field__input"
                                placeholder="Nhập lại mật khẩu"
                                value={confirmPassword}
                                onChange={(event) => setConfirmPassword(event.target.value)}
                                required
                            />
                        </div>

                        <button type="submit" className="auth-button auth-button--primary">
                            Đăng ký
                        </button>
                    </form>

                    <div className="auth-divider">
                        <span className="auth-divider__text">Hoặc</span>
                    </div>

                    <button
                        type="button"
                        className="auth-button auth-button--google"
                        onClick={handleGoogleSignup}
                    >
                        <img
                            src="https://www.gstatic.com/firebasejs/ui/2.0.0/images/auth/google.svg"
                            width={20}
                            height={20}
                            alt="Google"
                        />
                        <span>Đăng ký bằng Google</span>
                    </button>
                </div>

                <div className="auth-switch">
                    <span>Đã có tài khoản?</span>
                    <button
                        type="button"
                        className="auth-switch__link"
                        onClick={() => navigateTo('Login.jsx')}
                    >
                        Đăng nhập
                    </button>
                </div>
            </section>
        </main>
    )
}

export default Signup
