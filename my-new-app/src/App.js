import React, { useState } from "react";
import { Route, Switch, BrowserRouter as Router } from "react-router-dom";
import { ChakraProvider } from "@chakra-ui/react";
import Home from "./Home";
import Login from "./Login"; // Import your Login component
import NavBar from "./NavBar";


function App() {

  const [user, setUser] = useState(null);
  return (
    <ChakraProvider>
      <Router>
        <NavBar /> {NavBar}
        <Switch>
          <Route path="/login">
            <Login user={user} setUser={setUser} />
          </Route>
          <Route path="/">
            <Home />
          </Route>
        </Switch>
      </Router>
    </ChakraProvider>
  );
}

export default App;
