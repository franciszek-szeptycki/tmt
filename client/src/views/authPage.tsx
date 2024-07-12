import { useState } from "react";
import AuthForm from "../components/auth/authForm";

export default function AuthPage(props: {setAuthToken: React.Dispatch<React.SetStateAction<string>>}) {
  const { setAuthToken } = props
  const [target, setTarget] = useState("Login");

  return (
    <main className="auth_page">
      <AuthForm target={target} setTarget={setTarget} setAuthToken={setAuthToken}/>
    </main>
  );
}
