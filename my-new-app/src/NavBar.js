import React from "react";
import { Link } from "react-router-dom";
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
        <ChakraLink as={Link} to="/" fontSize="xl">
          Let's Taco Bout It
        </ChakraLink>
      </Box>
      <Flex align="center">
        <ChakraLink as={Link} to="/AddTaco" fontSize="lg" mr={4}>
          Add Taco
        </ChakraLink>
        <ChakraLink as={Link} to="/signup" fontSize="lg" mr={4}>
          Signup
        </ChakraLink>
        <ChakraLink as={Link} to="/login" fontSize="lg" mr={4}>
          Login
        </ChakraLink>
        {/* You can add more navigation links here if needed */}
      </Flex>
    </Flex>
  );
}

export default NavigationBar;
