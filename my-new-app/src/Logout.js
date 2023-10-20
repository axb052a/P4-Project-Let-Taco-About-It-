import React from "react";
import { useHistory } from "react-router-dom/cjs/react-router-dom.min";

export default function Logout({ setUser }) {
  const history = useHistory();
  function handleLogOut() {
    fetch("/logout", {
      method: "DELETE",
    }).then((r) => {
      if (r.ok) {
        setUser(null);
        history.push("/");
      }
    });
  }
  return <button onClick={handleLogOut}>Logout</button>;
}
