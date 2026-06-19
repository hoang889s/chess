import './Home.css'

const socialLinks = [
    {
        label: 'Facebook',
        icon: '/icons/logo_facebook.svg',
        href: '#',
    },
    {
        label: 'X',
        icon: '/icons/logo_x.svg',
        href: '#',
    },
    {
        label: 'GitHub',
        icon: '/icons/logo_github.svg',
        href: '#',
    },
    {
        label: 'LinkedIn',
        icon: '/icons/logo_linked.svg',
        href: '#',
    },
    {
        label: 'YouTube',
        icon: '/icons/logo_youtube.svg',
        href: '#',
    },
]

const linkmenu = '/icons/menu.svg';
const linkrook = '/icons/logo.svg';
const linkpawn = '/icons/pawn.svg';
const Home = () => {
    return (
        <main className="home-page">
            <div className="home-page__grain" aria-hidden="true" />

            <header className="home-nav">
                <button className="home-nav__menu" type="button" aria-label="Mở menu">
                    <img src={linkmenu} width={24} height={24} />
                </button>

                <div className="home-nav__actions">
                    <button className="home-nav__login" type="button">
                        Đăng nhập
                    </button>
                    <span className="home-nav__avatar" aria-hidden="true">
                        <img src={linkpawn} width={24} height={24} />

                    </span>
                </div>
            </header>

            <section className="home-hero" aria-labelledby="home-title">
                <div className="home-hero__content">
                    <p className="home-hero__eyebrow">Cờ cổ • Đấu trí • Thử thách</p>

                    <h1 className="home-hero__title" id="home-title">
                        <span className="home-hero__title-line">
                            Tham gia chơi cờ cùng
                        </span>
                        <span className="home-hero__title-line home-hero__title-line--reverse">
                            những đối thủ thú vị
                        </span>
                    </h1>

                    <div className="home-hero__connect-card">
                        <span className="home-hero__connect-label">
                            kết nối với người chơi khác
                        </span>
                        <button className="home-hero__primary-button" type="button">
                            Chơi ngay
                        </button>
                    </div>

                    <button className="home-hero__secondary-button" type="button">
                        <span className="home-hero__rook-icon" aria-hidden="true">
                            <img src={linkrook} width={24} height={24} />
                        </span>
                        <p>
                            Giải thử thách thú vị
                        </p>

                    </button>
                </div>

                <div className="home-hero__visual" aria-label="Bảng cờ minh họa">
                    <div className="home-hero__visual-card">
                        <div className="home-hero__visual-top">
                            <div className="home-hero__moon" aria-hidden="true" />
                            <div className="home-hero__column" aria-hidden="true" />
                        </div>

                        <div className="home-hero__mini-board" aria-hidden="true">
                            {Array.from({ length: 16 }).map((_, index) => {
                                const hasPiece = [1, 5, 10, 13].includes(index)

                                return (
                                    <div
                                        className={`home-hero__mini-square ${index % 2 === 0 ? 'home-hero__mini-square--light' : 'home-hero__mini-square--dark'}`}
                                        key={index}
                                    >
                                        {hasPiece && <span><img src={linkpawn} width={48} height={48} /></span>}
                                    </div>
                                )
                            })}
                        </div>


                    </div>
                </div>
            </section>

            <footer className="home-footer">
                <div className="home-footer__brand">
                    <span aria-hidden="true"><img src={linkrook} width={24} height={24} /></span>
                    <span>© Được làm bởi H</span>
                </div>

                <div className="home-footer__socials" aria-label="Liên kết mạng xã hội">
                    {socialLinks.map((link) => (
                        <a aria-label={link.label} className="home-footer__social" href={link.href} key={link.label}>
                            <img src={link.icon} width={40} height={40} />
                        </a>
                    ))}
                </div>
            </footer>
        </main>
    )
}

export default Home
