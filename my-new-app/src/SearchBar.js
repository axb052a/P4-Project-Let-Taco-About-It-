import React, { useState } from "react";
import { Input, Box } from "@chakra-ui/react";

export default function SearchBar({ onSearch }) {
  const [search, setSearch] = useState("");

  const handleSearchChange = (event) => {
    setSearch(event.target.value);
    onSearch(event.target.value);
  };

  return (
    <Box
      position="relative"
      bgImage="url('https://images.everydayhealth.com/images/creative-taco-recipes-bursting-with-nutrition-00-722x406.jpg?w=720')"
      bgSize="cover"
      bgPosition="center"
      minHeight="30vw" 
      display="flex" 
      justifyContent="center"
      alignItems="center"
    >
      <Box
        bg="white" 
        maxWidth="1000px" 
        width="100%" 
        borderRadius="md"
        boxShadow="md" 
      >
        <Input
          type="text"
          value={search}
          onChange={handleSearchChange}
          placeholder="Search for an interesting taco..."
          focusBorderColor="orange.300"
          color="orange.500"
          _placeholder={{ color: "inherit" }}
          bg="white" 
        />
      </Box>
    </Box>
  );
}
