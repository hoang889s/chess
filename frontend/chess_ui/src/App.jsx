import { useEffect, useState } from 'react'
import Home from './page/Home.jsx'
import Game from './page/Game.jsx'

const App = () => {
  const [path, setPath] = useState(window.location.pathname)

  useEffect(() => {
    const handlePathChange = () => setPath(window.location.pathname)

    window.addEventListener('popstate', handlePathChange)

    return () => window.removeEventListener('popstate', handlePathChange)
  }, [])

  return path === '/page/Game.jsx' ? <Game /> : <Home />
}

export default App
