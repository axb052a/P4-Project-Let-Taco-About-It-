import React, { useState } from "react";
import {
  Box,
  Flex,
  Stack,
  Heading,
  Text,
  Container,
  Input as ChakraInput,
  Button,
  SimpleGrid,
} from "@chakra-ui/react";
import { useHistory } from "react-router-dom";

export default function Signup({ setUser, fetchUser }) {
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const history = useHistory();

  function handleLogin() {
    history.push("/login");
  }

  function handleSubmit(e) {
    e.preventDefault();
    fetch("http://localhost:5555/signup", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ username, email, password }),
    }).then((r) => {
      if (r.ok) {
        r.json().then((user) => {
          setUser(user);
          fetchUser(user);
          history.push("/");
        });
      }
    });
  }

  return (
    <Box position={"relative"}>
      <Container
        as={SimpleGrid}
        maxW={"7xl"}
        columns={{ base: 1, md: 2 }}
        spacing={{ base: 10, lg: 32 }}
        py={{ base: 10, sm: 20, lg: 32 }}
      >
        <Stack spacing={{ base: 10, md: 20 }}>
          <Heading
            lineHeight={1.1}
            fontSize={{ base: "3xl", sm: "4xl", md: "5xl", lg: "6xl" }}
          >
            Welcome. {" "}
            <Text
              as={"span"}
              bgGradient="linear(to-r, yellow.400, orange.400)"
              bgClip="text"
            >
              Let's Taco About It
            </Text>{" "}
          </Heading>
        </Stack>
        <Stack
          bg={"yellow.50"}
          rounded={"xl"}
          p={{ base: 4, sm: 6, md: 8 }}
          spacing={{ base: 8 }}
          maxW={{ lg: "lg" }}
        >
          <Stack spacing={4}>
            <Heading
              color={"orange.800"}
              lineHeight={1.1}
              fontSize={{ base: "2xl", sm: "3xl", md: "4xl" }}
            >
             Create an account 
              <Text
                as={"span"}
                bgGradient="linear(to-r, yellow.400, orange.400)"
                bgClip="text"
              >
                !
              </Text>
            </Heading>
          </Stack>
          <Box as={"form"} onSubmit={(e) => handleSubmit(e)} mt={10}>
            <Stack spacing={4}>
              <ChakraInput
                bg={"yellow.100"}
                border={0}
                color={"orange.500"}
                _placeholder={{
                  color: "orange.500",
                }}
                type="text"
                value={username}
                placeholder="Username"
                onChange={(e) => setUsername(e.target.value)}
                required
              />
              <ChakraInput
                bg={"yellow.100"}
                border={0}
                color={"orange.500"}
                _placeholder={{
                  color: "orange.500",
                }}
                type="password"
                value={password}
                placeholder="Password"
                onChange={(e) => setPassword(e.target.value)}
                required
              />
              <ChakraInput
                bg={"yellow.100"}
                border={0}
                color={"orange.500"}
                _placeholder={{
                  color: "orange.500",
                }}
                type="email"
                value={email}
                placeholder="Email"
                onChange={(e) => setEmail(e.target.value)}
                required
              />
            </Stack>
            <Button
              fontFamily={"heading"}
              mt={8}
              w={"full"}
              bgGradient="linear(to-r, yellow.400, orange.400)"
              color={"white"}
              _hover={{
                bgGradient: "linear(to-r, yellow.400, orange.400)",
                boxShadow: "xl",
              }}
              type="submit"
            >
              Submit
            </Button>
            <Text
              color={"blue.400"}
              _hover={{
                color: "blue.600",
              }}
              onClick={handleLogin}
            >
              Already have an account? Login now!
            </Text>
          </Box>
        </Stack>
      </Container>
    </Box>
  );
}
