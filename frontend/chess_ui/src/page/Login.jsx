import { useState } from 'react'
import './Login.css'

const Login = () => {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [showPassword, setShowPassword] = useState(false)
  const [rememberMe, setRememberMe] = useState(false)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const navigateTo = (page) => {
    window.history.pushState({}, '', page)
    window.dispatchEvent(new Event('popstate'))
  }

  const handleSubmit = async (event) => {
    event.preventDefault()
    setError('')
    setLoading(true)

    // TODO: gọi API đăng nhập tại đây
    console.log('Đăng nhập:', { email, password, rememberMe })

    // Mock delay cho demo
    setTimeout(() => {
      setLoading(false)
    }, 1200)
  }

  const handleGoogleLogin = () => {
    // TODO: tích hợp Google OAuth
    console.log('Đăng nhập bằng Google')
  }

  return (
    <main className="login-page">
      <div className="login-page__grain" aria-hidden="true" />

      {/* Decorative chess pieces */}
      <div className="login-decor" aria-hidden="true">
        <span className="login-decor__piece login-decor__piece--top-left">♞</span>
        <span className="login-decor__piece login-decor__piece--top-right">♜</span>
        <span className="login-decor__piece login-decor__piece--bottom-left">♟</span>
        <span className="login-decor__piece login-decor__piece--bottom-right">♝</span>
      </div>

      <div className="login-card">
        {/* ===== Nút quay lại (Back button) ===== */}
        <button
          type="button"
          className="login-back"
          onClick={() => window.history.back()}
          aria-label="Quay lại"
        >
          <svg
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="1.5"
            strokeLinecap="round"
            strokeLinejoin="round"
            className="arrow-left"
            aria-hidden="true"
          >
            <line x1="19" y1="12" x2="5" y2="12" />
            <polyline points="12 19 5 12 12 5" />
          </svg>
        </button>

        {/* ===== Brand / Chess Logo ===== */}
        <div className="login-brand">
          <div className="login-brand__icon">♞</div>
          <span className="login-brand__text">AI POWERED CHESS</span>
        </div>

        {/* ===== Header ===== */}
        <div className="login-header">
          <p className="login-welcome">Chào mừng trở lại!</p>
          <h1 className="login-title">Đăng nhập</h1>
        </div>

        {/* ===== Error Message ===== */}
        {error && (
          <div className="login-error" role="alert">
            {error}
          </div>
        )}

        {/* ===== Form ===== */}
        <form className="login-form" onSubmit={handleSubmit} noValidate>
          {/* Trường Tên đăng nhập */}
          <div className="form-group">
            <label htmlFor="username" className="form-label">
              Tên đăng nhập
            </label>
            <div className="input-wrapper">
              <span className="input-icon input-icon--user" aria-hidden="true">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8">
                  <circle cx="12" cy="8" r="4" />
                  <path d="M4 20c0-4 4-6 8-6s8 2 8 6" />
                </svg>
              </span>
              <input
                id="username"
                name="username"
                type="text"
                autoComplete="username"
                placeholder=""
                value={email}
                onChange={(event) => setEmail(event.target.value)}
                required
                className="form-input"
              />
            </div>
          </div>

          {/* Trường Mật khẩu */}
          <div className="form-group">
            <label htmlFor="password" className="form-label">
              Mật khẩu
            </label>
            <div className="input-wrapper">
              <span className="input-icon input-icon--lock" aria-hidden="true">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8">
                  <rect x="3" y="11" width="18" height="11" rx="2" />
                  <path d="M7 11V7a5 5 0 0 1 10 0v4" />
                </svg>
              </span>
              <input
                id="password"
                name="password"
                type={showPassword ? "text" : "password"}
                autoComplete="current-password"
                placeholder=""
                value={password}
                onChange={(event) => setPassword(event.target.value)}
                required
                className="form-input"
              />
              <button
                type="button"
                className="password-toggle"
                onClick={() => setShowPassword(!showPassword)}
                aria-label={showPassword ? "Ẩn mật khẩu" : "Hiển thị mật khẩu"}
                tabIndex={0}
              >
                {showPassword ? (
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" aria-hidden="true">
                    <path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24" />
                    <line x1="1" y1="1" x2="23" y2="23" />
                  </svg>
                ) : (
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" aria-hidden="true">
                    <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z" />
                    <circle cx="12" cy="12" r="3" />
                  </svg>
                )}
              </button>
            </div>
          </div>

          {/* Remember Me + Forgot Password */}
          <div className="login-options">
            <label className="remember-me">
              <input
                type="checkbox"
                name="remember"
                checked={rememberMe}
                onChange={(event) => setRememberMe(event.target.checked)}
              />
              <span>Ghi nhớ đăng nhập</span>
            </label>
            <button
              type="button"
              className="forgot-password"
              onClick={() => console.log('Quên mật khẩu')}
            >
              Quên mật khẩu?
            </button>
          </div>

          {/* Nút Đăng nhập */}
          <button
            type="submit"
            className="login-button"
            disabled={loading}
          >
            {loading ? 'Đang đăng nhập...' : 'Đăng nhập'}
          </button>
        </form>

        {/* ===== Divider "Hoặc" ===== */}
        <div className="login-or">
          <span>Hoặc</span>
        </div>

        {/* ===== Nút đăng nhập bằng Google ===== */}
        <button
          type="button"
          className="google-login-button"
          onClick={handleGoogleLogin}
        >
          <svg viewBox="0 0 24 24" aria-hidden="true" className="google-icon">
            <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" />
            <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" />
            <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.84z" />
            <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" />
          </svg>
          <span>Tiếp tục với Google</span>
        </button>

        {/* ===== Link sang trang đăng ký ===== */}
        <div className="login-switch">
          <span>Chưa có tài khoản?</span>
          <button
            type="button"
            className="login-switch__link"
            onClick={() => navigateTo('/signup')}
          >
            Đăng ký
          </button>
        </div>
      </div>
    </main>
  )
}

export default Login