import { Button } from "@mui/material";
import TextField from "@mui/material/TextField";
export default function AuthForm(props: {
  target: string;
  setTarget: React.Dispatch<React.SetStateAction<string>>;
}) {
  const { target, setTarget } = props;
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
        />
        <TextField
          className="input"
          id="outlined-password-input"
          label="Password"
          type="password"
          autoComplete="current-password"
        />
        {target === "Login" ? (
          ""
        ) : (
          <TextField id="email" label="Email" type="email" className="input" />
        )}

        <Button  className="btn_login" variant="contained">
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
