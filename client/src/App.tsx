import { useState } from 'react' 
import './App.css'
import AuthPage from './views/authPage'

export default function App() {
  const [status, setStatus] = useState("...")

  fetch("https://tmt-u6cv.onrender.com/")
    .then(res => res.ok)
    .then(() => setStatus("OK"))
    .catch(() => setStatus("Error connecting to backend."))

  return (
    <AuthPage/>
  )
}


