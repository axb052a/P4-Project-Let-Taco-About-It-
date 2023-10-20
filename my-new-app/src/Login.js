import React, { useState } from "react";
import { Box, Input, Button, Heading, Text } from "@chakra-ui/react";
import { useHistory } from "react-router-dom";

function Login({ setUser }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(null);

  const history = useHistory();

  const handleSubmit = (e) => {
    e.preventDefault();

    // Send a POST request to your backend's /login route
    fetch("http://localhost:5555/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ username, password }),
    })
      .then((response) => {
        if (response.ok) {
          // If the login is successful, set the user state and redirect to the home page
          response.json().then((user) => {
            setUser(user);
            history.push("/");
          });
        } else {
          // If the login fails, handle the error
          response.json().then((data) => {
            setError(data.error || "An error occurred during login.");
          });
        }
      })
      .catch((error) => {
        setError("An error occurred during login.");
      });
  };

  return (
    <Box as="main" mt="20" textAlign="center">
      <Heading fontSize="4xl" mb="4">
        Login to your account
      </Heading>
      {error && (
        <Text color="red.500" mb="4">
          {error}
        </Text>
      )}
      <form onSubmit={handleSubmit}>
        <Input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          mb="2"
        />
        <Input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          mb="4"
        />
        <Button type="submit" colorScheme="blue">
          Sign In
        </Button>
      </form>
    </Box>
  );
}

export default Login;
