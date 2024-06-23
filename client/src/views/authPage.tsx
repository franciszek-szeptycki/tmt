import {  useState } from "react";
import AuthForm from "../components/auth/authForm";

export default function AuthPage() {
  const [target, setTarget] = useState("Login");

  return (
    <main className="auth_page">
      <AuthForm target={target} setTarget={setTarget} />
    </main>
  );
}
