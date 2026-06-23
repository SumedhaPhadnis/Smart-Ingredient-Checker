import React from 'react'
import ReactDOM from 'react-dom/client'
import { GoogleOAuthProvider } from '@react-oauth/google';
import App from './App'
import './index.css'

const clientId = "637812395299-742oti3v5imh087jrpd147nbhfmi0tt1.apps.googleusercontent.com";
const savedTheme = localStorage.getItem("theme") || "light";
document.documentElement.classList.remove("light", "dark", "amoled");
document.documentElement.classList.add(savedTheme);
ReactDOM.createRoot(document.getElementById('root')).render(
    <React.StrictMode>
        <GoogleOAuthProvider clientId={clientId}>
            <App />
        </GoogleOAuthProvider>
    </React.StrictMode>,
)
