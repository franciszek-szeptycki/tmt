import { useState } from "react";

export default function Input(props: { type: string }) {
  const { type } = props;
  const [value, setValue] = useState("");
  return (
    <>
      <label htmlFor={type}>{type}</label>
      <input
        id={type}
        name={type}
        value={value}
        onChange={(event) => setValue(event.target.value)}
      />
    </>
  );
}
