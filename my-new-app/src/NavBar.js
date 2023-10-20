import React from "react";
import { NavLink } from "react-router-dom";
import { Box, Flex } from "@chakra-ui/react";
import { Link as ChakraLink } from "@chakra-ui/react";

function NavigationBar() {
  return (
    <Flex
      bg="orange.300"
      color="white"
      p={4}
      align="center"
      justify="space-between"
    >
      <Box>
        <ChakraLink as={NavLink} to="/" fontSize="xl">
          Let's Taco Bout It
        </ChakraLink>
      </Box>
      <Flex align="center">
        <ChakraLink as={NavLink} to="/AddTaco" fontSize="lg" mr={4}>
         Your Fave Tacos
        </ChakraLink>
        <ChakraLink as={NavLink} to="/AddTaco" fontSize="lg" mr={4}>
          Add Taco
        </ChakraLink>
        <ChakraLink as={NavLink} to="/signup" fontSize="lg" mr={4}>
          Signup
        </ChakraLink>
        <ChakraLink as={NavLink} to="/login" fontSize="lg" mr={4}>
          Login
        </ChakraLink>
        {/* You can add more navigation links here if needed */}
      </Flex>
    </Flex>
  );
}

export default NavigationBar;
