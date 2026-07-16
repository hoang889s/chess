import './Game.css'
import NavbarGame from '../components/Navbar_game'
import BoardGame from '../components/Board_game'
import LeftBar from '../components/Left_bar'
import FooterGame from '../components/Footer_game'

const Game = () => {
    const goBack = () => {
        window.history.back()
    }

    return (
        <main className="game-page">
            <NavbarGame onBack={goBack} />

            <section className="game-layout" aria-label="Tạo ván cờ">
                <BoardGame />
                <LeftBar />
            </section>

            <FooterGame />
        </main>
    )
}

export default Game