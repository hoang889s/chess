import { useState, useRef } from 'react'
import './Signup.css'

const Signup = () => {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
  })

  const [errors, setErrors] = useState({})
  const [showPassword, setShowPassword] = useState(false)
  const [registerState, setRegisterState] = useState('idle') // idle | submitting
  const [googleState, setGoogleState] = useState('idle') // idle | loading

  const usernameRef = useRef(null)
  const emailRef = useRef(null)
  const passwordRef = useRef(null)

  const navigateTo = (page) => {
    window.history.pushState({}, '', page)
    window.dispatchEvent(new Event('popstate'))
  }

  // ---- Validation (khớp backend Flask: username 3-50 ký tự a-zA-Z0-9_, password >= 8, email format, max 100) ----
  const validate = () => {
    const newErrors = {}
    const usernameRegex = /^[a-zA-Z0-9_]{3,50}$/

    if (!formData.username.trim()) {
      newErrors.username = 'Tên đăng nhập không được để trống'
    } else if (!usernameRegex.test(formData.username)) {
      newErrors.username = 'Tên đăng nhập phải có từ 3-50 ký tự, chỉ chứa chữ, số và dấu gạch dưới'
    }

    if (!formData.password) {
      newErrors.password = 'Mật khẩu không được để trống'
    } else if (formData.password.length < 8) {
      newErrors.password = 'Mật khẩu phải có ít nhất 8 ký tự'
    }

    if (!formData.email.trim()) {
      newErrors.email = 'Email không được để trống'
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
      newErrors.email = 'Email không hợp lệ'
    } else if (formData.email.length > 100) {
      newErrors.email = 'Email quá dài (tối đa 100 ký tự)'
    }

    setErrors(newErrors)
    return Object.keys(newErrors).length === 0
  }

  const focusField = (field) => {
    if (field === 'username') usernameRef.current?.focus()
    else if (field === 'email') emailRef.current?.focus()
    else if (field === 'password') passwordRef.current?.focus()
  }

  const getFieldFromError = (message) => {
    if (message.includes('Username')) return 'username'
    if (message.includes('Email')) return 'email'
    if (message.includes('Password')) return 'password'
    return 'submit'
  }

  const handleRegister = async (event) => {
    event.preventDefault()
    if (!validate()) {
      const firstError = Object.keys(errors)[0]
      if (firstError) focusField(firstError)
      return
    }

    setRegisterState('submitting')
    try {
      const response = await fetch('/api/auth/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      })

      const data = await response.json()

      if (data.success) {
        // Đăng ký thành công -> chuyển sang màn hình đăng nhập
        navigateTo('/login')
      } else {
        const field = getFieldFromError(data.message)
        setErrors({ [field]: data.message })
        focusField(field)
      }
    } catch {
      setErrors({ submit: 'Không thể kết nối đến máy chủ. Vui lòng kiểm tra lại mạng.' })
    } finally {
      setRegisterState('idle')
    }
  }

  const handleGoogleSignup = () => {
    setGoogleState('loading')
    // TODO: tích hợp Google OAuth
    console.log('Đăng ký bằng Google')
    setGoogleState('idle')
  }

  const handleChange = (event) => {
    const { name, value } = event.target
    setFormData((prev) => ({ ...prev, [name]: value }))
    // Xóa thông báo lỗi của trường khi người dùng bắt đầu sửa
    if (errors[name]) {
      setErrors((prev) => ({ ...prev, [name]: '' }))
    }
  }

  // SVG Icons (icon components thay vì copy SVG từ công cụ thiết kế)
  const ArrowLeftIcon = () => (
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" aria-hidden="true">
      <line x1="19" y1="12" x2="5" y2="12" />
      <polyline points="12 19 5 12 12 5" />
    </svg>
  )

  const EyeIcon = () => (
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" aria-hidden="true">
      <path d="M1 12s4-8 11-8 11 8-4 8-11 8-11-8-11-8z" />
      <circle cx="12" cy="12" r="3" />
    </svg>
  )

  const EyeOffIcon = () => (
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" aria-hidden="true">
      <path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24" />
      <line x1="1" y1="1" x2="23" y2="23" />
    </svg>
  )

  const GoogleIcon = () => (
    <svg viewBox="0 0 24 24" aria-hidden="true">
      <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4" />
      <path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853" />
      <path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.84z" fill="#FBBC05" />
      <path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335" />
    </svg>
  )

  const UserIcon = () => (
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" aria-hidden="true">
      <circle cx="12" cy="8" r="4" />
      <path d="M4 20c0-4 4-6 8-6s8 2 8 6" />
    </svg>
  )

  const LockIcon = () => (
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" aria-hidden="true">
      <rect x="3" y="11" width="18" height="11" rx="2" />
      <path d="M7 11V7a5 5 0 0 1 10 0v4" />
    </svg>
  )

  return (
    <main className="signup-page">
      <div className="signup-page__grain" aria-hidden="true" />

      {/* Decorative chess pieces */}
      <div className="signup-decor" aria-hidden="true">
        <span className="signup-decor__piece signup-decor__piece--top-left">♞</span>
        <span className="signup-decor__piece signup-decor__piece--top-right">♜</span>
        <span className="signup-decor__piece signup-decor__piece--bottom-left">♟</span>
        <span className="signup-decor__piece signup-decor__piece--bottom-right">♝</span>
      </div>

      <div className="signup-card">
        {/* ===== Nút quay lại (Back button) ===== */}
        <button
          type="button"
          className="signup-back"
          onClick={() => window.history.back()}
          aria-label="Quay lại"
        >
          <ArrowLeftIcon />
        </button>

        {/* ===== Brand / Chess Logo ===== */}
        <div className="signup-brand">
          <div className="signup-brand__icon">♞</div>
          <span className="signup-brand__text">AI POWERED CHESS</span>
        </div>

        {/* ===== Header ===== */}
        <div className="signup-header">
          <p className="signup-welcome">Chào mừng trở lại!</p>
          <h1 className="signup-title">Đăng ký</h1>
        </div>

        {/* ===== Error Message ===== */}
        {errors.submit && (
          <div className="signup-error" role="alert">
            {errors.submit}
          </div>
        )}

        {/* ===== Form đăng ký ===== */}
        <form className="signup-form" onSubmit={handleRegister} noValidate>
          {/* Trường Tên đăng nhập */}
          <div className="form-field">
            <label htmlFor="username" className="form-label">
              Tên đăng nhập
            </label>
            <div className="input-wrapper">
              <span className="input-icon input-icon--user" aria-hidden="true">
                <UserIcon />
              </span>
              <input
                ref={usernameRef}
                id="username"
                name="username"
                type="text"
                className={`form-input ${errors.username ? 'form-input--error' : ''}`}
                placeholder="Nhập tên đăng nhập"
                value={formData.username}
                onChange={handleChange}
                aria-invalid={!!errors.username}
                aria-describedby={errors.username ? 'username-error' : undefined}
                disabled={registerState === 'submitting'}
              />
            </div>
            {errors.username && (
              <span id="username-error" className="form-error" role="alert">
                {errors.username}
              </span>
            )}
          </div>

          {/* Trường Mật khẩu (có hiện/ẩn) */}
          <div className="form-field">
            <label htmlFor="password" className="form-label">
              Mật khẩu
            </label>
            <div className="input-wrapper">
              <span className="input-icon input-icon--lock" aria-hidden="true">
                <LockIcon />
              </span>
              <input
                ref={passwordRef}
                id="password"
                name="password"
                type={showPassword ? 'text' : 'password'}
                className={`form-input ${errors.password ? 'form-input--error' : ''}`}
                placeholder="Nhập mật khẩu"
                value={formData.password}
                onChange={handleChange}
                aria-invalid={!!errors.password}
                aria-describedby={errors.password ? 'password-error' : undefined}
                disabled={registerState === 'submitting'}
              />
              <button
                type="button"
                className="password-toggle"
                onClick={() => setShowPassword((prev) => !prev)}
                aria-label={showPassword ? 'Ẩn mật khẩu' : 'Hiển thị mật khẩu'}
                disabled={registerState === 'submitting'}
              >
                {showPassword ? <EyeOffIcon /> : <EyeIcon />}
              </button>
            </div>
            {errors.password && (
              <span id="password-error" className="form-error" role="alert">
                {errors.password}
              </span>
            )}
          </div>

          {/* Trường Email */}
          <div className="form-field">
            <label htmlFor="email" className="form-label">
              Email
            </label>
            <div className="input-wrapper">
              <span className="input-icon input-icon--email" aria-hidden="true">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8">
                  <rect x="2" y="4" width="20" height="16" rx="2" />
                  <path d="M2 7l10 7 10-7" />
                </svg>
              </span>
              <input
                ref={emailRef}
                id="email"
                name="email"
                type="email"
                className={`form-input ${errors.email ? 'form-input--error' : ''}`}
                placeholder="Nhập email"
                value={formData.email}
                onChange={handleChange}
                aria-invalid={!!errors.email}
                aria-describedby={errors.email ? 'email-error' : undefined}
                disabled={registerState === 'submitting'}
              />
            </div>
            {errors.email && (
              <span id="email-error" className="form-error" role="alert">
                {errors.email}
              </span>
            )}
          </div>

          {/* Nút Đăng ký */}
          <button
            type="submit"
            className="register-button"
            disabled={registerState === 'submitting'}
            aria-busy={registerState === 'submitting'}
          >
            {registerState === 'submitting' ? 'Đang đăng ký...' : 'Đăng ký'}
          </button>
        </form>

        {/* ===== Divider "Hoặc" ===== */}
        <div className="oauth-divider">
          <span>Hoặc</span>
        </div>

        {/* ===== Nút đăng ký bằng Google ===== */}
        <button
          type="button"
          className="google-button"
          onClick={handleGoogleSignup}
          disabled={googleState === 'loading'}
          aria-label="Đăng ký bằng Google"
        >
          {googleState === 'loading' ? (
            'Đang xử lý...'
          ) : (
            <>
              <GoogleIcon />
              <span>Tiếp tục với Google</span>
            </>
          )}
        </button>

        {/* ===== Link sang trang đăng nhập ===== */}
        <div className="signup-switch">
          <span>Đã có tài khoản?</span>
          <button
            type="button"
            className="signup-switch__link"
            onClick={() => navigateTo('/login')}
          >
            Đăng nhập
          </button>
        </div>
      </div>
    </main>
  )
}

export default Signup