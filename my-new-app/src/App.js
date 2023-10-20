import React, { useState } from "react";
import { Route, Switch, BrowserRouter as Router } from "react-router-dom";
import { ChakraProvider } from "@chakra-ui/react";
import Home from "./Home";
import Login from "./Login"; // Import your Login component
import NavBar from "./NavBar";
import Signup from "./Signup"; // Import your Login component

import AddTaco from "./AddTaco";

function App() {
  const [user, setUser] = useState(null);
  const [refreshPage, setRefreshPage] = useState(false);

  const fetchUser = () =>
    fetch("http://localhost:5555/check_session").then((r) => {
      if (r.ok) {
        r.json().then((user) => {
          setUser(user);
          console.log(user);
        });
      }
    });

  return (
    <ChakraProvider>
      <Router>
        <NavBar />
        <Switch>
          <Route path="/login">
            <Login user={user} setUser={setUser} fetchUser={fetchUser} />
          </Route>
          <Route path="/signup">
            <Signup user={user} setUser={setUser} fetchUser={fetchUser} />
          </Route>
          <Route path="/AddTaco">
            <AddTaco setRefreshPage={setRefreshPage} />
          </Route>
          <Route path="/">
            <Home user={user} />
          </Route>
        </Switch>
      </Router>
    </ChakraProvider>
  );
}

export default App;
