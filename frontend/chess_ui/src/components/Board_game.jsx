import Piece from '../game_manager/Piece'

const boardFiles = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
const boardRanks = [8, 7, 6, 5, 4, 3, 2, 1]

const initialPieces = {
  a8: { type: 'rook', color: 'black' },
  b8: { type: 'knight', color: 'black' },
  c8: { type: 'bishop', color: 'black' },
  d8: { type: 'queen', color: 'black' },
  e8: { type: 'king', color: 'black' },
  f8: { type: 'bishop', color: 'black' },
  g8: { type: 'knight', color: 'black' },
  h8: { type: 'rook', color: 'black' },
  a7: { type: 'pawn', color: 'black' },
  b7: { type: 'pawn', color: 'black' },
  c7: { type: 'pawn', color: 'black' },
  d7: { type: 'pawn', color: 'black' },
  e7: { type: 'pawn', color: 'black' },
  f7: { type: 'pawn', color: 'black' },
  g7: { type: 'pawn', color: 'black' },
  h7: { type: 'pawn', color: 'black' },
  a2: { type: 'pawn', color: 'white' },
  b2: { type: 'pawn', color: 'white' },
  c2: { type: 'pawn', color: 'white' },
  d2: { type: 'pawn', color: 'white' },
  e2: { type: 'pawn', color: 'white' },
  f2: { type: 'pawn', color: 'white' },
  g2: { type: 'pawn', color: 'white' },
  h2: { type: 'pawn', color: 'white' },
  a1: { type: 'rook', color: 'white' },
  b1: { type: 'knight', color: 'white' },
  c1: { type: 'bishop', color: 'white' },
  d1: { type: 'queen', color: 'white' },
  e1: { type: 'king', color: 'white' },
  f1: { type: 'bishop', color: 'white' },
  g1: { type: 'knight', color: 'white' },
  h1: { type: 'rook', color: 'white' },
}

const BoardGame = () => {
  return (
    <section className="game-board-card" aria-label="Bàn cờ">
      <div className="game-board" role="img" aria-label="Bàn cờ vua 8x8">
        {boardRanks.map((rank) => (
          boardFiles.map((file) => {
            const fileIndex = boardFiles.indexOf(file)
            const isLight = (rank + fileIndex) % 2 === 0
            const squareKey = `${file}${rank}`
            const piece = initialPieces[squareKey]

            return (
              <div
                className={`game-board__square ${isLight ? 'game-board__square--light' : 'game-board__square--dark'}`}
                key={squareKey}
              >
                {fileIndex === 0 && <span className="game-board__rank">{rank}</span>}
                {rank === 1 && <span className="game-board__file">{file}</span>}
                {piece && (
                  <Piece type={piece.type} color={piece.color} className="game-board__piece" />
                )}
              </div>
            )
          })
        ))}
      </div>
    </section>
  )
}

export default BoardGame