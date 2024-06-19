import { useState } from 'react'
import './App.css'

function App() {
  const [status, setStatus] = useState("...")

  fetch("https://tmt-u6cv.onrender.com/")
    .then(res => res.ok)
    .then(() => setStatus("OK"))
    .catch(() => setStatus("Error connecting to backend."))

  return (
    <h1>Backend connection status: {status}</h1>
  )
}

export default App
