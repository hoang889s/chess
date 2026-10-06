import { useState } from 'react'
import './Login_Signup.css'

const Login = () => {
    const navigateTo = (page) => {
        window.history.pushState({}, '', `/${page}`)
        window.dispatchEvent(new (window.PopStateEvent || Event)('popstate'))
    }
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')

    const handleSubmit = (event) => {
        event.preventDefault()
        // TODO: gọi API đăng nhập tại đây
        console.log('Đăng nhập:', { email, password })
    }

    const handleGoogleLogin = () => {
        // TODO: tích hợp Google OAuth
        console.log('Đăng nhập bằng Google')
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
                    <h1 className="auth-panel__title">Đăng nhập</h1>
                    <p className="auth-panel__desc">
                        Nhập thông tin để tiếp tục tham gia những ván đấu thú vị
                    </p>
                </div>
            </section>

            {/* ===== FORM BÊN PHẢI ===== */}
            <section className="auth-panel auth-panel--right">
                <div className="auth-card">
                    <h2 className="auth-card__title">Đăng nhập</h2>

                    <form className="auth-form" onSubmit={handleSubmit}>
                        <div className="auth-field">
                            <label htmlFor="login-email" className="auth-field__label">
                                Tên đăng nhập :
                            </label>
                            <input
                                id="login-email"
                                type="text"
                                className="auth-field__input"
                                placeholder="Nhập tên đăng nhập của bạn"
                                value={email}
                                onChange={(event) => setEmail(event.target.value)}
                                required
                            />
                        </div>

                        <div className="auth-field">
                            <label htmlFor="login-password" className="auth-field__label">
                                Mật khẩu:
                            </label>
                            <input
                                id="login-password"
                                type="password"
                                className="auth-field__input"
                                placeholder="Nhập mật khẩu của bạn"
                                value={password}
                                onChange={(event) => setPassword(event.target.value)}
                                required
                            />
                        </div>

                        <div className="auth-field auth-field--right">
                            <a href="#" className="auth-field__forgot">
                                Quên mật khẩu?
                            </a>
                        </div>

                        <button type="submit" className="auth-button auth-button--primary">
                            Đăng nhập
                        </button>
                    </form>

                    <div className="auth-divider">
                        <span className="auth-divider__text">Hoặc</span>
                    </div>

                    <button
                        type="button"
                        className="auth-button auth-button--google"
                        onClick={handleGoogleLogin}
                    >
                        <img
                            src="https://www.gstatic.com/firebasejs/ui/2.0.0/images/auth/google.svg"
                            width={20}
                            height={20}
                            alt="Google"
                        />
                        <span>Đăng nhập bằng Google</span>
                    </button>
                </div>

                <div className="auth-switch">
                    <span>Chưa có tài khoản?</span>
                    <button
                        type="button"
                        className="auth-switch__link"
                        onClick={() => navigateTo('Signup.jsx')}
                    >
                        Đăng ký
                    </button>
                </div>
            </section>
        </main>
    )
}

export default Login
