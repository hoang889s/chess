import { useEffect, useState } from 'react'
import Home from './page/Home.jsx'
import Game from './page/Game.jsx'
import Login from './page/Login.jsx'
import Signup from './page/Signup.jsx'

const App = () => {
  const [path, setPath] = useState(window.location.pathname)

  useEffect(() => {
    const handlePathChange = () => setPath(window.location.pathname)

    window.addEventListener('popstate', handlePathChange)

    return () => window.removeEventListener('popstate', handlePathChange)
  }, [])

  return (
    <>
      {path === '/page/Game.jsx' ? (
        <Game />
      ) : path === '/page/Login.jsx' ? (
        <Login />
      ) : path === '/page/Signup.jsx' ? (
        <Signup />
      ) : (
        <Home />
      )}
    </>
  )
}

export default App
