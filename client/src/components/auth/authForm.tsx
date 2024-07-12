import { Button } from "@mui/material";
import TextField from "@mui/material/TextField";
import { AUTH_QUERIE } from "../../queries/authQueries";
import { useState } from "react";
import { IAuthForm } from "../../types/IauthForm";
export default function AuthForm(props: {
  target: string;
  setTarget: React.Dispatch<React.SetStateAction<string>>;
  setAuthToken: React.Dispatch<React.SetStateAction<string>>
}) {
  const { target, setTarget, setAuthToken } = props;
  const [form, setForm] = useState<IAuthForm>({
    login: '',
    password: '',
    email: ""
  })
  return (
    <form className={`auth_form ${target}`}>
      <header>
        <h1>{target}</h1>
        <p>
          {target === "login" ? "login to your account" : "create your account"}
        </p>
      </header>
      <section>
        <TextField
          id="name"
          label="Name"
          type="text"
          autoComplete=""
          className="input"
          value={form.login}
          onChange={(event) => setForm({...form, login: event.target.value})}
        />
        <TextField
          className="input"
          id="outlined-password-input"
          label="Password"
          type="password"
          autoComplete="current-password"
          value={form.password}
          onChange={(event) => setForm({...form, password: event.target.value}) }
        />
        {target === "Login" ? (
          ""
        ) : (
          <TextField id="email" label="Email" type="email" value={form.email}className="input" onChange={(event) => setForm({...form, email: event.target.value})} />
        )}

        <Button onClick={async () => setAuthToken(await AUTH_QUERIE(form.login, form.password, form.email, target))} className="btn_login" variant="contained">
          {target}
        </Button>
      </section>
      <footer>
        <button
          onClick={(e) => {
            e.preventDefault()
            setTarget(target === "Login" ? "Register" : "Login");
          }}
          className="btn_empty"
        >
          {target === "Login" ? "I have account" : "I don't have account"}
        </button>
      </footer>
    </form>
  );
}
