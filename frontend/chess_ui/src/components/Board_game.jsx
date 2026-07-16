const boardFiles = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
const boardRanks = [8, 7, 6, 5, 4, 3, 2, 1]

const BoardGame = () => {
    return (
        <section className="game-board-card" aria-label="Bàn cờ">
            <div className="game-board" role="img" aria-label="Bàn cờ vua 8x8">
                {boardRanks.map((rank) => (
                    boardFiles.map((file) => {
                        const fileIndex = boardFiles.indexOf(file)
                        const isLight = (rank + fileIndex) % 2 === 0

                        return (
                            <div
                                className={`game-board__square ${isLight ? 'game-board__square--light' : 'game-board__square--dark'}`}
                                key={`${file}${rank}`}
                            >
                                {fileIndex === 0 && <span className="game-board__rank">{rank}</span>}
                                {rank === 1 && <span className="game-board__file">{file}</span>}
                            </div>
                        )
                    })
                ))}
            </div>
        </section>
    )
}

export default BoardGame